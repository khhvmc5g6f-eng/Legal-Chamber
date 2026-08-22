---
regulator: Ordre National des Infirmiers (ONI / Ordre des infirmiers)
jurisdiction: France
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added for Virtual Hospital International's French healthcare regulator coverage; sourced via live WebSearch/WebFetch against ordre-infirmiers.fr and legifrance.gouv.fr, not recalled from training data
---

# Ordre des infirmiers (ONI)

Third regulator profile in this repository, following the format set by `cnil.md` (see `README.md`). Filled in per `../GOVERNANCE.md`'s sourcing requirement: primary source and check date per claim below.

## Statutory basis

The Ordre National des Infirmiers is France's statutory professional order for nurses, created by law in 2006 and governed by the Code de la santé publique (Book III, nursing profession). Its disciplinary jurisdiction, code of ethics (*code de déontologie*, Decree n°2016-1605), and roster-registration function are the nursing-profession structural analogue of the Ordre des médecins covered in `ordre-des-medecins.md`, but built on distinct articles of the Code (principally the L.4312 series for nurses, not the L.4124 series used for doctors) - the two orders are not simply interchangeable copies of the same legal text.

## Investigation / disciplinary stages

Per live search of `ordre-infirmiers.fr` and Légifrance (checked 2026-08-22), the structure mirrors CNOM's three tiers but is not identical in numbering or article basis:

- **First instance**: **14** *chambres disciplinaires de première instance* (CDPI), each attached to a regional or inter-regional council of the Order, each presided over by a magistrate from an administrative court or court of appeal, sitting with elected nurse assessors representing three modes of practice (private practice, private-sector employees, public-sector employees). A complaint against a nurse is filed with the president of the departmental or inter-departmental council where the nurse is registered.
- Per Article L.4312-5-IV of the Code de la santé publique (found via Légifrance-indexed search, not independently opened and read verbatim in this session - flagged `UNVERIFIED` at the sub-clause level), a nurse in public service employment is subject to a different disciplinary route and cannot be brought before the ordinal first-instance chamber in the same way as a nurse in private practice; this distinction was not independently re-verified against the article's full text this session.
- **Appeal**: the *chambre disciplinaire nationale*, attached to the Conseil National de l'Ordre des Infirmiers, presided over by a Conseil d'État member, with elected nurse assessors.
- **Cassation**: the **Conseil d'État**. This was independently confirmed live against a real decision - Conseil d'État, 5ème et 6ème chambres réunies, 11 October 2024, n° 475857, *Mme A... et autres c. Conseil national de l'ordre des infirmiers* - a cassation appeal by eight nurses against a chambre disciplinaire nationale decision of 11 May 2023 concerning the practice of "hydrotomie percutanée." The Conseil d'État partially annulled the disciplinary chamber's decision, finding it had exceeded its jurisdiction by issuing directives beyond the individual sanctions before it. This confirms the same cassation forum as CNOM (Conseil d'État) for the nursing order, checked directly against the case rather than assumed from the medical-order pattern.

## Sanction range

Per Article L.4124-6 of the Code de la santé publique, which search results indicate is applied to nurses' first-instance disciplinary chambers alongside the profession-specific L.4312 provisions (checked via Légifrance article text and cross-referencing search results, 2026-08-22):

- *Avertissement* (warning)
- *Blâme* (censure)
- Temporary or permanent prohibition from exercising certain or all nursing functions conferred or remunerated by the State, départements, communes, or public/publicly-recognised establishments
- Temporary prohibition from practising generally, with or without suspension, for a maximum of **three years**
- *Radiation* (removal from the register) - a definitive prohibition from practising as a nurse

## Appeal route and forum

CDPI to chambre disciplinaire nationale (merits appeal), then Conseil d'État on cassation only - confirmed live against the real 2024 decision cited above, not assumed from CNOM's structure. As with CNOM, do not treat this as identical to CNIL's appeal pattern (see `cnil.md`): there are two full ordinal tiers before any Conseil d'État involvement, and that involvement is cassation, not a fresh merits hearing.

## Primary sources checked

- `ordre-infirmiers.fr` (search-indexed pages on chambre disciplinaire structure, election notices, and a disciplinary-complaint guide PDF - the PDF's binary content could not be text-extracted in this session and its detail is not relied upon beyond what corroborating search snippets and Légifrance confirmed)
- `legifrance.gouv.fr` - Article L.4124-6, Code de la santé publique; Conseil d'État decision n° 475857 (11/10/2024), read via `legifrance.gouv.fr/ceta/id/CETATEXT000050336427`

## What is NOT in this profile

The exact text of Article L.4312-5 was not independently opened and read verbatim this session - its content here is drawn from search-result summaries of Légifrance-indexed text, not a direct primary-source read, and is flagged accordingly. No populated case-decision database beyond the single 2024 cassation decision checked live. No verification of whether the "hydrotomie percutanée" case's jurisdictional finding (chamber exceeding its authority by issuing directives) is representative of typical ONI disciplinary outcomes - it is cited here only to verify the cassation forum, not as a description of typical case content.
