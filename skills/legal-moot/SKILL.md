---
name: legal-moot
description: Stress-test a case theory adversarially before relying on it - a lighter, on-demand version of the full five-hearing workflow. Use when the user wants "does this actually hold up" rather than the full L5 CHAMBERS process.
---

# legal-moot

This is the on-ramp to `../../workflows/five-hearing-adversarial.md` - use this skill for a single focused adversarial pass; use the full workflow file directly for `L5 CHAMBERS`-tier matters.

## Minimum viable moot

1. **Steelman.** Build the strongest reasonable version of the opposing case from verified law, fact, and evidence - not a strawman. Use `../../agents/opposition/ROLE.md` as a fresh, isolated context; don't have the same context that built the case also attack it.
2. **Falsify.** Ask: what evidence or authority would make this conclusion wrong? Then actually look for it, rather than asserting none exists.
3. **Devil's advocate.** Look specifically for unstated assumptions, authority gaps, factual gaps, remedy gaps, and procedural vulnerabilities.
4. **Concession check.** Identify which points are safe to concede (and might even help credibility) versus which would be fatal if conceded.
5. **Judicial hot-bench.** Have `../../agents/judiciary/ROLE.md` (fresh context) ask the hardest questions it can about the weakest authority, the worst factual contradiction, jurisdiction, and remedy - and have the case answered from verified material only, not improvised.

## Output

A findings list ranked by how much each finding could change the outcome, plus what evidence/research would resolve the biggest open one first (the counterfactual test: which single fact, if changed, would most alter the result?).

## Escalate

If this reveals the matter is genuinely contested and high-stakes, move to the full `../../workflows/five-hearing-adversarial.md` rather than trying to cram five hearings' worth of scrutiny into one pass.
