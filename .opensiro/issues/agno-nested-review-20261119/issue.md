# Agno — independent six-function rerun and nested HumanReview gap (OpenSiro #58)

**Target transition:** NO_QUALIFIED_C_TARGET
**Proposal-stage decision:** NO_GO
**Research disposition:** NO_USEFUL_CHANGE

**Human-facing plan-only source draft.** [roadmap.md](roadmap.md) is canonical evidence; [constructor-sufficiency.md](constructor-sufficiency.md) records exact developer conditions. This does not publish a public fork Issue or contact maintainers.

## User-visible outcome and native resolution

The original [Agno #10935](https://github.com/agno-agi/agno/issues/10935) reports that nested workflow Steps with HumanReview can proceed without pausing, even when direct top-level Steps pause correctly. This is an important safety/correctness issue, but it is an **existing HumanReview enforcement bug**, not by itself evidence that a separate VSM S3* actor needs to be installed. Minimum original-native options: implement correct pause semantics in Condition/Loop/Parallel/Steps/Router, or reject unsupported nested review explicitly before execution. The maintainer must choose supported semantics; this OpenSiro report does not guess or repair code.

Separate [Agno #11742](https://github.com/agno-agi/agno/issues/11742) suggests team budget enforcement with existing hooks, and [#11749](https://github.com/agno-agi/agno/issues/11749) reproduces a mutable historical tool receipt. These are relevant operational correctness and observability inputs but still do not demonstrate a separately owned S3* audit-to-correction loop.

## Historical Index and current original

[Accepted Agno assessment](https://github.com/opensiro/vsm-harness-index/blob/c2e43bf4750841277b3e58d8ba80314121734764/assessments/ag/agno.md) blob e4ccb129a7a67baaca7c84b50f6f9820462d4382, reviewed 2026-09-15 at original 44219f8532e2fe6ce936850455f4b9a2567e4194 (Profile 0.2.1, Methodology 0.3.1). Current original [main@b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd](https://github.com/agno-agi/agno/commit/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd), observed 2026-11-19. A/C/P are functional ownership labels, not product maturity or missing-feature scores.

| Function | Historical Index state | Fresh source-grounded disposition |
| --- | --- | --- |
| **S1 · Operations** | A | Agent operations and tool-feedback ownership already present |
| **S2 · Coordination** | A | Multi-agent Team tasks, dependencies and shared assignments already present |
| **S3 · Current control** | A | Team leader controls current task board, reassignment and completion |
| **S3* · Complementary audit** | — | Native judge + post-hooks exist; separately independent audit-to-correction ownership not demonstrated |
| **S4 · Future intelligence** | — | No qualified adaptation-to-current-control C target in source review |
| **S5 · Policy and identity** | — | Human/application-configured permissions and identity, no independent policy actor |

## Why no new VSM constructor now?

Current [Team task-mode](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/team/mode.py), [TaskList](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/team/task.py), [AgentAsJudgeEval](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/eval/agent_as_judge.py), [Agent pre/post hooks](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/agent/agent.py) and [Team pre/post hooks](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/team/team.py) already cover coordination, management, optional evaluation and developer intervention. Another reviewing agent is only useful if its own evidence, decision right and binding to subsequent authorized correction provide an outcome unavailable from these existing mechanisms. No such user case was independently reproduced or validated by this run.

**P0:** NO_QUALIFIED_C_TARGET / NO_GO. **P1** (only if new evidence): compare native HumanReview fix and existing evaluator hooks against a truly independent evidence/receipt-and-correction actor, with deterministic false-review tests. **P2:** none. **Falsifier of NO_GO:** prove that an independently responsible actor and compulsory lawful feedback are needed and yield a material user outcome beyond existing hooks. Native tests NOT_RUN; cost NOT_MEASURED.

## Publication and history

Fork [opensiro-contributions/agno](https://github.com/opensiro-contributions/agno) owner state ACTIVE/ALLOW allows internal meta record. Current original license Apache-2.0; [CONTRIBUTING](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/CONTRIBUTING.md) requires a maintainer-triaged ready issue, original PR template and AI disclosures. No original PR, issue, comment, fork public Issue or code change is published. This fresh rerun independently agrees with the older [same-case S3* NO_GO](https://github.com/opensiro-contributions/agno/blob/0bcebdcad6163bdaab784714552785e64f741a7c/.opensiro/issues/agno-nested-review-20261119/roadmap.md) but adds explicit current-source review of native judgment, hooks and current Issues. Original #10935 is still open, not closed by this receipt.

## Second-look human decision — 2026-11-20

**Decision:** NO_GO / NO_QUALIFIED_C_TARGET; research NO_USEFUL_CHANGE (repeat of previously persisted NO_GO, independently re-evaluated against pinned current original). The issue-facing outcome remains: fix [Agno #10935](https://github.com/agno-agi/agno/issues/10935) with correct parent-approved HumanReview semantics. Do not replace a failing human gate with an autonomous reviewer.

The fresh Track A challenge also found original [#11742](https://github.com/agno-agi/agno/issues/11742) (USD budget plus hooks and caveats), [#9151](https://github.com/agno-agi/agno/issues/9151) (generic governance), [PR #11481](https://github.com/agno-agi/agno/pull/11481) (child-start cancellation correctness), and [PR #11721](https://github.com/agno-agi/agno/pull/11721) (AgentOS eval suites). These are original-owned maintenance and composition pathways; none yet establishes the incremental user result of a distinct audit-to-authorized-correction `S3*=C` constructor. Strongest Track B candidate remains independent evidence audit of nested Team/Workflow outcomes. It fails qualification until a particular post-native-fix failure, independent evidence access, a binding permitted rework action, and an A/B improvement are demonstrated.

Original at main b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd, canonical assessment included / e4ccb129a7a67baaca7c84b50f6f9820462d4382. No native tests, patches, cost measurements or third-party publication. See [second-look receipt](roadmap.md) for six-function disposition, alternatives, falsifiers, and historic comparison.

## 2026-11-20 — independent source-native reproduction completed

Actual `agno-agi/agno@b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd` was installed and executed. Sync + async test matrix:
**24 runs, 4/4 top-level pauses, 20/20 nested Step HumanReview bypasses** (both output review and
confirmation); downstream `publish` executes with no review for every nested container.
No model or external integration involved; [reproducer and raw result](evidence/nested-human-review-20261120/README.md).
This is a verified **original-native safety/correctness defect** under [maintainer issue #10935](https://github.com/agno-agi/agno/issues/10935).
The smallest legitimate fix is original-native pause/resume or explicit fail-closed rejection,
not a newly installed agent reviewer. VSM proposal remains NO_GO / NO_QUALIFIED_C_TARGET;
targeted evidence is partial, not an original full-suite PASS, and no external maintainer contact occurred.
