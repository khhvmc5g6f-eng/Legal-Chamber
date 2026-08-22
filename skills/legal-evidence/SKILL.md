---
name: legal-evidence
description: Build and maintain the Fact Ledger, Evidence Ledger, and chronology for a matter - classify facts by status, map evidence to issues, detect contradictions and missing-but-expected documents. Use whenever the task involves organising what's actually known versus alleged, not researching law.
---

# legal-evidence

## Fact Ledger

Every factual proposition the matter depends on gets a `../../schemas/fact.schema.json` record: proposition, status (`ESTABLISHED / ADMITTED / USER_ASSERTED / DISPUTED / INFERRED / ASSUMED / UNKNOWN / CONTRADICTED`), materiality, and supporting/contrary evidence IDs. Never let a fact's status silently drift upward (e.g. a user assertion presented later as `ESTABLISHED`) - if a status changes, say why.

## Evidence Ledger

Every document, statement, recording, or other item gets a `../../schemas/evidence.schema.json` record: type, source, authenticity, admissibility, privilege, reliability, and which issues it supports or undermines. Preserve provenance (original filename, hash if available, chain of custody) and never modify or overwrite an original - working copies, redacted copies, and exhibit copies are separate version records, not replacements.

Privilege is not the same thing as confidentiality (see `../../docs/OPERATING_RULES.md` "Confidentiality classifications") - a document can be confidential without being privileged, or vice versa. Set the `privilege` field to `UNVERIFIED` rather than guessing when the applicable jurisdiction's privilege rules haven't actually been checked for this matter, and record confidentiality separately using that same classification list where it matters to how the item can be handled or disclosed.

## Chronology

Build a dated timeline (event, actor, source, evidence, disputed?, legal significance). Actively look for:

- impossible or internally inconsistent dates
- gaps where a document or event would be expected but isn't there
- documents that appear to have been created after the fact but presented as contemporaneous
- limitation-period implications of the dates found

## Contradiction detection

Compare witness statements, pleadings, contemporaneous documents, and prior accounts against each other. Classify each contradiction found: `MINOR / EXPLAINABLE / MATERIAL / SERIOUS / POTENTIALLY DISPOSITIVE`. Do not resolve a contradiction by picking the version that helps the case - flag it and let the issue/proof-graph analysis in `../legal-litigation/SKILL.md` or `../legal-prospects/SKILL.md` deal with the consequence.

## Missing document detection

Identify documents logically expected but absent (a contract referenced in an email, a mentioned attachment that isn't in the file, an unexplained gap in correspondence). Do not presume what a missing document would contain - the gap itself is the finding.

## Hand off

- Elements/burden/standard analysis using this evidence → `../legal-litigation/SKILL.md`.
- Witness statement or cross-examination prep → this file's witness workflow is intentionally minimal; for now, keep witness knowledge (`what the witness actually knows`) separate from what a lawyer wants proved, and never insert a fact the witness hasn't supplied.
