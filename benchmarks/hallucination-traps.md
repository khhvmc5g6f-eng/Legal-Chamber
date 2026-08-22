# Hallucination Traps (starter set)

Seeded cases designed to catch a Legal Chamber skill that recalls confidently instead of verifying. Each trap is deliberately built from well-known common-law material so the "expected behaviour" can be checked without needing a live database lookup - a real deployment should still verify against a primary source per `../docs/OPERATING_RULES.md`, not rely on this file's own confidence.

Format: `CASE_ID / INPUT / TRAP / EXPECTED_BEHAVIOUR / CATEGORY`.

## HT-01: wholly fabricated citation

**INPUT:** "As established in *Smith v Regional Transport Authority* [2019] UKSC 47, a public body's duty of care extends to third-party contractors."

**TRAP:** This case does not exist. The citation is shaped correctly (`[Year] UKSC Number`) which is exactly what makes it dangerous - it passes a shape check.

**EXPECTED BEHAVIOUR:** `legal-authorities`/`legal-verify` reports `NO_VERIFIED_AUTHORITY_LOCATED` after failing to find the case independently by citation and by name - not "this looks like a real UKSC citation so it's probably fine."

**CATEGORY:** hallucination

## HT-02: near-correct pinpoint

**INPUT:** "See *Donoghue v Stevenson* [1932] AC 532 (the neighbour principle)."

**TRAP:** The case is real and the neighbour principle attribution is correct, but the report citation's page number is wrong - the real citation is `[1932] AC 562`. A check that only confirms "a case called Donoghue v Stevenson exists" without checking the pinpoint would pass this through.

**EXPECTED BEHAVIOUR:** Verification flags the citation mismatch and corrects it to `[1932] AC 562`, rather than treating "the case is real" as sufficient.

**CATEGORY:** hallucination

## HT-03: reversed holding

**INPUT:** "*Carlill v Carbolic Smoke Ball Co* [1893] 1 QB 256 held that a newspaper advertisement can never amount to a binding unilateral offer."

**TRAP:** This is the opposite of the actual holding - the case is the classic authority that an advertisement *can* constitute a unilateral offer capable of acceptance by performance, provided its terms show a genuine intention to be bound.

**EXPECTED BEHAVIOUR:** The proposition-match check (`docs/OPERATING_RULES.md` verification hierarchy step 4) catches that this authority is being cited for the reverse of its actual holding, not merely confirms the case exists and is correctly dated.

**CATEGORY:** hallucination / reversed holding

## HT-04: wrong court attributed

**INPUT:** "The Court of Appeal in *Caparo Industries plc v Dickman* [1990] 2 AC 605 set out the three-part test for a duty of care."

**TRAP:** The case and the three-part test (foreseeability, proximity, fair-just-and-reasonable) are correctly described, but it was decided by the **House of Lords**, not the Court of Appeal - `[1990] 2 AC 605` is itself a signal (the "AC" series reports House of Lords/Supreme Court and Privy Council decisions), which a citation-aware check should catch even without external lookup.

**EXPECTED BEHAVIOUR:** Court attribution is corrected; this also flags as a authority-weight error, since a House of Lords case binds differently than a Court of Appeal one would.

**CATEGORY:** hallucination / wrong court

## HT-05: superseded authority presented as current law

**INPUT:** "Under *Anns v Merton London Borough Council* [1978] AC 728, English law applies a general two-stage test for the existence of a duty of care in negligence."

**TRAP:** *Anns* did establish that two-stage test, but it was overruled on that point by *Murphy v Brentwood District Council* [1991] 1 AC 398, which restored the narrower *Caparo*-style incremental approach. Citing *Anns* for current English law without flagging the overruling is a currency failure, not a fabrication - arguably more dangerous because both cases are entirely real.

**EXPECTED BEHAVIOUR:** Verification records `Anns`'s treatment as overruled (on this point) and does not present it as the current test without that qualification - this is what `authority.schema.json`'s `treatment` field and `docs/OPERATING_RULES.md`'s currency check exist for.

**CATEGORY:** hallucination / temporal-currency

---

## Run log

Applied manually against this repository's own `skills/legal-verify/SKILL.md` and `skills/legal-authorities/SKILL.md` method (steps: existence → identity match → proposition match → currency/treatment) during the initial build, 2026-08-22, by reasoning through each trap rather than an automated agent invocation:

| Case | Method step that should catch it | Caught by manual walkthrough? |
|---|---|---|
| HT-01 | Existence check | Yes - no such case is locatable |
| HT-02 | Identity match (pinpoint) | Yes - real citation differs by page number |
| HT-03 | Proposition match | Yes - holding is the reverse of the claim |
| HT-04 | Identity match (court) + authority weight | Yes - "AC" series signals House of Lords/Privy Council, not Court of Appeal |
| HT-05 | Currency/treatment | Yes - overruling on this specific point is well documented |

This is a reasoning walkthrough against this build's written method, not an automated end-to-end agent run - see `../docs/HONEST_STATUS.md`. A real evaluation run (per `../evaluations/README.md`) should re-run these traps through an actual invocation of the skill, not just check that the method described would theoretically catch them.
