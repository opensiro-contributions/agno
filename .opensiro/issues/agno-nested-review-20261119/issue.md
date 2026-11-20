# Agno — optional Team task-result independent audit (Opensiro roadmap)

**PLAN_ONLY · proposal-stage GO · research NEEDS_EVIDENCE · DRAFT — NOT PUBLISHED**

**One-sentence proposal:** Permit a developer to configure a separately authorized, evidence-based reviewer that can challenge Agno Team(task-mode) success *before* task/goal completion and return a documented rework result to the existing Team leader. This is hypothetical optional architecture, not a shipped feature or a maintainer request.
**Canonical decision receipt:** [roadmap.md](roadmap.md) — authoritative for historical Index, target, P0/P1/P2 and decision; this is a v0.18.2 same-case refinement of an already completed Wave 4 review.
**Technical companion:** [constructor-sufficiency.md](constructor-sufficiency.md) — exact original-native actor, decision, feedback, implementation and falsification.
**Working fork:** opensiro-contributions/agno on opensiro/meta.
**Case:** .opensiro/issues/agno-nested-review-20261119/.

## 1. Why Opensiro and central accepted VSM assessment

Opensiro uses Stafford Beer's six-function lens to ask which organizational decisions are actually owned and which could be developer-composed at a specific deployed runtime boundary. This research does not prove performance, savings or that Agno should implement every VSM function.

### Central starting point — accepted Index, not the target

