---
regulator: MHRA (Medicines and Healthcare products Regulatory Agency)
jurisdiction: United Kingdom (executive agency of the Department of Health and Social Care, acting on behalf of the Secretary of State; medical device regulation extends to Great Britain and Northern Ireland under the post-Brexit UKCA/CE transitional regime, with some Northern Ireland-specific EU-alignment detail not researched here)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added alongside gdc.md to build out the UK healthcare-regulator set, sourced via live WebSearch against gov.uk (the MHRA's publishing platform) and legislation.gov.uk, not recalled from training data
---

# MHRA

The ninth regulator profile in this repository, and the first that is **not** an individual-practitioner fitness-to-practise body - see `README.md`.

## A different kind of regulator - read this before the sections below

Every other profile in this repository so far (ICO's data-protection role aside) or planned for this set (GMC, NMC, HCPC, GPhC, GDC) investigates and adjudicates allegations against a **named individual professional**, ending in a tribunal decision about that person's registration. The **MHRA does not work this way**. It is a **product and market-safety regulator** for medicines, medical devices, and blood components - its "subjects" are products, manufacturers, distributors, and marketing authorisation holders, not individual clinicians. It has no register of individual practitioners, no fitness-to-practise committee, and no tribunal that decides whether a named person can keep working. Forcing this profile into the "investigation of a person → tribunal → appeal" shape used elsewhere in this repository would misrepresent how MHRA regulation actually works, so the sections below are adapted rather than filled in by rote.

## Statutory basis

The MHRA is an executive agency of the Department of Health and Social Care, acting on behalf of the Secretary of State as the UK's competent authority for human medicines and medical devices. Its powers derive primarily from the **Human Medicines Regulations 2012** (for medicines) and the **Medical Devices Regulations 2002** (for devices), both made under enabling primary legislation, most recently consolidated and extended by the **Medicines and Medical Devices Act 2021**.

## What MHRA regulatory action looks like (in place of "investigation stages")

Per `gov.uk` (checked 2026-08-22): MHRA activity is organised around **market surveillance and post-market vigilance** rather than case-by-case allegations against a person. Its toolkit includes:

- **Market surveillance** - monitoring products already on the UK market for safety, quality, and performance issues (e.g. via the Yellow Card adverse-event reporting scheme).
- **Compliance escalation** - for manufacturing-standard (GMP/GDP) issues, the MHRA Inspectorate uses a graded escalation process from advisory letters through to licence suspension/revocation.
- **Formal caution** or **criminal prosecution** - breaches of the Human Medicines Regulations 2012 or Medical Devices Regulations 2002 are **criminal offences**, prosecuted by the MHRA through the ordinary criminal courts (magistrates' court or Crown Court on indictment), not through a fitness-to-practise-style tribunal. Under Regulation 338 of the Human Medicines Regulations 2012, a senior manager of a company can be personally prosecuted where an offence occurred with their neglect, consent, or connivance.
- **Device conformity assessment is delegated** - for medical devices, conformity certification (UKCA marking) is carried out by MHRA-appointed **Approved Bodies** (e.g. BSI), which themselves have power to award, suspend, and revoke certificates for safety or non-conformity reasons; the MHRA sits above this as the designated competent authority with its own separate market-surveillance and enforcement powers.

## Sanction range (criminal, not disciplinary)

Per `legislation.gov.uk`'s text of the Human Medicines Regulations 2012 and corroborating secondary sources (checked 2026-08-22): under **Regulation 255**, offences are triable either way - on **summary conviction**, a fine not exceeding the statutory maximum; on **conviction on indictment**, an **unlimited fine**, **imprisonment for up to two years**, or both. Convicted company directors can also face disqualification, and a convicted defendant typically bears the MHRA's prosecution costs. This is a criminal sanction range against a company or individual defendant in a criminal court, not a disciplinary sanction against a registered professional.

## Appeal route and forum

There is no single "appeal route" in the fitness-to-practise sense, because MHRA action doesn't run through a single adjudicative body. Two distinct routes were identified this session:

- **Criminal prosecutions** are appealed through the ordinary criminal appellate route (Crown Court to Court of Appeal (Criminal Division), as with any UK criminal conviction) - not independently re-verified against a primary MHRA source this session, so treat as `UNVERIFIED` pending a direct check.
- **Approved Body certificate decisions** (e.g. a UKCA certificate suspension) are challenged by **judicial review** in the Administrative Court, not a statutory appeal to a dedicated tribunal. Per a 2024 Court of Appeal judgment found this session (`RRR Manufacturing Pty Ltd v British Standards Institution and MHRA` [2024] EWCA Civ 530), the courts have shown marked deference to the regulator/Approved Body in this context, particularly on interim relief in public-health-adjacent cases.

## Primary sources checked

- `gov.uk/guidance/regulating-medical-devices-in-the-uk` and the MHRA's Medicines and Medical Devices Act 2021 corporate/enforcement material (indexed via WebSearch)
- `legislation.gov.uk/uksi/2012/1916/regulation/255` (Human Medicines Regulations 2012, offence and penalty provision, indexed via WebSearch)
- `mhrainspectorate.blog.gov.uk` (MHRA Inspectorate's own blog describing its compliance-escalation process, indexed via WebSearch)
- Secondary legal-sector sources (Lexology's two articles on UK pharmaceutical/device enforcement, BioSlice Blog and Dac Beachcroft's coverage of the 2024 Court of Appeal Approved Body judgment) for the judicial-review route on device certification

## What is NOT in this profile

The criminal-appeal-route claim above is explicitly flagged `UNVERIFIED` - it was not checked against a primary source this session and rests on general knowledge of the UK criminal appellate system, not a checked MHRA-specific source. No verified detail on MHRA's separate clinical-trials authorisation function (a third major MHRA remit alongside medicines and devices, not researched here). No verified detail on the Northern Ireland-specific medicines/device regime under the Windsor Framework - flagged in the jurisdiction line above as not researched. This profile does not and cannot describe an "investigation of a person" process, because that is not how this regulator functions - see the note at the top of this file.
