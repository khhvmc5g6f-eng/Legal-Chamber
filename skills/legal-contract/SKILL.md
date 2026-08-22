---
name: legal-contract
description: Draft, review, or negotiate a contract - clause-by-clause analysis, dependency mapping between clauses, red-flag detection. Use for transactional documents rather than litigation material.
---

# legal-contract

## Clause extraction

Pull out, per contract: parties, obligations, conditions, warranties, indemnities, liability caps, termination, renewal, payment, IP, data, confidentiality, dispute resolution, governing law, assignment, change control.

## Position matrix, per clause

```
Current wording → legal effect → commercial effect → risk →
market position → preferred position → fallback position → rationale
```

Don't assess a clause in isolation from what "market" actually looks like for this deal type - if you don't know current market practice for this specific sector/jurisdiction, say `UNVERIFIED` rather than asserting a market position from general impression.

## Dependency mapping

Contract clauses interact. Before finalising a change, trace its effect through the rest of the document - e.g. a termination clause change likely touches outstanding payments, IP licence cessation, data return, confidentiality survival, and indemnities. A clause-by-clause review that never checks dependencies will miss the ones that actually matter.

## Governing law

Apply the correct jurisdiction pack for the contract's actual governing-law clause, not the jurisdiction either party happens to be based in - these are frequently different, and the difference matters (see `../../jurisdictions/*/README.md` civil-law vs common-law framing, which changes how a clause is even interpreted).

## Due diligence mode

For red-flag review across a document set: produce a `RED_FLAG_REPORT` (issue, clause/document, why it's a flag, severity, recommended fix) and a `DUE_DILIGENCE_REGISTER` (item, status, owner). Track conditions precedent, required consents/approvals, and closing deliverables separately from the substantive risk review.

## Hand off

- Need the actual redline/draft produced → `../legal-draft/SKILL.md`.
- Need negotiation strategy around leverage, not legal merits → `../legal-negotiation/SKILL.md` (keep the two separate - a strong legal position and negotiating leverage are not the same thing).
