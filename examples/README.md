# Examples

Worked example matters showing the skills, schemas, and workflows actually being used together, end to end.

## Status

**One real example exists: `employment-tribunal-full-chambers/`** - an unedited England & Wales `L5 CHAMBERS` employment tribunal matter taken directly from a live stress test (2026-08-22), not hand-crafted. See its own `README.md` for what it demonstrates and the honest gate results, including a real, left-in imperfection (a stale matter-status field). Every other matter type/jurisdiction combination remains unbuilt - see `../docs/HONEST_STATUS.md`.

## What a good example should demonstrate

- A populated `matters/<MATTER-ID>/` workspace (as a fixture, not real client data - never commit real matter data, see `.gitignore` and `SECURITY.md`).
- At least one fact, one piece of evidence, one authority, and one issue record actually filled in against the schemas in `../schemas/`.
- A completed quality-gate pass (`../docs/QUALITY_GATES.md`) shown honestly, including any gate that didn't pass and why.
