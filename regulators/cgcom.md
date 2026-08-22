---
regulator: Consejo General de Colegios Oficiales de Médicos (CGCOM) and Spain's regional Colegios Oficiales de Médicos
jurisdiction: Spain (CGCOM is the national coordinating/deontological body; original licensing and disciplinary jurisdiction over an individual physician sits with the regional/provincial Colegio Oficial de Médicos where that physician is registered — see "Structure" below, this distinction is the reason this profile exists)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added for Virtual Hospital International's Spanish healthcare regulator coverage; sourced via live WebFetch/WebSearch against cgcom.es, icomem.es, and BOE listing pages this session, not recalled from training data — see "What is NOT in this profile" for where direct primary-legal-text access was blocked
---

# CGCOM and the regional Colegios Oficiales de Médicos

A regulator profile in this repository, following `ico.md`'s format (see `README.md`). This profile is deliberately about the *structure*, not just CGCOM alone — the single most important fact for anyone using this profile is that CGCOM is not where a Spanish doctor's licence to practise or discipline is decided.

## Statutory basis

CGCOM is the national umbrella body ("Consejo General") at the top of Spain's Organización Médica Colegial (OMC). Per `cgcom.es` (checked 2026-08-22), CGCOM "agrupa, coordina y representa a todos los Colegios de Médicos de España" (groups, coordinates, and represents all medical colleges in Spain) — a coordinating and representative role, not a first-instance licensing or disciplinary one. CGCOM's own materials describe it as the "vértice institucional de la colegiación médica" (the institutional apex of medical registration), language that itself signals CGCOM sits above, rather than performs, individual registration.

CGCOM's current governing statute is its Estatutos, approved by **Real Decreto 300/2016** (title and existence confirmed via BOE and `noticias.juridicas.com` search listings this session; the decree's full text could not be directly fetched — see "What is NOT in this profile"). An earlier statute, Real Decreto 1018/1980 (Estatutos generales de la Organización Médica Colegial y del CGCOM), and an intermediate Real Decreto 757/2006, also surfaced in BOE search results as part of this instrument's regulatory history; this profile does not verify which provisions of the earlier decrees, if any, remain in force alongside the 2016 statute.

## Structure: CGCOM vs the regional Colegios — the load-bearing distinction

Per `cgcom.es/funciones` and `cgcom.es/conocenos/cgcom` (checked 2026-08-22), CGCOM's actual functions are:

- Approving and maintaining the national **Código de Deontología Médica** (a 2022 edition, 26 chapters/93 articles, was located via search this session but not itself opened and read — see gap below) and overseeing its application.
- Maintaining a **Registro Central de la Profesión Médica**, described as interconnected with the registers kept by the provincial Colegios — i.e. the provincial Colegios hold the primary registration records, not CGCOM.
- Coordinating, at national scope, information requests about members and sanctions imposed by Colegios.
- Hearing and resolving **administrative appeals (recursos)** filed against decisions of individual Colegios, via a Comisión Central de Deontología, Derecho Médico y Visado — an appellate function, confirmed via `cgcom.es/conocenos/cgcom/comision-de-etica-y-deontologia-medica-de-la-omc` (checked 2026-08-22), which describes this commission as reporting on "recursos que se interpongan ante el Consejo contra los acuerdos de los Colegios" (appeals lodged with the Council against decisions of the Colegios).
- Representing Spanish medicine before EU institutions and international medical bodies.

**Colegiación (mandatory professional registration) — the actual licensing act — happens at, and is administered by, the regional or provincial Colegio Oficial de Médicos**, not CGCOM. A doctor must be registered with the Colegio of the territory where they practise to lawfully do so; that Colegio also runs its own Comisión de Ética y Deontología and handles disciplinary/ethics matters concerning its own members at first instance.

### Worked example: Colegio de Médicos de Madrid (ICOMEM)

