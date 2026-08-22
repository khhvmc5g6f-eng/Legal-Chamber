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

`../scripts/citation_lint.py` checks citation-shape patterns (UK neutral citation, EU case numbers, US reporter citations) and house-style issues (em dashes, stock phrasing, mixed quotation marks). It is a shape check, not a truth check - a citation can pass the linter and still be fabricated, and a real citation can be written in a shape the linter doesn't yet recognise. Run it as a first pass, never as the only pass:

```bash
python3 ../scripts/citation_lint.py path/to/draft.md
```

## What's not here yet

No jurisdiction-specific citation-format validator beyond the three shape patterns above. No academic citation styles beyond what the jurisdiction packs mention in passing (a dedicated `rubrics/` citation-style cross-reference is future work).

## Known linter limitation

`docs/OPERATING_RULES.md` and `docs/STYLE_GUIDE.md` deliberately quote the banned stock phrases as examples of what not to write (e.g. `no "it is important to note,"`). The linter has no way to distinguish that from an actual violation, so it flags those two files on every run. The CI job (`.github/workflows/ci.yml`, `house-style-lint`) is `continue-on-error: true` for exactly this reason - treat its baseline noise on those two files as expected, and watch for anything *beyond* that baseline rather than trying to get it to zero findings.
