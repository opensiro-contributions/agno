# Native Agno #10935 — pinned reproducibility evidence

**Scope:** A targeted, deterministic reproduction of the original maintainer's
[nested HumanReview defect](https://github.com/agno-agi/agno/issues/10935),
**not** a repair, full native-test-suite PASS, new VSM grade, approved external contribution or extra C constructor.

- Original repository: [agno-agi/agno @ main b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd](https://github.com/agno-agi/agno/commit/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd)
- Accepted historical [Index assessment](https://github.com/opensiro/vsm-harness-index/blob/c2e43bf4750841277b3e58d8ba80314121734764/assessments/ag/agno.md): `included`, unchanged (Profile 0.2.1, methodology 0.3.1)
- Local environment: Python 3.12.3, Agno 3.2.1 **editable installed from pinned original checkout**, no model/API calls, no database, no external integrations
- Executed at: 2026-11-19T23:20:34Z (UTC); report: `observed-results.json`
- Commands: `python3 -m venv .venv`, `.venv/bin/python -m pip install -e ./agno-original/libs/agno`, `.venv/bin/python repro_human_review.py` (from a working directory with that pinned `agno-original` checkout)
- Controls: six placements (`top_level`, `Condition`, `Loop`, `Parallel`, `Steps`, `Router`) × two `HumanReview` flags (`requires_output_review`, `requires_confirmation`) × two execution paths (`Workflow.run`, `Workflow.arun`)

## Actual observations

| Test population | Runs | Observed |
| --- | ---: | --- |
| Top-level control | 4 | 4/4 paused; output review stops **after** `draft`, confirmation stops **before** `draft` |
| Nested container | 20 | 20/20 returned `is_paused=False`, zero step requirements and `ran=['draft','publish']` |
| Execution exceptions | 24 | 0 exceptions |

The script asserts the exact **reproduced bug on the pinned baseline**, and therefore
**must start failing after a correct fix**. It is not a test that declares the bug fixed.
Original issue #10935 remains the authoritative maintainer issue.

Two previously merged, narrower native PRs—[#7227](https://github.com/agno-agi/agno/pull/7227)
(top-level `continue_run` pause semantics) and [#7433](https://github.com/agno-agi/agno/pull/7433)
(`HumanReview` config for container itself)—do **not** resolve review on a nested *child Step* in this test.

## Limits and next acceptance

Only isolated synchronous and asynchronous `run` paths are exercised here.
**Streaming, `continue_run`, concurrent races, native unit/integration suites,
maintainer design choice, production cost and user savings are NOT_TESTED/NOT_MEASURED.**
For native remediation, choose and test (a) appropriate nested pause/resume support with a
persisted review obligation or (b) explicit fail-closed rejection of unsupported nested `HumanReview`
*before* any child execution. Avoid a new independent reviewer that lets the existing human gate be bypassed.

The proposed separate S3* control C remains **NO_GO / NO_QUALIFIED_C_TARGET**:
a real native safety bug is not itself proof of separate independent audit ownership.
No original or fork GitHub Issue, PR, review, comment or product branch was published.
