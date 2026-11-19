from os import getenv
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from agno.os.interfaces.slack.helpers import post_ephemeral
from agno.utils.log import log_debug, log_warning

if TYPE_CHECKING:
    from agno.os.interfaces.slack.context import EventContext, SlackContext

_NOT_A_MEMBER_MESSAGE = "Not run: Only members of this workspace can use this app"
_NOT_IN_APPS_MESSAGE = "Not run: App is not in apps="
_SLACK_UNAVAILABLE_MESSAGE = "Not run: Slack unavailable"
_DIRECTORY_UNAVAILABLE_MESSAGE = "Not run: User directory unavailable"


def resolve_token(token: Optional[str] = None) -> str:
    """The bot token: the argument when given, even empty, else SLACK_TOKEN."""
    resolved = token if token is not None else getenv("SLACK_TOKEN")
    if not resolved:
        raise ValueError("Slack requires a bot token: pass token or set SLACK_TOKEN")
    return resolved


def resolve_signing_secret(signing_secret: Optional[str] = None) -> str:
    """The signing secret: the argument when given, even empty, else SLACK_SIGNING_SECRET."""
    resolved = signing_secret if signing_secret is not None else getenv("SLACK_SIGNING_SECRET")
    if not resolved:
        raise ValueError("Slack requires a signing secret: pass signing_secret or set SLACK_SIGNING_SECRET")
    return resolved


async def can_act(ctx: "SlackContext", user: str, event_context: "EventContext", client: Any = None) -> bool:
    """Whether a Slack user may stop or decide on a run: its owner, an approver, or the same agno user."""
    if not user:
        return False
    if user == event_context.owner:
        return True
    if ctx.approvers is not None and user in ctx.approvers:
        return True
    if ctx.users is not None:
        principal = ctx.users.get(user)
        return principal is not None and principal == event_context.user_id
    if ctx.resolve_user_identity and event_context.user_id:
        # Same derivation as the event context's user, so the owner can act after a restart
        if senders_authorized(ctx):
            try:
                principal = await member_principal(ctx, client or ctx.web(), user, event_context.team_id)
            except LookupError:
                return False
            return principal == event_context.user_id
        resolved_user_id, _ = await ctx.lookup_cache.user_identity(client or ctx.web(), user)
        return resolved_user_id == event_context.user_id
    return False


def principal_authorization(app: Any, principal_id: str, roles: Optional[List[str]] = None) -> Any:
    """An authority that checks principal_id's roles, or the given roles when set."""
    from agno.os.auth import resolve_authorization_provider
    from agno.os.authz.provider import AuthorizationContext
    from agno.run.authorization import RunAuthorization

    return RunAuthorization(
        resolve_authorization_provider(app),
        AuthorizationContext(principal_id=principal_id, claims={"sub": principal_id}, roles=roles),
        enforce_tools=False,
    )


async def resolve_principal_authorization(
    app: Any, principal_id: str, resource: str, resource_id: str, roles: Optional[List[str]] = None
) -> Any:
    """A principal's authority, with roles when given; None with authorization off. Raises if disabled or denied."""
    from agno.os.auth import _authorization_enforced

    state = getattr(app, "state", None)
    user_store = getattr(state, "user_store", None)
    if user_store is not None:
        try:
            disabled = bool(await user_store.ais_disabled(principal_id))
        except Exception as e:
            # Directory unreachable: honour the configured policy
            fail_closed = bool(getattr(state, "user_directory_fail_closed", False))
            log_warning(
                f"user directory check failed for {principal_id!r}: {e} (failing {'closed' if fail_closed else 'open'})"
            )
            disabled = fail_closed
        if disabled:
            raise PermissionError("User is disabled")
    # The user directory applies on its own, as over HTTP; roles only under AgentOS authorization.
    # The middleware is checked here too: one added after get_app() is not in the flag
    if not _authorization_enforced(app):
        return None
    # Roles are resolved fresh on every check, so a revoked grant applies to the next message
    authority = principal_authorization(app, principal_id, roles)
    await authority.arequire(resource, "run", resource_id)
    return authority


