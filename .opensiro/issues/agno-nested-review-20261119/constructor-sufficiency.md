# Agno — source-native S3* C-construction technical contract

**DRAFT — NOT PUBLISHED** · PLAN_ONLY · v0.18.2 same-case refinement of previously completed Wave 4.
**Human decision:** [issue.md](issue.md).
**Canonical decision receipt:** [roadmap.md](roadmap.md); receipt owns historical vector, priority and the unchanged terminal verdict.

## 1. Function-specific construction boundary and methodology checks

**Source and mode boundary:** Original [agno-agi/agno@e59ca576219e589136e53b6cff8d6677899cf95f](https://github.com/agno-agi/agno/commit/e59ca576219e589136e53b6cff8d6677899cf95f), first-party Team(mode=tasks), task-management tools and member-run lifecycle; AgentOS HTTP, Workflow HumanReview and application governance are adjacent native alternatives, not delegated S3* ownership.
**Target transition:** S3*=— -> S3*=C
**Six-function dependencies (S1/S2/S3/S3*/S4/S5):** Accepted current case [roadmap.md](roadmap.md) is S1=A / S2=A / S3=A / S3*=— / S4=— / S5=—. S1 member agents produce observable work; S2 TaskList/dependencies coordinate; S3 leader can retry/reassign/mark completion; S3* reviewer must own an independent challenge with effect; no S4 adaptation or S5 policy authority is granted.
**Function witness:** A Team member claims a task succeeded. Distinct configured auditor inspects independently obtainable artifact and trusted task/run terminal record, chooses ACCEPT, CHALLENGE or INCONCLUSIVE; first-party task/goal completion effect must be guarded before finalization. Challenged evidence and state return to the Team leader for lawful repair, followed by new evidence and re-audit.
**Counterfactual owner test:** With auditor removed while existing hooks/transport remain, the Team leader can mark a successful result completed without independent raw-evidence challenge; post-run scoring does not impose the same precommit decision.
**Possible methodological negative control:** A parent-verified HumanReview is human-owned, not autonomous S3*. A second model giving optional advice but no binding decision or return fails the S3* ownership contract. Existence of historical S3*=— is not proof of maintainer intent.
**Contributor / maintainer priorities:** NOT_STATED for an autonomous audit feature. Existing [#10935](https://github.com/agno-agi/agno/issues/10935) addresses human review correctness and must be handled separately.

## 2. Source-pinned baseline and parallel native Track A / on-top Track B

**Original native workflow:** [TaskMode tools](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/_task_tools.py) create/update tasks; execute_task dispatches member run, handles pause/errors, and marks completed when member returns; update_task_status directly permits manual completed; mark_all_complete sets goal_complete. [TaskList](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/task.py) persists current board.
**Closest existing solution:** [AgentAsJudgeEval](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/eval/agent_as_judge.py), [Team post-hooks](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/_hooks.py) and [first-party cookbook](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/cookbook/09_evals/agent_as_judge/agent_as_judge_team_post_hook.py) supply output evaluation and callbacks; application-level deterministic checks or parent HumanReview may be enough without an S3* construction.
**Relevant original Issues/PRs:** [#10935 open](https://github.com/agno-agi/agno/issues/10935) nested HumanReview; [#11585 merged](https://github.com/agno-agi/agno/pull/11585) resumed post-hook guardrails; [#11721 open](https://github.com/agno-agi/agno/pull/11721) AgentOS eval suites. These are not evidence of a first-party independent per-task audit-to-corrective-closure implementation. Partial search cannot prove all original PRs absent.

| Required C link or operator outcome | Track A: native coverage | Track B: smallest missing native integration | Falsifier |
| --- | --- | --- | --- |
| Independent raw-evidence task decision | Existing judge sees output; leader/worker controls claims | Developer-injected separately authorized evidence accessor + reviewer ACCEPT/CHALLENGE/INCONCLUSIVE | Current complete independent reviewer already makes identical task decision |
| Effect before claimed task/goal completion | [execute_task/update_task_status/mark_all_complete](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/_task_tools.py) can record complete without audit | Opt-in first-party guard before all completion transitions, including async/parallel/resume; binding audit receipt keyed to task/run/version | Unsupported bypass remains, or only after-run notification is possible |
| Corrective feedback bounded by parent | Leader owns retry/reassign, parent owns HITL/S5 | CHALLENGE yields source-linked task finding, leader reworks, distinct evidence is re-audited; stale/missing evidence holds only in enforce mode | Auditor impersonates parent authority or cannot return feedback into next operation |

**On-top distinctness:** A post_hook judge can rate final Team content but runs too late to serve as all-paths per-task acceptance. A reviewer assigned as ordinary Team member can be bypassed by S3's own completion tools. Only an opt-in native completion decision and feedback path is a qualified distinct architectural possibility; implementation and value not proved.
**Source ambiguity / rights blockers:** Exact raw artifact provenance, parent-authorized reviewer identity, remote run terminal status and async/race ownership must be tested. No current permission to add original code or talk to third-party maintainers; fork metadata state is ACTIVE/ALLOW only for internal analysis.

## 3. Minimal complete S3* first-party C construction

**Required property:** The original's task-mode runtime must let a developer compose a separately responsible autonomous audit actor, whose lawful independent evidence decision has an enforced downstream operational effect and a returned corrective feedback loop. Number of physical ports is not prescribed.

| Native component or port | Current Agno path / coverage | Minimum proposed change / composition | Decisive owner, effect and return |
| --- | --- | --- | --- |
| Per-task auditor invocation | [execute_task](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/_task_tools.py) has member run and task identity | Before writing TaskStatus.completed, optionally invoke independently configured reviewer on trusted member artifact/terminal identity | Auditor returns typed evidence decision, not worker's self-certification |
| Other task/goal completion paths | [update_task_status and mark_all_complete](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/_task_tools.py) update without independent audit | Same scoped guard for direct completion and goal closure, all supported async/stream/resume paths; no-reviewer deployment remains unchanged | First-party deterministic hold prevents leader bypass only in configured enforce mode |
| Return into existing S3 | [TaskList / leader retries](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/task.py) already handle assignments and failures | Append bound finding and evidence reference to task state; challenge leaves task noncompleted and leader can retry/reassign before re-audit | S3 leader owns repair; auditor alone owns independent evidentiary acceptance; parent owns final policy |
| Evidence, replay and parent rights | Existing run/session metadata and member artifacts are not automatically audit-grade | Verify versioned raw artifact, terminal receipt, non-forgeable decision reference, parent refusal and no stale replay | Missing or contradictory evidence INCONCLUSIVE; enforce mode blocks; no unauthorized policy escalation |

**Architectural C-sufficiency argument:** We compared (A) native after-run judge/post-hooks, (B) optional reviewer Team member, and (C) a narrow task-mode acceptance seam. A cannot veto task success; B is leader-bypassable; C could achieve independent audit closure if it truly binds all task and goal transitions and returns a finding to the existing leader. No generalized new supervisor is required. All source assumptions and tests remain prospective, not shipped evidence.
**Explicit non-goals:** Do not replace original #10935 HumanReview bug fix, authorize a new policy S5, mandate new S4, regrade Index or claim PR #11721 duplicates this separate hypothetical C chain.
**Implementation dependency graph:** P1 prove independent artifact/receipt+reviewer rights and enumerate every completion path → implement P0 opt-in precommit guard and task finding return → validate both non-reviewer backward compatibility and corrective re-audit across sync/async/parallel/resume → only after source evidence revisit product use or Index in separate workflows.

## 4. Priorities, optional alternative and stopping rules

**P0 and P1:** Receipt P0 = native optional S3* audit for Team(task-mode) with enforced accept/challenge/unknown and return; P1 = evidence/identity/bypass/parent bounds and tests. Never treat these as merged implementation tasks.
**P2:** NONE. No automatic Workflow adapter or second function.
**Alternative path:** Existing judge/post-hooks plus deterministic checks, or original-native nested HumanReview repair, is preferable when the user outcome only needs output evaluation or human approval and not independent autonomous operational audit.
**Stop:** Equivalent original-native independent evidence and completion control already shipped; no lawful independent evidence/decision owner; unavoidable completion bypass; failed authority or task-state feedback closure. Mere lack of product demand is not an architectural NO_GO by itself.

## 5. Future source-native acceptance — derive tests, do not copy a matrix

**Native test commands and entry points:** Source-backed current Agno team task and guardrail test directories include [unit Team hooks tests](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/tests/unit/team/test_hooks_guardrails.py) and [integration task streaming](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/tests/integration/teams/test_tasks_mode_streaming.py). Proposed acceptance tests below were NOT_RUN; no specific command is claimed executed.
**Positive functional closure:** Distinct reviewer reads real independent member artifact, challenges false task success before completed, Team leader reworks/reassigns from recorded finding, fresh ACCEPT allows completion.
**Independent alternative (where applicable):** The composed reviewer may lawfully ACCEPT verified success or CHALLENGE contradictory evidence using identical deterministic guard transport, distinguishing decision ownership from transport-only hooks.
**Negative authority and compatibility (where applicable):** Enforce mode must reject missing/stale/replayed/forged evidence; block direct status/goal bypass, parallel/race and resume, never bypass parent approval; no-reviewer deployments remain old behavior.
**Matched native alternative:** Compare identical tasks with existing judge/post_hooks and an independently composed reviewer; benefit and engineering cost cannot be claimed without an A/B result.

| Future native case (NOT_RUN) | Source-supported setup | Expected effect / return | Falsifier |
| --- | --- | --- | --- |
| False-success member claim | Team(mode=tasks) and verified contradictory artifact, configured reviewer | CHALLENGE leaves task open; leader receives finding, repair and re-audit ACCEPT | Task or goal becomes complete without audit |
| Absent/replayed/partial evidence | Force missing/obsolete terminal identity in enforce mode | INCONCLUSIVE holds; parent can abort; no forged certificate | Stale result opens completion |
| Mode and parent compatibility | Nonreviewer baseline and configured audit in sync, async, stream, resume | Baseline unchanged, all enforce paths bounded, parent approval retained | Any unguarded alternate completion or unauthorized right |

## 6. Proposal verdict, falsification, evidence ownership and handoff

**Proposal-stage decision:** GO
**Research disposition:** NEEDS_EVIDENCE
**Primary falsifier:** An already-existing independently owned binding same-task evidence audit, or evidence/authority/completion holes preventing lawful complete S3* chain. GO is conditional hypothetical C sufficiency, not a shipped C grade.
**Validation state:** NOT_RUN for native product acceptance, tests, and cost experiments; the historical unrelated HumanReview reproduction is not this test.
**Ownership of truth:** Profile governs semantics, Skills procedure, Index historic general assessment, original Agno implementation/adoption, [roadmap.md](roadmap.md) this case's proposal decision; neither this technical companion nor a model reviewer replaces these authorities.
**Cost status:** NOT_MEASURED.
**Next permitted action:** Same-case internal template/source evidence maintenance only; future product native A/B must follow original maintainers' permissions and separate approvals.
**Human backlink:** [issue.md](issue.md).
**case receipt:** [roadmap.md](roadmap.md).
**AI disclosure:** Prepared with AI assistance, no independent human validation, native runtime execution or original external publication implied. **DRAFT — NOT PUBLISHED**.
