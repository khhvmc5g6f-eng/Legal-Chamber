---
regulator: CQC (Care Quality Commission)
jurisdiction: England only - the quality/provider regulator for the English NHS and independent health and adult social care sector; has no jurisdiction in Wales, Scotland, or Northern Ireland, each of which has its own separate equivalent (see hiw.md, his.md; Northern Ireland's is the RQIA, not covered in this set)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added alongside mhra.md to build out the UK healthcare-regulator set, sourced via live WebSearch against cqc.org.uk and gov.uk, not recalled from training data
---

# CQC

The tenth regulator profile in this repository, and - like MHRA - **not** an individual-practitioner fitness-to-practise body: CQC regulates **care providers and premises** (NHS trusts, GP practices, care homes, independent hospitals, and other regulated-activity providers), not named individual clinicians - see `README.md`.

## Statutory basis

The CQC is the statutory regulator of health and adult social care providers in England, under the **Health and Social Care Act 2008**. Its distinguishing feature, per the sources checked, is that it created **one single registration regime covering both NHS bodies and independent/private providers together for the first time** - both an NHS trust and a private clinic carrying out a "regulated activity" (as defined by the **Health and Social Care Act 2008 (Regulated Activities) Regulations 2014**) must register with the CQC and meet the same fundamental standards (Regulations 8-20A of the 2014 Regulations). This single-regime, provider-registration model is notably different from Scotland's and Wales's equivalents, which register independent providers but only *inspect* (without a parallel registration-and-cancellation power) their national NHS bodies - see `his.md` and `hiw.md` for that distinction, confirmed on both sides this session.

## Enforcement stages (registration/inspection, not "investigation of a person")

Per `cqc.org.uk` (checked 2026-08-22): CQC's civil enforcement escalation runs through:

- **Warning Notice** - used to require rapid improvement; a registered person has **10 working days** to make written representations, and there is **no right of appeal to a tribunal** against a Warning Notice itself.
- **Notice of Proposal** - CQC's formal proposal to take enforcement action (e.g. to impose/vary conditions, or to cancel registration); the registered person has **28 days** to make written representations disputing it.
- **Notice of Decision** - issued if CQC does not accept the representations and confirms the proposed action; this is the point at which a right of appeal to a tribunal arises (see below).
- **Urgent procedures** - for serious, immediate risk to life, health, or wellbeing, CQC can apply to a **magistrate** for an order to cancel registration immediately, bypassing the Notice of Proposal stage; any appeal in this situation is fast-tracked.

Separately, since April 2015 CQC has had power to **prosecute** breaches of the fundamental standards (Regulated Activities Regulations 2014, Regulations 8-20A) as criminal offences without needing police involvement, most commonly Regulation 12 (Safe Care and Treatment); several of these regulations require the breach to have exposed people to avoidable harm, a significant risk of it, or financial loss before they qualify for prosecution.

## Sanction range

Per the sources checked: civil enforcement outcomes include **conditions on registration**, **suspension**, and **cancellation of registration** (which, for a provider, functionally ends its ability to legally operate the regulated activity). Criminal prosecution under the 2014 Regulations carries an **unlimited fine** (no custodial sentence identified in the sources checked - CQC prosecutions are against organisations/registered managers, not a criminal offence carrying imprisonment in the sources reviewed this session).

## Appeal route and forum

Per `cqc.org.uk`'s own enforcement-policy pages (checked 2026-08-22): a registered person can appeal a **Notice of Decision** to the **First-tier Tribunal (Care Standards)**, within **28 days** of service of the notice - the same tribunal, and the same 28-day window, used by Wales's HIW for its own registration appeals (see `hiw.md`). There is explicitly **no** tribunal appeal against a Warning Notice, a penalty notice, or a criminal conviction (the latter follows the ordinary criminal appeal route instead).

## Primary sources checked

- `cqc.org.uk/guidance-regulation/providers/enforcement` and its "Representations and appeals", "Notices of Proposal, Notices of Decision and urgent cancellation orders", and "Enforcement policy" sub-pages (indexed via WebSearch)
- `cqc.org.uk/guidance-regulation/providers/enforcement/offences/health-social-care-act-2008-regulated-activities-offences` (prosecutable offences list, indexed via WebSearch)
- `cqc.org.uk/guidance-regulation/providers/registration/scope-registration` (registration scope covering both NHS trusts and independent providers, indexed via WebSearch)
- Secondary legal-sector sources (Stephensons Solicitors, House of Commons Library briefing CBP-8754, Ashfords, Dac Beachcroft, HCR Law) cross-checked for prosecution trends and the unlimited-fine position

## What is NOT in this profile

No individually-verified confirmation of whether any custodial sentence attaches to a Regulated Activities Regulations 2014 offence for an individual (as opposed to an unlimited fine) - the sources checked this session describe fines only; this should be re-checked directly against the Regulations before asserting a custodial maximum either way. No case-by-case CQC enforcement-action or prosecution database - this is a procedural/structural profile only. No verified detail on CQC's separate ratings system (Outstanding/Good/Requires Improvement/Inadequate) - a distinct CQC function from formal enforcement, not researched here.