def no_roles_authorization(app: Any, owner: str) -> Any:
    """An authority with no roles for a Slack user not in users=, None with authorization off."""
    from agno.os.auth import _authorization_enforced

    if not _authorization_enforced(app):
        return None
    return principal_authorization(app, f"slack:{owner}")


def senders_authorized(ctx: "SlackContext") -> bool:
    """Whether an agent, team or workflow runs each sender as their directory user: authorize_senders without users=."""
    return ctx.authorize_senders and ctx.users is None and ctx.company is None


async def is_other_app(ctx: "SlackContext", client: Any, user: str, bot_id: str) -> bool:
    """Whether a message is another app's: a bot id with no user, or a user the cached users.info reports as a bot."""
    if not bot_id:
        return False
    if not user:
        return True
    # A user-token post carries a person's user id with the bot id
    await ctx.lookup_cache.user_identity(client, user)
    return bool((ctx.lookup_cache.member(user) or {}).get("is_bot"))


async def member_principal(ctx: "SlackContext", client: Any, user: str, team_id: Optional[str]) -> Optional[str]:
    """A Slack member's directory user: their confirmed email under resolve_user_identity, else slack:{team}:{id}."""
    await ctx.lookup_cache.user_identity(client, user)
    member = ctx.lookup_cache.member(user)
    # Slack could not be asked, so neither the member nor their email is known
    if member is None:
        raise LookupError()
    workspace = member.get("team_id") or team_id
    # A Slack Connect member belongs to another workspace; an Enterprise Grid member also belongs to each
    # workspace listed on their enterprise_user
    teams = (member.get("enterprise_user") or {}).get("teams")
    external = bool(member.get("is_stranger")) or (
        bool(team_id) and workspace != team_id and not (isinstance(teams, list) and team_id in teams)
    )
    guest = bool(member.get("is_restricted") or member.get("is_ultra_restricted"))
    # A deactivated account, a guest or an outsider runs nothing unless allow_guests_and_external lets the last two in
    if member.get("deleted") or ((guest or external) and not ctx.allow_guests_and_external):
        return None
    # Only a member's own confirmed email names their existing user; a guest's or an outsider's never does
    email = (member.get("profile") or {}).get("email")
    if ctx.resolve_user_identity and email and member.get("is_email_confirmed") and not (guest or external):
        return email
    return f"slack:{workspace}:{user}"


async def app_principal(
    ctx: "SlackContext", client: Any, event: Dict[str, Any], team_id: Optional[str]
) -> Optional[str]:
    """Another app's directory user: its principal in apps=, else slack:{team}:{app id}; None when apps= omits it."""
    # One app posts under several bot ids but names the same app id; an incoming webhook's event names none,
    # so its bot's bots.info record does
    app_id = event.get("app_id") or (event.get("bot_profile") or {}).get("app_id")
    bot_id = event.get("bot_id") or ""
    if not app_id and bot_id:
        await ctx.lookup_cache.bot_identity(client, bot_id)
        bot = ctx.lookup_cache.bot(bot_id)
        # Slack could not be asked, so the app is not known
        if bot is None:
            raise LookupError()
        app_id = bot.get("app_id")
    app_id = app_id or bot_id
    if ctx.apps is not None:
        return ctx.apps.get(app_id)
    return f"slack:{team_id}:{app_id}"


async def provision_sender(ctx: "SlackContext", principal: str, claims: Dict[str, Any]) -> None:
    """Create a sender's directory user on their first message, with the platform default role; raises if it fails."""
    from agno.os.auth import aprovision_user_with_default_role
    from agno.os.middleware.jwt import is_reserved_principal

    state = getattr(ctx.app, "state", None)
    user_store = getattr(state, "user_store", None)
    if user_store is None or not getattr(state, "user_auto_provision", False) or is_reserved_principal(principal):
        return
    await aprovision_user_with_default_role(user_store, getattr(state, "role_store", None), principal, claims)


async def refuse(
    client: Any, event_context: "EventContext", user: Optional[str], text: str, thread_ts: Optional[str]
) -> None:
    """Tell a refused person why with an ephemeral; another app cannot see one, so its refusal is only logged."""
    if user is None:
        log_debug(f"Slack event skipped: another app was refused ({text})")
    else:
        await post_ephemeral(client, event_context.channel, user, text, thread_ts)


