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
- **A 99-area practice-area taxonomy** ([`docs/PRACTICE_AREAS.md`](docs/PRACTICE_AREAS.md)), with a **"Coverage status" table that is the authoritative, honest count** of how much of it actually has real content - currently **86 of 99 named areas** have a populated, primary-source-verified Authority Graph entry (84 in England & Wales, 2 in US-Federal), all deliberately narrow (one or two doctrinal points each, not a survey of the field). Ten of eleven taxonomy categories are complete end to end: Core private law, Criminal law/process, Public law, Employment/Labor, Business/Commercial/Financial, Intellectual property and technology, Property and construction, Regulatory and sector-specific, Procedure/dispute resolution and the legal profession, and International and comparative. Only Rights-based, social, and emerging remains open (2 of 13 areas built). The other 11 areas repo-wide are named in the taxonomy with no mechanism yet - the table says so plainly rather than letting a bare list of names imply broader coverage than exists.
- **33 real regulator profiles** (`regulators/`) - three general data-protection/consumer regulators (ICO, CNIL, FTC), plus a full set of healthcare regulators across the UK, US, Canada, Australia, New Zealand, France, and Spain (fitness-to-practise bodies, medicines/devices agencies, and provider-quality inspectorates) - each documenting the regulator's actual statutory power, investigation stages, sanction range, and appeal route from primary sources, not a generic template. See `regulators/README.md` for the full country-by-country breakdown.
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
│                   33 real profiles: ICO/CNIL/FTC plus UK/US/Canadian/
│                   Australian/NZ/French/Spanish healthcare regulators
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

Every jurisdiction pack actually carries **two separate status axes**, not one, and conflating them is the single most common way to over-read this table - so both are shown here rather than one summary word:

1. **Structural narrative status** - the pack's own README: court hierarchy, authority-precedence rules, citation-style conventions. `STRUCTURAL_DRAFT` means this was written from general, stable public knowledge of how the legal system is organised, but wasn't checked against a primary source, claim by claim, in a specific session with a date attached. `COMMUNITY_REVIEWED` means it was.
2. **Authority Graph status** - the specific, individually-verified case law and statutes in `jurisdictions/<x>/authorities/`, each file independently checked against a live primary source with its own date, method, and (where relevant) named limitation. This is a per-file status, not a per-pack one, and it is what `docs/PRACTICE_AREAS.md`'s "Coverage status" table tracks.

A pack can be `COMMUNITY_REVIEWED` on axis 1 while having zero Authority Graph content, and a pack can carry deep Authority Graph content while its own README narrative is still `STRUCTURAL_DRAFT` - which is exactly what happened here until England & Wales's narrative was promoted this week. Nothing in this table's status column implies anything about the other axis; check both.

| Jurisdiction | Structural narrative | Authority Graph |
|---|---|---|
| England & Wales | `COMMUNITY_REVIEWED` - court hierarchy checked live against `judiciary.uk`, OSCOLA citation checked live against `law.ox.ac.uk/oscola`, both 23 August 2026 (see `jurisdictions/england-wales/README.md` frontmatter) | **90 files across 84 practice-area subjects** - ten of eleven taxonomy categories complete, only Rights-based, social, and emerging remains open - each verified live against Find Case Law and legislation.gov.uk |
| US Federal | `STRUCTURAL_DRAFT` - court hierarchy, Bluebook citation basics, not yet independently re-checked this session | Two populated entries - `authority-graph.json` (the CFAA "exceeds authorized access" question) and `authorities/` (3 files: federal pleading standard, Article III standing, personal jurisdiction); live case-law lookups via a CourtListener MCP connector when available |
| Scotland | `STRUCTURAL_DRAFT` - court hierarchy, citation basics | None |
| Australia | `STRUCTURAL_DRAFT` - court hierarchy, AGLC citation basics | None |
| Canada | `STRUCTURAL_DRAFT` - court hierarchy, McGill citation basics | None |
| New Zealand | `STRUCTURAL_DRAFT` - court hierarchy, citation basics | None |
| Spain | `STRUCTURAL_DRAFT` - civil-law authority hierarchy, citation conventions | None |
| France | `STRUCTURAL_DRAFT` - civil-law authority hierarchy, citation conventions | None |
| European Union (supranational) | `STRUCTURAL_DRAFT` - added after a stress test showed a country pack (e.g. France, Spain) cannot substitute for EU-level authority (GDPR and other Regulations are directly applicable) - CJEU hierarchy, citation basics | None |
| Everything else | `EXPERIMENTAL` (schema only) | None - router will say `NO VERIFIED AUTHORITY LOCATED` and ask you to supply or research sources before proceeding |

