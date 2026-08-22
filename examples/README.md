# Examples

Worked example matters showing the skills, schemas, and workflows actually being used together, end to end.

## Status

**Not built in this version.** See `../docs/HONEST_STATUS.md` and its roadmap: the recommended first example is one matter type, one jurisdiction (e.g. an unfair-dismissal question in England & Wales, or a contract dispute in US Federal via the CourtListener connector), run fully through `legal-work` → `legal-research` → `legal-verify` → the quality gates, with every authority actually checked against a primary source rather than illustrated schematically.

## What a good example should demonstrate

- A populated `matters/<MATTER-ID>/` workspace (as a fixture, not real client data - never commit real matter data, see `.gitignore` and `SECURITY.md`).
- At least one fact, one piece of evidence, one authority, and one issue record actually filled in against the schemas in `../schemas/`.
- A completed quality-gate pass (`../docs/QUALITY_GATES.md`) shown honestly, including any gate that didn't pass and why.
