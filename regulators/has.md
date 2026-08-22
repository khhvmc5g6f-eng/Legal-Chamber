---
regulator: Haute Autorité de Santé (HAS)
jurisdiction: France
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added for Virtual Hospital International's French healthcare regulator coverage; sourced via live WebFetch against has-sante.fr, not recalled from training data
---

# HAS

Fifth regulator profile in this repository, following the format set by `cnil.md` (see `README.md`). Filled in per `../GOVERNANCE.md`'s sourcing requirement: primary source and check date per claim below.

## Important scope note - read before using this profile

**HAS is not a disciplinary regulator**, and this profile deliberately does not force it into the fitness-to-practise / sanction-and-appeal shape used for `cnil.md`, `ordre-des-medecins.md`, and `ordre-infirmiers.md`. Per `has-sante.fr/jcms/p_3367987/fr/organisation-de-la-has` (checked 2026-08-22), HAS is a public authority whose own stated purpose is to "développer la qualité dans le champ sanitaire, social et médico-social" (develop quality across the healthcare, social, and medico-social fields). It has **no sanctioning power over individual practitioners** and does not run an investigation-to-sanction pipeline. It is closer in function to a standards-setting, health-technology-assessment (HTA), and quality-certification body than to a professional order or a data-protection enforcer.

## Statutory basis

HAS was created in 2004 as an independent public authority (checked via `has-sante.fr`, 2026-08-22). The exact founding statute/article was not independently opened and read this session and is flagged `UNVERIFIED` at that level of citation precision.

## Missions

Confirmed live per `has-sante.fr/jcms/p_3367987/fr/organisation-de-la-has` (checked 2026-08-22):

- **Health product evaluation**: evaluating medicines, vaccines, medical devices, professional acts, and health technologies to inform reimbursement eligibility decisions by health insurance (an HTA-type function, not a licensing function - that is ANSM's role, see `ansm.md`).
- **Healthcare facility certification**: HAS's *Commission de certification des établissements de santé* decides the certification level of health establishments, and its certification service (SCES) pilots certification and follow-up procedures and the network of expert-visitors (confirmed also via `has-sante.fr/jcms/p_3219705/fr/la-certification-des-etablissements-de-sante-pour-la-qualite-des-soins` and `has-sante.fr/jcms/fc_2875474/fr/certification-des-etablissements-de-sante`, checked 2026-08-22). This certification evaluates an establishment's capacity for continuous improvement of patient care, including risk identification and control - it is an institutional quality-assurance mechanism, not a mechanism for sanctioning an individual clinician.
- **Physician/team accreditation**: HAS administers a voluntary accreditation scheme for physicians and medical teams (per the organisation page's description of its SEvOQSS division) - this is a distinct, opt-in quality scheme, not the same thing as ordinal registration/discipline covered by CNOM.
- **Clinical practice guidance**: HAS produces *recommandations de bonnes pratiques professionnelles* (clinical practice guidelines) - the guideline-authority role already reflected for HAS in `virtual-hospital/jurisdictions/src/registry.ts`'s France entry.

## What HAS does NOT do (confirmed by omission/contrast, checked 2026-08-22)

No sanction range, no disciplinary chamber, no appeal-to-Conseil-d'État pathway of the kind documented for CNOM/ONI was found for HAS, and none should be assumed. Where an establishment fails certification or a product evaluation goes against a manufacturer, the consequence runs through funding/reimbursement or regulatory-authorisation levers held by other bodies (health insurance, ANSM, the ARS - see `ars-note.md`), not through an HAS-run sanctions process against an individual.

## Primary sources checked

- `has-sante.fr/jcms/p_3367987/fr/organisation-de-la-has`
- `has-sante.fr/jcms/p_3219705/fr/la-certification-des-etablissements-de-sante-pour-la-qualite-des-soins`
- `has-sante.fr/jcms/fc_2875474/fr/certification-des-etablissements-de-sante`

## What is NOT in this profile

No verified founding-statute citation. No verified detail on the certification cycle's periodicity, scoring methodology, or consequences of a failed certification for an establishment's operating authorisation (that consequence, if any, likely runs through the ARS - see `ars-note.md` - but the linkage was not independently verified this session). No case-decision or enforcement-log content, because HAS does not run an enforcement process of that kind as far as this session's sources show.
