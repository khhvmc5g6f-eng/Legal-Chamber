---
name: legal-verify
description: Pure verification pass over already-drafted legal material - checking every citation, quotation, fact, and procedural claim against a primary source without re-doing the substantive drafting. Use when a document already exists (written by the user, or by another Legal Chamber skill) and needs an integrity check before it is relied upon.
---

# legal-verify

This skill does one thing: it tries to break the document in front of it, on integrity grounds, not on strategy or style.

## Run through, in this order

1. **Quotation lock.** Every quoted string gets checked against its stated source and pinpoint. If it can't be verified, the quotation marks come off and the point is paraphrased instead, or marked `UNVERIFIED` - see `../../docs/OPERATING_RULES.md`.
2. **Citation existence test.** For every citation: does it exist (search the citation and case name independently), is the court/date/jurisdiction right, and does it actually establish the proposition it's cited for - not dicta-as-ratio, not a dissent, not an overturned decision, not a different statutory regime. Use `../../schemas/authority.schema.json` to record the result of each check, and run `../../scripts/citation_lint.py` for shape-level issues (it cannot confirm a citation is real - only that it's shaped like one, or that the surrounding prose violates house style).
3. **Fact audit.** Every factual proposition traces to a source at least as strong as its claimed `../../schemas/fact.schema.json` status. A fact marked `ESTABLISHED` that actually only traces to a user assertion gets its status corrected, not left inflated.
4. **Procedural check.** Every deadline or filing requirement gets checked against the applicable jurisdiction pack and, where a specific date is asserted, `../../scripts/deadline_calculator.py` with a real `--rule-source` - not recalled from memory.
5. **Adverse authority check.** Was a disconfirming search actually run for the document's main propositions? If not, that's a gap to flag, not to quietly patch by inventing a plausible-sounding counterargument yourself.
6. **Style pass, last.** Only after the above, run the `../../docs/STYLE_GUIDE.md` checks. A style edit must never change a fact, date, number, quotation, or legal proposition - if it would, stop and flag `SUBSTANTIVE_REVIEW_REQUIRED` instead of making the edit.

## Output

A findings list, not a rewritten document by default (unless asked to fix in place): for each issue, what's wrong, why, and what would resolve it. Never silently upgrade a document's filing state - see `../../docs/QUALITY_GATES.md`. `VERIFIED FOR FILING` is set only by a human reviewer.
