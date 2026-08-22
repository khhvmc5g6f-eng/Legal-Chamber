# Matter Lifecycle

```
INTAKE → RESEARCHING → DRAFTING → REVIEWING → ADVERSARIAL_REVIEW →
HUMAN_REVIEW_PENDING → VERIFIED_FOR_FILING → CLOSED
```

These are the `status` values on `../schemas/matter.schema.json`. A matter can move backward (e.g. `REVIEWING` finds a gap → back to `RESEARCHING`) - the lifecycle is not strictly linear, and forcing it to look linear in the record would misrepresent what actually happened.

**Update `intake/matter.json`'s `status` field every time a matter actually moves to a new stage below - not just at intake.** A stress test found a matter that had completed all five moot hearings and a final disposition while its own record still read `status: "INTAKE"`. A status that isn't kept current is worse than no status at all - `scripts/verify_matter_persistence.py` and any human reviewer both rely on it being real.

## 1. INTAKE

`../agents/intake/ROLE.md` classifies matter type and complexity tier. `../agents/jurisdiction/ROLE.md` resolves jurisdiction(s) - by asking, never by inference. A lightweight conflict check runs before anything sensitive is ingested (parties, related entities, opposing counsel named so far).

Open `matters/<MATTER-ID>/` with the standard subdirectories (see `../skills/legal-work/SKILL.md` Step 3). This directory is gitignored in this repository - never commit matter data.

## 2. RESEARCHING

`../skills/legal-research/SKILL.md` / `../agents/research/ROLE.md` build the Fact Ledger, Evidence Ledger (with `../agents/evidence/ROLE.md`), and verified authorities. Bidirectional search is mandatory - a supporting-only research pass does not satisfy this stage.

## 3. DRAFTING

`../skills/legal-draft/SKILL.md`, informed by `../agents/solicitors/ROLE.md` for case-theory-driven documents. Draft metadata (`../schemas/draft.schema.json`) is attached from the first version.

## 4. REVIEWING

`../agents/counsel/ROLE.md` (fresh context) challenges the draft/case theory before it goes further. `../skills/legal-verify/SKILL.md` runs the integrity pass (citations, quotations, facts, dates).

## 5. ADVERSARIAL_REVIEW

For `L4` and above: `../skills/legal-moot/SKILL.md` or the full `five-hearing-adversarial.md` workflow, using `../agents/opposition/ROLE.md` and `../agents/judiciary/ROLE.md` in isolated contexts.

## 6. HUMAN_REVIEW_PENDING

`../agents/quality/ROLE.md` runs `../docs/QUALITY_GATES.md` against the matter record and reports pass/fail per gate. The matter sits here until an actual human reviewer acts.

## 7. VERIFIED_FOR_FILING

Set only by a human reviewer editing the matter record directly. No skill, agent, or workflow in this repository sets this value. Once a document is marked `sent_or_filed: true` on its draft record, it is immutable - further changes create a new version, never an overwrite.

## 8. CLOSED

Terminal state. The matter workspace remains for the record; it is not deleted.
