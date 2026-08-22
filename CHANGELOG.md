# Changelog

All notable changes to this project are documented here. Format loosely follows [Keep a Changelog](https://keepachangelog.com/). Each entry corresponds to one real commit - see the git history for exact diffs.

## [0.1.4] - persistence checker, style audit, first regulator profile, first example (unreleased)

### Added

- `scripts/verify_matter_persistence.py` - a deterministic backstop for the disk-vs-claim check (`0.1.3`'s D-08 fix): maps a matter's declared `status` to the workspace subdirectories that status implies should be non-empty, and flags anything missing or empty. Wired into CI and `CONTRIBUTING.md` alongside the other two scripts.
- `STYLE_AUDIT_REPORT.md` - ran `scripts/citation_lint.py` against all 52 drafts the stress test actually generated; found real, uncorrected em dashes in 7 files (up to 74 in one). Root cause: `docs/STYLE_GUIDE.md`'s no-em-dash rule was stated as prose but nothing told a drafting agent to actually run the linter that already existed to check it.
- `regulators/cnil.md` - the first real regulator profile in the repository (France's CNIL), sourced live from `cnil.fr` and `conseil-etat.fr`: investigation stages (ordinary vs simplified procedure), sanction range, and the 2-month appeal route to the *Conseil d'État*. `COMMUNITY_REVIEWED`, not yet `MAINTAINER VERIFIED`.
- `examples/employment-tribunal-full-chambers/` - the first populated worked example: an unedited England & Wales `L5 CHAMBERS` matter taken directly from the live stress test, left un-cleaned-up including a real imperfection (a stale `matter.json` status field) rather than only showing the system at its best.

### Fixed

- `docs/STYLE_GUIDE.md` and `skills/legal-draft/SKILL.md`: both now explicitly instruct running `scripts/citation_lint.py` against a document before treating it as finished, rather than only saying "apply the style guide."
- `workflows/matter-lifecycle.md`: added an explicit instruction to update `matter.json`'s `status` field at every real stage transition - a spot-check found a matter that had completed all five moot hearings still recorded as `status: "INTAKE"`.

### Noted, not resolved

`docs/HONEST_STATUS.md` records an unresolved observation: one generated example file describes a fix ("authority-weight discipline... per `agents/solicitors/ROLE.md`") that could not have existed in that file at the time the file was written, per its own mtime. Left documented rather than quietly explained away.

## [0.1.3] - Matter 4 rerun: root cause of the disk-vs-claim gap, plus 5 more defects

### Fixed

- **Root cause of `0.1.2`'s D-03 finding**: none of the 13 agent roles in `agents/*/ROLE.md` declared `Write` or `Edit` tool access, despite most being designed to persist ledgers, case theories, and hearing records. Added to the 12 roles that need it (`intake` correctly stays read-only).
- `skills/legal-work/SKILL.md` and `agents/solicitors/ROLE.md`: added explicit gates requiring conflict-check clearance and confirmation of which party is "the user's side" before substantive case work proceeds - a matter had reached a disposition-stage output with `conflict_check.cleared: false` and both parties unnamed.
- `skills/legal-work/SKILL.md`: removed a false pointer claiming `docs/OPERATING_RULES.md` contains "the full taxonomy" of matter types - it doesn't (confirmed by direct grep).

### Added

- `scripts/verify_matter_refs.py` - deterministic checker confirming cross-referenced IDs (fact_ids, evidence_ids, etc.) between a matter's JSON records actually resolve, per `docs/ID_CONVENTIONS.md`'s documented convention. Wired into CI.

### Matter 4 result

Rerun cleanly after the `0.1.2` test-harness schema bug was fixed: all 70 agents succeeded, the seeded fabricated NSWCA authority was rejected, both stress conditions were met, and genuine Australian Consumer Law/contract-law authority was engaged (Darlington Futures, Comandate Marine, Rinehart, Karpik v Carnival).

See `DEFECT_REGISTER.md` (D-08 through D-12), `LEGAL_CHAMBER_COVERAGE_MATRIX.md`, and `LEGAL_CHAMBER_STRESS_TEST_REPORT.md` for full results - all 7 matters now complete. Release classification: `BETA`.

## [0.1.2] - live 7-matter stress test finds and fixes 7 real defects

### Added

- A live Workflow-orchestrated stress test: 6 seeded hard-safety hallucination/bad-authority traps plus 7 simulated legal matters (England & Wales employment tribunal and judicial review, US federal litigation, Australian contract dispute, French/EU regulatory matter, New Zealand appeal, postgraduate academic assessment), each run by real agents actually reading and following the repository's own files.

### Results

12/12 seeded fabrication traps caught on the six matters that completed (Matter 4 failed on a test-harness bug, fixed and rerun in `0.1.3`). Zero cross-matter canary-fact leakage. Simulated judiciary ruled against the user in 2 of 6 matters (no sycophancy). Five-hearing moot showed genuine round-to-round evolution. `matters/` gitignore protection held under real load (~104 generated files, zero tracked).

### Fixed

- `schemas/chronology.schema.json`: `date` was wrongly required on every event; made optional, `date_certainty` made required instead.
- Added `jurisdictions/eu/README.md`: no EU-level jurisdiction pack existed despite GDPR being directly-applicable EU law; a country pack alone can't answer an EU-law question.
- `agents/quality/ROLE.md` and `docs/QUALITY_GATES.md`: added a disk-vs-claim check - three matters had a stage claim an output (a case theory, a completed essay) that didn't actually exist as a file.
- `agents/solicitors/ROLE.md`: added an authority-weight check - a case theory cited an authority recorded as only secondary-verified as if it were binding.
- `skills/legal-draft/SKILL.md`: a draft's `verification_status` metadata must not claim a fuller verification state than the document's own body supports.
- `skills/legal-work/SKILL.md`: the router's complexity-tier list had no natural-language mapping to its own README's "Full Chambers" example - found during reconnaissance before the seven matters ran.

See `DEFECT_REGISTER.md`, `LEGAL_CHAMBER_COVERAGE_MATRIX.md`, `LEGAL_CHAMBER_STRESS_TEST_REPORT.md`, `REPOSITORY_CAPABILITY_MAP.md`, `DEAD_COMPONENT_REPORT.md`, and `ROUTER_TEST_RESULTS.md` for full evidence.

## [0.1.1] - initial scaffold and independent review pass

### Added

- Router skill `skills/legal-work` with matter classification, jurisdiction resolution (ask-based, no auto-detection), complexity tiers (L1-L6), and matter workspace lifecycle.
- 16 specialist skills scaffolded under `skills/`; `legal-research`, `legal-verify`, `legal-draft`, and `legal-authorities` written with real, usable instructions; the remaining 12 written as smaller real skills covering their core workflow with explicit TODOs for the deeper spec items not yet built.
- 13 agent role specifications under `agents/`, each a genuine prompt spec respecting the researcher/drafter/opposition/judge/reviewer independence rule.
- 8 jurisdiction packs (England & Wales, Scotland, US Federal, Australia, Canada, New Zealand, Spain, France) at `STRUCTURAL_DRAFT` status, plus a `_template/` for adding more.
- JSON Schemas for matter, fact, evidence, authority, issue, deadline, legal conclusion, draft, and prospect records.
- Deterministic scripts: `scripts/deadline_calculator.py` and `scripts/citation_lint.py`, both with `--selftest`.
- Quality gates (`docs/QUALITY_GATES.md`), operating rules (`docs/OPERATING_RULES.md`), and style guide (`docs/STYLE_GUIDE.md`) reference docs.
- Five-hearing adversarial litigation workflow (`workflows/five-hearing-adversarial.md`) and matter lifecycle workflow (`workflows/matter-lifecycle.md`).
- Starter hallucination-trap benchmark (`benchmarks/hallucination-traps.md`).
- Business Source License 1.1 (converts to Apache-2.0 on 2030-08-22), contributing/governance/security docs, and `docs/HONEST_STATUS.md`.

### Fixed (from the independent review pass, before the first commit)

- `jurisdictions/australia/README.md`: corrected "Family Court of Australia" being named as a standalone court (merged into the FCFCOA in 2021).
- `jurisdictions/scotland/README.md`: refined the court diagram - Outer House and Sheriff Court are parallel first-instance tracks, not sequential tiers.
- `scripts/citation_lint.py`: fixed the US reporter regex (couldn't match `F.2d`/`F.3d`/`F. Supp. 2d`), the UK neutral-citation regex (couldn't match two-word court codes like `EWCA Civ`), and the fenced-code-block stripper (mismatched nested backtick fences).
- `scripts/deadline_calculator.py`: added `--roll-if-non-business` as an explicit opt-in for calendar-day deadlines.
- `schemas/hearing.schema.json` added, and `workflows/five-hearing-adversarial.md` rewritten so "hearing memory" is an actual file each hearing reads.
- `schemas/chronology.schema.json` and `docs/ID_CONVENTIONS.md` added.
- `disclosure`, `family`, `version_of` fields added to `schemas/evidence.schema.json`, and `workflows/disclosure-register.md` added.
- A "day-one triage" step added to `skills/legal-litigation/SKILL.md`; a correspondence-register step added to `skills/legal-draft/SKILL.md`.
- Additional open legal-data APIs documented in `connectors/README.md`.

### Known gaps at this point (tracked, not hidden)

No populated Authority Graph for any jurisdiction, no benchmark suite had been run yet, `regulators/`, `rubrics/`, `connectors/`, `evaluations/`, and `examples/` were stubs. Closed progressively in later versions - see above.
