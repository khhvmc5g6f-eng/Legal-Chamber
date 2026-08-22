---
name: legal-prospects
description: Assess likelihood of success without producing a full research/drafting/adversarial cycle - a standalone "what are my chances" output. Use for a focused prospects question; the fuller assessment still runs through legal-litigation/legal-moot for anything consequential.
---

# legal-prospects

## Assess each dimension separately - do not average

Law, facts, evidence, procedure, credibility, causation, remedy, discretion, appellate uncertainty. A mechanical average across these hides which one is actually driving the risk. Use `../../schemas/prospect.schema.json`.

## Calibrated language, not false precision

`VERY STRONG / STRONG / REASONABLE / BALANCED / WEAK / VERY WEAK`. If a numeric range is requested, state it with the assumptions driving it - never present a number as if it were an empirical measurement.

## Scenario and sensitivity analysis

State best realistic / central / worst realistic case, with the assumption driving each. Then run the counterfactual test: which single fact or piece of evidence, if it changed, would most alter the outcome? That's usually where further work should actually go.

## Uncertainty budget

Track where the uncertainty is actually coming from - factual gaps, legal uncertainty, authority conflict, evidential gaps, procedural ambiguity - rather than letting it disappear into a confidently-worded prose conclusion.

## Remedy-first

Before quoting prospects on liability, confirm the remedy sought is one the decision-maker can actually grant (see `../legal-litigation/SKILL.md`). Strong liability prospects toward an unavailable remedy is not a strong case.

## Hand off

- Prospects look weak on a specific issue → `../legal-research/SKILL.md` to re-check that issue, or `../legal-evidence/SKILL.md` if the gap is evidential.
- Want this pressure-tested rather than just estimated → `../legal-moot/SKILL.md`.
