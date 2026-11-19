# Agno — independent Upstream #58 v0.18 six-function rerun

- Receipt contract: proposal-gate
- Original repository: agno-agi/agno
- Original HEAD: b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd
- Observed at: 2026-11-19
- Accepted Index assessment: https://github.com/opensiro/vsm-harness-index/blob/c2e43bf4750841277b3e58d8ba80314121734764/assessments/ag/agno.md
- Accepted assessment blob SHA: e4ccb129a7a67baaca7c84b50f6f9820462d4382
- Accepted review ref: 44219f8532e2fe6ce936850455f4b9a2567e4194
- Accepted reviewed at: 2026-09-15
- Accepted Index commit: c2e43bf4750841277b3e58d8ba80314121734764
- Accepted catalog blob SHA: 8609180ea6b25cc0d3e51e3c8111f2a4ae4f73f7
- Profile version: 0.2.1
- Assessment methodology version: 0.3.1
- System in focus: agno-agi/agno first-party Agents, Teams in tasks/route/broadcast/coordinate modes, Workflow nested HumanReview, evaluations, hooks, and publicly shipped AgentOS integration within one declared harness recursion; not separate CompanyOS deployment templates or external maintainers
- Accepted VSM vector: S1=A · S2=A · S3=A · S3*=— · S4=— · S5=—
- Repository-wide source map: Original README/AGENTS/CONTRIBUTING/LICENSE, libs/agno/agno/agent/agent.py, team/{mode.py,task.py,_task_tools.py,_messages.py,team.py}, workflow/workflow.py and nested container contracts, eval/agent_as_judge.py, guardrails and hooks, current issues and open PR search, Index assessment/catalog
- S1 disposition: Model/tool operational Agents already present; no C target
- S2 disposition: Agent Team tasks-mode coordination through shared TaskList and dependencies is already A; no C target
- S3 disposition: Team leader sees and regulates current tasks, retries, assignments and goal complete; already A, not a quality grade
- S3* disposition: AgentAsJudgeEval and Team post-hooks are native developer-composable reviewers, but no proven independent evidence/authority/correction closure at declared recursion; absence of grade is not a feature request
- S4 disposition: Model/provider warnings, memory, scheduled application tasks and externally operated CompanyOS templates do not show a first-party future-environment adaptation-to-S3 feedback function
- S5 disposition: Instructions, approvals, authentication and human review are configured by human/deployment or operator; no distinct autonomous S5 decision actor demonstrated
- Target transition: NO_QUALIFIED_C_TARGET
- Priority rationale: Concrete nested HumanReview behavior is a product-native fail-open defect (#10935), not evidence of a missing complementary audit owner; existing eval/post-hooks make a generic extra reviewer redundant absent an independently demonstrated new outcome
- Evaluation object: Nested workflow HumanReview safety and optional independent review of Team completion; compare exact source-native fix and standard Eval/Team hooks before proposing S3* construction
- Existing-work overlap: HumanReview at top-level workflow, nested Condition/Loop/Parallel/Steps/Router processing, Agent and Team pre/post_hooks, AgentAsJudgeEval with evaluator_agent and on_fail, tasks-mode monitoring/replanning, PR/Issue inventory
- Our on-top contribution: None qualified; plan-only source map and falsifiable boundary for any future separately attributable audit actor
- Incremental benefit: Not established beyond enforcing native HumanReview or composing existing evaluator with independent task tests
- Decision scope: Terminal NO_GO to a new VSM C constructor, NOT a rejection of original issue #10935, not a recommendation to ignore real defects, and not permission to publish externally
- P1 dependencies: Maintainer resolve support-versus-reject nested HumanReview, native regression on 5 container types and async/streaming paths, owner-authorized feedback route; only then test a new independent audit requirement against existing hooks
- P2 optional: None; no S4 or S5 construction justified merely by absent assessment functions
- Proposed C construction: Rejected hypothetical second actor would read independent workflow/task evidence, decide verified/reject/unknown, and enforce a legitimate correction into later task execution without taking reviewer-controlled human approval; current native contract and independent-user benefit unproven
- C sufficiency falsifier: Existing typed HumanReview fix or configured post_hook/AgentAsJudgeEval plus deterministic checks resolves the observed need without a new independently owned function
- Scenario basis: OBSERVED
- Proposal-stage decision: NO_GO
- Research disposition: NO_USEFUL_CHANGE
- Proposed validation: First reproduce original #10935 nested review bypass on current pinned original, distinguish unsupported nested semantics from missing S3* actor, implement/test native guard or pause only via separately authorized task; assess any distinct external evidence/correction requirement against native judge
- Validation state: NOT_RUN
- Proposal falsifier: A source-backed legitimate need requiring separate operational evidence, independent decision authority, compulsory safe return to Team/Workflow, and observed benefit over existing human review + eval hooks could overturn NO_GO
- Result: NO_USEFUL_CHANGE
- External issue: DRAFT — NOT PUBLISHED
- Cost status: NOT_MEASURED

## Identity and pins

Original default main [b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd](https://github.com/agno-agi/agno/commit/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd) observed on 2026-11-19. Accepted included https://github.com/opensiro/vsm-harness-index/blob/c2e43bf4750841277b3e58d8ba80314121734764/assessments/ag/agno.md, exact assessment blob e4ccb129a7a67baaca7c84b50f6f9820462d4382, last_checked_ref cbc10df7c7d377ce86f8d8f9c1e8c364fd94334d, review_ref 44219f8532e2fe6ce936850455f4b9a2567e4194, reviewed 2026-09-15, Profile 0.2.1, Methodology 0.3.1. [Catalog](https://github.com/opensiro/vsm-harness-index/blob/c2e43bf4750841277b3e58d8ba80314121734764/data/catalog.psv) includes agno, same source and review ref; exact historical assessment is older than current original and is not silently recomputed. Verified matching fork opensiro-contributions/agno with opensiro/meta, product main unchanged.

## Rights and authority

Original [Apache-2.0](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/LICENSE) and [CONTRIBUTING](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/CONTRIBUTING.md): external PR must link maintainer-triaged ready-labeled issue and preserve template, no duplicate, disclose AI assistance. Issue [#10935](https://github.com/agno-agi/agno/issues/10935) was still open when inspected; no matching PR found from targeted search, not an exhaustive no-PR proof. Owner event 20261119T182226Z--owner-upstream58-active in fork .opensiro/state.json establishes ACTIVE/ALLOW for internal metadata. It is not consent to post a public fork Issue, contact original maintainers, modify code, override review policy or change the Index. Public interaction remains DRAFT — NOT PUBLISHED.

## Existing work / overlap

Current original native [TeamMode.tasks](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/team/mode.py) supplies task-based coordination and [TaskList](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/team/task.py) stores assignees, dependencies, statuses, task notes and completion. [Task management tools](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/team/_task_tools.py) expose plan/reassignment and current status. [Team prompt](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/team/_messages.py) tells Lead to inspect results and change plans when a task fails. [Agent hooks](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/agent/agent.py) and [Team hooks](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/team/team.py) support pre/post intervention. [AgentAsJudgeEval](https://github.com/agno-agi/agno/blob/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd/libs/agno/agno/eval/agent_as_judge.py) provides a separately configurable evaluator_agent, binary/numeric scoring and on_fail callback; its presence is not proof of independent operational S3*.

Original [#10935](https://github.com/agno-agi/agno/issues/10935) documents a reproducible **native HumanReview safety inconsistency**: top-level Step pauses, nested Condition/Loop/Parallel/Steps/Router may continue without required review. Its issue asks maintainers to choose nested pause semantics or explicit fail-closed rejection. It is about existing human authorization semantics, not autonomous independent post-operation audit ownership. A distinct current [#11742](https://github.com/agno-agi/agno/issues/11742) requests a team USD budget cookbook using existing hooks; this supports native-cost control rather than the S3* construction. Another [#11749](https://github.com/agno-agi/agno/issues/11749) shows mutable tool argument receipts; independently useful as product-native historical-fact integrity, not by itself a six-function C target. Searches of open original PRs did not find a relevant #10935 implementation; no claim that all PRs were enumerated.

## Function ownership

- **S1=A:** first-party model agent executes tools, uses memory/session state and returns outcomes.
- **S2=A:** distinct member agents coordinate via persistent task list, dependency blocking, assignments and failures.
- **S3=A:** task-mode Team Lead observes whole board, retries/reassigns work and marks goal completion; agent-owned current regulation.
- **S3*=—:** evaluator and human review tools do not establish a separately responsible independent audit actor with distinct evidence and a mandatory audit-to-correction loop over operational reality; potential hooks are insufficient by themselves.
- **S4=—:** provider changes, knowledge/memory and external lifecycle tasks are candidate inputs, not a demonstrated autonomous future planning/capability adoption function at this recursion.
- **S5=—:** configured agent identity, policy, approvals and workflow HumanReview remain parent/application authority.

## Parallel contribution-on-top review

| Track A actual first-party operation | Track B minimal possible additional C | Observed need and reason to reject now |
| --- | --- | --- |
| Top-level HumanReview pauses; nested review can be skipped (#10935) | Separate auditor of nested workflow steps | Native bug has a smaller product fix: apply or reject nested HumanReview consistently, not a new independent governance actor |
| Task-mode Lead reads status and retries/reassigns | Independent operational auditor with return to task board | No independently demonstrated outcome or authority channel beyond model review and existing Team hooks |
| AgentAsJudgeEval + post_hooks offer configured judge and on_fail | New S3* reviewer lifecycle, receipt and enforced correction | Judge already does input/output review; new benefit and independent operational evidence are absent |
| Model/provider retirement (#11756) and memory/learning facilities | Future adaptation agent for provider changes | Issue proposes direct source/config fixes, not a continuous first-party S4 decision/return contract |

The P0 verdict is **NO_QUALIFIED_C_TARGET**. A dash in historical Index alone never justifies C. No repaired code, native tests, runtime runs, cost economics or new grade are claimed.

## Capability priority

**P0: NO_QUALIFIED_C_TARGET / NO_GO**, because the live concrete user harm is native review enforcement and current library already has composable judging hooks. **P1 (conditional, not scheduled):** demonstrate unavoidable independent post-outcome audit distinct from hooks and ordinary human approval, show safe binding to original task outcome plus lawful corrective feedback and measurable incremental benefit. **P2:** no speculative S4/S5.

## Implementation options

The cheapest proposed improvement to #10935 is an explicit native fail-closed reject of nested HumanReview until full nested pausing is supported, or native correct pause on all containers with tests, per maintainer design. Application users can compose explicit post-hooks + AgentAsJudgeEval/deterministic checks for output evaluation. Only if these fail a matched externally evidenced outcome might a small opt-in S3* actor be justified; neither a generic reviewer prompt nor a re-labelled hook can satisfy ownership/correction sufficiency. No patch is implemented as part of this plan.

## Specification and domain alternatives

No defect in Profile or Skills definitions was demonstrated. A first-party nested HumanReview fix would be a source-native correctness contribution, not a VSM grade change. The fork could hold a bounded reproduction/acceptance recipe, but public GitHub Issue and original PR both have separate publication rights; do not publish or represent original maintainer endorsement. Parent operator retains S5. Original code and Index source of truth remain unchanged.

## Cost experiment

If an independent audit case is later claimed, preregister identical nested-workflow test and false-completion artifact, compare (A) native HumanReview fix and configured post_hook/AgentAsJudgeEval versus (B) separate independent audit actor, measuring bypass rate, false approval, time to corrective action, reviewer agreement, runtime cost and upkeep. The issue's reporter did run a previous reproduction at historical source, but **this re-run performed source review only; tests NOT_RUN; savings NOT_MEASURED**.

## Delivery and publication

Final fresh-context v0.18 proposal decision **NO_GO / NO_QUALIFIED_C_TARGET**, research disposition **NO_USEFUL_CHANGE**; source pinned current original and included Index are distinguished. Independent first-pass verdict was formed **before** opening the historical [older case](https://github.com/opensiro-contributions/agno/blob/0bcebdcad6163bdaab784714552785e64f741a7c/.opensiro/issues/agno-nested-review-20261119/roadmap.md), which also rejected a new S3* constructor, although it primarily focused on nested HumanReview. Evolution: owner control is now ACTIVE/ALLOW, source HEAD advanced from 365c9c7e74719c1d20b557178add8c65f27a4426, and current Team/AgentAsJudge source plus #11742/#11749/#11756 were separately screened. Human [issue.md](issue.md), AI [constructor-sufficiency.md](constructor-sufficiency.md), this receipt and the existing fork Issue draft remain internal plan-only artifacts. External Issue/PR/comment: DRAFT — NOT PUBLISHED; no source patch, Index regrade, native validation or economic claim. The structural validator (when separately run) is not semantic certification.
