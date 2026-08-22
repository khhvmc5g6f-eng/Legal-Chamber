---
regulator: Conseil National de l'Ordre des Médecins (CNOM / Ordre des médecins)
jurisdiction: France
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added for Virtual Hospital International's French healthcare regulator coverage; sourced via live WebFetch/WebSearch against conseil-national.medecin.fr and legifrance.gouv.fr, not recalled from training data
---

# Ordre des médecins (CNOM)

Second regulator profile in this repository, following the format set by `cnil.md` (see `README.md`). Filled in per `../GOVERNANCE.md`'s sourcing requirement: primary source and check date per claim below.

## Statutory basis

The Ordre des médecins is France's statutory professional order for physicians, established under the Code de la santé publique (Book I, Title II). Registration on an *ordre* roster (*tableau de l'ordre*) is a legal precondition to practising medicine in France. The Conseil National de l'Ordre des Médecins (CNOM) sits at the top of a three-tier structure of departmental, regional, and national councils, and separately operates the disciplinary jurisdiction described below. This is a professional-order disciplinary regulator, structurally the French counterpart to the UK's GMC, not a data-protection or market regulator like CNIL.

## Investigation / disciplinary stages

Per `conseil-national.medecin.fr/lordre-medecins/linstitution-ordinale/juridiction-ordinale` (checked 2026-08-22), the disciplinary jurisdiction has three tiers, and it is a genuinely separate jurisdictional structure from the ordre's administrative councils, not merely an internal committee:

- **First instance**: one *chambre disciplinaire de première instance* (CDPI) per region, attached to the regional council of the Order. Each is presided over by an administrative magistrate, assisted by physician assessors elected at ordinal level.
- **Anyone can lodge a complaint** against a physician - patients, other doctors, public administrations, associations - and there is **no statutory time limit** (no *prescription*) to seize the Order.
- Complaints are first examined by the departmental council in plenary session; if not resolved by conciliation, the departmental council is obliged to transmit the complaint to the CDPI with its own reasoned opinion.
- **Appeal**: the *chambre disciplinaire nationale* (national disciplinary chamber), presided over by a *Conseil d'État* member (a professional magistrate, not a physician), with physician assessors elected at ordinal level. Appeals can seek aggravation, mitigation, or cancellation of the sanction. Parties entitled to appeal include the complainant, the physician concerned, the Minister of Health, the *Procureur de la République*, the ARS director general, the departmental council, and the national council of the Order itself.
- **Cassation**: beyond the appeal level, the *Conseil d'État* itself reviews the national chamber's decisions, but only on points of law (*le respect des règles de droit*), not on the merits.

## Sanction range

Per Article L.4124-6 of the Code de la santé publique (checked live via `legifrance.gouv.fr`, 2026-08-22), the disciplinary chamber may impose:

- *Avertissement* (warning)
- *Blâme* (reprimand)
- Temporary prohibition from practising medicine, with or without suspension, for a maximum of **three years**
- Permanent prohibition from practising, i.e. *radiation du tableau de l'ordre* (removal from the register)

The first two sanctions carry an additional three-year loss of eligibility to sit on departmental, regional, or national ordinal councils; the remaining sanctions carry permanent loss of that eligibility. A struck-off physician cannot re-register with another council.

## Appeal route and forum

Confirmed via `conseil-national.medecin.fr` (checked 2026-08-22): the internal appeal from a CDPI decision goes to the *chambre disciplinaire nationale*, not directly to the Conseil d'État. Only beyond that - as a *cassation* appeal against the national chamber's own decision - does the matter go to the **Conseil d'État**, and only on legal-rule compliance, not on the facts. This is structurally similar to CNIL's pattern of the Conseil d'État being the final forum (see `cnil.md`), but the internal route is materially different: CNIL sanctions go straight from the *formation restreinte* to the Conseil d'État on appeal, with no intermediate ordinal appeal chamber, whereas a physician's case passes through two full merits-hearing tiers (CDPI, then chambre disciplinaire nationale) before any Conseil d'État involvement, and that involvement is limited to cassation rather than a full merits appeal. Do not assume the CNIL appeal pattern transfers unchanged to CNOM - it does not.

## Primary sources checked

- `conseil-national.medecin.fr/lordre-medecins/linstitution-ordinale/juridiction-ordinale`
- `legifrance.gouv.fr` - Article L.4124-6, Code de la santé publique

## What is NOT in this profile

No populated case-decision database for CNOM (this is a procedural/structural profile, not a precedent library, consistent with `../docs/HONEST_STATUS.md`'s standard for a `COMMUNITY_REVIEWED` pack). No verified figure for average case duration or current caseload statistics - a CNOM "rapport d'activité de la juridiction ordinale" PDF was found in search results but not opened and read in this session, so any duration/caseload claim from it would be unverified and is deliberately omitted. No cross-check of Article L.4124-6 against the *chambre disciplinaire nationale*'s own procedural rules beyond what conseil-national.medecin.fr's overview page states.
