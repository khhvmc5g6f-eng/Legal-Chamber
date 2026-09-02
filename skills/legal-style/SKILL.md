---
name: legal-style
description: Run the deterministic authorship-and-style-integrity pass over any document, not only one legal-draft just produced - paste in an existing draft, a document from elsewhere, or anything you want polished for clarity and house style. A plain-language drafting-polish tool, not an AI-detector-evasion one - see "What this will never do" below before assuming otherwise.
---

# legal-style

`../legal-draft/SKILL.md` Step 6 runs this same process automatically on a document it just wrote. This skill is the same process, callable directly on any document at any time, standalone.

## What this actually does

Two passes, in order, never reordered:

1. **Structural pass** - argument flow, paragraph order, repetition, headings, transitions.
2. **Sentence pass** - diction, punctuation, rhythm, clichés, no stock AI-prose phrases ("it is important to note," "in today's," mechanical rhetorical triples, generic headings, boilerplate that restates rather than resolves).

Then a **substantive re-verification pass**: every quotation, citation, date, number, and legal proposition is checked against the pre-edit version. If a style edit changed meaning, it is reverted and flagged `SUBSTANTIVE_REVIEW_REQUIRED`, not silently kept. See `../../docs/STYLE_GUIDE.md`'s order of precedence: legal accuracy, evidential accuracy, procedural accuracy, and precision all outrank naturalness and stylistic preference. Naturalness never outranks law.

## The actual mechanism, not just the instruction

Reading the style guide is not the same as running it. Do this, in order, against the actual file:

```bash
python3 ../../scripts/citation_lint.py <the file>          # 1. see what's flagged
python3 ../../scripts/style_audit.py --json <the file>     # 2. explain rhythm, repetition, length, and stock phrasing
cp <the file> <the file>.pre-style                       # 3. preserve the source for the change lock
python3 ../../scripts/style_fix.py --apply <the file>      # 4. auto-fix the safe, same-grammatical-slot subset
# 5. make the structural/sentence edits that require judgement
python3 ../../scripts/style_audit.py --compare <the file>.pre-style <the file>  # 6. exact-value lock
python3 ../../scripts/citation_lint.py <the file>          # 7. re-check what's left
```

`style_audit.py` is deterministic and explainable. Its score describes editorial signals only; it is not an authorship probability. Comparison mode checks repeated occurrences of quotations, citations, dates, numbers, measurements, URLs, and email addresses, and exits non-zero with `SUBSTANTIVE_REVIEW_REQUIRED` when they drift. That exact-value check supports but cannot replace a human re-check of legal propositions.

`style_fix.py` only touches a short, deliberately conservative list of stock phrases with a safe plain-English replacement (see its own docstring). It never touches a quotation, a fenced code block, an em dash, or a hedged/absolute legal claim - em dashes and anything context-dependent stay flagged for a human/editorial judgement call, because the right replacement (comma, colon, semicolon, or a full stop, never breaking grammar to force it) depends on clause structure the tool can't judge safely. What step 7 still flags after step 4 is exactly that remainder - fix it by hand, then confirm `citation_lint.py` comes back clean.

## House defaults, in brief

- `em_dash: prohibited` - comma, colon, semicolon, or full stop instead, never at the cost of grammar.
- UK English by default (`analyse`, `organisation`, `licence` as noun) unless the document is for a jurisdiction whose own filings use different conventions (e.g. US spelling/terminology for a US filing).
- Hedge language (`arguably`, `likely`, `may`) only where genuine uncertainty exists - don't hedge what binding authority settles, don't assert confidence a proposition doesn't have.
- Sentence and paragraph length follow the conceptual unit, not an artificial uniform rhythm.

## Author voice (optional)

`../../templates/author_voice.example.yml` shows the schema for an optional per-user voice profile (sentence length, formality, punctuation preferences), learned only from writing samples the user actually supplies. It preserves *how a specific user writes* - it is never used to imitate a specific other identifiable person's authorship, and never introduces deliberate errors to seem more human. A skilled human legal writer does not demonstrate humanity by writing badly.

## What this will never do

- No detector-feedback loop (submit, see what an AI-detection tool flags, rewrite, resubmit). A detector's score is not an optimisation target here, and never will be.
- No adversarial detector-evasion - no watermark stripping, no token-pattern disruption. Ordinary Unicode hygiene (stray zero-width characters, smart-quote consistency) is in scope; provenance concealment is not.
- No claim that output is "undetectable" or "guaranteed human." This skill optimises for correct, natural, professionally credible legal writing, full stop - not for what a classifier decides about it afterward.

If asked to make text "pass" an AI detector, evade detection, or claims about detectability, say plainly that this skill doesn't do that and explain why (see `../../docs/STYLE_GUIDE.md`'s "What this repo will not build") rather than quietly reframing the request as a style pass.

## Hand off

- Document is still being produced from facts/evidence/authority, not yet written → `../legal-draft/SKILL.md` - this skill's process runs there automatically at the end, no need to call both.
- Need citation/fact integrity checked, not prose style → `../legal-verify/SKILL.md`.
- Need the argument itself reviewed for soundness, not just how it reads → `../legal-review/SKILL.md`.
