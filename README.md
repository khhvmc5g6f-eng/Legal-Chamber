# Legal Chambers

![Legal Chambers](docs/assets/banner.png)

Global legal intelligence, research, drafting, evidence, litigation, transaction, academic, and adversarial reasoning system, built as a Claude Code Agent Skill / plugin. Current version: **0.1.7** - see [`CHANGELOG.md`](CHANGELOG.md) for the full version history.

Primary router skill: **`legal-work`**

> **Read this before anything else:** [`docs/HONEST_STATUS.md`](docs/HONEST_STATUS.md) states exactly what in this repository is real and verified, what is architecture-only scaffolding, and what is an explicit placeholder. Legal Chambers' own governing rule (below) forbids treating any of the latter two as the first.

## What this is

Legal Chambers is a modular operating system for legal work: a router skill that classifies a legal task, resolves jurisdiction, loads the right specialist skill and jurisdiction pack, and coordinates deterministic tooling and adversarially-checked reasoning around a Fact Ledger, Evidence Ledger, and Legal Proof Graph.

It is **not** a single giant prompt. It is a directory of small, composable skills, jurisdiction packs, schemas, and deterministic scripts that a router loads only as needed (progressive disclosure).

## Governing principle

```
VERIFIED FACTS → VERIFIED LAW → VERIFIED AUTHORITY → LEGAL TEST →
APPLICATION → EVIDENCE → COUNTERARGUMENT → PROCEDURE → REMEDY →
ADVERSARIAL TESTING → CONCLUSION
```

Legal Chambers must never fabricate cases, citations, statutes, court rules, quotations, judges, facts, or evidence. Where something cannot be verified, it is labelled `UNKNOWN`, `UNVERIFIED`, `INSUFFICIENT EVIDENCE`, or `NO VERIFIED AUTHORITY LOCATED`, never quietly filled in. See [`docs/OPERATING_RULES.md`](docs/OPERATING_RULES.md) for the full rule set this repo is built against, and [`docs/QUALITY_GATES.md`](docs/QUALITY_GATES.md) for the 14 gates a matter must pass before any output can be marked `VERIFIED FOR FILING`.

**This system does not replace a qualified, jurisdiction-admitted lawyer.** Every output it can produce carries an `AI_GENERATED` / `VERIFICATION_STATUS` / `HUMAN_REVIEW_STATUS` header (see [`schemas/draft.schema.json`](schemas/draft.schema.json)), and the `VERIFIED FOR FILING` state is only ever set by an authorised human reviewer, never by the system itself.

## Install

As a Claude Code plugin (from a clone or marketplace add):

```bash
claude plugin install legal-chambers
```

Or point Claude Code at the skill directly by adding this repo's `skills/` directory to your project's skill search path. See [`docs/INSTALL.md`](docs/INSTALL.md).

## Quick start

```
Review my employment tribunal case using Full Chambers.
```

