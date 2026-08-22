---
regulator: AEMPS (Agencia Española de Medicamentos y Productos Sanitarios)
jurisdiction: Spain — genuinely national and unified for medicines/device authorisation, unlike CGCOM/CGE's professional-discipline split (see `cgcom.md`, `consejo-general-enfermeria.md`); this profile also covers, at lower confidence, the separate Ministerio de Sanidad-vs-Autonomous-Community split for health-service delivery and quality oversight
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added for Virtual Hospital International's Spanish healthcare regulator coverage, alongside `cgcom.md` and `consejo-general-enfermeria.md`; sourced via live WebFetch/WebSearch against aemps.gob.es and official Autonomous Community sites this session, not recalled from training data
---

# AEMPS

A regulator profile in this repository, following `ico.md`'s format (see `README.md`). Unlike CGCOM and CGE, AEMPS is **not** split between a national coordinating body and regional licensing bodies — it is a single national agency with unified authorisation power over medicines and medical devices across all of Spain. That structural contrast with the two professional-discipline profiles is deliberate and is the reason this file exists alongside them.

## Statutory basis

Confirmed via a direct fetch of `aemps.gob.es/la-aemps/constitucion-y-desarrollo-de-la-aemps/` (checked 2026-08-22):

- **Ley 29/2006**, de 26 de julio, de garantías y uso racional de los medicamentos y productos sanitarios, was the foundational law establishing the guarantees-and-rational-use framework the Agency operates within.
- **Real Decreto 1275/2011**, de 16 de septiembre, created AEMPS as a state agency ("Agencia estatal") and approved its Statute — elevating it from a simple autonomous body ("organismo autónomo") to a state-agency structure with more flexible management. This decree's existence and date were independently corroborated by a separate BOE search-result listing this session.
- **Real Decreto Legislativo 1/2015**, de 25 de julio, later consolidated the legal framework and is described by AEMPS's own page as "the current basic norm for the Agency's activities" — i.e. this consolidated text, not the original 2006 law standing alone, is what should be treated as the operative statutory basis today.
- A later amending law, **Ley 10/2013**, de 24 de julio, modified the 2006 law to incorporate EU pharmacovigilance and falsified-medicines directives (found via BOE/secondary search listings, not independently opened as a full text this session).

AEMPS is attached to the Ministerio de Sanidad (currently via its General Secretariat, per the constitución-y-desarrollo page).

## Scope and unified national character

Per the same `aemps.gob.es` fetch and the agency's home page (both checked 2026-08-22), AEMPS's scope covers:

- **Human medicines** — authorisation, registration, pharmacovigilance
- **Veterinary medicines** — clinical research, prescribing oversight
- **Medical devices** — commercialisation, clinical investigations, incident surveillance, operating under the **EU Medical Device Regulation (MDR)**
- **Cosmetics, biocides, and personal-care products** — safety and market surveillance

AEMPS maintains **CIMA** (Centro de Información online de Medicamentos), the official product-information database, and **REec**, its clinical-trials registry, and coordinates with the European Medicines Agency (EMA) on EU pharmaceutical standards. The constitución-y-desarrollo page's own account of AEMPS's history shows progressive *centralisation* of these competencies into one agency, with no mention anywhere in that page of regional or Autonomous-Community variation in the authorisation function itself — supporting treating AEMPS, unlike CGCOM/CGE, as genuinely unified at national level for medicines/device authorisation specifically.

## Ministerio de Sanidad vs Autonomous Communities — the separate health-service delivery/quality split

This is a **different** devolution axis from AEMPS's own unified remit, and only partially analogous to a CQC-style facility regulator — flagged here at lower confidence than the AEMPS material above, per the task that produced this file.

