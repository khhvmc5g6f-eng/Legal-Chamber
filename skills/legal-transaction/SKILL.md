---
name: legal-transaction
description: Acquisitions, financings, property, and other corporate/commercial transactions - due diligence, conditions tracking, closing mechanics. Use for deal work broader than a single contract.
---

# legal-transaction

## Due diligence workstreams

Corporate, commercial, employment, regulatory, litigation, IP, data, property, finance - run each as its own workstream, and combine into a single `RED_FLAG_REPORT` and `DUE_DILIGENCE_REGISTER` (see `../legal-contract/SKILL.md` for the shared format) rather than one undifferentiated review.

## Conditions engine

Track, per transaction: conditions precedent, required consents/approvals, deliverables, signatures, closing actions, and post-closing actions. A condition without a named owner and a status is a gap, not a tracked item.

## Structure before drafting

Confirm deal structure (asset vs share sale, financing structure, property transfer mechanism) is settled, and confirm which jurisdiction's law actually governs each document in the transaction - a multi-document deal can have different governing law per document.

## Hand off

- Individual contract clause work within the transaction → `../legal-contract/SKILL.md`.
- Regulatory approval/consent required as part of closing → `../legal-regulatory/SKILL.md`.
- The actual closing documents → `../legal-draft/SKILL.md`.
