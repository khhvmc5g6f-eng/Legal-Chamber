# Benchmarks

QA benchmarks a Legal Chambers build should be run against before its outputs are trusted for real work. See `../evaluations/README.md` for how to actually run these.

## Status by category

| Category | Status |
|---|---|
| Hallucination (fake/near-correct citations, reversed holdings, fictional judges) | **Populated starter** - `hallucination-traps.md` has real seeded traps and has been exercised at least once against this build's own skill instructions (see that file's "run log"). |
| Adversarial (cases the user should win / should lose / are balanced / are unresolved) | **Populated starter** - `adversarial-traps.md`, 4 seeded traps (false reassurance, skipped steelman, manufactured confidence, false certainty on an open question). |
| Jurisdiction (same fact pattern, different jurisdictions, different correct answer) | **Populated starter** - `jurisdiction-traps.md`, 4 seeded traps (unstated jurisdiction, conflict of laws, common-law/civil-law framework mismatch, unpopulated-regulator extrapolation). |
| Temporal (same question, different `LAW_AS_OF` dates) | **Populated starter** - `temporal-traps.md`, 4 seeded traps (stale-figure recall, a regime change spanning the question, this repo's own `verified_at` tag treated as permanent, a repealed statute cited as current). |
| Privilege (obvious legal-advice vs commercial vs litigation vs non-privileged material) | **Populated starter** - `privilege-traps.md`, 4 seeded traps (lawyer-as-businessperson, dominant purpose not checked, waiver by disclosure, in-house counsel jurisdiction variance). |
| Evidence (seeded contradictions and missing documents) | **Populated starter** - `evidence-traps.md`, 4 seeded traps (contradiction, missing document, hearsay as personal knowledge, bundle exhibit-numbering gap). |
| Procedural (deliberately wrong deadline/form/court, must be caught) | **Populated starter** - `procedural-traps.md`, 4 seeded traps. PR-01/PR-02 are backed by an actually-executed `../scripts/deadline_calculator.py` run (real command + output inline in the file), not just a reasoning walkthrough - the one benchmark category with real deterministic tooling to exercise. |
| Academic (synthetic pass/merit/distinction/exceptional work graded against a rubric) | Structure only, and blocked on `../rubrics/README.md` actually having a real rubric to grade against - deliberately, per `docs/SPEC_FULL_TEXT.md` Part LXXXVII ("do not invent institutional rubrics"); not a gap this build can fill by writing more content, only by someone supplying a real institution's rubric. |

## Format for a benchmark case (once populated)

```
CASE_ID
INPUT (the prompt/document given)
TRAP (what's wrong, and why a naive pass would miss it)
EXPECTED_BEHAVIOUR (what a correct Legal Chambers response does)
CATEGORY
```

## Regression rule

A new version of this repository should not perform materially worse on a populated benchmark than the previous version without an explicit, reasoned exception noted in `../CHANGELOG.md`.
