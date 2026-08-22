# Style Guide (Legal Chamber 2.1, Authorship & Style Integrity)

Order of precedence, always:

1. Legal accuracy
2. Evidential accuracy
3. Procedural accuracy
4. Precision
5. Clarity
6. Naturalness
7. Stylistic preference

Naturalness never outranks law. A stylistic pass is never allowed to change a legal proposition, a number, a date, a quotation, or a citation, see the "substantive change lock" below.

## House defaults

- `em_dash: prohibited`, replace with comma, colon, semicolon, or a full stop; never break grammar to force the substitution.
- UK English by default (`analyse`, `organisation`, `licence` as noun) unless the jurisdiction pack in use specifies otherwise (e.g. US filings use US spelling and terminology, plaintiff/defendant/motion/brief).
- No stock AI-prose phrases presented as required style: "it is important to note," "in today's," "moreover" as a paragraph-starter reflex, mechanical rhetorical triples, generic headings ("Analysis," "Discussion"), boilerplate introductions/conclusions that restate rather than resolve.
- Hedge language (`arguably`, `likely`, `may`) only where genuine uncertainty exists. Do not hedge a proposition that binding authority settles; do not assert confidence a proposition doesn't have.
- Sentence and paragraph length should follow the conceptual unit, not an artificial uniform rhythm.
- Prefer concrete, dated, sourced propositions over abstract commentary about the document itself ("this section will explore...").

## Two-pass model

1. **Structural pass**, argument flow, paragraph order, repetition, headings, transitions.
2. **Sentence pass**, diction, punctuation, rhythm, clichés.

Followed by a **substantive re-verification pass**: re-check every quotation, citation, date, number, and legal proposition survived the style passes unchanged. If a style edit changed meaning, it is reverted and flagged `SUBSTANTIVE_REVIEW_REQUIRED` rather than silently kept.

## Author voice

`templates/author_voice.example.yml` shows the schema for an optional per-user voice profile (sentence length, formality, punctuation preferences) learned only from writing samples the user supplies. It is used to preserve *how* a user writes, never to imitate a specific other identifiable person's authorship, and never to introduce deliberate errors "to look human." A skilled human legal writer does not demonstrate humanity by writing badly.

## What this repo will not build

- A detector-feedback loop (submit → see what's flagged → rewrite → resubmit against an AI-detection tool). Detector scores are not an optimisation target here.
- Adversarial detector-evasion (watermark stripping, token-pattern disruption). Ordinary Unicode hygiene (stray zero-width characters, smart-quote consistency) is in scope; provenance concealment is not.
- Any claim that output is "undetectable" or "guaranteed human." This system optimises for correct, natural, professionally credible legal writing, not for a classifier's verdict.