The other eight jurisdictions remain `STRUCTURAL_DRAFT` on the narrative axis simply because nobody has yet run the same live fetch-and-check pass against their own court-service/citation-authority websites that England & Wales just went through - it is real, bounded work (per `GOVERNANCE.md`: a primary source, a checked date, and a named reviewer, per claim changed), not a blocked or structurally impossible step. It happens jurisdiction by jurisdiction, same as the Authority Graph itself did. See [`docs/HONEST_STATUS.md`](docs/HONEST_STATUS.md) and [`docs/PRACTICE_AREAS.md`](docs/PRACTICE_AREAS.md)'s "Coverage status" table for the exact, area-by-area Authority Graph breakdown.

## Areas of law covered

The practice-area taxonomy in [`docs/PRACTICE_AREAS.md`](docs/PRACTICE_AREAS.md) names 99 areas across 11 categories. The number after each category is areas with a populated, primary-source-verified Authority Graph entry, out of that category's total - not every named area is built, and the linked table says exactly which ones aren't:

| Category | Built |
|---|---|
| Core private law (contract, tort, equity & trusts, land, succession, restitution, consumer, company, human rights) | 9/9 |
| Criminal law and process | 5/5 |
| Public law (judicial review, parliamentary sovereignty, immigration, asylum, electoral, local government, freedom of information) | 8/8 |
| Business, commercial, and financial (banking, insurance, securities, insolvency, tax, competition, international trade, franchise, partnership) | 11/11 |
| Employment and labor | 5/5 |
| Intellectual property and technology (patent, copyright, trade secrets, design rights, data protection, AI regulation, media, telecoms) | 11/11 |
| Property and construction (landlord & tenant, construction, planning, environmental, agricultural, mining, energy, water) | 8/8 |
| Regulatory and sector-specific (gaming, food & drug, aviation, maritime, transport, sports, arts & cultural property, animal law) | 12/12 |
| Procedure, dispute resolution, and the legal profession (civil procedure, evidence, arbitration, mediation & ADR, class actions, legal ethics, conflict of laws) | 7/7 |
| International and comparative (public international law, IHL, ICL, human rights, law of the sea, space law, EU law, comparative law, diplomatic & consular, treaty law) | 10/10 |
| Rights-based, social, and emerging (civil rights, disability, elder, housing, welfare, refugee, indigenous rights, climate, blockchain, biotech, robotics, election law, national security) | 2/13 |

Ten of eleven categories are complete end to end. Rights-based, social, and emerging is the one still open - civil rights and disability law are built, the other eleven named areas in that category aren't yet. Every built entry is deliberately narrow: one or two doctrinal points backed by a real, checked case and statute, not a survey of the whole field - see any file in `jurisdictions/england-wales/authorities/` for what "built" actually means here.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`GOVERNANCE.md`](GOVERNANCE.md). Jurisdiction packs require primary sources, source dates, and a named reviewer before they can move from `EXPERIMENTAL` to `COMMUNITY REVIEWED`, see [`docs/SPEC_FULL_TEXT.md`](docs/SPEC_FULL_TEXT.md)'s jurisdiction-pack-contributions section.

## Author's note

I'm a UK law graduate, with a Master's in Law completed at commendation level, and I have high-functioning autism. I built Legal Chambers because I enjoy reading and studying law, and because the legal system is often hardest to navigate for exactly the people who most need it navigable. This project is my attempt to make real, honestly-sourced legal structure and research tooling available to people who don't have a solicitor on speed dial - built the way I'd want a legal reference tool to work: never guessing, never smoothing over a gap with something that sounds confident, and saying "I don't know, here's how to find out" whenever that's the true answer. The governing principle at the top of this file isn't marketing copy - it's the actual standard I hold every line of this repository to.

## Legal disclaimer

Legal Chambers is a research and drafting aid, not a lawyer and not a source of legal advice. Nothing it produces is a substitute for advice from a qualified, jurisdiction-admitted solicitor or barrister who knows your actual facts. Its outputs can be wrong, incomplete, or based on law that has since changed - always verify anything it gives you against a live primary source before relying on it, and get proper legal advice for any real matter. See the "Governing principle" section above and [`docs/OPERATING_RULES.md`](docs/OPERATING_RULES.md) for how the repository tries to make that failure mode visible rather than hidden, and [`docs/HONEST_STATUS.md`](docs/HONEST_STATUS.md) for exactly what is and isn't verified in this build.

## License

Business Source License 1.1 - free for any use except offering Legal Chambers itself as a competing hosted/SaaS product; converts automatically to Apache-2.0 on 2030-08-22. See [`LICENSE`](LICENSE).
