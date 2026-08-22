---
regulator: CNIL (Commission nationale de l'informatique et des libertés)
jurisdiction: France
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added after a stress test's regulatory-mode matter (M5) found this repository's regulators/ directory was empty; sourced via live WebSearch against cnil.fr and conseil-etat.fr, not recalled from training data
---

# CNIL

The first regulator profile in this repository - see `README.md` for the format every future profile should follow. Filled in per `../GOVERNANCE.md`'s sourcing requirement: primary source and check date per claim below.

## Statutory basis

CNIL is France's independent data protection authority, empowered under the French Data Protection Act (*Loi Informatique et Libertés*) and, since 2018, as the French supervisory authority under the GDPR. It also became a supervisory authority under the EU AI Act with penalty powers reported up to €35 million as of 2026 - flagged `UNVERIFIED` pending a primary-source check of the exact AI Act provision, since this pack's own house rule is not to assert a specific figure from a secondary summary alone.

## Investigation stages

Per `cnil.fr/en/investigation-powers-of-cnil` (checked 2026-08-22): investigations may be carried out on-site, document-based, by hearing, or online. CNIL can enter business premises during business hours, access IT systems, and copy relevant data. A sanction procedure may follow a complaint, a reported violation, or CNIL's own investigation.

Per `cnil.fr/en/sanctions-procedure` and `cnil.fr/en/steps-procedure-sanction` (checked 2026-08-22), there are **two distinct enforcement tracks**, not one:

- **Ordinary procedure**: the CNIL chair appoints a *rapporteur* (from among the commissioners, excluding restricted-committee members) and refers the matter to the *formation restreinte* (restricted committee) - 5 commissioners plus an elected chairperson. The incriminated organisation is informed, receives the documents exchanged between the rapporteur and the organisation during the written procedure, and may be heard if the rapporteur considers it useful. The restricted committee deliberates in camera and decides whether its decision is made public. This track can impose the full range of GDPR penalties.
- **Simplified procedure** (introduced 2022): for cases without particular difficulty, decided by a single committee member ruling alone, without a public hearing unless the organisation requests one.

Do not assume a matter automatically gets a public adversarial hearing - only the ordinary-procedure track works that way, and even then a hearing is not automatic per the sources checked.

## Sanction range

Per the sources above: fines up to €20 million or 4% of global annual turnover (whichever is higher, per GDPR Article 83's structure - the exact cross-reference was not independently re-checked against the Article text itself in this pass), injunctions, and temporary or permanent processing bans. CNIL issued 83 sanctions totalling €486.8 million in 2025 per a secondary source (Recording Law/CMS-type enforcement-tracker summary) - recorded as context, not as a verified regulatory rule.

## Appeal route and forum

Per `cnil.fr` and the *Conseil d'État*'s own published decisions (e.g. décisions n° 467774, n° 449284, checked 2026-08-22): a CNIL sanction decision is appealed to the **Conseil d'État** (not an ordinary court) within **2 months** of notification. This is a real, jurisdiction-specific procedural deadline - if a matter needs it calculated, use `../scripts/deadline_calculator.py` with `--rule-source` citing this profile and re-verify the 2-month figure against the specific decision's notification, not assumed from this summary alone.

## Primary sources checked

- `cnil.fr/en/investigation-powers-of-cnil`
- `cnil.fr/en/sanctions-procedure`
- `cnil.fr/en/steps-procedure-sanction`
- `cnil.fr/en/powers-restricted-committee`
- `conseil-etat.fr` decisions n° 467774 (2023-03-27) and n° 449284 (2022-04-26), confirming the appeal route

## What is NOT in this profile

No verified GDPR Article 83 cross-reference for the fine cap. No verified current text of the AI Act provision giving CNIL its reported €35m AI-related penalty power - that figure came from a secondary source, not `cnil.fr` or an official EU text, and must be re-checked before being relied upon. No case-by-case CNIL decision database - this is a procedural/structural profile, not a populated precedent library, consistent with `../docs/HONEST_STATUS.md`'s standard for what a `COMMUNITY_REVIEWED` (not yet `MAINTAINER VERIFIED`) profile actually contains.
