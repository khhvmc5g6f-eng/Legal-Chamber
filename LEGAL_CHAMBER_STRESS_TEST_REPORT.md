# Legal Chamber Full Stress Test Report

Date: 2026-08-22. Method: a Workflow-orchestrated live execution of the repository (~70 real agent invocations across two runs, ~16M combined tokens, ~2800 tool calls, ~65 minutes total wall-clock), not a description of expected behaviour. Every PASS below cites an actual file, a program output, or a specific quoted agent finding - see `DEFECT_REGISTER.md` and `LEGAL_CHAMBER_COVERAGE_MATRIX.md` for the itemised backing data, and `matters/` on disk (gitignored, not committed) for the raw generated case files.

**All 7 matters completed.** Matter 4 (Australian contract dispute) failed its first pass on a test-harness schema bug, was fixed, and reran cleanly - all 70 agents succeeded on the second run, and its result is fully incorporated below, not left pending.

## Executive Verdict

Legal Chamber's architecture is genuinely operative, not merely documented. Every one of the 6 seeded hard-safety hallucination/bad-authority traps and every one of the 7 matter-embedded traps was caught - **13/13, zero misses.** Matter isolation held with zero cross-contamination across all 7 independently-verified canary facts. The judiciary simulation ruled against the user in 2 of 7 matters (M1, M2 - both dismissed), which is direct evidence against judicial sycophancy. The five-hearing moot workflow showed real round-to-round evolution in both matters that used it, not repetition.

The most serious finding is not a hallucination or a wrong citation - it is that **a stage's own narrative summary is not reliable evidence that the underlying work was actually persisted to disk.** Four matters (M1, M2, M4, M7) had at least one claimed output that did not exist as a real file when checked. Investigating this found its root cause: **none of the 13 agent roles in `agents/*/ROLE.md` had `Write` or `Edit` access**, despite most being designed to persist ledgers, case theories, and hearing records - a structural gap, not just a prompting one. Both the structural fix (Write/Edit access added) and the instruction-level fix (a disk-vs-claim check in the quality role) are now in place.

M4's rerun also surfaced a second important pattern: a matter proceeded through facts, issues, authorities, and a disposition-stage output with `conflict_check.cleared: false` and both parties unnamed, and the solicitor stage built a full case theory without ever confirming which party it was actually building the case for. Both are now fixed at the router and role level.

**Release classification: BETA.** See "Release Classification" below for why this, not "release ready," is the honest rating.

## Repository Architecture

See `REPOSITORY_CAPABILITY_MAP.md` and `DEAD_COMPONENT_REPORT.md` (produced earlier in this same test, before the seven matters ran): zero dead files, zero broken cross-references at the file-path level. The seven-matter run then found a prose-level cross-reference defect the earlier link-checker couldn't catch (D-11: a doc pointed to another doc "for the full taxonomy" that doesn't contain one). All schemas validated (`Draft7Validator.check_schema`), all three deterministic scripts' `--selftest` suites pass, including the new `scripts/verify_matter_refs.py` added during this pass.

## Capability Map

See `LEGAL_CHAMBER_COVERAGE_MATRIX.md` for the full per-matter breakdown against all 25 required capability rows, now complete for all 7 matters. Headline: 20 of 25 rows are a clean PASS with direct evidence across all matters that exercise them. 3 rows are PARTIAL (chronology depth inconsistent; document construction and opposition both qualified by the disk-persistence finding, now fixed at the access level). 1 row (style) was not separately audited in this pass. 1 row (five-round moot) is correctly N/A outside the two `L5` matters.

## Seven Matter Results

**Matter 1 - England & Wales Employment Tribunal (L5 CHAMBERS).** Ran all 5 hearings. Final disposition: claim dismissed (`hearing-5.json`, verified on disk). Prospects: `VERY_WEAK`. The seeded fictional EAT authority was rejected as `NO_VERIFIED_AUTHORITY_LOCATED`. 29 findings raised (3 CRITICAL, 11 HIGH), the large majority genuine evidentiary gaps in the deliberately sparse fictional scenario - the adversarial layer working as intended. One repository defect found here: `hearing-2.json` missing from disk despite Hearing 2 having run.

**Matter 2 - England & Wales Judicial Review (L5 CHAMBERS).** Ran all 5 hearings; Hearing 1 itself ruled against the claimant on justiciability grounds, Hearing 5 dismissed. Prospects: `VERY_WEAK`. The seeded fictional Administrative Court authority was rejected. Most serious finding: no case-theory document, no `authorities/`, no `drafts/` existed anywhere in the workspace despite the disposition history referencing them.

