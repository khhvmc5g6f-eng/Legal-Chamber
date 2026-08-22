---
regulator: Agences Régionales de Santé (ARS)
jurisdiction: France
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added for Virtual Hospital International's French healthcare regulator coverage; sourced via live WebFetch against ars.sante.fr, not recalled from training data
---

# ARS - regional quality/facility oversight layer

Short supplementary note, not a full profile in the `cnil.md` template shape, because the task scope here is narrower: confirm live what the ARS role actually is, as France's rough regional equivalent of the UK's CQC (see `cnil.md`'s sibling profile `ordre-des-medecins.md` for the CQC-equivalent comparison already used in this repository's England pack via `virtual-hospital`).

## Statutory basis and status

Per `ars.sante.fr/quest-ce-quune-agence-regionale-de-sante` (checked 2026-08-22): the ARS are *"établissements publics, autonomes moralement et financièrement"* (public institutions, morally and financially autonomous), placed under the oversight of the ministries responsible for social affairs and health, established in **2010**. There is one ARS per French region (metropolitan and overseas).

## Role relevant to healthcare-facility quality oversight

Confirmed live (2026-08-22), the ARS Director General holds several regulatory levers directly relevant to a CQC-style comparison:

- **Authorisation and control**: authorising the creation of health and medico-social establishments and services (*"l'autorisation de la création des établissements et services"*), plus ongoing operational oversight.
- **Inspection**: ARS regional inspection services (*inspection régionale autonomie santé*, IRAS - composed of health professionals, engineers, and administrative staff) conduct inspections of health and medico-social establishments, which can be scheduled or triggered urgently in case of serious risk to patients, and can be announced or unannounced (per `iledefrance.ars.sante.fr` and `centre-val-de-loire.ars.sante.fr` regional-ARS pages found in search results and `ars.sante.fr/la-mission-dinspection-controle-des-agences-regionales-de-sante`, checked 2026-08-22).
- **Administrative sanctions**: where problems identified by inspection are not resolved, the ARS can impose administrative sanctions - financial sanctions, provisional administration (*administration provisoire*), suspension, or closure of the establishment - or refer the matter to the courts or to the relevant professional order (per `ars.sante.fr`-linked search results, checked 2026-08-22; this last point was corroborated across multiple ARS-domain sources but the exact statutory sanction list was not independently opened and read article-by-article this session, so treat the specific sanction taxonomy as `UNVERIFIED` at that level of precision even though the general power is confirmed).
- **Funding**: the ARS also allocates operating budgets to establishments, which is a lever CQC does not directly hold in England (funding sits with NHS England/commissioners there) - this is a real structural difference, not just a naming difference, and should not be treated as a like-for-like CQC equivalent without that caveat.

## Relationship to the other profiles in this directory

The ARS director general is one of the parties entitled to appeal a CNOM disciplinary decision (see `ordre-des-medecins.md`), which is a concrete point of contact between the regional facility-oversight layer and the professional-order disciplinary layer. Whether/how the ARS and HAS certification process (see `has.md`) interact procedurally (e.g. whether a failed HAS certification triggers an ARS authorisation review) was not independently verified this session and is flagged `UNVERIFIED`.

## Primary sources checked

- `ars.sante.fr/quest-ce-quune-agence-regionale-de-sante`
- `ars.sante.fr/la-mission-dinspection-controle-des-agences-regionales-de-sante` (referenced via search, general inspection-mission content corroborated but not independently WebFetched line-by-line this session)

## What is NOT in this profile

No verified statutory article citations for ARS sanction powers. No verified linkage between HAS certification outcomes and ARS authorisation decisions. This is explicitly a short note, not a full CQC-equivalent profile - a fuller ARS profile (with the same `cnil.md`-shaped Investigation stages / Sanction range / Appeal route sections) would need a dedicated pass with more primary-source depth than this task's scope covered.
