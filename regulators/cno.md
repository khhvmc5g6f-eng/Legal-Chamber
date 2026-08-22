---
regulator: College of Nurses of Ontario (CNO)
jurisdiction: Canada - Ontario (provincial; nursing only)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added alongside cpso.md as the second Ontario reference-province profile, giving the "canada-ontario" jurisdiction pack a matching nursing regulator to its physician regulator; sourced via live WebSearch and direct `rtk curl` fetch against cno.org, not recalled from training data
---

# CNO

The sixth regulator profile in this repository, following `ico.md`'s format and `cpso.md`'s Canadian-provincial treatment - see `README.md`. Like `cpso.md`, this profile covers one province (Ontario) rather than a non-existent national nursing regulator - Canada has no single national nursing regulator, and nursing licensure/discipline, like physician licensure/discipline, is set province-by-province.

## Statutory basis

Per `cno.org` (checked 2026-08-22) and corroborating sources: CNO's authority derives from the **Nursing Act, 1991**, together with the **Regulated Health Professions Act, 1991 (RHPA)** and its **Health Professions Procedural Code** (Schedule 2 to the RHPA - the same procedural code underlying `cpso.md`, shared across all 28 RHPA-governed Ontario health-profession colleges), and CNO's own regulations and by-laws made under these Acts. CNO regulates the nursing profession in Ontario (Registered Nurses, Registered Practical Nurses, and Nurse Practitioners) in the public interest.

## Investigation stages

Per `cno.org/en/protect-public/making-a-complaint-public/` (fetched directly, checked 2026-08-22):

- **Complaint intake** - patients, family members, caregivers, or any concerned member of the public can file a complaint (a complaint cannot be made anonymously); a separate mandatory-report pathway exists for employers, facility operators, and other health professionals.
- **Alternative dispute resolution (optional)** - where both the complainant and the nurse consent, a CNO investigator can facilitate a resolution agreement instead of a full investigation; this is confidential and cannot be used in other proceedings, and the resulting agreement still requires **Inquiries, Complaints and Reports Committee (ICRC)** approval on public-interest grounds. Not available for all complaint types (e.g. not for the most serious conduct concerns, per CNO's own scoping - exact excluded categories not independently re-verified this session beyond this general statement).
- **Investigation** - where ADR is not used or not appropriate, an investigation proceeds; the nurse receives notice of the complaint and an opportunity to respond in writing.
- **ICRC decision** - the ICRC performs a screening function, deciding whether allegations are serious enough to refer to discipline. Per sources checked, the ICRC does not hear live witnesses and cannot make credibility findings. It can: take no action; require the nurse to attend a caution; require completion of an educational/remedial program (including a Specified Continuing Education or Remediation Program, SCERP); or refer allegations to the **Discipline Committee**.
- **Discipline hearing** - the Discipline Committee is a statutory committee that hears matters referred by the ICRC and decides whether the nurse engaged in professional misconduct or is incompetent; per sources checked, a typical panel is five members (three nurses, two public members).

## Sanction range

Per sources checked (CNO's own "Professional Conduct: Disciplinary Proceedings" fact sheet, cross-checked against legal-practice summaries): where the Discipline Committee finds professional misconduct or incompetence, it may order one or more of: an **oral reprimand**; a **fine**; **suspension** of registration for a specified period; **terms, conditions, or limits** on registration (e.g. restricting scope of practice); mandatory **remedial courses**; or **revocation** of the certificate of registration - directing the Registrar to revoke where the finding is sufficiently serious.

## Appeal route and forum

As with `cpso.md`, two distinct routes exist under the shared RHPA/Health Professions Procedural Code framework - do not conflate them:

- **ICRC decisions** are reviewable by either the nurse or the complainant before the **Health Professions Appeal and Review Board (HPARB)** - the same independent board that reviews CPSO's ICRC decisions and those of all 28 RHPA-governed colleges. Per sources checked, HPARB review of a CNO ICRC decision is limited to whether the investigation was adequate and whether the ICRC's decision was reasonable; ICRC decisions that refer a matter directly to the Discipline Committee are **not** reviewable by HPARB, nor are decisions following a Registrar's-report investigation, incapacity referrals to the Fitness to Practise Committee, or interim registration-suspension decisions. Per CNO's own 2024 Inquiries, Complaints and Reports Committee annual report (referenced via WebSearch, checked 2026-08-22), HPARB review requests against CNO rose materially year-on-year (152 in 2024, a reported 50.5% increase on 2023), with nurses increasingly initiating reviews themselves (not only complainants) to challenge register notations such as cautions and SCERPs.
- **Discipline Committee decisions** are appealed to the **Divisional Court** under section 70 of the Health Professions Procedural Code, the same route and general timeline (around 30 days) as `cpso.md`'s discipline appeals, since both colleges operate under the same procedural code.

## Primary sources checked

- `cno.org/en/protect-public/making-a-complaint-public/` (fetched directly via `rtk curl`, checked 2026-08-22 - full complaint process, ADR, and ICRC description)
- CNO's "Addressing Complaints at the College of Nurses of Ontario" guide and "Professional Conduct: Disciplinary Proceedings" fact sheet (referenced via WebSearch; not independently fetched in full this session)
- CNO's Inquiries, Complaints and Reports Committee 2024 Annual Report (referenced via WebSearch for HPARB review-volume figures)
- `canlii.org` listing for the Nursing Act, 1991 (SO 1991, c 32) - existence and citation confirmed, full provision text not independently re-read this session
- Legal-practice summaries of CNO discipline sanctions and HPARB review scope (Koziebrocki Law, ACL Law, gfsllp.ca), cross-checked against the Health Professions Appeal and Review Board's own published scope

## What is NOT in this profile

No verified current statutory text of the Nursing Act, 1991's or Health Professions Procedural Code's specific sections (cited by number/title only). No independently re-confirmed list of which complaint categories are excluded from alternative dispute resolution. No case-by-case CNO discipline-decision database - this is a procedural/structural profile, consistent with `../GOVERNANCE.md`'s `COMMUNITY_REVIEWED` (not yet `MAINTAINER VERIFIED`) standard. Covers Registered Nurses, Registered Practical Nurses, and Nurse Practitioners together as CNO regulates them; no separate treatment per nursing class.
