# Public fork Issue draft — NOT PUBLISHED

**Destination:** https://github.com/opensiro-contributions/agno/issues (new public fork Issue)
**Action:** create one fork-local GitHub Issue; **NOT authorized in this conversation**.
**Title:** Agno — nested HumanReview safety and S3* sufficiency roadmap (OpenSiro plan-only)

## Exact proposed public body

# Agno — nested HumanReview safety and S3* sufficiency roadmap (OpenSiro plan-only)

**OpenSiro · PLAN_ONLY / NEEDS_EVIDENCE · Decision: NO_GO now · DRAFT — NOT PUBLISHED**

[Human decision](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/issue.md) · [AI/developer contract](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/constructor-sufficiency.md) · [Receipt](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/roadmap.md) · [Fork](https://github.com/opensiro-contributions/agno)

## 1. Why OpenSiro and accepted historical VSM assessment

OpenSiro studies whether reusable VSM-informed organizational specifications can standardize agent-harness development and reduce total engineering, integration, and maintenance cost. This is a hypothesis, not a measured saving or an obligation for Agno maintainers.

**ACCEPTED INDEX — HISTORICAL STARTING POINT, NOT A CURRENT/TARGET GRADE: `S1=A · S2=A · S3=A · S3*=— · S4=— · S5=—`**  
[Accepted assessment pinned to Index 34e11ec4dd52](https://github.com/opensiro/vsm-harness-index/blob/34e11ec4dd52e1ba3ee0111d8bca73f13918f54f/assessments/ag/agno.md) · assessment blob `e4ccb129a7a67baaca7c84b50f6f9820462d4382` · `review_ref=44219f8532e2fe6ce936850455f4b9a2567e4194` · reviewed 2026-09-15 · Profile 0.2.1 / assessment procedure 0.3.1.

| Function | Accepted | Meaning and current decision |
| --- | --- | --- |
| S1 Operations | A | Autonomous agent/team operation; no mandatory C work |
| S2 Coordination | A | First-party task interdependence and routing; preserve |
| S3 Current control | A | Agent team leader regulates tasks/assignments; no mandatory C work |
| S3* Independent complementary audit | — | No accepted closed independent review channel; nested human approval is **not** proof of autonomous S3* |
| S4 Future adaptation | — | No source-backed external/prospective adaptation target in this case |
| S5 Identity/policy | — | Reserved ultimate policy is not transferred by an approval hook |

**Boundary:** Agno first-party `Workflow`, `Step`, `HumanReview`, nested `Condition/Loop/Parallel/Steps/Router`, and its neighboring team/eval capabilities. Original HEAD: [`365c9c7e74719c1d20b557178add8c65f27a4426`](https://github.com/agno-agi/agno/commit/365c9c7e74719c1d20b557178add8c65f27a4426), observed 2026-11-19; this HEAD differs from historical Index review. Last accepted review is 65 days old: recommend source-pinned Index reassessment, but do not block source analysis. License Apache-2.0. [Contribution rules](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/CONTRIBUTING.md) require a maintainer `ready` label before external PRs and AI disclosure. CLA/DCO and external acceptance are not asserted.

## 2. Operator outcome and decision

**User task:** an operator enables review for a nested draft step and expects a later publish step not to run before the reviewer has acted. [Original issue #10935](https://github.com/agno-agi/agno/issues/10935) is open, without `ready` label/assignee at observation. It documents `human_review` ignored for child Steps inside Condition, Loop, Parallel, Steps and Router. [Current top-level pause handling](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/workflow/workflow.py) handles top-level checks; [nested components](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/workflow/condition.py) do not show equivalent child review propagation. [Type validation](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/workflow/types.py) already rejects unsupported review flags for some container types.

**Best native alternative:** resolve #10935 **without new organizational machinery**. Preserve the existing top-level `HumanReview` and choose one of two maintainer-approved native contracts: (a) implement an actual nested pause/review/resume chain where supported; or (b) reject unsupported nested review flags at construction so unsafe workflows cannot silently proceed. In particular, Parallel explicitly documents that child pause is unsupported; fail-loud validation is safer than pretending child review works.

**Potential S3* construction:** an independent developer-composed reviewer of operational results with separate evidence access, legitimate review decision, corrective return to the worker, enforced resumption and observed later result. `HumanReview` is a parent approval path, and [`AgentAsJudgeEval`](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/eval/agent_as_judge.py) is a separate evaluation facility: neither source, alone, proves a connected independent corrective workflow. Do **not** claim S3*=C from this bug.

## 3. Native overlap and remaining gap

| Scope | First-party observed / external status | Remaining verified need |
| --- | --- | --- |
| Nested HITL | `workflow.py` top-level pre-/post-step pause checks; #10935 OPEN, no matching #10935 PR located | Current nested child review can be silently bypassed; first choose reject-vs-pause behavior |
| Output review failure | [Issue #11284](https://github.com/agno-agi/agno/issues/11284) OPEN; [PR #11342](https://github.com/agno-agi/agno/pull/11342) CLOSED UNMERGED; [`hitl.py`](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/workflow/utils/hitl.py) still defaults false on predicate exception | Separate native fail-closed repair, not folded into this roadmap |
| Complementary S3* | Standalone `AgentAsJudgeEval` plus human review, no source-backed end-to-end corrective reviewer return established | No evidenced new C constructor demand, owner, lawful modes or measured native-vs-C benefit |

## 4. Priority, P0/P1/P2 and sufficiency

| Priority | Decision | Minimum useful result |
| --- | --- | --- |
| **P0 — safe nested review** | **Source-native bug remediation only; NOT a qualified S3* C proposal** | Unsupported child review rejected at construction **or**, if maintainers elect support, real pause/review/resume blocks the dependent publish step |
| **P1 — prerequisites** | Maintainer decides allowed nested modes; obtain `ready` before any external PR; preserve sync/async and streaming/resume behavior | First-party tests for positive pause, reject/unknown, downstream no-publish, parallel refusal and compatibility |
| **P2** | **NONE** | No speculative separate S4, S5, S3 or second review controller |

**C sufficiency verdict:** `NEEDS_EVIDENCE` for S3*. A future independent first-party review constructor would require evidence source, independently selected reviewer decision actor, scoped rights, a durable correction request, enforced worker return/re-run and a traceable acceptance result. Current #10935 only substantiates human-review safety. [Detailed conditional ports and negative acceptance](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/constructor-sufficiency.md); **no new C grade or software is claimed**.

## 5. Acceptance and stop gates (proposed, not executed)

- **A1 — no bypass:** configure nested output review. A dependent publish must not run unreviewed; either fail construction or actually pause before publication.
- **A2 — lawful correction:** if nested support is chosen, reviewer rejection/edit must return to the correct task and only the reviewed version may continue.
- **A3 — unsupported mode:** Parallel child HITL that cannot pause is explicitly refused, not silently ignored.
- **A4 — compatibility:** a top-level `HumanReview` still pauses/resumes normally; unaffected steps retain behavior across supported sync/async paths.
- **A5 — independent S3* falsification:** without a genuinely independent reviewer and corrective return, no S3* constructor claim, even if all A1–A4 pass.
- **A6 — cost:** compare native safety repair with a hypothetical constructor for the same user workflow. `NOT_MEASURED`; no savings claimed.

Native tests: **NOT RUN** (plan-only source investigation). External PR: **NOT PUBLISHED**; issue #10935 has no `ready` label. Fork Issue: **NOT PUBLISHED**; requires separate exact current-conversation approval and owner-control handling.

## 6. Independent participation paths

Native: fix or clarify existing #10935 first, respecting its maintainer decision. Method: challenge [Profile](https://github.com/opensiro/vsm-harness-profile) or [Skills](https://github.com/opensiro/vsm-harness-skills) only with separate evidence. Domain-specific fork: optional lawful experiment, not mandatory upstream implementation.

## 7. Engineering cost

`NOT_MEASURED`. A paired test would measure the same nested review → dependent publish task using supported native fail-loud/pause behavior versus an independently justified S3* composition, including implementation, tests, review, maintenance, and regression costs.

## 8. Final decision and handoff

**Terminal operator decision: NO_GO now** to a new VSM S3* constructor in Agno. The bug is real and better addressed first under original [#10935](https://github.com/agno-agi/agno/issues/10935), with native support-or-reject semantics and maintainer `ready` gating; that corrective work is **not authorized by this plan**. No C proof, Index regrade, new public issue/PR or claimed savings.

**Research disposition:** `NEEDS_EVIDENCE` for additional C utility, but the current decision is final rather than a request to continue. Conditional unlock for reconsidering S3*: an actual user requirement for independent reviewer-led correction beyond native human HITL, a legitimate first-party ownership/return design, and a matched native alternative and cost test.

**AI/developer contract:** [`constructor-sufficiency.md`](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/constructor-sufficiency.md) preserves the same vector/P0/P1/P2 and decision; [receipt](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/roadmap.md).

**AI disclosure:** prepared with AI assistance. No independent human review, native test execution, maintainer endorsement or proven cost advantage claimed.

