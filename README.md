# Legal Chamber

![Legal Chamber](docs/assets/banner.png)

Global legal intelligence, research, drafting, evidence, litigation, transaction, academic and adversarial reasoning system, built as a Claude Code Agent Skill / plugin.

Primary router skill: **`legal-work`**

> **Read this before anything else:** [`docs/HONEST_STATUS.md`](docs/HONEST_STATUS.md) states exactly what in this repository is real and verified, what is architecture-only scaffolding, and what is an explicit placeholder. Legal Chamber's own governing rule (below) forbids treating any of the latter two as the first.

## What this is

Legal Chamber is a modular operating system for legal work: a router skill that classifies a legal task, resolves jurisdiction, loads the right specialist skill and jurisdiction pack, and coordinates deterministic tooling and adversarially-checked reasoning around a Fact Ledger, Evidence Ledger, and Legal Proof Graph.

It is **not** a single giant prompt. It is a directory of small, composable skills, jurisdiction packs, schemas, and deterministic scripts that a router loads only as needed (progressive disclosure).

## Governing principle

```
VERIFIED FACTS → VERIFIED LAW → VERIFIED AUTHORITY → LEGAL TEST →
APPLICATION → EVIDENCE → COUNTERARGUMENT → PROCEDURE → REMEDY →
ADVERSARIAL TESTING → CONCLUSION
```

Legal Chamber must never fabricate cases, citations, statutes, court rules, quotations, judges, facts, or evidence. Where something cannot be verified, it is labelled `UNKNOWN`, `UNVERIFIED`, `INSUFFICIENT EVIDENCE`, or `NO VERIFIED AUTHORITY LOCATED`, never quietly filled in. See [`docs/OPERATING_RULES.md`](docs/OPERATING_RULES.md) for the full rule set this repo is built against, and [`docs/QUALITY_GATES.md`](docs/QUALITY_GATES.md) for the gates a matter must pass before any output can be marked `VERIFIED FOR FILING`.

**This system does not replace a qualified, jurisdiction-admitted lawyer.** Every output it can produce carries an `AI_GENERATED` / `VERIFICATION_STATUS` / `HUMAN_REVIEW_STATUS` header (see [`schemas/draft.schema.json`](schemas/draft.schema.json)), and the `VERIFIED FOR FILING` state is only ever set by an authorised human reviewer, never by the system itself.

## Install

As a Claude Code plugin (from a clone or marketplace add):

```bash
claude plugin install legal-chamber
```

Or point Claude Code at the skill directly by adding this repo's `skills/` directory to your project's skill search path. See [`docs/INSTALL.md`](docs/INSTALL.md).

## Quick start

```
Review my employment tribunal case using Full Chambers.
```

The `legal-work` router asks for (or infers from context you've already given it) the jurisdiction and matter type, opens a matter workspace, and loads only the specialist skill, jurisdiction pack, and agent roles that matter needs.

## Repository layout

```
legal-chamber/
├── skills/         16 specialist skills, entry point legal-work/
├── agents/         13 agent role specs (intake, research, solicitors, counsel,
│                   opposition, judiciary, quality, ...) - prompts + guardrails,
│                   not automated legal advice generators
├── jurisdictions/  one pack per jurisdiction: authority hierarchy, citation
│                   style, court structure, procedural basics, VERIFICATION_STATUS
├── courts/         cross-jurisdiction court-rule notes and templates
├── regulators/     regulator profiles (powers, procedure, appeal routes)
├── citation/       citation style definitions + deterministic validator
├── rubrics/        academic rubric schema + evidence requirements (empty by
│                   design - no institutional rubric is invented)
├── templates/      jurisdiction-agnostic document skeletons
├── schemas/        JSON Schemas for matter/fact/evidence/authority/issue/...
├── workflows/      matter lifecycle, five-hearing adversarial workflow, gates
├── connectors/      abstraction layer + status of each research data source
├── scripts/        deterministic tools: deadline calculator, citation linter,
│                   style linter (arithmetic and pattern matching, not an LLM)
├── benchmarks/      hallucination / adversarial / jurisdiction / temporal traps
├── evaluations/     how to run the benchmarks and read the results
├── examples/        worked example matters
└── docs/           status, operating rules, gates, install, contributing detail
```

## Jurisdictions in this build

| Jurisdiction | Pack status | What's actually verified |
|---|---|---|
| US Federal | `STRUCTURAL_DRAFT` | Court hierarchy, citation basics; live case-law lookups via CourtListener are usable per-matter |
| England & Wales | `STRUCTURAL_DRAFT` | Court hierarchy, OSCOLA citation basics, primary-source pointers |
| Scotland | `STRUCTURAL_DRAFT` | Court hierarchy, citation basics, primary-source pointers |
| Australia | `STRUCTURAL_DRAFT` | Court hierarchy, AGLC citation basics, primary-source pointers |
| Canada | `STRUCTURAL_DRAFT` | Court hierarchy, McGill citation basics, primary-source pointers |
| New Zealand | `STRUCTURAL_DRAFT` | Court hierarchy, citation basics, primary-source pointers |
| Spain | `STRUCTURAL_DRAFT` | Civil-law authority hierarchy, citation conventions, primary-source pointers |
| France | `STRUCTURAL_DRAFT` | Civil-law authority hierarchy, citation conventions, primary-source pointers |
| European Union (supranational) | `STRUCTURAL_DRAFT` | Added after a stress test showed a country pack (e.g. France, Spain) cannot substitute for EU-level authority (GDPR and other Regulations are directly applicable) - court hierarchy (CJEU), citation basics, primary-source pointers |
| Everything else | `EXPERIMENTAL` (schema only) | Nothing, router will say `NO VERIFIED AUTHORITY LOCATED` and ask you to supply or research sources before proceeding |

`STRUCTURAL_DRAFT` means: court hierarchy, citation style, and authority-precedence rules are recorded and believed accurate as a matter of public legal-system structure, but **no case law, specific statutory text, or procedural deadline in these packs has been independently re-verified against a live primary source in this build**, every pack file says so at the top, and every workflow that uses one re-states that before relying on it. See [`docs/HONEST_STATUS.md`](docs/HONEST_STATUS.md).

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`GOVERNANCE.md`](GOVERNANCE.md). Jurisdiction packs require primary sources, source dates, and a named reviewer before they can move from `EXPERIMENTAL` to `COMMUNITY REVIEWED`, see [Part CLX](docs/OPERATING_RULES.md#jurisdiction-pack-contributions).

## License

Business Source License 1.1 - free for any use except offering Legal Chamber itself as a competing hosted/SaaS product; converts automatically to Apache-2.0 on 2030-08-22. See [`LICENSE`](LICENSE).
