# Five-Hearing Adversarial Workflow

The `L5 CHAMBERS` tier from `../skills/legal-work/SKILL.md`. Each hearing must build on the findings and repairs from the one before it - five hearings that repeat the same arguments is a failure of the workflow, not a thorough one.

Run each hearing with `../agents/opposition/ROLE.md` and `../agents/judiciary/ROLE.md` in contexts isolated from whichever agent built the case being tested - see `AGENTS.md`'s independence rule. Because those contexts are isolated, "building on the last hearing" is not something that happens automatically - it happens because hearing N+1 is handed hearing N's `../schemas/hearing.schema.json` record and told to read it before starting. There is no other channel between hearings. Store each hearing's record at `matters/<ID>/moot/hearing-<n>.json`.

## Before hearing 1 - what this workflow does not model

This workflow tests argument and evidence quality across five simulated hearings. It does **not** model the interim procedural layer that resolves or reshapes most real cases before a full hearing ever happens: disclosure timing, interim applications (strike-out, summary judgment, injunctions), case management conferences, or amendment of pleadings. Hearing 1's strike-out check below is a merits-quality test ("would this survive scrutiny"), not a simulation of an actual interim strike-out application with its own procedure and timing. Treat this workflow as testing the case that would eventually reach a full hearing, not as a substitute for `../skills/legal-litigation/SKILL.md`'s procedural tracking of what happens before then. `interim-applications.md` (this directory) gives strike-out/summary-judgment/injunction/case-management a decision framework - structural, not jurisdiction-verified content - see `../docs/HONEST_STATUS.md` for exactly what that does and doesn't close.

## Hearing 1 - Justiciability and pleadability

Test: jurisdiction, standing, limitation, whether a cause of action actually exists on these facts, whether the essential elements are even arguable, and strike-out risk. If the matter fails here, later hearings are moot - say so rather than running them anyway.

Write a `hearing.schema.json` record (`hearing_number: 1`, `stage: JUSTICIABILITY_AND_PLEADABILITY`) with `findings`, `repairs_required`, and `disposition` before moving to Hearing 2.

## Hearing 2 - Doctrinal and authority challenge

Read Hearing 1's record first - re-litigating a point it already resolved without addressing its `repairs_required` is the "five identical arguments" failure mode this workflow exists to prevent.

Test: is the legal test actually as stated, do the binding authorities actually say what's claimed (per `../docs/OPERATING_RULES.md`'s verification hierarchy), and what adverse authority exists that hasn't been addressed. Write the Hearing 2 record the same way.

## Hearing 3 - Evidence and proof

Read Hearings 1-2's records first. Test: burden and standard actually met, admissibility of key evidence, credibility, corroboration, causation, and any contradictions found by `../agents/evidence/ROLE.md`. Write the Hearing 3 record.

## Hearing 4 - Procedure and remedy

Read Hearings 1-3's records first. Test: procedural compliance (deadlines actually verified, not recalled), whether the remedy sought is actually available, and relevant discretion. Write the Hearing 4 record.

Costs are deliberately **not** assessed here. In real practice, costs are argued and decided *after* the substantive outcome - they follow the event, and are often the subject of separate submissions (conduct during the case, settlement offers, proportionality of the winning side's own costs). Predicting a costs outcome before the merits are even decided in Hearing 5 gets the sequence backwards; see "After hearing 5" below for where costs actually belong.

## Hearing 5 - Full merits

Read Hearings 1-4's records first. User's counsel (`../agents/counsel/ROLE.md`, separate context from whoever built the case) presents. Opposing counsel (`../agents/opposition/ROLE.md`) presents the strongest reasonable opposing case. A reply. `../agents/judiciary/ROLE.md` (separate context from both) delivers a reasoned simulated disposition - which may go against the user. Write the Hearing 5 record, including `disposition` and `reasons`.

### Making "may decide against the user" a checkable claim, not just an aspiration

The isolation rule in `AGENTS.md` is the mechanism, but on its own it's unaudited - nothing currently tracks whether it actually produces adverse dispositions in practice. Once more than a handful of real matters have been run through this workflow, `hearing.schema.json`'s `disposition` field across all `hearing-5.json` records is a real, checkable data point: if a corpus of runs never once produces a disposition against the user, that is itself a finding worth investigating (either the isolation isn't working, or the cases run through it were simply strong) - see `../docs/HONEST_STATUS.md` and `../benchmarks/README.md`'s adversarial benchmark category, which this data should eventually feed.

## After hearing 5

Now assess costs, using the actual disposition from Hearing 5: likely costs consequences given who won, on what issues, and any settlement offers or conduct in play - see `../skills/legal-negotiation/SKILL.md` if a settlement/offer history is relevant to the costs position.

Run the appellate question both directions (`../skills/legal-appeal/SKILL.md`): if the user won, how might the opponent appeal; if the user lost, what appeal points genuinely exist.

Feed everything back into `../schemas/prospect.schema.json` and the matter's issue/proof records - the five hearings should visibly change those records, not just produce a narrative report that sits beside them unused.