Confirmed via `icomem.es` (checked 2026-08-22): ICOMEM is the official Colegio for the Madrid region. It is the body physicians in Madrid must register with ("colegiación") to practise, and its site prominently features "Acceso a la profesión médica (colegiación)" as a core function. ICOMEM's privacy policy states its legal basis includes "el cumplimiento de una misión realizada en interés público o en el ejercicio de poderes públicos conferidos", naming "ordenación profesional y control deontológico" (professional regulation and deontological oversight) specifically — i.e. ICOMEM itself asserts it exercises delegated public power over registration and conduct, not merely a private-association role. ICOMEM also runs its own Comisión de ética y deontología with a published Código de Deontología. This is the pattern that repeats, with local variation, across Spain's other regional Colegios — ICOMEM is cited here as one verified worked example, not as representative of every regional Colegio's exact procedure.

## Sanction range

**UNVERIFIED.** No specific, sourced scale of disciplinary sanctions available to a regional Colegio against an individual physician (equivalent to, e.g., the GMC's warning/conditions/suspension/erasure ladder in `gmc.md`) was found and confirmed this session. Do not assume Spanish Colegio sanctions map onto another jurisdiction's ladder — check the specific Colegio's own reglamento or the Código de Deontología Médica directly before relying on a sanction-range claim.

## Appeal route and forum

Confirmed this session: a physician can appeal a Colegio's decision to **CGCOM** (via its Comisión Central de Deontología, Derecho Médico y Visado), per `cgcom.es`. What is **not** verified this session is the further judicial route beyond CGCOM — Colegios and CGCOM are public-law corporations (corporaciones de derecho público) exercising delegated public functions, which in Spanish administrative law generally makes their acts reviewable before the contentious-administrative jurisdiction (jurisdicción contencioso-administrativa), but this profile does not confirm that specific court/tribunal chain live this session, so it is flagged `UNVERIFIED` rather than asserted.

## Primary sources checked

- `cgcom.es` (home page, `/funciones`, `/conocenos/cgcom`, `/conocenos/omc`, `/conocenos/cgcom/comision-de-etica-y-deontologia-medica-de-la-omc`) — fetched directly, checked 2026-08-22
- `icomem.es` (home page) — fetched directly, checked 2026-08-22
- BOE search-result listings confirming the existence and title of Real Decreto 300/2016 and Real Decreto 1018/1980 (direct full-text BOE fetch was attempted twice and failed with a connection error both times — see gap below)
- `iefs.es`'s CGCOM explainer page, used as a secondary source and cross-checked against `cgcom.es` for consistency, not relied on alone
- A PDF titled "ESTATUTOS-CGCOM" hosted by a provincial Colegio (`comciudadreal.es`) — confirmed as the CGCOM statutes document by filename/metadata, but its body text could not be parsed this session (returned as raw binary/PDF stream to the fetch tool), so no article-level claim in this profile rests on that PDF's content

## What is NOT in this profile

- The full text of Real Decreto 300/2016 was **not directly read** this session — `boe.es` direct fetch failed with a connection error on two separate attempts, and a `noticias.juridicas.com` mirror failed on a certificate error. Everything above about CGCOM's specific functions rests on CGCOM's own website content and one independent secondary explainer, not on the statute's own article text. A maintainer should re-attempt a direct BOE fetch (or manual browse) before upgrading this past `COMMUNITY_REVIEWED`.
- No verified sanction range or disciplinary procedure detail for a regional Colegio proceeding against an individual doctor.
- No verified judicial appeal forum beyond CGCOM's internal appeal route.
- No verified count of how many provincial/regional Colegios exist, and no claim that ICOMEM's procedure is identical to any other region's Colegio — it is offered only as one directly-checked worked example, per the task that produced this file.
- No case-by-case CGCOM or Colegio decision database — this is a procedural/structural profile only, consistent with `../GOVERNANCE.md`'s `COMMUNITY_REVIEWED` (not yet `MAINTAINER VERIFIED`) standard.
