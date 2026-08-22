# ID Conventions

Every `schemas/*.schema.json` ID field is a free-text string by design (different matters, teams, and tools will want different schemes) - but leaving it completely unspecified means a long-running matter worked across multiple sessions or agents will produce colliding or inconsistent IDs with nothing to catch it. This file fixes a default convention. A matter may adopt its own instead, as long as it's stated once in that matter's `intake/` record and used consistently.

## Default prefixes

| Record type | Prefix | Example |
|---|---|---|
| Fact (`schemas/fact.schema.json`) | `F-` | `F-001` |
| Evidence (`schemas/evidence.schema.json`) | `EX-` | `EX-014` |
| Authority (`schemas/authority.schema.json`) | `AUTH-` | `AUTH-007` |
| Issue (`schemas/issue.schema.json`) | `ISS-` | `ISS-003` |
| Deadline (`schemas/deadline.schema.json`) | `DL-` | `DL-002` |
| Chronology event (`schemas/chronology.schema.json`) | `CHR-` | `CHR-045` |
| Legal conclusion (`schemas/conclusion.schema.json`) | `CONC-` | `CONC-001` |
| Draft (`schemas/draft.schema.json`) | `DRAFT-` | `DRAFT-001` (with `version` incrementing within the same ID, not a new ID per revision) |
| Hearing (`schemas/hearing.schema.json`) | `H-` | `H-1` through `H-5` for the five-hearing workflow, or `H-<n>` for `legal-moot`'s single-pass use |

## Numbering rule

Sequential within a matter, zero-padded to at least 3 digits (`F-001`, not `F-1`), never reused even if a record is later superseded - a superseded fact keeps its ID and gets its status updated (e.g. to `CONTRADICTED`), it does not get deleted and its number recycled.

## Cross-references

When a chronology event, issue, or conclusion cites a fact or evidence item, it references the exact ID string (`fact_ids: ["F-003", "F-012"]`), not a description of the item. This is what makes the Fact Ledger, Evidence Ledger, and chronology actually checkable against each other rather than three separately-maintained narratives that can silently drift - see `docs/QUALITY_GATES.md` Gate 2 and Gate 7.
