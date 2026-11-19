"""authorize_senders runs an agent, team or workflow as each Slack sender's AgentOS directory user."""

from unittest.mock import AsyncMock, patch

import pytest

pytest.importorskip("slack_sdk", reason="slack_sdk not installed")

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.os import AgentOS, UserDirectory
from agno.os.authz import Authorization
from agno.os.interfaces.slack.handlers import handle_message

from .conftest import make_async_client_mock, make_ctx, make_event_body

_EXECUTOR = "agno.os.interfaces.slack.handlers.executor"
SECRET = "slack-directory-secret-at-least-32-bytes"
SENDER = "slack:T123:U123"
DENIED = "Not run: Permission required: agents:agent-1:run"


def _app(tmp_path, default_role: bool = True, **directory_kwargs):
    """An AgentOS app with a user directory and a "member" role that may run agent-1."""
    auth = Authorization(verification_keys=[SECRET], algorithm="HS256")
    auth.define_role("member", ["agents:run"], default=default_role)
    db = SqliteDb(db_file=str(tmp_path / "os.db"))
    directory = UserDirectory(**directory_kwargs) if directory_kwargs else True
    agent_os = AgentOS(
        id="slack-directory",
        db=db,
        agents=[Agent(id="agent-1")],
        authorization=auth,
        user_directory=directory,
        telemetry=False,
    )
    return agent_os.get_app()


def _member(**fields):
    """A users.info response for U123, a full member of T123, with fields overridden."""
    member = {"id": "U123", "team_id": "T123", "profile": {"email": "test@example.com", "display_name": "Test User"}}
    member.update(fields)
    return {"ok": True, "user": member}


async def _send(ctx, member=None, **body_kwargs):
    """Handle one Slack message; users.info returns member, or raises it when it is an exception."""
    client = make_async_client_mock()
    if isinstance(member, Exception):
        client.users_info = AsyncMock(side_effect=member)
    elif member is not None:
        client.users_info = AsyncMock(return_value=member)
    with patch(f"{_EXECUTOR}.run_event", new_callable=AsyncMock) as run_event:
        await handle_message(make_event_body(**body_kwargs), client, ctx)
    return run_event, client


def _ephemeral(client):
    """The text of the last ephemeral, None when there was none."""
    return client.chat_postEphemeral.call_args.kwargs["text"] if client.chat_postEphemeral.called else None


@pytest.mark.asyncio
async def test_without_authorize_senders_nothing_changes(tmp_path):
    app = _app(tmp_path)
    run_event, client = await _send(make_ctx().bind(app))
    assert run_event.called and run_event.call_args.args[0].authority is None
    assert await app.state.user_store.acount() == 0


@pytest.mark.asyncio
async def test_sender_is_created_once_with_the_default_role_and_runs_as_it(tmp_path):
    app = _app(tmp_path)
    ctx = make_ctx(authorize_senders=True).bind(app)
    run_event, _ = await _send(ctx)
    event_context = run_event.call_args.args[0]
    assert (event_context.user_id, event_context.authority is not None) == (SENDER, True)
    user = await app.state.user_store.aget(SENDER)
    assert (user["name"], user["email"]) == ("Test User", None)
    assert await app.state.role_store.aroles_of(SENDER) == ["member"]
    await _send(ctx, ts="1700000000.000200", event_id="Ev2")
    assert await app.state.user_store.acount() == 1


@pytest.mark.asyncio
async def test_without_a_default_role_the_sender_waits_for_an_assigned_role(tmp_path):
    app = _app(tmp_path, default_role=False)
    ctx = make_ctx(authorize_senders=True).bind(app)
    run_event, client = await _send(ctx)
    assert not run_event.called and _ephemeral(client) == DENIED
    assert await app.state.user_store.aget(SENDER) is not None
    await app.state.role_store.aassign(SENDER, "member")
    run_event, _ = await _send(ctx, ts="1700000000.000200", event_id="Ev2")
    assert run_event.called


@pytest.mark.asyncio
@pytest.mark.parametrize("confirmed, principal", [(True, "test@example.com"), (False, SENDER)])
async def test_resolve_user_identity_uses_only_a_confirmed_email(tmp_path, confirmed, principal):
    app = _app(tmp_path)
    ctx = make_ctx(authorize_senders=True, resolve_user_identity=True).bind(app)
    run_event, _ = await _send(ctx, member=_member(is_email_confirmed=confirmed))
    assert run_event.call_args.args[0].user_id == principal
    assert await app.state.user_store.aget(principal) is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "fields, principal",
    [({"is_restricted": True}, SENDER), ({"team_id": "T_OTHER"}, "slack:T_OTHER:U123")],
    ids=["guest", "other-organization"],
)
@pytest.mark.parametrize("allowed", [False, True])
async def test_guests_and_external_members_need_allow_guests_and_external(tmp_path, fields, principal, allowed):
    app = _app(tmp_path)
    ctx = make_ctx(authorize_senders=True, resolve_user_identity=True, allow_guests_and_external=allowed).bind(app)
    run_event, client = await _send(ctx, member=_member(is_email_confirmed=True, **fields))
    assert run_event.called is allowed
    if allowed:
        # Kept apart by their workspace and member id; their email never names a user
        assert run_event.call_args.args[0].user_id == principal
    else:
        assert _ephemeral(client) == "Not run: Only members of this workspace can use this app"
        assert await app.state.user_store.acount() == 0


@pytest.mark.asyncio
async def test_disabled_sender_is_refused(tmp_path):
    app = _app(tmp_path)
    ctx = make_ctx(authorize_senders=True).bind(app)
    await _send(ctx)
    await app.state.user_store.aset_disabled(SENDER, True)
    run_event, client = await _send(ctx, ts="1700000000.000200", event_id="Ev2")
    assert not run_event.called and _ephemeral(client) == "Not run: User is disabled"


