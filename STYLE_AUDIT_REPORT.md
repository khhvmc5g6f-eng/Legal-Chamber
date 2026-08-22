# Style Audit Report

Method: ran `scripts/citation_lint.py` against all 52 markdown files the seven-matter stress test actually generated under `matters/` (2026-08-22) - real freshly-generated drafts, not this repository's own hand-written documentation.

## Findings

7 of 52 files contained real em-dash violations of `docs/STYLE_GUIDE.md`'s house style:

| File | Em dashes found |
|---|---|
| `matters/M1-KESTREL/opposition/opposition_case.md` | 74 |
| `matters/M2-OSPREY/opposition/opposition_case.md` | 32 |
| `matters/M6-KIWI/research/research-log.md` | 22 |
| `matters/M6-KIWI/prospects/authority-verification-and-forum-note.md` | 18 |
| `matters/M6-KIWI/intake/intake.md` | 8 |
| `matters/M7/opposition/opposing-case-theory.md` | 6 |
| `matters/M7/drafts/case-theory-argument-map.md` | 6 |

No stock-phrase, mixed-quotation-mark, or double-space findings were flagged in any of the 52 files - the em dash is the only house-style rule that was actually violated at scale in live-generated output. Citation-shape detection also worked correctly across these files, picking up real UK neutral citations, NZ citations, and others embedded in the generated opposition cases and research logs.

## What this means

`docs/STYLE_GUIDE.md`'s no-em-dash rule was stated as prose instruction in every skill file that produces documents, but nothing in the actual drafting workflow told an agent to run the deterministic linter that already exists to check it. Stating a rule and checking a rule are different things - this is exactly the same class of gap as the disk-vs-claim finding (`DEFECT_REGISTER.md` D-03/D-08), applied to style rather than persistence: an instruction that isn't actually exercised isn't reliably followed.

## Fix applied

- `skills/legal-draft/SKILL.md` and `docs/STYLE_GUIDE.md` now both explicitly instruct running `scripts/citation_lint.py` against a document before treating it as finished, rather than only saying "apply the style guide."
- Not fixed retroactively: the 7 files above still contain their em dashes. `matters/` is gitignored test data from a stress test, not shipped repository content, so it was left as the honest evidence behind this finding rather than silently cleaned up - see `docs/HONEST_STATUS.md`.

## What this audit did not check

Only the em-dash/stock-phrase/quotation/citation-shape checks `scripts/citation_lint.py` actually implements. It did not assess prose quality, argument structure, rhetorical repetition, or any of the subtler style concerns `docs/STYLE_GUIDE.md` describes (stock introductions, formulaic triples, vague attribution) - those require human or LLM judgement, not a deterministic script, and were not separately assessed in this pass.
