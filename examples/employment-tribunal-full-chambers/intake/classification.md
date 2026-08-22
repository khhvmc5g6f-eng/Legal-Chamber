# Classification, M1-KESTREL

Produced by actually running `skills/legal-work/SKILL.md` Steps 1-4 against the facts given, not a description of what those steps would do.

## Step 1, matter type and complexity tier

**Matter type: `employment`** (`schemas/matter.schema.json` enum value). The facts are a single employee's dispute with a single employer over dismissal and treatment during employment - this is not general civil `litigation` in the schema's residual sense, it is the named `employment` category, even though the actual task-in-hand routes through the generic `legal-litigation` skill (see Step 4 below) because no dedicated employment specialist skill exists in `skills/` (checked: `ls skills/` lists academic, appeal, authorities, contract, draft, evidence, litigation, moot, negotiation, prospects, regulatory, research, review, transaction, verify, work - no `legal-employment`). That gap is recorded as a defect below, not silently absorbed.

**Complexity tier: `L6 COMPLEX MATTER`.** Per `skills/legal-work/SKILL.md` Step 1, L6 is "signalled by the facts, not a phrase." Here: eight overlapping heads of claim each with its own elements and burden (ordinary and automatic unfair dismissal, whistleblowing detriment, three distinct disability-discrimination causes of action plus reasonable adjustments, victimisation, and procedural fairness going to remedy); a disputed chronology; contradictory internal emails; occupational health material; sickness absence records; a disciplinary process; termination documentation; and a live, unresolved limitation question turning on facts not yet fixed (see `procedure/limitation.md`). This is a large, multi-workstream document set with several genuinely separate legal theories that must be run in parallel without letting any one concession bleed into another (`legal-litigation/SKILL.md` step 7) - exactly the L6 trigger, regardless of the fact the user did not use the words "complex" or "full chambers." Not `L5` (`CHAMBERS`): the user has not asked for a simulated opposing counsel and judicial outcome together, only for classification and jurisdiction resolution at this stage, so the L5 five-hearing workflow is not being invoked yet, though `legal-litigation/SKILL.md` step 6 would still require running its first two adversarial stages once substantive work on the case theory begins.

## Step 2, jurisdiction

See `intake/jurisdiction_note.md` for the full resolution record. Summary: **England & Wales, Employment Tribunal** - user-stated, not inferred (no geolocation capability exists in this system). Pack exists at `jurisdictions/england-wales/README.md`; its `verification_status: STRUCTURAL_DRAFT` front-matter field was read and checked before relying on anything inside it (see next section). No jurisdiction matrix needed - single jurisdiction, no cross-border element on the facts given.

## Step 3, matter workspace

Opened at `matters/M1-KESTREL/` (gitignored per repo root `.gitignore` and `CLAUDE.md` rule 2 - this workspace and everything in it must never be committed). Canary fact `EXAMPLE-FIXTURE-ID` recorded at `facts/facts.json` F-001 specifically so a later reviewer can confirm this exact record, not a paraphrase, was produced and read back.

## Step 4, routing

Per the Step 4 table, this matter needs more than one specialist skill in sequence, exactly as the table anticipates ("more than one may apply in sequence"):

| Need | Skill |
|---|---|
| Contradictory emails, disputed chronology, OH/sickness records as evidence | `skills/legal-evidence/SKILL.md` |
| Whistleblowing/discrimination/unfair-dismissal law and authority (none verified yet - see below) | `skills/legal-research/SKILL.md` |
| The actual ET1 claim, once facts and law are settled | `skills/legal-draft/SKILL.md` |
| Building and testing the claim itself in the tribunal, day-one limitation triage, issue tree, case-killer check | `skills/legal-litigation/SKILL.md` (entry point actually run first here, since it is the one that names the day-one triage that gates everything else) |
| Final check before anything is called reliable | `skills/legal-verify/SKILL.md` |

`legal-litigation/SKILL.md` was read and its Step 0 day-one triage actually executed for limitation (see `procedure/limitation.md`); client-care/costs-information and pre-action-protocol/ACAS-EC-compliance triage are flagged as outstanding, not yet actioned, since no client instructions beyond the task scenario exist to action them against.

## Quality gate check (Step 5 of the router)

Per `docs/QUALITY_GATES.md` minimum bar for anything above L1: jurisdiction stated (yes), facts labelled with a status (yes, `facts/facts.json` uses the `schemas/fact.schema.json` vocabulary throughout, several correctly marked `ASSUMED`/`UNKNOWN` rather than overstated), authorities actually checked not recalled (yes for the three ERA/EqA provisions fetched live from legislation.gov.uk this session; no for everything else in this matter - no case law has been checked yet, and none should be asserted until it is), and a disconfirming search actually attempted (not yet done - this session stopped at classification and jurisdiction resolution, per the task's actual scope; the case-killer sweep beyond limitation, and any search for authority against the claimant, are outstanding). Nothing here is being presented as `VERIFIED FOR FILING` or as a conclusion the user can act on without further work - it is a classification and jurisdiction resolution, stated as such.
