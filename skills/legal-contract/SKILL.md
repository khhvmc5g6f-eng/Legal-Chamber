---
name: legal-contract
description: Draft, review, or negotiate a contract - clause-by-clause analysis, dependency mapping between clauses, red-flag detection. Use for transactional documents rather than litigation material.
---

# legal-contract

For clause extraction, the position matrix, and dependency mapping below, run `../../agents/transactional/ROLE.md` in a fresh context.

## Clause extraction

Pull out, per contract: parties, obligations, conditions, warranties, indemnities, liability caps, termination, renewal, payment, IP, data, confidentiality, dispute resolution, governing law, assignment, restrictive covenants, audit rights, insurance, third-party rights.

- **Restrictive covenants** - non-compete, exclusivity, no-solicit of customers, no-solicit of employees, and any stated exception to those restrictions. Easy to miss under a generic "obligations" read; they're a distinct, commonly-negotiated risk category with their own market-position norms (cross-checked against CUAD, the Contract Understanding Atticus Dataset, CC-BY-4.0 - see `../../docs/EXTERNAL_SOURCES.md`).
- **Most Favored Nation** - a pricing/terms guarantee clause, not implied by any of the other buckets above. High commercial impact, easy to miss if not checked for explicitly.
- **Audit rights, insurance, third-party beneficiary** - standard in many services/licensing agreements, absent from "obligations"/"liability caps" unless checked for by name.
- **Right of first refusal/offer/negotiation (ROFR/ROFO/ROFN)** - relevant in supply, distribution, and equity-adjacent deals.
- **Liquidated damages** - a distinct mechanism from a liability cap (a pre-agreed fee vs. a ceiling on recoverable loss) - don't fold it into "liability caps" without checking which one the clause actually is.
- **"Change control" vs. "change of control" - these are not the same clause, disambiguate on sight.** "Change of control" is the M&A-trigger sense (who can terminate/must consent if ownership of a party changes) - closely related to assignment. "Change control" is the procedure for varying scope or deliverables during contract performance - an operational clause, not a risk-allocation one. Extract both separately if both are present; don't let one word cover for the other.
- **IP** collapses several materially different questions worth asking separately when IP terms matter to the deal: who owns it (ownership assignment vs. joint ownership), who's licensed to use it (license grant, non-transferable vs. affiliate-extendable), and whether that license is perpetual/irrevocable or terminates with the agreement. IP disputes usually turn on exactly this distinction, not on "IP" as a single bucket.

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
- Due diligence mode above is for a single contract or document set. When the review is one workstream inside a larger deal (multiple workstreams, conditions precedent, closing mechanics) → `../legal-transaction/SKILL.md`, which owns the combined `RED_FLAG_REPORT`/`DUE_DILIGENCE_REGISTER` across workstreams.
