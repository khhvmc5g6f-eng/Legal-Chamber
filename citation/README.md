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

## Deterministic shape validator

`../scripts/citation_lint.py` checks seven citation-shape patterns - UK neutral citations (with an optional trailing division/chamber parenthetical), UK OSCOLA law-report citations, UK OSCOLA statute citations, EU case numbers, ECLI identifiers (covering EU/France/Spain case law at once), Canadian (McGill Guide) neutral citations, and US reporter citations - plus house-style issues (em dashes, stock phrasing, mixed quotation marks). US reporter citations are additionally checked against a real, vendored table of ~3,590 known reporter abbreviations (Free Law Project's reporters-db, BSD-2-Clause), not shape alone. It is still a shape check, not a truth check - a citation can pass the linter and still be fabricated, and a real citation can be written in a shape the linter doesn't yet recognise. Run it as a first pass, never as the only pass:

```bash
python3 ../scripts/citation_lint.py path/to/draft.md
```

For US reporter citations specifically, `../scripts/verify_citation_years.py` is a second, narrower deterministic check: it looks up the cited reporter edition's real historical start/end date (from the same vendored reporters-db table) and flags a citation whose year falls outside it - e.g. a case "reported" in A.3d in 1990, three decades before that edition existed. Also a plausibility check, not a truth check, and it only fires on reporters `citation_lint.py` already recognises as real:

```bash
python3 ../scripts/verify_citation_years.py path/to/draft.md
```

## What's not here yet

No French/Spanish citation-format validator beyond the shared ECLI pattern above (their fuller conventions - article numbers, name/date forms - aren't separately shape-checked). No academic citation styles beyond what the jurisdiction packs mention in passing (a dedicated `rubrics/` citation-style cross-reference is future work). `scripts/citation_lint.py`'s own docstring documents each pattern's exact known limitations (e.g. the UK neutral pattern's trailing parenthetical isn't checked against real division/chamber codes, and the US reporter pincite handling).

## Known linter limitation

`docs/OPERATING_RULES.md`, `docs/STYLE_GUIDE.md`, `docs/SPEC_FULL_TEXT.md`, `CHANGELOG.md`, `../skills/legal-style/SKILL.md`, and this file deliberately quote the banned stock phrases as examples of what not to write (e.g. `no "it is important to note,"` two paragraphs up), or in `CHANGELOG.md`'s case, describe past fixes to those phrases. The linter has no way to distinguish that from an actual violation, so it flags those six files on every run. The CI job (`.github/workflows/ci.yml`, `house-style-lint`) is `continue-on-error: true` for exactly this reason - treat its baseline noise on those six files as expected, and watch for anything *beyond* that baseline rather than trying to get it to zero findings.
