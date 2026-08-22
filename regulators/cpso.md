---
regulator: College of Physicians and Surgeons of Ontario (CPSO)
jurisdiction: Canada - Ontario (provincial; physicians and surgeons only)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added as the worked reference-province example for Canadian physician regulation - Canada has no single national physician regulator, so this profile deliberately covers one province (matching virtual-hospital's existing "canada-ontario" jurisdiction pack) rather than a non-existent national body; sourced via live WebSearch and direct `rtk curl` fetch against cpso.on.ca, not recalled from training data
---

# CPSO

The fifth regulator profile in this repository, following `ico.md`'s format - see `README.md`. This is the first Canadian *professional* regulator profile (compare `health-canada.md`, a products regulator). Canada has no national equivalent of the UK's GMC: physician licensure and discipline is set province-by-province under each province's own legislation, so this profile intentionally covers one province - Ontario, the largest by population - as the worked example, matching the `canada-ontario` entry already in `virtual-hospital`'s jurisdiction registry. `cno.md` (nursing) and `college-des-medecins-quebec.md` (Quebec's differently-structured model) sit alongside it.

## Statutory basis

Per `cpso.on.ca` (checked 2026-08-22): CPSO's authority and powers derive from the **Regulated Health Professions Act, 1991 (RHPA)**, specifically its **Health Professions Procedural Code** (Schedule 2 to the RHPA, which supplies the procedural framework common to all 28 of Ontario's regulated health professions' colleges), together with the profession-specific **Medicine Act, 1991** and regulations made under both statutes. CPSO governs the practice of medicine in Ontario, including physicians and (per its own site) physician assistants under a separate regulatory framework.

## Investigation stages

Per `cpso.on.ca/public/services/complaints-and-concerns` (checked 2026-08-22) and corroborating legal-practice sources describing the same statutory process:

- **Complaint/report intake** - the public can file a complaint; employers, facilities, and other health professionals can file a mandatory report; CPSO's Registrar can also initiate an investigation on the College's own motion.
- **Investigation** - an investigator gathers information and reports to the **Inquiries, Complaints and Reports Committee (ICRC)**, which oversees all investigations into a registrant's care, conduct, or capacity to practise.
- **ICRC decision** - after reviewing the investigation, the ICRC may: take no further action; require the physician to attend a caution in person; require remedial education, a Specified Continuing Education or Remediation Program (SCERP), or an undertaking restricting practice; or refer the matter to discipline.
- **Discipline hearing** - referred matters are heard by the **Ontario Physicians and Surgeons Discipline Tribunal (OPSDT)**. Per sources checked, OPSDT is the operating identity CPSO adopted (from around 2021) for what remains, in statute, the Discipline Committee under the Health Professions Procedural Code - it functions as a neutral, independent adjudicative body with a dedicated full-time independent chair, holding hearings similar to a court, rather than a purely internal College committee. `UNVERIFIED`: whether OPSDT has since been formally re-constituted as a legally distinct tribunal (as opposed to remaining the statutory Discipline Committee under a public-facing brand) was not fully confirmed this session - the practical process and appeal route are the same either way per sources checked.

## Sanction range

Per sources checked: CPSO/OPSDT discipline outcomes range from advice, remediation, and a **public reprimand**, through **terms, conditions, or limits** placed on a certificate of registration, to **suspension** (fixed period), to **revocation** of the certificate of registration. A finding of professional misconduct following a discipline hearing must be published by CPSO. Reported examples checked this session include a licence revocation and a four-month suspension, illustrating the range in practice rather than only in theory.

## Appeal route and forum

Two distinct routes exist depending on which decision is being challenged - do not conflate them:

- **ICRC decisions** (e.g. a caution, a SCERP, or a decision not to refer to discipline) are reviewable by either the physician or the complainant before the **Health Professions Appeal and Review Board (HPARB)**, an independent adjudicative agency (unaffiliated with CPSO or the Ontario government) that reviews decisions of all 28 RHPA-governed colleges, typically within 30 days of the ICRC decision. Per sources checked, HPARB review is deliberately limited in scope - no live witnesses, no transcripts/recordings - and is confined to two questions: whether CPSO's investigation was adequate, and whether the ICRC's decision was reasonable. HPARB decisions referring a matter to discipline (rather than resolving it) are themselves **not** appealable to HPARB.
- **Discipline Tribunal/Discipline Committee decisions** are appealed to the **Divisional Court** under section 70 of the Health Professions Procedural Code, generally within 30 days, typically heard by a three-judge panel with written and oral argument. Per a reported Court of Appeal decision checked this session, significant deference is owed to the Tribunal's penalty orders on appeal - the Divisional Court does not lightly depart from established penalty ranges.

## Primary sources checked

- `cpso.on.ca/public/services/complaints-and-concerns` (fetched directly via `rtk curl`, checked 2026-08-22 - complaint intake and process overview)
- `cpso.on.ca/About/Committees` and `cpso.on.ca/About/Legislation-By-Laws` (statutory framework, referenced via WebSearch)
- `canlii.org` full text listings for the Regulated Health Professions Act, 1991 (SO 1991, c 18) and the Medicine Act, 1991 (SO 1991, c 30) - existence and citation confirmed, full provision text not independently re-read this session
- Reporting on the Ontario Physicians and Surgeons Discipline Tribunal's establishment and role (Society of Ontario Adjudicators and Regulators; CPSO's own `dialogue.cpso.on.ca` "Tribunal Outcomes" page, referenced via WebSearch)
- Legal-practice summaries of HPARB review scope and the Divisional Court appeal route (Koziebrocki Law, Wise Health Law), cross-checked against the Health Professions Appeal and Review Board's own Wikipedia-sourced description and a reported Court of Appeal decision on deference to penalty orders

## What is NOT in this profile

No verified current statutory text of the Health Professions Procedural Code's specific sections (cited by number/title only, not independently re-read against the primary legislative text this session beyond confirming the Act's existence on CanLII). No confirmation of OPSDT's precise legal status (branded operating identity of the statutory Discipline Committee, versus a formally re-constituted distinct tribunal) - flagged `UNVERIFIED` above. No case-by-case CPSO discipline-decision database - this is a procedural/structural profile, consistent with `../GOVERNANCE.md`'s `COMMUNITY_REVIEWED` (not yet `MAINTAINER VERIFIED`) standard. Covers physicians and surgeons only, not physician assistants' separate regulatory track.
