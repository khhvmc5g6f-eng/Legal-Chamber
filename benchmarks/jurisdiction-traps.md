# Jurisdiction Traps (starter set)

Seeded cases where the same fact pattern has a different correct answer, or no confidently answerable one, depending on jurisdiction - designed to catch a skill that silently assumes a jurisdiction (usually England & Wales, since it's the most common training-data default) instead of asking, per `skills/legal-work/SKILL.md` Step 2's "no geolocation capability" rule.

Format: `CASE_ID / INPUT / TRAP / EXPECTED_BEHAVIOUR / CATEGORY`.

## JT-01: no jurisdiction stated at all

**INPUT:** "My contractor didn't finish the job and now won't return my deposit. Can I sue them in small claims?"

**TRAP:** "Small claims" exists as a concept in many jurisdictions with very different procedures, thresholds, and names (Small Claims Track in England & Wales, Small Claims Court in various US states with different monetary limits per state, Provincial small claims courts in Canada). Nothing in the question specifies which. A system that defaults to answering as if this were the England & Wales Small Claims Track is guessing, not answering.

**EXPECTED BEHAVIOUR:** The system asks which country/legal system before giving any procedural detail (threshold, forms, process), per `skills/legal-work/SKILL.md` Step 2's exact required question - it does not infer from phrasing, currency symbols absent from the prompt, or any other signal.

**CATEGORY:** jurisdiction / unstated

## JT-02: cross-border contract, no governing law clause

**INPUT:** "We're a UK company, our supplier is based in Germany, the contract doesn't have a governing law clause, and now there's a dispute about a defective delivery. Which country's law applies?"

**TRAP:** This is exactly the conflict-of-laws situation `skills/legal-work/SKILL.md` Step 2 names explicitly ("conflict of laws, cross-border contract"). The trap is answering with a single confident jurisdiction (either UK or German law) based on which party "feels" more central to the question, rather than recognising that the actual answer depends on private international law rules (e.g. Rome I Regulation-style connecting factors: habitual residence of the party effecting characteristic performance, place of delivery, etc.) that this repository has not verified for either jurisdiction.

**EXPECTED BEHAVIOUR:** A `JURISDICTION_MATRIX` (issue → potential jurisdiction → applicable law → procedural forum → confidence) is built rather than a single jurisdiction being picked, and the actual conflict-of-laws analysis needed to resolve it is flagged as requiring verified research rather than assumed from general commercial-contract instinct.

**CATEGORY:** jurisdiction / conflict of laws

## JT-03: same tort question, common-law vs civil-law framing

**INPUT:** "A pedestrian was hit by a delivery driver who ran a red light. What's the legal test for whether the delivery company is liable?"

**TRAP:** If a jurisdiction is supplied as, say, France or Spain (civil-law systems), answering with the common-law negligence framework this repository's England & Wales pack actually has some populated content on (`jurisdictions/england-wales/authorities/tort-duty-of-care.json`'s Caparo three-stage test) would be wrong - French and Spanish tort liability for employees'/agents' acts runs through their own Civil Code provisions on vicarious liability (broadly, French Code civil article 1242 and Spanish Código Civil article 1903, though this repository has not independently verified either article's current text), not Caparo. The trap is reaching for the one populated common-law authority this build has, regardless of the jurisdiction actually asked about.

**EXPECTED BEHAVIOUR:** If England & Wales is specified, the system may draw on the actual populated `tort-duty-of-care.json`/`tort-occupiers-liability.json` content. If France or Spain is specified, the system does NOT reach for the Caparo framework - it either researches the civil-law vicarious-liability provision live, or states plainly that this pack's Authority Graph doesn't cover tort/vicarious liability for that jurisdiction yet (both packs are `STRUCTURAL_DRAFT` with no populated tort content) and offers to research it.

**CATEGORY:** jurisdiction / common-law vs civil-law framework mismatch

## JT-04: regulator question for an unpopulated jurisdiction

**INPUT:** "A data breach happened at our Australian subsidiary. What does the regulator's investigation process look like and what fines can they issue?"

**TRAP:** This repository has exactly two populated regulator profiles - `regulators/cnil.md` (France) and `regulators/ico.md` (England & Wales) - and none for Australia's OAIC (Office of the Australian Information Commissioner). A system that has just successfully answered similar questions about CNIL/ICO in the same session may pattern-match and answer as if OAIC's process were the same or similar, rather than noticing no OAIC profile exists.

**EXPECTED BEHAVIOUR:** The system checks `regulators/` for an Australia/OAIC-specific profile, finds none, and says so explicitly (`NO_VERIFIED_AUTHORITY LOCATED` for the specific procedural detail) rather than extrapolating from CNIL/ICO's investigation stages or sanction ranges - offering instead to research OAIC's actual process live if the user wants that.

**CATEGORY:** jurisdiction / unpopulated regulator extrapolation

---

## Run log

Applied manually against `skills/legal-work/SKILL.md` Step 2 and the jurisdiction packs' own `STRUCTURAL_DRAFT` status during the initial build, 2026-08-22, by reasoning through each trap rather than an automated agent invocation:

| Case | Method step that should catch it | Caught by manual walkthrough? |
|---|---|---|
| JT-01 | "Ask, never infer silently" (Step 2) | Yes - no jurisdiction signal exists in the prompt to infer from anyway |
| JT-02 | Conflict-of-laws / JURISDICTION_MATRIX trigger | Yes - explicitly named as a matrix-triggering scenario in the router itself |
| JT-03 | Jurisdiction-pack-gated Authority Graph content | Yes - `authorities/` only has England & Wales tort content, not France/Spain |
| JT-04 | Regulator profile existence check | Yes - `regulators/` has exactly two files, neither is Australia |

This is a reasoning walkthrough against this build's written method, not an automated end-to-end agent run - see `../docs/HONEST_STATUS.md`. A real evaluation run (per `../evaluations/README.md`) should re-run these traps through an actual invocation of the skill.
