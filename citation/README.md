# Citation

This directory documents citation styles by name and shape; it does not itself verify that any specific citation is real - that's the verification hierarchy in `../docs/OPERATING_RULES.md`, run per-authority in `../skills/legal-authorities/SKILL.md`.

## Styles referenced by jurisdiction packs

| Style | Used by (in this build) |
|---|---|
| OSCOLA | England & Wales, Scotland |
| Bluebook | US Federal |
| AGLC | Australia |
| McGill Guide | Canada |
| Spanish legal convention (name/date + ECLI) | Spain |
| French legal convention (article + ECLI) | France |

Each jurisdiction pack (`../jurisdictions/<slug>/README.md`) states its own style and basic citation shape - this file does not duplicate that content, it indexes it.

## OSCOLA 5 linter

`../scripts/oscola_lint.py` is the dedicated OSCOLA 5 format gate for
drafts. It reports stable rule codes with line and column locations, ignores
fenced code examples, and can emit JSON for editors and CI:

```bash
bin/legal oscola path/to/draft.md
bin/legal oscola --json path/to/draft.md > oscola-findings.json
```

It catches deterministic mistakes including `v.` in English case names,
unbracketed UK neutral-citation years, `section` in place of `s`/`ss`,
missing `SI` prefixes, prose-style case pinpoints, `p`/`pp` before
pinpoints, `op cit`/`loc cit`, double-quoted article titles, bare web
addresses, and unpunctuated Markdown footnotes.

The rules target the fifth edition published by the Oxford Law Faculty in
March 2026:

- <https://www.law.ox.ac.uk/oscola>
- <https://www.law.ox.ac.uk/sites/default/files/2026-03/OSCOLA%205.pdf>

This is format linting, not authority verification. A clean result does not
show that a source exists, is current, or supports a proposition. Continue
to the live primary-source checks required by `docs/OPERATING_RULES.md`.

## General citation and house-style linter

`../scripts/citation_lint.py` checks seven citation-shape patterns - UK neutral citations (with an optional trailing division/chamber parenthetical), UK OSCOLA law-report citations, UK OSCOLA statute citations, EU case numbers, ECLI identifiers (covering EU/France/Spain case law at once), Canadian (McGill Guide) neutral citations, and US reporter citations - plus house-style issues (em dashes, stock phrasing, mixed quotation marks). US reporter citations are additionally checked against a real, vendored table of ~3,590 known reporter abbreviations (Free Law Project's reporters-db, BSD-2-Clause), not shape alone. It is still a shape check, not a truth check - a citation can pass the linter and still be fabricated, and a real citation can be written in a shape the linter doesn't yet recognise. Run it as a first pass, never as the only pass:

```bash
python3 ../scripts/citation_lint.py path/to/draft.md
```

For US reporter citations specifically, `../scripts/verify_citation_years.py` is a second, narrower deterministic check: it looks up the cited reporter edition's real historical start/end date (from the same vendored reporters-db table) and flags a citation whose year falls outside it - e.g. a case "reported" in A.3d in 1990, three decades before that edition existed. Also a plausibility check, not a truth check, and it only fires on reporters `citation_lint.py` already recognises as real:

```bash
python3 ../scripts/verify_citation_years.py path/to/draft.md
```

## What's not here yet

No French/Spanish citation-format validator beyond the shared ECLI pattern above (their fuller conventions - article numbers, name/date forms - aren't separately shape-checked). OSCOLA coverage is deterministic and intentionally partial rather than a complete parser for every source type. `scripts/citation_lint.py` and `scripts/oscola_lint.py` document their exact limits.

## Known linter limitation

`docs/OPERATING_RULES.md`, `docs/STYLE_GUIDE.md`, `docs/SPEC_FULL_TEXT.md`, `CHANGELOG.md`, `../skills/legal-style/SKILL.md`, and this file deliberately quote the banned stock phrases as examples of what not to write (e.g. `no "it is important to note,"` two paragraphs up), or in `CHANGELOG.md`'s case, describe past fixes to those phrases. The linter has no way to distinguish that from an actual violation, so it flags those six files on every run. The CI job (`.github/workflows/ci.yml`, `house-style-lint`) is `continue-on-error: true` for exactly this reason - treat its baseline noise on those six files as expected, and watch for anything *beyond* that baseline rather than trying to get it to zero findings.
