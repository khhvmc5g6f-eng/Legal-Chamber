# Benchmarks

QA benchmarks a Legal Chamber build should be run against before its outputs are trusted for real work. See `../evaluations/README.md` for how to actually run these.

## Status by category

| Category | Status |
|---|---|
| Hallucination (fake/near-correct citations, reversed holdings, fictional judges) | **Populated starter** - `hallucination-traps.md` has real seeded traps and has been exercised at least once against this build's own skill instructions (see that file's "run log"). |
| Adversarial (cases the user should win / should lose / are balanced / are unresolved) | Structure only - see below. |
| Jurisdiction (same fact pattern, different jurisdictions, different correct answer) | Structure only. |
| Temporal (same question, different `LAW_AS_OF` dates) | Structure only. |
| Privilege (obvious legal-advice vs commercial vs litigation vs non-privileged material) | Structure only. |
| Evidence (seeded contradictions and missing documents) | Structure only. |
| Procedural (deliberately wrong deadline/form/court, must be caught) | Partially covered by `../scripts/deadline_calculator.py --selftest`, which checks the arithmetic; no seeded end-to-end procedural-trap case yet. |
| Academic (synthetic pass/merit/distinction/exceptional work graded against a rubric) | Structure only, and blocked on `../rubrics/README.md` actually having a real rubric to grade against. |

## Format for a benchmark case (once populated)

```
CASE_ID
INPUT (the prompt/document given)
TRAP (what's wrong, and why a naive pass would miss it)
EXPECTED_BEHAVIOUR (what a correct Legal Chamber response does)
CATEGORY
```

## Regression rule

A new version of this repository should not perform materially worse on a populated benchmark than the previous version without an explicit, reasoned exception noted in `../CHANGELOG.md`.
