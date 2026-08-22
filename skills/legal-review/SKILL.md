---
name: legal-review
description: Review someone else's legal reasoning, draft, or strategy for soundness - distinct from legal-verify's narrow citation/fact integrity pass. Use for a broader "is this argument any good" review, of a document the user or a third party produced.
---

# legal-review

## What this checks that legal-verify doesn't

`../legal-verify/SKILL.md` checks integrity (citations, facts, quotations, dates). This skill checks whether the argument itself is sound: does the issue tree cover what it needs to (`../../schemas/issue.schema.json`), does each conclusion actually trace to supporting authority/fact/evidence (`../../schemas/conclusion.schema.json`), was a disconfirming search plausibly run, and does the document steelman or strawman the other side.

## Method

1. Reconstruct the argument map as it actually is (not as the document claims it is) - conclusion, propositions, authority, evidence, counterargument-and-answer.
2. Check every load-bearing conclusion has real support, not just an assertion with a citation attached that doesn't actually establish it (this is the "authority proposition test" from `../../docs/OPERATING_RULES.md`).
3. Look for the case-killers the document might have missed: limitation, jurisdiction, standing, an unaddressed exclusion clause.
4. Check remedy: does the relief sought match what's actually available?
5. Note gaps as gaps - don't quietly patch them yourself and present the result as a review of the original.

## Output

A structured review, not a rewrite: strongest point, weakest point, missing element, unaddressed counterargument, and (if asked) a prospects read using `../legal-prospects/SKILL.md`'s dimensions.
