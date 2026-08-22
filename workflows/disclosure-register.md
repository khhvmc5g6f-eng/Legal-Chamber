# Disclosure Register

A working register for tracking document review and disclosure decisions on a matter, built on `../schemas/evidence.schema.json`'s `disclosure` object. Naming and specific rules (what must be disclosed, standard vs specific disclosure, privilege log format) are jurisdiction-specific - check the relevant `../jurisdictions/<slug>/README.md` and the applicable procedural rules before relying on this as more than a tracking template.

## Fields (per evidence item, from `evidence.schema.json`)

`bundle_reference · exhibit_number · page_range · disclosure_status · relevance_decision · reviewed_by · reviewed_date`

## Workflow

1. Every document ingested into `matters/<ID>/evidence/` gets an `evidence.schema.json` record before it is reviewed, with `disclosure_status: NOT_YET_REVIEWED`.
2. Review sets `relevance_decision` and moves `disclosure_status` to `DISCLOSED`, `WITHHELD_PRIVILEGE`, `WITHHELD_OTHER`, or `REDACTED_AND_DISCLOSED` - never leave an item at `NOT_YET_REVIEWED` once a bundle is being assembled.
3. A withheld-for-privilege item needs its `privilege` field on the same record populated with a real basis (`legal advice privilege`, `litigation privilege`, etc.) per `../docs/OPERATING_RULES.md` - `WITHHELD_PRIVILEGE` without a stated basis is not a defensible privilege log entry.
4. Bundle assembly (`bundle_reference`, `exhibit_number`, `page_range`) happens only for items marked `DISCLOSED` or `REDACTED_AND_DISCLOSED` - see `../courts/README.md` for the target court's own bundle/pagination rules, which override any generic numbering here.
5. Attachments and their cover email/document share a `family` value (see `evidence.schema.json`) so the register can reconstruct what came with what.

## Missing-document check

Cross-reference the register against `../skills/legal-evidence/SKILL.md`'s missing-document detection - a document logically expected (an attachment mentioned in a disclosed email, a referenced contract) but absent from the register at all is a gap to flag, not to fill in from inference.

## Status

This is a tracking template, not an automated disclosure-review engine - relevance and privilege decisions are made by a human or an agent role (`../agents/evidence/ROLE.md`), not derived automatically. See `../docs/HONEST_STATUS.md`.
