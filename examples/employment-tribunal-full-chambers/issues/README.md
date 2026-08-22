# Issue tree, M1-KESTREL - methodology and verification status

`issues.json` holds 9 `schemas/issue.schema.json` records (ISS-001 to ISS-009), 24 elements total, covering the ACAS EC/limitation threshold plus the eight substantive heads named in the task instruction (procedural unfairness is treated as a remedy/fairness-assessment issue rather than a ninth free-standing cause of action, since it has no independent elements of its own separate from ERA 1996 s.98(4) and the ACAS Code uplift/Polkey mechanics - noted expressly on ISS-009 rather than silently merged away).

## What is, and is not, verified here

- **Verified live this session (by the prior session that opened this matter, re-confirmed by inspection this session)**: ERA 1996 s.111, s.207B, and Equality Act 2010 s.123 - fetched against legislation.gov.uk, see `procedure/limitation.md`. ISS-001 rests on these.
- **NOT independently re-verified against a primary source this session**: every other statutory reference used to build elements below - ERA 1996 ss.94, 95, 98, 98(4), 103A, 47B, 48; Equality Act 2010 ss.6, 15, 20, 21, 27, 136; Trade Union and Labour Relations (Consolidation) Act 1992 s.207A. These are stated from general legal knowledge of well-established UK employment law doctrine, not from a live check against legislation.gov.uk or a case-law source this session. Per `CLAUDE.md` rule 1 for this repository, this is flagged rather than presented as checked. Before any of ISS-002 to ISS-009 is relied on for actual drafting or advice, these provisions should be independently confirmed the same way ISS-001's were.
- No `schemas/authority.schema.json` records exist for this matter (no `authorities/` directory under `matters/M1-KESTREL/`), so `authority_ids` is omitted from every element rather than populated with invented IDs - the statutory references live only in the free-text `element`/`standard` fields for now.

## Evidence

No `schemas/evidence.schema.json` records exist for this matter either (no `evidence/` directory), because no actual documents (emails, OH reports, sickness records, disciplinary file, termination letter) were supplied - only their existence is alleged. `evidence_available_ids` is therefore empty on every element; `evidence_missing` lists what would need to be obtained, in line with `skills/legal-evidence/SKILL.md`'s missing-document-detection instruction. Fabricating evidence records for documents nobody has produced would misrepresent the state of the file.

**Correction, later session**: the statement above that "no `authorities/` directory exists" is now stale - `authorities/authorities.json` was added in a subsequent session (7 `schemas/authority.schema.json` records, including the rejected seeded/fabricated citation and its full verification trail - see `research/research_log.md`). Left as a live example of exactly the doc-vs-data drift `docs/ID_CONVENTIONS.md` and `CLAUDE.md`'s "schemas are the source of truth" principle warn about: this file was not updated when the data changed underneath it. `authority_ids` on the issue elements above still has not been backfilled to point at the now-existing `AUTH-002` to `AUTH-007` records - that cross-link remains outstanding.

## Proof status is deliberately low

Almost every element is `UNSUPPORTED` or `PARTIALLY_SUPPORTED`. This is not a drafting shortcut - it reflects that the scenario states the *existence* of the relevant categories of material (disclosures, disciplinary process, OH material, sickness records, termination documentation, contradictory emails) without stating their *content*. An issue tree that showed `SUPPORTED` anywhere on that basis would be overstating the file.
