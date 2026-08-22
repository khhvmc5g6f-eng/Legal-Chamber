---
name: legal-draft
description: Produce a legal document - pleading, memo, submission, letter, contract clause - from already-verified facts, evidence, and authority. Use after legal-research/legal-evidence have established what's actually known, or when the user supplies the substance and wants it drafted well.
---

# legal-draft

Drafting comes after verification, not instead of it. If the facts and authorities behind this document haven't been through `../legal-research/SKILL.md` or `../legal-evidence/SKILL.md` yet, do that first (or flag plainly that this draft rests on unverified material).

## 0. Correspondence register - decide before writing a word

If this document is correspondence rather than a court/institutional filing, decide first whether it is `WITHOUT PREJUDICE` or open (see `../../docs/OPERATING_RULES.md` confidentiality classifications) and hold that register throughout. Do not let negotiating or settlement content appear in an open letter, and do not let an open admission of fact hide inside a without-prejudice one - a document mixing the two is not protected the way either pure form would be, and courts scrutinise exactly this. Mark the document's register in its own metadata (not just in the text) so `../legal-verify/SKILL.md` can check it later without re-reading the whole thing.

## 1. Purpose before prose

Before writing, state internally: what must this document cause its reader to understand, accept, or do? Structure around that, for the actual audience (`docs/OPERATING_RULES.md` doesn't fix a single register - a submission to a tribunal, a client letter, and an academic answer are written differently; see `../../docs/STYLE_GUIDE.md`).

## 2. Build the argument map before the prose

```
CONCLUSION
├── Proposition A → authority + evidence
├── Proposition B → authority + evidence
└── Counterargument → answer
```

Every paragraph in the final document should trace to a node in this map. If a paragraph doesn't advance the argument, cut it - see the "prolixity" note in `../../docs/STYLE_GUIDE.md`.

## 3. Steelman the other side before finishing

Construct the strongest reasonable version of the opposing argument and answer it in the document, or explicitly note where the draft leaves it unanswered. Do not attack a weak version of the opposing case.

## 4. Compliance

Check the document against the relevant jurisdiction pack's procedural notes and, where applicable, actual court/institution formatting rules (page limits, statement of truth, certification) before calling it ready - `../../docs/QUALITY_GATES.md` Gate 13. Court/institutional rules always override house style or generic templates.

## 5. Tag it

Every draft gets `../../schemas/draft.schema.json` metadata: `ai_generated: true`, a real `verification_status`, and `human_review_status: PENDING` until an actual human reviewer changes it. Never write or imply `VERIFIED FOR FILING` yourself.

## 6. Style pass last, and don't let it change meaning

Apply `../../docs/STYLE_GUIDE.md` (no em dashes, no stock phrasing, calibrated confidence) as the final pass, then re-check that no fact, date, citation, or quotation moved. If a template exists for this document type, start from `../../templates/` rather than freeform.

## Hand off

- Need a hostile read before this goes anywhere → `../legal-verify/SKILL.md` or `../legal-moot/SKILL.md`.
- This is a contract, not litigation material → `../legal-contract/SKILL.md` has clause-specific guidance this file doesn't duplicate.