async def authorize_sender(ctx: "SlackContext", event_context: "EventContext", client: Any) -> bool:
    """Run a message as its sender's directory user, created on their first message; that user's roles decide."""
    event = event_context.event
    other_app = await is_other_app(ctx, client, event.get("user") or "", event.get("bot_id") or "")
    user = None if other_app else event_context.owner
    thread_ts = event_context.thread_ts
    state = getattr(ctx.app, "state", None)
    fail_closed = bool(getattr(state, "user_directory_fail_closed", False))
    # Failing open is a UserDirectory(fail_closed=False) choice; without a directory a sender never runs unchecked
    if getattr(state, "user_store", None) is None:
        fail_closed = True
    try:
        if other_app:
            principal = await app_principal(ctx, client, event, event_context.team_id)
        else:
            principal = await member_principal(ctx, client, event_context.owner, event_context.team_id)
    except LookupError:
        log_warning(f"Slack lookup failed for {event_context.owner!r} (failing {'closed' if fail_closed else 'open'})")
        if fail_closed:
            await refuse(client, event_context, user, _SLACK_UNAVAILABLE_MESSAGE, thread_ts)
            return False
        # Failing open runs it unchecked, as without authorize_senders; no email user or app is known without Slack
        if ctx.resolve_user_identity or other_app:
            return True
        # A slack:{workspace}:{id} user needs no lookup, so its disabled switch and roles still apply
        principal = f"slack:{event_context.team_id}:{event_context.owner}"
    if principal is None:
        reason = _NOT_IN_APPS_MESSAGE if other_app else _NOT_A_MEMBER_MESSAGE
        await refuse(client, event_context, user, reason, thread_ts)
        return False
    # A principal from apps= is mapped, like users=, so no user is created for it
    if not (other_app and ctx.apps is not None):
        claims: Dict[str, Any] = {"email": principal} if "@" in principal else {}
        if event_context.display_name:
            claims["name"] = event_context.display_name
        try:
            await provision_sender(ctx, principal, claims)
        except Exception as e:
            log_warning(
                f"user directory check failed for {principal!r}: {e} (failing {'closed' if fail_closed else 'open'})"
            )
            if fail_closed:
                await refuse(client, event_context, user, _DIRECTORY_UNAVAILABLE_MESSAGE, thread_ts)
                return False
            # Roles are usually stored with the directory, so failing open runs it unchecked
            return True
    if not await authorize_run(ctx, event_context, principal, client, user, thread_ts):
        return False
    event_context.user_id = principal
    return True


async def authorize_unmapped(
    ctx: "SlackContext",
    event_context: "EventContext",
    client: Any,
    user: str,
    thread_ts: Optional[str] = None,
) -> bool:
    """Authority of a run whose owner is not in users=: the default role's; else no roles on Super Agent, else none."""
    # The member acts and is recorded as themselves; the default role only supplies the permissions
    if ctx.default_role is not None:
        return await authorize_run(
            ctx, event_context, event_context.user_id, client, user, thread_ts, roles=[ctx.default_role]
        )
    # Without a default role only Super Agent (ctx.company is set) is checked, with no roles; others run unchecked
    if ctx.company is None:
        return True
    event_context.authority = no_roles_authorization(ctx.app, event_context.owner)
    return True


async def authorize_run(
    ctx: "SlackContext",
    event_context: "EventContext",
    principal: str,
    client: Any,
    user: Optional[str],
    thread_ts: Optional[str] = None,
    roles: Optional[List[str]] = None,
) -> bool:
    """Set the run's platform authority for a principal; a refused person gets the "Not run" ephemeral."""
    try:
        if ctx.company is not None:
            event_context.authority = await ctx.company.authorize(ctx.app, principal, ctx.entity_id, roles)
        else:
            event_context.authority = await resolve_principal_authorization(
                ctx.app, principal, ctx.resource, ctx.entity_id, roles
            )
    except PermissionError as e:
        await refuse(client, event_context, user, f"Not run: {e}", thread_ts)
        return False
    return True