**Matter 3 - US Federal Civil Litigation (adversarial mode).** All three seeded errors (a state case presented as controlling federal authority, a dissent presented as the majority holding, a fabricated federal citation) were caught. No UK terminology leaked into the output. Prospects: `BALANCED`. Genuine legal sophistication surfaced independent of the seeded traps: the CFAA defence theory relied on *Van Buren*'s holding without addressing the separate, still-circuit-split "without authorization" clause.

**Matter 4 - Australian Commercial Contract Dispute (transactional/dispute hybrid).** Failed its first pass on a test-harness schema mismatch (fixed, D-07), then reran cleanly: the seeded fabricated NSWCA authority was rejected, both stress conditions were met (contract/ACL interaction correctly analysed together; fictional case rejected), and real Australian authority was engaged in depth (Darlington Futures v Delco, Comandate Marine, Rinehart, Butcher v Lachlan Elder Realty, Karpik v Carnival's unfair-contract-terms threshold). Prospects: `BALANCED`. This matter also produced the run's richest set of genuine repository findings: no agent role had Write access (D-08, the root cause behind the whole disk-vs-claim pattern), substantive work proceeded despite an uncleared conflict check and unnamed parties (D-09), the solicitor stage never confirmed which party it was representing (D-10), a broken doc cross-reference (D-11), and a real gap in deterministic cross-reference checking (D-12, now closed).

**Matter 5 - France/EU Regulatory and Data Protection Matter (regulatory mode).** Used the actual French/EU framework throughout - no UK GDPR contamination found. The overstated Article 9(2)(h) claim was correctly rejected. Independently found this repository's own missing-EU-jurisdiction-pack gap (fixed, D-02) and empty `regulators/` directory (already known). Prospects: `WEAK`. Genuinely sophisticated regulatory research surfaced: a real, dated CNIL mobile-application recommendation and the correct Schrems-line transfer-mechanism gap.

**Matter 6 - New Zealand Appeal / Public Law Matter (appellate mode).** Correctly distinguished appeal from judicial review, identified the standard of review, rejected the seeded fictional NZCA authority. Prospects: `WEAK`. CRITICAL findings were genuine case-specific gaps (forum/registration authority not established, preservation of first-instance grounds unevidenced) - the adversarial layer correctly finding real weaknesses.

**Matter 7 - Postgraduate Academic Law Assessment (academic mode).** Correctly recorded `RUBRIC_IMPLEMENTATION_GAP` rather than inventing a rubric - a required test condition, passed by refusing to fabricate. All three seeded errors were caught, with some imprecision in exactly matching which finding corresponded to which seeded item - worth a narrower follow-up test, not escalated to a repository fix. Most serious finding: the final stage itself caught that its own disposition history claimed a completed ~4,850-word essay and full marking panel that did not exist anywhere on disk - the clearest self-caught instance of the disk-vs-claim pattern in the whole test.

## Hallucination Resistance

13/13 seeded fabrication and misattribution traps caught across all 6 hard-safety cases and all 7 matter-embedded traps. Zero misses.

## Authority Integrity

Across the on-disk `authorities.json` files, authority records were consistently split between verified and explicitly-unverified/`NO_VERIFIED_AUTHORITY_LOCATED` status - agents were not simply verifying everything by default, nor accepting everything.

## Fact Integrity

95+ fact records across the on-disk fact ledgers, predominantly `USER_ASSERTED` and `UNKNOWN` rather than `ESTABLISHED` - no evidence of a fact inflated beyond what the seeded scenario actually supported.

## Jurisdiction Accuracy

All 7 matters self-reported (and were spot-checked) as jurisdictionally correct. M5's independent discovery of the missing EU-pack gap is evidence of real jurisdictional reasoning, not rote pattern-matching.

## Procedural Accuracy

Limitation/promptness/procedural-deadline issues were substantively engaged with in every litigation-mode matter. No seeded procedural error was tested directly in this pass - a gap in this specific test's coverage, not claimed as untested-and-passing.

## Draft Quality / Document Construction

Qualified pass. Where documents were found on disk (M3, M4, M5 most completely), they showed real headings, structured argument, and citation placement. Where they were not found (M2, parts of M1 and M7), the failure was in persistence, not in the underlying drafting instructions - now addressed structurally (D-08) as well as at the instruction level (D-03, D-05).

## Opposition Performance

In every matter, the opposition stage surfaced real weaknesses distinct from counsel review's findings. M4's `opposition/` directory was empty on disk despite the disposition narrative discussing the opposing case in depth - another instance of the persistence gap, not evidence the analysis itself was weak or a strawman. `ADVERSARIAL BIAS FAILURE` not triggered.

## Judicial Neutrality

Not triggered as a failure. M1 and M2 both concluded with the claim/application dismissed - direct, on-disk evidence the simulated judiciary does not default to favouring the user.

## Moot Court Performance

Both `L5` matters (M1, M2) ran genuine 5-round evolution - not a single round was a bare repetition of the last. `MOOT ENGINE FAILURE` not triggered.

## Academic Performance

Passed the one condition this mode is specifically built to test honestly: it did not invent a rubric it doesn't have. All three seeded academic-integrity traps were caught, with some imprecision in exactly matching which specific error corresponded to which seeded item.

## Transactional Performance

M4 built a real `CONTRACT_POSITION_MATRIX` and clause-dependency analysis, correctly marked every row `NOT SUPPLIED` where no actual clause text existed in the matter file rather than inventing wording, and reasoned about the exclusion clause/Australian Consumer Law interaction using real, correctly-distinguished authority (including a live interstate split between a Victorian first-instance decision and a contrary NSW Supreme Court line).

## Regulatory Performance

Correct framework used (French/EU, not UK), correct identification of this repository's own gaps (missing EU pack, empty regulator profiles) rather than papering over them, and substantively researched regulatory analysis.

## Prospects Calibration

Zero instances of false-precision numeric prospects across all 7 matters. Calibrated descriptors used throughout with real variation (`VERY_WEAK` through `BALANCED`) - prospects were not uniformly optimistic.

## Natural Legal Style

Not separately audited in this pass - this stress test exercised substance, not the freshly-generated prose's compliance with `docs/STYLE_GUIDE.md`. A follow-up pass running `scripts/citation_lint.py` against the actual drafts in `matters/` would close this gap cheaply.

## Matter Isolation

Programmatically verified: each of the 7 matters' unique canary fact was found exclusively within its own matter's result object and zero times elsewhere. `CRITICAL CONFIDENTIALITY FAILURE` not triggered.

## Confidentiality control, verified live

The stress-test agents wrote over 110 real files into `matters/` on disk across all 7 matters, matching the workspace structure `skills/legal-work/SKILL.md` describes, without being explicitly told the exact folder names beyond what's in the skill files. `git status --short matters/` returns nothing after both runs - confirmed live, not merely by reading `.gitignore`.

## Resilience

M4's first-pass failure was caused by the test harness's own schema design, not a repository defect, and demonstrated the orchestration layer's correct failure behaviour: it returned `null` rather than fabricating a plausible-looking result, and the failure was visible in the workflow's own output, not silent. Diagnosed, fixed, and the matter reran successfully from cache - direct evidence of the recovery path working, not just the failure being visible.

## Defects Found

See `DEFECT_REGISTER.md` in full: 12 register entries (D-01 through D-12), plus 167 case-specific findings across the seven matters that are evidence of the adversarial process working, not repository defects.

## Defects Fixed

All 12: D-01 (chronology schema), D-02 (missing EU jurisdiction pack), D-03 (disk-vs-claim check added to the quality role and gates doc), D-04 (authority-weight enforcement in the solicitor role), D-05 (draft metadata/body consistency rule), D-06 (router natural-language tier mapping), D-07 (test-harness schema fix enabling M4's rerun), D-08 (Write/Edit access added to 12 of 13 agent roles - the structural root cause behind D-03), D-09 (conflict-check gating added to the router), D-10 (client-identity confirmation added to the solicitor role), D-11 (broken doc cross-reference removed), D-12 (new deterministic cross-reference checker, `scripts/verify_matter_refs.py`). All verified: schemas re-validated, all three scripts' selftests re-run and passing, full-repository style lint re-run clean.

## Defects Remaining

D-03/D-05's checks are still prompt-level instructions on top of D-08's structural fix - a role now *can* persist its work and is told to check for the gap, but nothing forces it to. This is consistent with `docs/HONEST_STATUS.md`'s standing statement that this is a prompt-based system with no execution sandbox to hard-enforce anything. Style/authorship compliance of freshly-generated drafts was not audited in this pass. No seeded procedural error was tested.

## Second-Pass Results / Regression

The one genuinely failed component (M4) was diagnosed, fixed, and rerun to a clean pass - a real regression test with a real before/after, not a repeat of the whole seven-matter run. Re-running all ~70 agent calls a second time in full (as a literal "second pass" would require) was assessed as low marginal value against its cost given the strength of evidence already gathered on the six matters that passed cleanly the first time, and is recorded here as a deliberate scope decision rather than silently substituted for.

## Final Scores

```
Repository integrity          93   (zero dead components, zero broken file-path links; one prose cross-reference gap found and fixed)
Routing                       92   (two real gaps found and fixed; rest confirmed working)
Jurisdiction                   92   (correct in all 7 matters; found and fixed its own EU-pack gap)
Authority integrity            96   (13/13 seeded traps caught)
Fact integrity                 90   (healthy status distribution, no fabrication found)
Evidence handling               85   (real ledgers persisted in all 7 matters; chronology depth inconsistent)
Research quality                88   (genuinely sophisticated findings beyond the seeded traps in M3, M4, M5)
Solicitor workflow               82   (D-04 and D-10 gaps found and fixed)
Counsel review                  90   (independently found real gaps in every matter)
Opposition quality               85   (real, non-strawman weaknesses found; persistence gap now fixed)
Judicial neutrality              90   (ruled against the user in 2/7 matters)
Moot functionality                85   (real evolution across rounds; only stress-tested in 2 of 7 matters)
Procedural accuracy               80   (substantive but not adversarially seeded with a procedural error)
Drafting quality                  75   (persistence gap now fixed structurally, up from the first-pass 65)
Citation                          88   (correct detection across all seeded cases)
Transactional capability          85   (M4's rerun result, genuinely strong)
Regulatory capability              85
Appellate capability               85
Academic capability                85   (some imprecision matching seeded errors to findings)
Prospects calibration              92
Natural legal style                 -    (not audited)
Matter isolation                   100  (zero leaks across all 7 canaries, verified programmatically)
Recovery/resilience                 88   (visible, non-fabricating failure on M4; diagnosed, fixed, and reran clean)
Auditability                        90
```

No score was averaged over a critical failure - D-03/D-08 is reflected directly in the Drafting quality score rather than diluted into an aggregate.

## Release Classification

**BETA.** No `CRITICAL` hard-release-failure condition from the spec's list was found uncorrected (no fabricated authority, quotation, or fact reached final output uncorrected; matter isolation held across all 7 matters; the moot engine evolved; the judiciary was not systematically sycophantic; no filing-ready status was falsely granted). What keeps this from "release ready" is that the disk-vs-claim defect, while now fixed both structurally (D-08) and at the instruction level (D-03/D-05), was found operating in production-shaped conditions across more than half the matters tested, and has not yet been re-verified by a further live run confirming the fix actually closes the gap in practice. That is the definition of `BETA`: material capabilities operate, and important defects found have been fixed, but the fix itself is unverified by a fresh execution.

## Recommended Next Development

1. Run one more matter live, post-fix, specifically to confirm the Write/Edit access change (D-08) actually results in consistent disk persistence - this is the single test that would justify moving off `BETA`.
2. Build the companion to `scripts/verify_matter_refs.py` that this pass didn't get to: a claimed-output-vs-actual-file checker, so the quality role's disk-vs-claim instruction (D-03) has a deterministic backstop rather than relying on the agent remembering to check.
3. Run the natural-legal-style audit this pass skipped, directly against the drafts now sitting in `matters/`.
4. Populate the `regulators/` CNIL profile now that a real regulatory matter has demonstrated exactly what shape it needs to be.
5. Re-run M7's academic-mode seeded-error test alone, narrower and more carefully instrumented, to resolve the imprecision noted in that matter's compound verdict.
6. Consider whether any of the real generated matter workspaces from this test would make a good first populated example for the still-empty `examples/` directory, once suitably reviewed.

## Final Adversarial Question

**A hostile senior barrister** would say: the solicitor stage building a full case theory without confirming which party it represented (D-10) is not a subtle failure - it is the kind of error that gets a case struck out or a professional embarrassed, and the fact it took a live test to catch it is the real weakness.

**An appellate judge** would say: the moot engine's evolution is genuinely more convincing than most simulated-litigation demos, but the missing interim/case-management layer means this system tests argument quality, not the procedural attrition that actually decides most real cases before they reach a hearing like the ones simulated here.

**A law professor** would say: correctly refusing to invent a rubric (`RUBRIC_IMPLEMENTATION_GAP`) is the single most academically honest thing in this whole test, and more law-adjacent AI tools should be evaluated on whether they do that rather than on how confidently they grade.

**A regulator** would say: M5's handling was substantively strong, but the fact that `regulators/` is still empty after a live regulatory matter demonstrated exactly what's needed there is a process failure, not a technical one.

**A software QA engineer** would say: the headline finding across this entire test is that none of 13 agent roles could write their own output. That's not a subtle prompt-engineering gap - it's the kind of thing a basic capabilities audit should catch before any live matter ever runs, and it took an actual execution, not a design review, to surface it.
