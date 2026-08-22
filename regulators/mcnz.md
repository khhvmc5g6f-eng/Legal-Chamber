---
regulator: Medical Council of New Zealand (Te Kaunihera Rata o Aotearoa)
jurisdiction: New Zealand (national - one regulator, no sub-national variation)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added to give New Zealand a doctors' regulator profile alongside the ICO/CNIL/FTC set, sourced via live WebSearch/WebFetch against mcnz.org.nz, hpdt.org.nz, and legislation search results, not recalled from training data
---

# MCNZ

The fourth regulator profile in this repository, following `ico.md`'s format - see `README.md`. This is the first HPCAA-family profile; `nursing-council-nz.md` shares its Tribunal/appeal structure and should be read alongside it.

## Statutory basis

The Medical Council of New Zealand is the statutory regulator for doctors, established under the **Health Practitioners Competence Assurance Act 2003 (HPCAA)** - the single Act that creates a separate statutory council for each regulated health profession in New Zealand (medicine, nursing, pharmacy, dentistry, and others), all sharing common mechanisms for professional conduct committees, a disciplinary tribunal, and appeals. The Council's principal statutory function is public protection: assessing and responding to concerns about a doctor's conduct, competence, and health that might affect fitness to practise.

## Investigation stages - and the split with the Health and Disability Commissioner

This is the point most likely to be got wrong, so stated explicitly first, per `ico.org.uk`-style sourcing discipline (checked live 2026-08-22 via `mcnz.org.nz`):

- **All complaints about a doctor received by the Medical Council must be referred to the Health and Disability Commissioner (HDC).** This is not optional triage - it is how the Council's own published complaints guidance describes the relationship. The HDC is legislatively the front door for complaints implicating a health consumer's rights (see `hdc.md`).
- **The Commissioner sometimes refers a complaint back to the Council for assessment** - typically where the concern is about the doctor's ongoing fitness to practise (conduct, competence, or health) rather than, or in addition to, whether a specific consumer's rights under the Code of Health and Disability Services Consumers' Rights were breached.
- Separately, under the Health and Disability Commissioner Act 1994 and HPCAA (referenced together in Ombudsman and legislative search results checked 2026-08-22, though the full text of HPCAA s64(1) was not itself successfully fetched this session - flagged `UNVERIFIED` at the level of exact subsection wording, not at the level of the referral relationship itself, which is independently confirmed by the Council's own published page), a complaint referred to the Commissioner is treated as if made directly to the Commissioner.

Once a matter is with the Council (either directly for a non-HDC-mediated fitness concern, such as a self-report or third-party notification about health or competence, or via referral back from HDC), the Council may take one of several paths per its own published fitness-to-practise material:

- Refer to a **Health Committee** to inquire into a health concern.
- Refer to a **Competence Review Committee** for assessment and report on a competence concern.
- Refer to a **Professional Conduct Committee (PCC)** to investigate a conduct concern and decide whether to lay a disciplinary charge.

A PCC's investigation can end in no further action, counselling, referral to police, a review of the doctor's practice, or a disciplinary charge laid before the **Health Practitioners Disciplinary Tribunal (HPDT)**.

## Disciplinary body - shared across professions, not doctor-specific

The HPDT is **not** a Medical-Council-only body. It was established under **section 84 of the HPCAA** on 18 September 2004, superseding the old Medical Practitioners Disciplinary Tribunal, and hears charges against practitioners across the professions regulated under the HPCAA - confirmed live this session by the Tribunal's own decision-search file-number prefixes (`Med` for medical practitioners, `Nur` for nurses, `Phys` for physiotherapists, among others) at `hpdt.org.nz`. The Tribunal comprises a legally-qualified chairperson, deputy chairs, and registered-practitioner and lay members, all Minister-of-Health appointed. It does not itself receive or investigate complaints - charges are filed either by a PCC or by the HDC's **Director of Proceedings** (see `hdc.md`), which is the second route by which an HDC-originated complaint can reach the Tribunal independently of the Council's own PCC route.

## Sanction range

Per HPCAA s101 (confirmed via live search of HPDT decision documents citing s101(1) paragraphs), the Tribunal's powers include, roughly in descending severity: cancellation of registration; suspension for up to three years; conditions on practice for up to three years; censure; a fine of up to **NZ$30,000**; and an order for part or all of the costs of the investigation, prosecution, and hearing. Unpaid fines or costs can result in the Registrar declining to act on that practitioner's registration.

## Appeal route and forum

Appeals against HPDT decisions go to the **High Court** under HPCAA Part 5 (around s106), to be filed within **20 working days** of the Tribunal's decision. The High Court's decision is final except on points of law, which may be further appealed to the **Court of Appeal**. Penalties generally stay in force pending appeal unless a court orders otherwise.

## Primary sources checked

- `mcnz.org.nz/fitness-to-practise/` (fitness-to-practise overview - conduct, competence, health)
- `mcnz.org.nz/support/support-for-patients/councils-principles-for-assessment-and-management-of-complaints-and-notifications/` (referenced in search results confirming the mandatory HDC-referral relationship; the page itself 404'd on direct fetch this session, so this specific claim rests on the search engine's synthesis of that page's content rather than a direct read - flagged accordingly)
- `mcnz.org.nz/support/related-agencies/health-practitioners-disciplinary-tribunal/` (Council-HPDT relationship)
- `hpdt.org.nz` (Tribunal establishment, cross-profession scope via decision file-number prefixes, statutory basis)
- Search-engine synthesis of HPCAA s101 and s106 text and of HPDT decision PDFs citing those sections (direct fetch of `legislation.govt.nz` and `nzlii.org` was blocked by HTTP 403 this session - the statutory text itself is therefore secondhand via search snippets and citing case documents, not independently read in full)

## What is NOT in this profile

No independently-read primary text of HPCAA s64, s84, s101, or s106 - `legislation.govt.nz` and `nzlii.org` both returned HTTP 403 to direct fetch this session, so those provisions are sourced through search-engine summaries and Tribunal decision documents that cite them, not through reading the Act itself. Verify the exact statutory wording directly against `legislation.govt.nz` before relying on this profile for anything requiring precise subsection citation. No case-by-case MCNZ or HPDT decision database - this is a procedural/structural profile only, consistent with `COMMUNITY_REVIEWED` (not `MAINTAINER VERIFIED`).
