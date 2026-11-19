# Agno — technical constructor sufficiency, independent v0.18 rerun

**Target transition:** NO_QUALIFIED_C_TARGET
**Proposal-stage decision:** NO_GO
**Research disposition:** NO_USEFUL_CHANGE

Read [roadmap.md](roadmap.md) for source pins and final decision and [issue.md](issue.md) for the user-facing six-function table. Do not infer C merely because historical S3* is not present.

## Source-first chain

Current pinned [original main](https://github.com/agno-agi/agno/commit/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd) is distinct from included Index [accepted Agno](https://github.com/opensiro/vsm-harness-index/blob/c2e43bf4750841277b3e58d8ba80314121734764/assessments/ag/agno.md) reviewed 2026-09-15 at 44219f8532e2fe6ce936850455f4b9a2567e4194, assessment blob e4ccb129a7a67baaca7c84b50f6f9820462d4382; historical S1=A, S2=A, S3=A, S3*=—, S4=—, S5=— is not a current reassessment. Do not edit the Index.

- [Agent S1](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/agent/agent.py): model/tool work, structured response, pre/post hooks.
- [Team S2/S3](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/team/_task_tools.py): shared TaskList, assignments, dependencies, results, retries/replan, task-mode leader.
- [Native review/eval](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/eval/agent_as_judge.py): separately configured evaluator_agent, criteria, binary/numeric scoring, on_fail callback; not independent evidence or enforced correction by itself.
- [Workflow HumanReview](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/workflow/workflow.py): top-level pause/review path; current [#10935](https://github.com/agno-agi/agno/issues/10935) documents unresolved nested-container consistency.
- [Current related issues #11742](https://github.com/agno-agi/agno/issues/11742) team USD budget cookbook, [#11749](https://github.com/agno-agi/agno/issues/11749) historical tool_args mutated by a consumer, and [#11756](https://github.com/agno-agi/agno/issues/11756) provider-model retirement/defaults. None independently supplies a new accepted C witness.

## Track A — cheapest complete native response

Exact original #10935 requests either nested HumanReview honoring pause semantics, or explicit rejection of unsupported nested flag for Condition/Loop/Steps/Router/Parallel. Correctness under existing parent human policy is primary; adding independent agent review while leaving a fail-open approval boundary would not solve it. Native fix must be explicitly chosen by maintainers; linked review PR requires original issue with ready label.

For output checks, start from existing pre/post_hooks and AgentAsJudgeEval plus deterministic artifact verification, not a fresh custom VSM control plane. For cost control, #11742 already proposes hooks and nested budget slices. For mutable tool receipts, #11749 describes a conventional snapshot/immutable-history bug. These should not be silently escalated into S3*, S4 or S5 ownership gaps.

## Track B — hypothetical S3* mechanism and why not qualified

A qualifying *different* function would have independent observational access to operational artifacts/events (not only self-reported model output), a separate reviewer identity and sufficient decision authority, a durable evidence/provenance record, and enforcement of a lawful feedback signal changing subsequent Team/Workflow operations. Human safety gates and S5 policy must remain with parent/deployment. A LLM judge alone, a post_hook alone, or a text claim of independent review cannot establish this.

No current user scenario demonstrates such additional authority/closure is needed **beyond** native review semantics and hooks. No side-by-side model/user-quality/cost comparison exists. Therefore P0=NO_QUALIFIED_C_TARGET and NO_GO, not GO/NEEDS_EVIDENCE. This is a terminal proposal-stage decision, not a diagnosis that Agno has no need for the original bug fix.

## Falsifiable acceptance and negatives, not executed

| Case | Native witness/test | Outcome needed before considering new C |
| --- | --- | --- |
| A1 | Original nested HumanReview on top-level and all 5 container types | Maintainer-approved pause or explicit reject, no silent continue |
| A2 | Async and streaming nested HumanReview | Same parent-review safety guarantees as the supported sync path |
| A3 | Existing post_hook / AgentAsJudgeEval with deterministic evidence | Detect incorrect outputs and record result without adding separate control plane |
| B1 | Distinct untrusted worker claims success; independent artifact check fails | Reviewer rejects with own evidence and authorized later correction |
| B2 | Absent reviewer, stale evidence, colluding/invalid judge | No false certification, explicit UNKNOWN or failed/held path |
| B3 | Reviewer attempts to bypass human approval or change task policy | Denied; parent operator retains control |
| B4 | Existing hooks already match B1-B3 with lower effort | Reject new constructor as redundant |

**Tests NOT_RUN** by this independent source review; observed historical reproduction in original issue does not become our reproduced test. Benefits, savings, false-negative reduction and budget costs **NOT_MEASURED**.

## Old case and current status

Older [case snapshot](https://github.com/opensiro-contributions/agno/blob/0bcebdcad6163bdaab784714552785e64f741a7c/.opensiro/issues/agno-nested-review-20261119/roadmap.md) also reached NO_GO to a new S3* constructor, primarily because nested HumanReview was a native correctness bug. This independent v0.18 first-pass source verdict preceded checking that case and additionally examines current native evaluation hooks and original #11742/#11749/#11756. Owner ACTIVE/ALLOW permits metadata record only. Public GitHub fork Issue or external communication is not authorized; original contribution policy still governs separate native fix.
