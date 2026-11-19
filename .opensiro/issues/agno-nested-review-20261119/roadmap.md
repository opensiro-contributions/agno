# Agno capability roadmap receipt — 2026-11-19

## Identity and pins

- Original repository: agno-agi/agno
- Original HEAD: 365c9c7e74719c1d20b557178add8c65f27a4426
- Observed at: 2026-11-19
- Accepted Index assessment: https://github.com/opensiro/vsm-harness-index/blob/34e11ec4dd52e1ba3ee0111d8bca73f13918f54f/assessments/ag/agno.md
- Accepted assessment blob SHA: e4ccb129a7a67baaca7c84b50f6f9820462d4382
- Accepted review ref: 44219f8532e2fe6ce936850455f4b9a2567e4194
- Accepted reviewed at: 2026-09-15
- System in focus: Agno native Workflow with nested HumanReview, related Team/evaluation but no private plugins
- Profile version: 0.2.1
- Assessment procedure version: 0.3.1
- Last assessed source check: 2026-09-16 at cbc10df7c7d377ce86f8d8f9c1e8c364fd94334d (64 days old)
- Result: NEEDS_EVIDENCE
- Terminal operator decision: NO_GO
- External issue: DRAFT — NOT PUBLISHED
- Cost status: NOT_MEASURED

## Rights and authority

[Original Apache-2.0 LICENSE](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/LICENSE) and [CONTRIBUTING](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/CONTRIBUTING.md) read. The latter requires external PR reference to a `ready`-labeled issue and AI disclosure. [#10935](https://github.com/agno-agi/agno/issues/10935) OPEN, no `ready` label or assignee at observation; CLA/DCO remain UNVERIFIED. Verified new fork [`opensiro-contributions/agno`](https://github.com/opensiro-contributions/agno) is correctly parented; initial metadata owner control is deliberately `PAUSE` and attention `DORMANT`. No product implementation, external or fork public issue/PR consent; initial bootstrap is the only authorized write.

## Existing work / overlap

[Accepted historical six-function assessment](https://github.com/opensiro/vsm-harness-index/blob/34e11ec4dd52e1ba3ee0111d8bca73f13918f54f/assessments/ag/agno.md) is **`S1=A · S2=A · S3=A · S3*=— · S4=— · S5=—`**. This is not the current HEAD grade. First-party [`workflow.py`](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/workflow/workflow.py) has top-level `step_pause_status` and `check_output_review_status`; nested [`condition.py`](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/workflow/condition.py) and [`types.py`](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/workflow/types.py) do not establish child review propagation and explicitly exclude Parallel child pause. Original #10935 documents the ignored flags and remains OPEN. No directly matching #10935 PR found in bounded live PR search; status of unrelated heads not treated as proof. Adjacent [#11284](https://github.com/agno-agi/agno/issues/11284) OPEN and [PR #11342](https://github.com/agno-agi/agno/pull/11342) CLOSED UNMERGED, as [`hitl.py`](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/workflow/utils/hitl.py) still defaults to no review on predicate exception. Do not open a duplicate original Issue.

## Function ownership

S1=A operating agents, S2=A task coordination and S3=A current-team management are accepted historical. Review by an operator under `HumanReview` is a parent-owned gate, not an independently agent-owned S3* corrective audit. Standalone [`AgentAsJudgeEval`](https://github.com/agno-agi/agno/blob/365c9c7e74719c1d20b557178add8c65f27a4426/libs/agno/agno/eval/agent_as_judge.py) does not demonstrate a connected independent reviewer → corrected worker output → later operations. S3*=— historical; no C proof, no S4 future loop, no S5 policy transfer.

## Capability priority

- **P0:** safe native nested HumanReview behavior only (not a new S3* constructor): reject unsupported child flags before work or implement complete pause/review/resume for specifically supported containers.
- **P1:** maintainer decides support or reject contract in existing #10935, adds `ready` if desired, tests sync/async negative/positive and no dependent publish bypass.
- **P2:** NONE. S3* C materiality and ownership gaps remain; no speculative upgrade quota.
- **Terminal decision:** **NO_GO now** to a new VSM S3* construction; address existing native issue as a separate eligible repair if maintainer permits. This is the final roadmap verdict, not an interim continuation request.

## Implementation options

Cheapest original-native fix: explicit validation error for unsupported nested `human_review`. More capable alternative when actually required: propagate native pause/review/corrected-output continuation through Condition/Loop/Steps/Router, with Parallel only when safely supported; no bypass and persisted review state. Conditional S3* constructor would need independent auditor with alternative evidence access, selectable correction judgment, scoped authority and observed return to worker work; **not currently qualified**. [Human layer](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/issue.md) and [separate AI contract](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/constructor-sufficiency.md) contain complete hypotheses and N1–N7 proposed tests (not executed).

## Specification and domain alternatives

Do not alter Profile or Skills without a separate reproducible semantic counterexample. A legally permitted optional domain fork may compare independent review composition against the native solution, but no domain experiment or patch is currently mandated. `A/C/P` are ownership configurations, not a maturity ladder.

## Cost experiment

`NOT_MEASURED`: same nested draft/review/publish workflow in existing native fail-loud/pausing path versus independent S3* composition; track initial engineering, review/test, integration, recurring maintenance and verified user outcome. No claimed savings.

## Delivery and publication

**PLAN_ONLY**; `Result: NEEDS_EVIDENCE` as a narrative research label; **final decision NO_GO now**. New matching public fork created, default branch untouched, only initial `opensiro/meta` metadata case bootstrap planned. [Human](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/issue.md) ↔ [AI](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/constructor-sufficiency.md) ↔ [case README](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/README.md). [Exact proposed public fork Issue](https://github.com/opensiro-contributions/agno/blob/opensiro/meta/.opensiro/issues/agno-nested-review-20261119/fork-issue-draft.md) is **DRAFT — NOT PUBLISHED**. No product implementation, contribution record, public fork Issue, external issue/comment/PR or native test claimed. Owner PAUSE must be handled and exact current-conversation publication approval is needed before public issue publication.
