# Contributing

Thank you for considering a contribution to Legal Chambers. This is a system that talks about law, so the bar for merging content is different from a typical dev-tool repo: **wrong here can mean a missed deadline or a fabricated citation in front of a court, not just a bug.**

## Before you open a PR

- Read `docs/OPERATING_RULES.md` and `GOVERNANCE.md` in full. They are short on purpose.
- Decide which kind of contribution this is:
  - **Architecture** (router logic, schemas, workflows, scripts, style), normal software review standards apply.
  - **Jurisdiction / court / regulator / rubric content**, needs a primary source, a checked date, and your name as reviewer, for every proposition. See `GOVERNANCE.md` → "Merging jurisdiction or court content."
  - **Agent role prompts**, needs a description of the independence rule it respects (see `AGENTS.md`) and, ideally, a benchmark case in `benchmarks/` that would catch a regression.

## What we will not merge

- A jurisdiction pack entry that asserts a case, statute, or rule you have not personally checked against a primary source (or a named, credible secondary source if no primary source exists).
- Anything that raises a pack's `VERIFICATION_STATUS` without the sourcing `GOVERNANCE.md` requires.
- Detector-evasion tooling of any kind (see `docs/STYLE_GUIDE.md`, "what this repo will not build").
- A new top-level skill/agent/jurisdiction that duplicates something already scaffolded, instead of deepening it.

## Style

- Follow `docs/STYLE_GUIDE.md` (no em dashes, no stock AI-prose phrasing, UK English by default).
- Keep `SKILL.md` files small; move detail into linked files.

## Running the deterministic checks locally

```bash
python3 scripts/citation_lint.py --selftest
python3 scripts/deadline_calculator.py --selftest
python3 scripts/verify_matter_refs.py --selftest
python3 scripts/verify_matter_persistence.py --selftest
python3 scripts/legal_cli.py --selftest
python3 scripts/legal_api.py --selftest
```

Both exit non-zero on failure and print what broke.

## Adding a jurisdiction

Copy `jurisdictions/_template/` to `jurisdictions/<your-jurisdiction>/`, fill in every `TODO` (do not leave one silently blank, write `UNVERIFIED` if you genuinely don't know), and set `VERIFICATION_STATUS: EXPERIMENTAL` until `GOVERNANCE.md`'s review requirements are met.
