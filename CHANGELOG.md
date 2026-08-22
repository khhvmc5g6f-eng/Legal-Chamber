# Changelog

All notable changes to this project are documented here. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [0.1.1] - independent review pass and fixes

### Fixed

- `jurisdictions/australia/README.md`: corrected a factual error naming "Family Court of Australia" as a standalone court (merged into the FCFCOA in 2021). Found by a live fact-check review.
- `jurisdictions/scotland/README.md`: refined the court diagram - Outer House and Sheriff Court are parallel first-instance tracks, not sequential tiers.
- `scripts/citation_lint.py`: fixed the US reporter regex (previously couldn't match `F.2d`/`F.3d`/`F. Supp. 2d` citations), the UK neutral-citation regex (previously couldn't match two-word court codes like `EWCA Civ`), and the fenced-code-block stripper (previously mismatched nested backtick fences of different lengths). Removed dead `STOCK_PHRASES`/`STOCK_REGEXES` duplication.
- `scripts/deadline_calculator.py`: calendar-day deadlines now support an explicit `--roll-if-non-business` opt-in for jurisdictions whose rules roll a weekend/holiday deadline forward (never a default). Selftest expanded from 4 to 10 cases.

### Added

- `schemas/hearing.schema.json` and a rewrite of `workflows/five-hearing-adversarial.md` so "hearing memory" is an actual file each hearing reads, not just an assertion - also fixed a sequencing error where costs were assessed before the merits disposition existed to base them on, and added an explicit note on what the workflow does not model (interim applications, disclosure timing, case management).
- `schemas/chronology.schema.json` and `docs/ID_CONVENTIONS.md` - chronology previously had no structured record at all despite being the most-described workflow in the build.
- `disclosure`, `family`, and `version_of` fields on `schemas/evidence.schema.json`, and `workflows/disclosure-register.md`, closing a gap where redacted/working/exhibit copies of the same document were unrelated records with no shared key.
- `date_certainty` and a chronology cross-reference on `schemas/fact.schema.json`.
- A "day-one triage" step (limitation check first, client care/costs information, pre-action protocol/ADR gate) in `skills/legal-litigation/SKILL.md`, an expert-evidence note, and court-fee tracking alongside deadlines.
- A correspondence-register step (without-prejudice vs open) in `skills/legal-draft/SKILL.md`.
- Additional open legal-data API options documented in `connectors/README.md` (Find Case Law, legislation.gov.uk, EUR-Lex/CELLAR, Légifrance/PISTE, Federal Register, Regulations.gov, CanLII), checked live via WebSearch, not yet wired into a jurisdiction pack's verification story.
- Switched license from Apache-2.0 to Business Source License 1.1 (converts to Apache-2.0 on 2030-08-22).

See `docs/HONEST_STATUS.md`'s "Independent review pass" section for the full review methodology and what was and wasn't fixed.

## [0.1.0] - initial scaffold

### Added

- Router skill `skills/legal-work` with matter classification, jurisdiction resolution (ask-based, no auto-detection), complexity tiers (L1-L6), and matter workspace lifecycle.
- 16 specialist skills scaffolded under `skills/`; `legal-research`, `legal-verify`, `legal-draft`, and `legal-authorities` written with real, usable instructions; the remaining 12 written as smaller real skills covering their core workflow with explicit TODOs for the deeper spec items not yet built.
- 13 agent role specifications under `agents/`, each a genuine prompt spec respecting the researcher/drafter/opposition/judge/reviewer independence rule.
- 8 jurisdiction packs (England & Wales, Scotland, US Federal, Australia, Canada, New Zealand, Spain, France) at `STRUCTURAL_DRAFT` status, plus a `_template/` for adding more. See `docs/HONEST_STATUS.md` for exactly what is and isn't verified in each.
- JSON Schemas for matter, fact, evidence, authority, issue, deadline, legal conclusion, draft, and prospect records.
- Deterministic scripts: `scripts/deadline_calculator.py` (business-day-aware deadline arithmetic) and `scripts/citation_lint.py` (citation-shape pattern linter), both with `--selftest`.
- Quality gates (`docs/QUALITY_GATES.md`), operating rules (`docs/OPERATING_RULES.md`), and style guide (`docs/STYLE_GUIDE.md`) reference docs.
- Five-hearing adversarial litigation workflow description (`workflows/five-hearing-adversarial.md`) and matter lifecycle workflow (`workflows/matter-lifecycle.md`).
- Starter hallucination-trap benchmark (`benchmarks/hallucination-traps.md`) with seeded fake-citation and reversed-holding traps.
- Business Source License 1.1 (converts to Apache-2.0 on 2030-08-22; free for any use except a competing hosted/SaaS offering), contributing/governance/security docs, and an honest status report (`docs/HONEST_STATUS.md`) distinguishing real capability from scaffolding.

### Known gaps (tracked, not hidden)

See `docs/HONEST_STATUS.md` in full. Headline items: no populated Authority Graph for any jurisdiction, no benchmark suite has been run, adversarial/jurisdiction/temporal/privilege/procedural/academic benchmark categories exist as structure only, `regulators/`, `rubrics/`, `connectors/`, `evaluations/`, and `examples/` are stubs.
