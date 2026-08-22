# Example: England & Wales Employment Tribunal, Full Chambers (L5)

This is a real, unedited output from a live stress test (2026-08-22) of `legal-work` → `legal-litigation` → the five-hearing adversarial workflow, run against a fictional NHS unfair-dismissal/whistleblowing scenario. It is not a hand-crafted showcase - every file here is exactly what the actual agents produced, with only one change: the stress test's internal canary-fact marker (used to verify matter isolation, see `../../LEGAL_CHAMBERS_STRESS_TEST_REPORT.md`) was replaced with `EXAMPLE-FIXTURE-ID` throughout. Nothing else was cleaned up, and the imperfections below were left in deliberately, per `../README.md`'s own instruction to show a gate that didn't pass and why.

## What's here

- `intake/` - matter classification, jurisdiction resolution, and a live defect note the intake stage itself raised about the router
- `facts/facts.json`, `chronology/`, `issues/issues.json`, `authorities/authorities.json` - the real Fact Ledger, chronology, issue tree, and authority records, schema-shaped
- `research/research_log.md` - the bidirectional research log, including the seeded fictional EAT authority being checked and rejected
- `opposition/opposition_case.md` - the isolated-context opposing case
- `moot/hearing-1.json` through `hearing-5.json` - the full five-hearing adversarial workflow, with real round-to-round evolution (see the stress test report's "Moot Court Performance" section)
- `final/case_theory_memo.md` - the solicitor-side case theory, written after the moot record, candidly addressing (not hiding from) the hearings' adverse disposition

## Honest quality-gate results (run live, not asserted)

```
$ python3 scripts/verify_matter_refs.py examples/employment-tribunal-full-chambers
Checked 2 cross-references in examples/employment-tribunal-full-chambers
No broken cross-references found.

$ python3 scripts/verify_matter_persistence.py examples/employment-tribunal-full-chambers
matter: examples/employment-tribunal-full-chambers
declared status: INTAKE
No claimed-but-missing outputs found for this matter's declared status.
```

The persistence checker's clean result is itself misleading in one specific way, left in as an honest example of exactly the kind of gap `docs/DEFECT_REGISTER.md` D-14 describes: `intake/matter.json`'s `status` field still reads `INTAKE` despite this matter having gone through all five hearings and a final case theory - so the checker's status-based expectations (which only require `intake/` to exist for `INTAKE` status) don't actually test what's really here. Judged only by what's on disk rather than the stale status field, this matter workspace is far more complete than `INTAKE` would suggest.

## Known imperfections, not hidden

- `final/case_theory_memo.md` itself documents (in its own "Defects noticed" section) that the case theory the moot hearings were run against was never separately persisted as its own file - the memo is, by its own account, the first time that document was actually written down.
- The memo also raises a genuine, still-relevant point about `agents/solicitors/ROLE.md`'s tool access (partially addressed by `DEFECT_REGISTER.md` D-08's Write/Edit fix, made after this example was generated).
- Some of the memo's self-referential claims about exactly when certain fixes existed do not fully check out against file timestamps - see `docs/HONEST_STATUS.md`'s "unresolved observation" note. Left in rather than quietly edited out, because a worked example that only shows the system at its best isn't an honest worked example.

## Prospects, as actually calculated

`VERY_WEAK` for the lead heads on the current record (primarily a limitation/evidence problem, not a doctrinal one), `VERY_WEAK to unpleadable` for the disability-discrimination cluster - both stated with the reasoning behind them, not as a bare number. See `final/case_theory_memo.md` Section 6.
