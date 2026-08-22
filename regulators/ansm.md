---
regulator: Agence Nationale de Sécurité du Médicament et des Produits de Santé (ANSM)
jurisdiction: France
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added for Virtual Hospital International's French healthcare regulator coverage; sourced via live WebFetch against ansm.sante.fr, not recalled from training data
---

# ANSM

Fourth regulator profile in this repository, following the format set by `cnil.md` (see `README.md`). Filled in per `../GOVERNANCE.md`'s sourcing requirement: primary source and check date per claim below.

## Statutory basis

ANSM is France's medicines and medical-devices regulator, created by the law of 29 December 2011 to replace the former AFSSAPS with reinforced powers and means, following the "Mediator" (benfluorex) scandal. It is a French public établissement, governed by the Code de la santé publique (Book III, per `legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072665/LEGISCTA000006140633/`, not independently opened and read article-by-article this session - flagged `UNVERIFIED` at that level of detail). Per `ansm.sante.fr/qui-sommes-nous` (checked 2026-08-22), ANSM describes itself as "the public actor who permits, in the name of the State, access to health products in France and ensures their safety throughout their life cycle."

Unlike CNOM/ONI above, ANSM is a product-safety regulator, not a professional-conduct regulator - it does not discipline individual doctors or nurses; its remit is medicines, vaccines, and medical devices themselves.

## Missions and powers

Per `ansm.sante.fr/qui-sommes-nous` (checked 2026-08-22), ANSM's three stated primary missions are:

1. Facilitating access to therapeutic innovation through adapted authorisation procedures (including clinical-trial authorisation and *autorisations temporaires d'utilisation*/derogatory early-access routes)
2. Ensuring product safety throughout the product lifecycle, via evaluation, expertise, and surveillance (including pharmacovigilance)
3. Informing and exchanging with healthcare professionals, patients, and the public

Confirmed operational powers per the same source and corroborating search results (checked 2026-08-22): marketing-authorisation (*AMM*) decisions, inspection of manufacturers and distributors, and *police sanitaire* (health-police) action including suspension or withdrawal of authorisations and financial sanctions where a product presents a danger to health or where legislative/regulatory requirements are not met - the fetched page states sanction amounts "are proportionate to the gravity of the violations found," without a numeric cap independently verified this session.

ANSM operates within the EU's medicines framework alongside the European Medicines Agency (EMA); the exact division of competence between ANSM and EMA (e.g. centralised vs. national authorisation procedures) was not independently verified against a primary source this session and is flagged `UNVERIFIED`.

## Sanction range

Confirmed live (2026-08-22): suspension, prohibition, or financial sanctions, which may be accompanied by daily penalty payments (*astreintes*), against persons producing or marketing the products or associated services, "in cases provided by law." No specific euro figure or percentage-of-turnover cap for ANSM financial sanctions was found and independently verified in this session - unlike CNIL's sanction cap (see `cnil.md`), do not assume a comparable figure for ANSM without checking the specific Code de la santé publique article that sets it.

## Appeal route and forum

Not independently verified this session. ANSM decisions are administrative decisions of a public établissement, so the general French administrative-justice route (*tribunaux administratifs*, with onward appeal) would ordinarily apply, but this was not checked against a primary source specific to ANSM sanction decisions in this session - flagged `UNVERIFIED`, do not assert a specific appeal forum or deadline for ANSM without checking it directly.

## Primary sources checked

- `ansm.sante.fr/qui-sommes-nous`

## What is NOT in this profile

No verified appeal route/forum or deadline for ANSM sanction decisions. No verified numeric sanction cap. No independent read of the Code de la santé publique's ANSM-specific Book III articles beyond the section-index page found in search results. No verification of the ANSM/EMA competence split. This profile is deliberately narrower than `cnil.md` and `ordre-des-medecins.md` - only what was actually checked live is asserted; the gaps above are the concrete next steps for anyone extending this profile.