> **ACCEPTED HISTORICAL INDEX — not a current-HEAD regrade or proposal after-state**
>
> **S1=A · S2=A · S3=A · S3*=— · S4=— · S5=—**
>
> Accepted included [Agno assessment](https://github.com/opensiro/vsm-harness-index/blob/a3fcf7c156ef4d1132680890bc11544681fd30c0/assessments/ag/agno.md), Index main a3fcf7c156ef4d1132680890bc11544681fd30c0; assessment blob e4ccb129a7a67baaca7c84b50f6f9820462d4382, reviewed 2026-09-15; original review ref 44219f8532e2fe6ce936850455f4b9a2567e4194, Profile 0.2.1, Skills/assessment procedure 0.3.1; exact original/catalog identity checked.

**Repository-wide audit:** Original agno-agi/agno main [e59ca576219e589136e53b6cff8d6677899cf95f](https://github.com/agno-agi/agno/commit/e59ca576219e589136e53b6cff8d6677899cf95f) (observed 2026-11-20). Boundary: deployed first-party Agent and Team(mode=tasks) with the model-selected task leader, not upstream project governance, AgentOS hosting, parent policy or incidental cookbook dogfood. Inspected Team task tools/state, run hooks, first-party judge/eval, workflow HumanReview, example/tests, license/CONTRIBUTING and relevant original Issue/PR bodies. Six functions refer to this runtime and its lawful parent/recursion limits.

| Function / plain-language role | Historical Index state | Current source-backed owner/closure | Candidate and reason |
| --- | --- | --- | --- |
| **S1 · Operations** | A | [Member execution](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/_task_tools.py) dispatches Agent/Team work and returns results | NO_TARGET: existing autonomous operations |
| **S2 · Coordination** | A | [TaskList](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/task.py) tracks dependencies, assignments and interference | NO_TARGET: existing task coordination |
| **S3 · Current management** | A | [Task tools](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/_task_tools.py) let the leader reprioritize, retry and mark overall completion | NO_TARGET: current leader controls task board |
| **S3* · Independent review** | — | [Judge](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/eval/agent_as_judge.py) and [post-hooks](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/_hooks.py) observe/evaluate outputs, but do not independently hold task completion based on raw evidence | P0: optional independent auditor plus binding corrective return |
| **S4 · Future adaptation** | — | Knowledge/memory/evaluation are inputs, not a demonstrated prospective external-intelligence decision/return path to S3 | DEFER: no qualified construction selected |
| **S5 · Identity and policy** | — | Human/application configurations, approvals and roles remain parent-owned | NO_TARGET: no authority transfer implied |

**Interpretation:** A means autonomous ownership, C a developer-composable first-party closure path, P a parent-governed function where applicable; — means no demonstrated path at the accepted assessed boundary and ? means unresolved evidence. These are **ownership categories**, **not quality ranks** or a mandatory construction roadmap.
**Priority rationale:** S1/S2/S3 are already A in historical assessment; a narrow task result acceptance gap at S3* has a source-specific optional decision/effect/feedback construction. No independent S4/S5 case is established.
**Deliberate exclusions / methodology challenge:** Do not call the existing nested HumanReview bug S3* or transfer S5. An explicit missing C is not evidence that the maintainers intentionally omitted a feature. Model/evaluator configuration is not independently established audit closure.
**Contributor / maintainer interests:** NOT_STATED for the proposed optional audit. Native [#10935](https://github.com/agno-agi/agno/issues/10935) requests a different HumanReview correctness fix, not this construction.

## 2. Selected construction hypothesis and operator outcome

**Target transition:** S3*=— -> S3*=C
**Function-specific disturbance:** HYPOTHETICAL member output announces success while independent raw execution artifacts or trusted terminal receipt contradict its claim; the Team leader may otherwise mark the task/goal complete.
**Proposed C capability (P0):** Optional, developer-composed S3* reviewer with a distinct lawful identity and independent evidence access. On verified ACCEPT the task may complete; CHALLENGE preserves a noncompleted task and gives the S3 leader a finding for repair/reassignment; INCONCLUSIVE holds only in explicitly configured enforce mode.
**Best native operator alternative:** Keep [AgentAsJudgeEval](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/eval/agent_as_judge.py) and [Team post_hooks](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/_hooks.py) for after-run scoring, plus application-owned deterministic checks and existing parent HumanReview. These are suitable when observation, not independent precommit task acceptance, is needed.
**Expected user benefit:** HYPOTHETICAL: a developer can compose a distinct evidence-challenging decision owner and prevent false task finalization before downstream use; benefit magnitude, demand and cost are NOT_MEASURED.
**Architectural sufficiency argument:** The existing task mode already carries member results and a leader retry/reassignment loop. Missing C-specific links are a separate evidence-authorized audit verdict and first-party enforced hold across task and goal completion paths, followed by returned feedback. A generic judge prompt or after-run evaluation without effect is insufficient; no reviewer configured must retain current behavior.

## 3. Existing native work versus missing construction

**Track A — native coverage:** [execute_task, update_task_status and mark_all_complete](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/_task_tools.py) update task and goal status; [Team hooks](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/libs/agno/agno/team/_hooks.py) run at the Team lifecycle, not necessarily before each task's completion. [Merged PR #11585](https://github.com/agno-agi/agno/pull/11585) repairs post-hook guardrail handling on resumed runs; [open PR #11721](https://github.com/agno-agi/agno/pull/11721) extends AgentOS evaluation suites, not necessarily task-completion veto. [Issue #10935](https://github.com/agno-agi/agno/issues/10935) is nested human approval correctness and must not be displaced.
**Track B — independent on-top C construction:** Prefer a narrow, opt-in acceptance seam at Agno's *native* TaskMode completion transitions and their async/stream equivalents, with raw member-run evidence and a typed audit record; no generic supervisor framework or automatic parent authority.

| C-sufficiency requirement | Already present / original-native Track A | Remaining smallest native Track B |
| --- | --- | --- |
| Distinct evidence-based decision before task success | Judge evaluator supports scoring; execute_task stores member output and marks completed | Make developer-installed autonomous reviewer independently examine raw task artifacts and terminal receipt before final task acceptance |
| Binding decision, lawful return to leader | Task tools permit retry/reassignment and leader-controlled goal completion | Guard execute_task, update_task_status and mark_all_complete plus async/resumed paths in enforce mode; send CHALLENGE/INCONCLUSIVE finding to Team board |
| Safe parent and absent-reviewer behavior | Existing configured parent HITL and unrestricted baseline task completion | Preserve baseline without reviewer; deny reviewer override of human approvals; bind evidence to run/task/version against replay |

**Distinctness and falsifier:** Existing same-scope native independent reviewer + evidence + *all-paths* completion hold and correction would make this duplicate; equally, any unguardable completion route or inability to obtain lawful independent artifacts defeats the proposed sufficiency.

## 4. Priorities and minimum sufficient result

- **P0:** Architecturally source-native opt-in S3* task acceptance actor that holds falsely completed Team tasks before goal closure and returns corrective evidence to S3; not an implementation approval.
- **P1:** Confirm lawful independent evidence/receipt, guard all task and goal completion paths (sync/async/parallel/resume), enforce parent veto, and test correct rework/re-audit without regression.
- **P2:** NONE. Additional Workflow/S4/S5 constructs are not automatically entailed.

**Proposed C-sufficiency verdict:** PROPOSED_C_SUFFICIENT at design stage, conditional on all authority, effect, evidence and return links; no shipped C evidence.

## 5. Proposed acceptance and stop gates

**Future positive test:** A member wrongly reports success with contradicted raw artifact; independent reviewer returns CHALLENGE; Team task remains noncompleted, leader repairs/reassigns, re-audit ACCEPT permits completion and returns durable feedback.
**Future negative test:** Missing, forged, stale, replayed or partial terminal evidence holds under configured enforce mode; parent denial remains binding; no-reviewer mode stays behaviorally unchanged across all supported sync, async and resume flows.
**Proposed falsifier:** Existing native same-boundary complete S3* decision/effect/return, or any reachable completion bypass that cannot be safely closed.
**Validation state:** NOT_RUN for proposed feature and product acceptance; prior unrelated 24-case HumanReview reproduction is historical evidence, not a new audit test.

## 6. Independent paths

**Original-native contribution:** This is PLAN_ONLY research. Maintainers must first decide whether this independent function is useful and permissible; no external Issue/PR follows automatically.
**Profile / Skills:** Historical A/A/A/—/—/— is untouched; no Profile/Skills correction was evidenced. Methodological C constructibility is separate from product adoption.
**Domain fork:** Independent research could run in an authorized private/local disposable branch; no new product branch or public fork Issue is created in this task.

## 7. Cost hypothesis

Matched comparison should use (A) existing post-hooks and deterministic review vs (B) independent precommit audit at the same task, measuring false acceptance, repaired decisions, review latency, maintenance and API cost. **Cost status: NOT_MEASURED.** No cost-saving or adoption claim.

## 8. Decision / handoff

**Proposal-stage decision:** GO
**Research disposition:** NEEDS_EVIDENCE
**Decision reason / next permitted step:** This is the same architectural GO/NEEDS_EVIDENCE as the already persisted [Wave 4 independent verdict](https://github.com/opensiro/upstream/issues/58#issuecomment-7042788169), not a new first run. The [separately sealed v0.18.2 source-only review](https://github.com/opensiro/upstream/issues/58#issuecomment-7047137737) and same-case documentation clarify the native task-completion ports and limits. Further engineering requires product-owner choice, separate rights and tests.
**Agent/developer handoff:** [constructor-sufficiency.md](constructor-sufficiency.md) supplies the technical contract; [roadmap.md](roadmap.md) is the unchanged terminal verdict source.
**Rights and publication:** Agno original Apache-2.0 and contributing policy require a ready-labeled native Issue for external PR. Verified OpenSiro fork ACTIVE/ALLOW permits internal metadata; no public fork Issue, original Issue/comment/PR, product modification, Index regrade or parent authority grant. Separate exact current-conversation approval required for external publication. **DRAFT — NOT PUBLISHED**.
**AI disclosure:** Prepared with AI assistance. No independent human audit or new native test execution is claimed.

### Historical comparison after current-source first pass

The previous case held original #10935's genuine nested HumanReview bypass distinct from proposed S3*. Earlier NO_GO entries remain historically valid for their recorded evaluation objects; the later Wave 4 GO uses the published architectural constructibility rule, not an assertion that a new reviewer is desired or implemented. No original maintainer publication occurs.