The `legal-work` router asks for (or infers from context you've already given it) the jurisdiction and matter type, opens a matter workspace, and loads only the specialist skill, jurisdiction pack, and agent roles that matter needs.

Want a document polished for style and authorship integrity without full case-building? Call `legal-style` directly - it's the same two-pass process `legal-draft` runs automatically, made standalone.

## What's actually built

This repo grows by depth (real, primary-source-verified content) rather than by breadth (more jurisdictions with only structural stubs) - see [`CLAUDE.md`](CLAUDE.md). Headline numbers, each backed by a script or a file you can open and check yourself:

- **17 specialist skills** (`skills/`), entry point `legal-work` - litigation, transactional, regulatory, academic, negotiation, drafting, evidence, verification, research, review, prospects, appeal, moot, style, and more. Each stays small and links out to `agents/`, `jurisdictions/`, `schemas/`, and `workflows/` rather than inlining their content.
- **13 agent roles** (`agents/`) - solicitor, counsel, opposition, judiciary, quality, research, intake, and specialist roles (academic, negotiation, regulatory, transactional, evidence, jurisdiction) - prompt specs with guardrails, not automated legal-advice generators.
- **12 deterministic scripts** (`scripts/`), all dependency-free Python with `--selftest` coverage, wired into CI: a citation-shape linter (7 patterns, checked against a real ~3,590-entry US reporter table), a citation-year plausibility checker, a house-style auto-fixer, a US court-name/abbreviation lookup (2,809 vendored records), a deadline calculator, a cross-matter conflict-of-interest name matcher, a matter schema-conformance checker, an ID-convention checker, a matter cross-reference checker, a matter-persistence checker, and a CLI/API pair (`legal_cli.py`/`legal_api.py`) covering the original spec's command verbs.
- **A 99-area practice-area taxonomy** ([`docs/PRACTICE_AREAS.md`](docs/PRACTICE_AREAS.md)), with a **"Coverage status" table that is the authoritative, honest count** of how much of it actually has real content - currently **46 of 99 named areas** have a populated, primary-source-verified Authority Graph entry (44 in England & Wales, 2 in US-Federal), all deliberately narrow (one or two doctrinal points each, not a survey of the field). Five full taxonomy categories are complete end to end: Core private law, Criminal law/process, Public law, Employment/Labor, and Business/Commercial/Financial. The other 53 areas are named in the taxonomy with no mechanism yet - the table says so plainly rather than letting a bare list of names imply broader coverage than exists.
- **3 real regulator profiles** (`regulators/`) - ICO (UK), CNIL (France), FTC (US) - each documenting the regulator's actual power, procedure, and appeal routes from primary sources, not a generic template.
- **One real academic rubric** (`rubrics/level7-distinction-standard.md`) - genuine UK Level 7 Distinction classification bands, sourced from a real institution's published regulations at the user's request, with the institution's identity withheld at their further request. This repository will not invent an institutional rubric where a real one hasn't been supplied - see `rubrics/README.md`.
- **A live research connector** for US-Federal via CourtListener (case search, docket lookup, citation-graph checks) when the session has that MCP server connected - see `jurisdictions/us-federal/README.md`.

## Repository layout

```
legal-chambers/
├── bin/legal       CLI entry point (wraps scripts/legal_cli.py)
├── skills/         17 specialist skills, entry point legal-work/
├── agents/         13 agent role specs (intake, research, solicitors, counsel,
│                   opposition, judiciary, quality, academic, negotiation,
│                   regulatory, transactional, evidence, jurisdiction) -
│                   prompts + guardrails, not automated legal advice generators
├── jurisdictions/  one pack per jurisdiction: authority hierarchy, citation
│                   style, court structure, procedural basics, VERIFICATION_STATUS.
│                   England & Wales and US-Federal carry real, populated
│                   Authority Graph content; the rest are STRUCTURAL_DRAFT
├── courts/         cross-jurisdiction court-rule notes and templates
├── regulators/     regulator profiles (powers, procedure, appeal routes) -
│                   three real profiles (ICO, CNIL, FTC)
├── citation/       citation style definitions + deterministic validator
├── rubrics/        academic rubric schema + evidence requirements - one real,
│                   source-withheld institutional rubric now exists
├── templates/      jurisdiction-agnostic document skeletons (memo, statement
│                   of case, witness statement, expert instruction letter,
│                   author-voice profile schema)
├── schemas/        JSON Schemas for matter/fact/evidence/authority/issue/
│                   chronology/conclusion/draft/hearing/prospect/deadline -
│                   the source of truth for every record shape in this repo
├── workflows/      matter lifecycle, five-hearing adversarial workflow,
│                   disclosure register, interim applications, research log
├── connectors/     abstraction layer + status of each research data source
├── scripts/        12 deterministic tools, all dependency-free with
│                   --selftest: citation_lint.py, verify_citation_years.py,
│                   style_fix.py, verify_court_name.py, deadline_calculator.py,
│                   verify_matter_refs.py, verify_matter_schema.py,
│                   verify_id_conventions.py, check_conflicts.py,
│                   verify_matter_persistence.py, legal_cli.py, legal_api.py
├── benchmarks/     hallucination / adversarial / jurisdiction / temporal /
│                   privilege / evidence / procedural trap categories
├── evaluations/    how to run the benchmarks and read the results
├── examples/       worked example matters - real stress-test output, kept
│                   unedited except for house-style em-dash fixes
└── docs/           status, operating rules, gates, practice-area coverage
                    table, install, contributing detail
```

## Jurisdictions in this build

| Jurisdiction | Pack status | What's actually verified |
|---|---|---|
| England & Wales | `STRUCTURAL_DRAFT` | Court hierarchy, OSCOLA citation basics, primary-source pointers; a populated Authority Graph now exists (`jurisdictions/england-wales/authorities/` - **50 files across 44 practice-area subjects**, spanning Core private law, Criminal law/process, Public law, Employment/Labor, and Business/Commercial/Financial in full, plus IP, verified live against Find Case Law and legislation.gov.uk) |
| US Federal | `STRUCTURAL_DRAFT` | Court hierarchy, Bluebook citation basics; live case-law lookups via a CourtListener MCP connector when available; two populated Authority Graph entries - `authority-graph.json` (the CFAA "exceeds authorized access" question) and `authorities/` (3 files: federal pleading standard, Article III standing, personal jurisdiction) |
| Scotland | `STRUCTURAL_DRAFT` | Court hierarchy, citation basics, primary-source pointers |
| Australia | `STRUCTURAL_DRAFT` | Court hierarchy, AGLC citation basics, primary-source pointers |
| Canada | `STRUCTURAL_DRAFT` | Court hierarchy, McGill citation basics, primary-source pointers |
| New Zealand | `STRUCTURAL_DRAFT` | Court hierarchy, citation basics, primary-source pointers |
| Spain | `STRUCTURAL_DRAFT` | Civil-law authority hierarchy, citation conventions, primary-source pointers |
| France | `STRUCTURAL_DRAFT` | Civil-law authority hierarchy, citation conventions, primary-source pointers |
| European Union (supranational) | `STRUCTURAL_DRAFT` | Added after a stress test showed a country pack (e.g. France, Spain) cannot substitute for EU-level authority (GDPR and other Regulations are directly applicable) - court hierarchy (CJEU), citation basics, primary-source pointers |
| Everything else | `EXPERIMENTAL` (schema only) | Nothing, router will say `NO VERIFIED AUTHORITY LOCATED` and ask you to supply or research sources before proceeding |

`STRUCTURAL_DRAFT` means: court hierarchy, citation style, and authority-precedence rules are recorded and believed accurate as a matter of public legal-system structure, but case law and statutory text are only verified where a populated Authority Graph is explicitly documented above - every pack file says so at the top, and every workflow that uses one re-states that before relying on it. See [`docs/HONEST_STATUS.md`](docs/HONEST_STATUS.md) and [`docs/PRACTICE_AREAS.md`](docs/PRACTICE_AREAS.md)'s "Coverage status" table for the exact, area-by-area breakdown.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`GOVERNANCE.md`](GOVERNANCE.md). Jurisdiction packs require primary sources, source dates, and a named reviewer before they can move from `EXPERIMENTAL` to `COMMUNITY REVIEWED`, see [`docs/SPEC_FULL_TEXT.md`](docs/SPEC_FULL_TEXT.md)'s jurisdiction-pack-contributions section.

## License

Business Source License 1.1 - free for any use except offering Legal Chambers itself as a competing hosted/SaaS product; converts automatically to Apache-2.0 on 2030-08-22. See [`LICENSE`](LICENSE).