Per a WebSearch pass on Spain's health-competency distribution (checked 2026-08-22, drawing on `sanidad.gob.es`'s own pages on the Consejo Interterritorial and on Autonomous Community competencies, among other results): the Spanish state retains a small set of **exclusive** national competencies in health — "Sanidad Exterior" (external/border health), "bases y coordinación general de la sanidad" (bases and general coordination of health), and pharmaceutical-products legislation (i.e. AEMPS's own remit, above) — plus a "alta inspección" (high inspection) power. Everything not expressly reserved to the state — by the general principle of subsidiarity in the Spanish constitutional health-competency scheme — falls to the 17 Autonomous Communities, including **organisation and management of health services**, planning and execution of public-health programmes, and health-personnel management. The **Consejo Interterritorial del Sistema Nacional de Salud** is the coordinating forum where minimum safety/quality guarantees for authorising the opening and operation of health centres, services, and establishments are discussed at national level — i.e. Ministerio de Sanidad's role here is setting minimum standards and coordinating, not itself inspecting or licensing individual facilities.

**Confirmed regional example**: Andalusia. Per a direct fetch-corroborated finding from `juntadeandalucia.es` (an official Junta de Andalucía government domain, checked 2026-08-22), Andalusia runs its own **Inspección de Servicios Sanitarios**, which participates in authorising health centres/services/establishments by checking regulatory requirements, under Decreto 69/2008 (which also created the Registro Andaluz de Centros, Servicios y Establecimientos Sanitarios). The Junta de Andalucía's own page states the Autonomous Community holds "competencia exclusiva sobre organización, funcionamiento interno, evaluación, inspección y control de centros, servicios y establecimientos sanitarios" (exclusive competence over the organisation, internal functioning, evaluation, inspection, and control of health centres, services, and establishments).

A second data point — Catalonia running an analogous inspection function under its own Decret 151/2017, per its Estatut d'Autonomia's exclusive competence over the same matters — surfaced in the same search pass, but was sourced only via a secondary legal-database summary (`noticias.juridicas.com`) rather than a directly fetched Generalitat de Catalunya primary page, so it is carried at lower confidence than the Andalusia finding and should be independently re-checked before relying on it.

**Known gap, stated honestly per this task's instruction**: this profile does **not** claim to have identified or verified a complete list of which of Spain's 17 Autonomous Communities run a named, CQC-analogous health-service inspection body, nor does it claim Andalusia's or Catalonia's model is representative of all 17. It confirms only that (a) the devolved competence is real and constitutionally/statutorily exclusive to each Autonomous Community, and (b) at least two Autonomous Communities (Andalusia directly, Catalonia at secondary-source confidence) do in fact operate their own inspection function under that competence. Treat any other specific Autonomous Community's arrangement as unverified until separately checked.

## Primary sources checked

- `aemps.gob.es/la-aemps/constitucion-y-desarrollo-de-la-aemps/` — fetched directly, checked 2026-08-22
- `aemps.gob.es` home page — fetched directly, checked 2026-08-22
- BOE search-result listing corroborating Real Decreto 1275/2011's title and date
- `sanidad.gob.es` pages on the Consejo Interterritorial and on Autonomous Community competencies — surfaced via WebSearch, checked 2026-08-22 (not independently opened as full-page fetches)
- `juntadeandalucia.es` — official Junta de Andalucía page on Inspección de Servicios Sanitarios and Decreto 69/2008 — surfaced via WebSearch summary of an official government domain, checked 2026-08-22
- `noticias.juridicas.com` summary referencing Catalonia's Decret 151/2017 and its Estatut d'Autonomia competence — secondary source, lower confidence, checked 2026-08-22

## What is NOT in this profile

- No independently fetched full text of Ley 29/2006, Real Decreto 1275/2011, Real Decreto Legislativo 1/2015, or Ley 10/2013 — all four are named and dated from AEMPS's own summary page and corroborating search listings, not read article-by-article this session.
- No verified sanction range or enforcement-procedure detail for AEMPS itself (e.g. penalties for non-compliant marketing of a medicine or device) — not researched this session.
- No verified appeal route/forum for an AEMPS decision (e.g. administrative appeal to the Ministerio de Sanidad, then contentious-administrative jurisdiction) — not researched this session, do not assume.
- No complete, region-by-region survey of Autonomous Community health-service inspection bodies — only Andalusia (directly confirmed) and Catalonia (secondary-source, lower confidence) were checked; the other 15 are an explicit, stated gap, not silently assumed to work the same way.
- No case-by-case AEMPS decision database — this is a procedural/structural profile only, consistent with `../GOVERNANCE.md`'s `COMMUNITY_REVIEWED` (not yet `MAINTAINER VERIFIED`) standard.
