---
regulator: Collège des médecins du Québec (CMQ)
jurisdiction: Canada - Quebec (provincial; physicians only)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added as a second, structurally different Canadian provincial physician-regulator model alongside cpso.md - Quebec's professional order system under the Code des professions, overseen by the Office des professions du Québec, runs meaningfully differently from Ontario's RHPA/HPARB model; sourced via live WebSearch and direct `rtk curl` fetch against cmq.org, not recalled from training data
---

# CMQ

The seventh regulator profile in this repository, following `ico.md`'s format - see `README.md`. This profile exists specifically to show that "Canadian provincial physician regulation" is not one model repeated thirteen times: Quebec's system is built on a general **Code des professions** covering 46 professional orders (not just health professions), with a distinct **syndic** (investigating officer) role, a **conseil de discipline** structured as an independent tribunal with a government-appointed lawyer as chair, and an appeal route through Quebec's ordinary court system rather than a specialist health-professions appeal board. Compare `cpso.md` and `cno.md` for Ontario's RHPA/Health Professions Procedural Code/HPARB model.

## Statutory basis

Per `cmq.org` and `quebec.ca` (checked 2026-08-22): CMQ derives its authority from the **Medical Act** (Quebec's profession-specific statute for physicians) together with the **Code des professions**, the framework law common to all 46 of Quebec's professional orders. The **Office des professions du Québec (OPQ)** is the government surveillance/oversight body created under the Code des professions to ensure each professional order actually fulfils its public-protection mandate - verifying the order has adequate resources, monitoring the internal functioning of its board of directors, ensuring public-interest representation within the order, and advising government on the professional system generally. The OPQ oversees CMQ as one of the 46 orders; it is not itself the physician regulator.

## Investigation stages

Per `cmq.org/fr/proteger-le-public/faire-signalement/processus-de-plainte` (fetched directly, checked 2026-08-22):

- **Receipt and screening** - the CMQ's **Bureau du syndic** (syndic's office) receives over 2,000 requests per year from the public, health professionals, hospitals, and other organisations. Each request is analysed; where the request is not admissible, the file is closed and the requester informed.
- **Brief intervention (optional alternative to a full investigation)** - where appropriate and with the requester's agreement, a brief intervention with the physician can substitute for opening a full investigation.
- **Investigation** - the syndic opens roughly 1,000 investigations per year. A physician contacted by the Bureau du syndic - whether under investigation, a witness, or a holder of relevant information - cannot invoke professional secrecy and has a duty to answer the syndic's questions or provide relevant documents.
- **Investigation outcomes** - per CMQ's own three-outcome structure: (1) **case closure without further measures**, where no breach is found; (2) a **preventive or educational intervention** - remarks/suggestions, participation in a training activity, a practice limitation on certain acts or on prescribing certain medications, a professional inspection visit, or (in particular cases, under article 48 of the Code des professions) an ordered medical examination of the member, or cessation of practice; or (3) **filing a complaint before the conseil de discipline (disciplinary council)**.
- **Review of a syndic's decision not to prosecute** - per `cmq.org`, a requester dissatisfied that the syndic did not file a complaint can, within 30 days, ask the **comité de révision** (review committee) for its opinion; the review committee has 90 days to respond and can conclude no complaint is warranted, suggest the syndic continue investigating, or conclude a complaint should be filed (potentially via a suggested syndic ad hoc).

## Sanction range

Per `cmq.org/fr/proteger-le-public/suivre-dossier-disciplinaire/conseil-discipline` (fetched directly, checked 2026-08-22): the **conseil de discipline** is an independent tribunal - independent of CMQ in exercising its functions - composed of a government-appointed lawyer as chair plus two physicians drawn from a list nominated by CMQ's board. It holds public hearings (subject to in-camera exceptions), hears the syndic's evidence and the physician's defence, and rules on guilt. Where guilt is found, it may impose one or more of the following sanctions:

- **Reprimand**
- **Temporary or permanent radiation** (striking-off) from the professional roll - available even against a physician no longer on the roll at the time of the finding, provided the offence occurred while they were registered
- **Fine of between $2,500 and $62,500 per infraction** (this minimum and maximum can be doubled for a repeat offence)
- An order to **return money** owed to a person
- An order to **provide, complete, correct, or delete** a document or information it contains
- **Revocation of the licence to practise**
- **Revocation of a specialist certificate**
- **Limitation or suspension** of the right to practise professional activities

Disciplinary council decisions are public; radiations, suspensions, practice limitations, and licence revocations are communicated to members via CMQ's website/newsletter and are also published in a local newspaper where the physician practises, subject to certain exceptions.

## Appeal route and forum

Per `quebec.ca` and `tribunaldesprofessions.ca` (checked 2026-08-22): a conseil de discipline decision is appealed to the **Tribunal des professions**, formed of judges of the **Court of Québec** (typically drawn from its criminal/penal, civil, and youth chambers) sitting in this specialised appellate capacity - a materially different forum from Ontario's HPARB/Divisional Court split. The appeal is filed at the registry of the Court of Québec within **30 days** of service of the conseil de discipline's decision (article 164, Code des professions). The Tribunal des professions can confirm, vary, or overturn the conseil de discipline's decision, and may itself render the decision it considers should have been rendered (article 175). Per sources checked, a Tribunal des professions decision is final - **not further appealable**.

## Primary sources checked

- `cmq.org/fr/proteger-le-public/faire-signalement/processus-de-plainte` (fetched directly via `rtk curl`, checked 2026-08-22 - full investigation-stage description, syndic role, review committee)
- `cmq.org/fr/proteger-le-public/suivre-dossier-disciplinaire/conseil-discipline` (fetched directly via `rtk curl`, checked 2026-08-22 - conseil de discipline composition, process, and full sanction list including the $2,500-$62,500 fine range)
- `quebec.ca/gouvernement/ministeres-organismes/office-professions/mission-services/mission-mandats/role` and `.../mandat-surveillance` (OPQ's role and mandate, referenced via WebSearch)
- `tribunaldesprofessions.ca` and its published FAQ on disciplinary appeals, plus `quebec.ca`'s "Professions Tribunal" and "Recours disciplinaires" pages (Tribunal des professions structure, appeal procedure, and finality, referenced via WebSearch)

## What is NOT in this profile

No verified current full statutory text of the Medical Act or the Code des professions' specific articles beyond the article numbers cited by CMQ's and the OPQ's own published guidance (article 48, article 164, article 175) - not independently re-read against the primary legislative text this session. No case-by-case conseil de discipline decision database - this is a procedural/structural profile, consistent with `../GOVERNANCE.md`'s `COMMUNITY_REVIEWED` (not yet `MAINTAINER VERIFIED`) standard. English-language CMQ pages exist (`cmq.org/en/...`) but this profile was sourced from the French-language pages; terminology given in French with an English gloss rather than re-verified against the English mirror pages.