@pytest.mark.asyncio
@pytest.mark.parametrize("apps, principal", [(None, "slack:T123:A_OTHER"), ({"A_OTHER": "reviewer"}, "reviewer")])
async def test_another_app_runs_as_its_own_user_or_its_apps_mapping(tmp_path, apps, principal):
    app = _app(tmp_path)
    await app.state.role_store.aassign("reviewer", "member")
    ctx = make_ctx(authorize_senders=True, respond_to_other_apps=True, apps=apps).bind(app)
    ctx.bot_id, ctx.bot_user_id = "B_SELF", "U_SELF"
    run_event, client = await _send(ctx, user="", bot_id="B_OTHER", app_id="A_OTHER")
    assert run_event.call_args.args[0].user_id == principal
    # A mapped app is not added to the directory, like a member in users=
    assert await app.state.user_store.acount() == (0 if apps else 1)
    run_event, client = await _send(
        ctx, user="", bot_id="B_OTHER", app_id="A_UNMAPPED", ts="1700000000.000200", event_id="Ev2"
    )
    assert run_event.called is (apps is None)
    assert not client.chat_postEphemeral.called


@pytest.mark.asyncio
async def test_users_mapping_is_checked_first(tmp_path):
    app = _app(tmp_path)
    await app.state.role_store.aassign("alice", "member")
    ctx = make_ctx(authorize_senders=True, users={"U123": "alice"}).bind(app)
    run_event, _ = await _send(ctx)
    assert run_event.call_args.args[0].user_id == "alice"
    assert await app.state.user_store.aget(SENDER) is None
    run_event, client = await _send(ctx, user="U_UNMAPPED", ts="1700000000.000200", event_id="Ev2")
    assert not run_event.called
    assert _ephemeral(client) == "Your Slack account is not linked to an account on this AgentOS."


@pytest.mark.asyncio
@pytest.mark.parametrize("fail_closed", [True, False])
async def test_failed_lookup_and_unreachable_directory_follow_fail_closed(tmp_path, fail_closed):
    app = _app(tmp_path, fail_closed=fail_closed)
    ctx = make_ctx(authorize_senders=True).bind(app)
    run_event, client = await _send(ctx, member=RuntimeError("ratelimited"))
    assert run_event.called is not fail_closed
    if fail_closed:
        assert _ephemeral(client) == "Not run: Slack unavailable"
    else:
        # A slack: user needs no lookup, so failing open still runs it as that user, with its roles
        assert run_event.call_args.args[0].user_id == SENDER
    with patch.object(app.state.user_store, "aget", AsyncMock(side_effect=RuntimeError("db down"))):
        run_event, client = await _send(ctx, ts="1700000000.000200", event_id="Ev2")
    if fail_closed:
        assert not run_event.called and _ephemeral(client) == "Not run: User directory unavailable"
    else:
        # Roles are usually stored with the directory, so failing open runs it unchecked
        assert run_event.call_args.args[0].authority is None


@pytest.mark.asyncio
async def test_an_apps_incoming_webhook_runs_as_the_same_app(tmp_path):
    app = _app(tmp_path)
    await app.state.role_store.aassign("reviewer", "member")
    ctx = make_ctx(authorize_senders=True, respond_to_other_apps=True, apps={"A_OTHER": "reviewer"}).bind(app)
    ctx.bot_id, ctx.bot_user_id = "B_SELF", "U_SELF"
    client = make_async_client_mock()
    # A webhook post names only its own bot id; bots.info names the app
    client.bots_info = AsyncMock(
        return_value={"ok": True, "bot": {"id": "B_HOOK", "app_id": "A_OTHER", "name": "hook"}}
    )
    with patch(f"{_EXECUTOR}.run_event", new_callable=AsyncMock) as run_event:
        await handle_message(make_event_body(user="", bot_id="B_HOOK", subtype="bot_message"), client, ctx)
    assert run_event.call_args.args[0].user_id == "reviewer"


@pytest.mark.asyncio
async def test_failed_lookup_failing_open_keeps_the_disabled_switch(tmp_path):
    app = _app(tmp_path, fail_closed=False)
    await _send(make_ctx(authorize_senders=True).bind(app))
    await app.state.user_store.aset_disabled(SENDER, True)
    # A new interface has no cached lookup, as after a restart
    ctx = make_ctx(authorize_senders=True).bind(app)
    run_event, client = await _send(ctx, member=RuntimeError("ratelimited"), ts="1700000000.000200", event_id="Ev2")
    assert not run_event.called and _ephemeral(client) == "Not run: User is disabled"


@pytest.mark.asyncio
@pytest.mark.parametrize("fail_closed", [True, False])
async def test_a_webhook_whose_app_cannot_be_looked_up_creates_no_user(tmp_path, fail_closed):
    app = _app(tmp_path, fail_closed=fail_closed)
    ctx = make_ctx(authorize_senders=True, respond_to_other_apps=True).bind(app)
    ctx.bot_id, ctx.bot_user_id = "B_SELF", "U_SELF"
    client = make_async_client_mock()
    client.bots_info = AsyncMock(side_effect=RuntimeError("ratelimited"))
    with patch(f"{_EXECUTOR}.run_event", new_callable=AsyncMock) as run_event:
        await handle_message(make_event_body(user="", bot_id="B_HOOK", subtype="bot_message"), client, ctx)
    assert run_event.called is not fail_closed
    assert await app.state.user_store.acount() == 0
