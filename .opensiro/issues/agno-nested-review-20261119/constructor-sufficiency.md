# Agno — nested HumanReview and S3* constructor sufficiency (AI/developer contract)

**Status:** `PLAN_ONLY / NEEDS_EVIDENCE`; **terminal decision: NO_GO now** for a new S3* constructor. **No implementation and no public Issue/PR.** [Human decision](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/issue.md) · [Receipt](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/roadmap.md). The P0/P1/P2 contract below mirrors the Human document.

## Functional scope and historical state

**ACCEPTED INDEX (historical at 2026-09-15): `S1=A · S2=A · S3=A · S3*=— · S4=— · S5=—`** · [pinned assessment](https://github.com/opensiro/vsm-harness-index/blob/34e11ec4dd52e1ba3ee0111d8bca73f13918f54f/assessments/ag/agno.md), blob `e4ccb129a7a67baaca7c84b50f6f9820462d4382`, review `44219f8532e2fe6ce936850455f4b9a2567e4194`, Profile 0.2.1, Skills assessment 0.3.1. [Current original `365c9c7e74719c1d20b557178add8c65f27a4426`](https://github.com/agno-agi/agno/commit/365c9c7e74719c1d20b557178add8c65f27a4426) is **not** reassessed here.

| Function | Historical owner | Treatment |
| --- | --- | --- |
| S1=A | Agent/member operation | Preserve |
| S2=A | Team coordination | Preserve |
| S3=A | Leader-owned current team task decisions | Preserve; approval middleware is not S3 ownership |
| S3*=— | No qualifying independent complementary audit closure established | S3* C is **not proven** by existing HITL/evaluation |
| S4=— | No external future-option/S3↔S4 witness in scope | Exclude |
| S5=— | Parent legitimate ultimate policy | Exclude; no autonomous S5 promotion |

**System in focus:** first-party Agno Workflow execution graph, nested child Steps, existing human review/resume interfaces and any first-party evaluation/teams bridge. Current issue [#10935](https://github.com/agno-agi/agno/issues/10935) describes a draft → review → publish safety violation. No provider plugins, private agent model, tenant governance, original maintainer powers or external policy changes are admitted.

## 1. Observed source, user outcome and counterfactual

- [`workflow.py`](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/workflow/workflow.py) has top-level `step_pause_status` and `check_output_review_status` calls; verified in read-only current source.
- [`condition.py`](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/workflow/condition.py) manages child step execution, but equivalent child `check_output_review_status` coverage is not evidenced at pinned HEAD.
- [`types.py`](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/workflow/types.py) restricts review mode by component and says Parallel children cannot individually pause. This offers a native **fail-loud contract**, avoiding invented machinery.
- [`hitl.py`](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/workflow/utils/hitl.py) separately has an exception-as-no-review path, tracked by [#11284](https://github.com/agno-agi/agno/issues/11284); [PR #11342](https://github.com/agno-agi/agno/pull/11342) is closed without merge. Adjacent issue, not the P0 expansion.
- [`AgentAsJudgeEval`](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/eval/agent_as_judge.py) is an evaluation class, **not evidence** that a live team/workflow has an independent complementary auditor with compulsory corrective return.
- [#10935](https://github.com/agno-agi/agno/issues/10935) OPEN at observation, no `ready` label or assignees. No same-number relevant PR found in bounded search. Issue reproduction ran on a *past* revision; we did not execute it at `365c9c7e74719c1d20b557178add8c65f27a4426`.

**Native counterfactual:** reject a nested child `human_review` configuration when unsupported, or make the same first-party `HumanReview` genuinely pause/resume all selected supported nested modes. Either protects user intent without a new S3* agent. The owner may choose which; independent S3* C functionality remains unqualified.

## 2. Shipped vs issue-only vs unverified

| Element | Status and source | Right and correction path |
| --- | --- | --- |
| Top-level `Step` output/confirmation pause | SHIPPED at `workflow.py` and `hitl.py` | Human reviewer decides approved/rejected/edited output; runtime enforces gate |
| Nested child Step gate | ISSUE_ONLY #10935: unsupported/bypassed path described; current source inspection supports concern | Whether support or early rejection is chosen belongs to Agno maintainers |
| Nested `Parallel` child pause | Explicitly unsupported by `types.py` docs | Must fail visibly, not forge review |
| `AgentAsJudgeEval` | SHIPPED evaluation utility | Independent audit **decision-to-operational-correction closure unverified** |
| S3* first-party C constructor | MISSING WITNESS / NOT QUALIFIED | No verified independent reviewer actor wiring, mandatory correction, durable return, later observation |
| Native overlap | #10935 OPEN; #10204 historical; #11284 OPEN; #11342 CLOSED UNMERGED | Do not open duplicate original Issues; first-party PRs require `ready` label |

## 3. Conditional construction ports — why S3* C is not approved

These are **conditional sufficiency questions**, not installation instructions or asserted available APIs:

| Function-specific port | Input → output | Decision and ownership | Current evidence |
| --- | --- | --- | --- |
| Independent review source | Completed S1 worker output, provenance and immutable context → auditable review case | Access must be sufficiently independent from the worker's self-report | First-party result objects exist; independence not evidenced |
| Reviewer choice | Developer-selected independent evaluator → `accept / request_changes / reject` grounded in evidence | Reviewer, not core hardcoding nor worker self-approval, owns actual audit judgment | `HumanReview` grants human gate; `AgentAsJudgeEval` is separate utility; no closed hook established |
| Bound corrective action | `request_changes` → return to original responsible work with scope/attempt limit | Preserve S3 ownership, no cross-tenant or parent-policy bypass | Workflow `OnReject.retry` exists, but same reviewer/evidence connection unverified |
| Durable reviewer feedback | Reviewed revision and result → a later resumed Step/Team task and traceable disposition | Enforcement and feedback must reach subsequent operations | Existing HumanReview can resume top-level; no independent S3* return shown |
| Supported distribution | Developer can wire above via public first-party supported interfaces | Missing reviewer/rights = refuse or fall back to existing authorized human gate | No new C claim or native proof |

**Sufficiency verdict:** `NEEDS_EVIDENCE`, **NO_GO now**. The five-port map is a falsification plan, not a proposed speculative patch quota. A future valid S3* C requires all links, real user value over native HITL, and native tests; it would need fresh assessment separately if shipped.

## 4. P0/P1/P2 and minimum native course

- **P0 — safe nested HumanReview (not a C target):** fix #10935 in the existing Agno path. Minimum conservative fix: reject child review flags in unsupported container modes at construction; optional nested pause/resume only where full state/requirements propagation is supported and maintainers request it.
- **P1A — maintainer contract decision:** resolve support-vs-reject per Condition, Loop, Steps, Router, Parallel; obtain issue `ready` before any external PR, check assignment and PR overlap afresh.
- **P1B — executable native positive/negative tests:** cover declared supported modes and unsupported rejection, pause/resume persistence, sync/async and ordinary top-level compatibility.
- **P1C — authority and feedback:** reviewer rejection/edit must not silently advance the dependent `publish`; no bypass on validation or storage failure.
- **P2: NONE** — no second independent constructor or S4/S5 scope.

## 5. Acceptance scenarios — source-native design, NOT RUN

| Case | Setup and reviewer actor | Expected real result | Negative/falsification |
| --- | --- | --- | --- |
| N1 — nested output-review integrity | #10935 draft Step requiring output review under a sequential container | Either constructor refuses unsupported mode or workflow reaches paused state and **publish does not execute** | Silent continue with publish executed |
| N2 — confirmation before side effect | Nested Step requiring pre-execution confirmation | Reviewer holds/denies before draft side effect; refusal is explicit if unsupported | Step executes before confirmation |
| N3 — reviewer correction | Supported nested path, reviewer rejects/edits and requests retry | Only approved/corrected output enters downstream task; observable continued run | Original unreviewed output accepted |
| N4 — Parallel compatibility | Parallel child requiring HumanReview | Explicit rejection before concurrent execution if pause unsupported | Silent drop of review requirement |
| N5 — existing top-level behavior | Top-level HumanReview with documented cookbook | Pause/resume/edit remains compatible | Regressed prior supported mode |
| N6 — qualified S3* negative | No separate independently empowered auditor | Do **not** classify as S3*=C regardless of N1–N5 | Claimed C from generic approval guardrail |
| N7 — original-native cost counterfactual | Same draft/review/publish case with basic fail-loud fix | Compare effort/maintenance with S3* constructor only after genuine new demand | No material extra operator value implies NO_GO |

Tests **NOT RUN**. Starting references: [#10935 reproduction](https://github.com/agno-agi/agno/issues/10935), [native full review cookbook](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/cookbook/04_workflows/08_human_in_the_loop/output_review/05_full_review_cycle.py), [human-review type validation](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/workflow/types.py). Choose actual test file/command only within a later implementation and verify CI, don't pretend these scenarios passed.

## 6. Falsification, risks, cost and rights

A `HumanReview` gate is human parent control, **not autonomous complementary audit** by default. A standalone `AgentAsJudgeEval` run without a separate legitimate reviewer judgment and correction reaching later workflow is not a first-party S3* constructor. Do not add policy identities, self-approving auditors, generic event buses, fake labels or six new VSM subsystems.

Fork [`opensiro-contributions/agno`](https://github.com/opensiro-contributions/agno) verified parent `agno-agi/agno`, Apache-2.0. New metadata bootstrap starts `PAUSE/DORMANT` absent attributable ALLOW; that forbids subsequent effectful actions without proper owner control. No product branch, independent review PR, original PR, issue comment or public fork Issue authorized. Original `CONTRIBUTING.md` requires `ready` and AI disclosure. CLA/DCO: **UNVERIFIED**, so no external PR assumed. Cost `NOT_MEASURED`, no independent audit or native test execution.

**Terminal operator decision: NO_GO now** to new S3* C construction. Instead keep #10935 as the source-native resolution locus, with an explicit maintainer support/reject choice and tests; separate owner action required for implementation. [Back to Human Issue](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/issue.md).
