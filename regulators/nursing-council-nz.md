---
regulator: Nursing Council of New Zealand (Te Kaunihera Tapuhi o Aotearoa)
jurisdiction: New Zealand (national - one regulator, no sub-national variation)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added alongside mcnz.md to cover nurses under the same HPCAA framework, sourced via live WebSearch against nursingcouncil.org.nz (direct WebFetch of nursingcouncil.org.nz pages returned HTTP 403 this session - see sourcing note below), not recalled from training data
---

# Nursing Council of New Zealand

The fifth regulator profile in this repository, following `ico.md`'s format - see `README.md`. This profile shares its statutory framework (HPCAA, the Health Practitioners Disciplinary Tribunal, and the appeal route) with `mcnz.md`; read that file for the parts of the structure that are common across HPCAA professions rather than repeated here in full.

## Statutory basis

The Nursing Council of New Zealand is the statutory regulator for nurses (and nurse practitioners), operating under the same **Health Practitioners Competence Assurance Act 2003 (HPCAA)** that establishes the Medical Council and the other profession-specific councils - see `mcnz.md`'s "Statutory basis" section for the shared HPCAA structure. Confirmed live via search-engine synthesis of `nursingcouncil.org.nz` content this session (direct WebFetch of the Council's own pages was blocked with HTTP 403 in this session - see sourcing note at the end of this file).

## Investigation stages

Per search-engine synthesis of `nursingcouncil.org.nz` content (checked live 2026-08-22):

- A concern or complaint about a nurse is made in writing to the **Registrar**.
- The **Registrar** makes the initial call on whether the matter is a health, conduct, or competence issue, and assesses risk - this can include interim orders such as suspension of a practising certificate or conditions on scope of practice pending resolution.
- The Registrar **considers HDC opinions** as part of that assessment - i.e. where the Health and Disability Commissioner has already formed a view on a related complaint, the Council's own process takes that into account rather than starting from nothing. This is the same front-door relationship with HDC described in `mcnz.md` and `hdc.md`: complaints about a nurse's care that implicate a consumer's rights route through HDC, and HDC can refer fitness-to-practise-flavoured aspects to the Council.
- Conduct matters of a serious professional nature go to a **Professional Conduct Committee (PCC)**, which investigates and decides whether to refer the matter to the **Health Practitioners Disciplinary Tribunal (HPDT)** or take no further disciplinary action.
- Unlike health and competence concerns, there is **no blanket mandatory obligation** to report a conduct concern about a nurse - except where the conduct involves public safety, which does carry a reporting obligation per the Council's own published guidance.
- Complainants and others who raise health or competence notifications, or who make submissions to a PCC, are protected from civil or disciplinary proceedings over those statements unless made in bad faith.

## Disciplinary body and sanction range

Nurses appear before the same cross-profession **Health Practitioners Disciplinary Tribunal** described in `mcnz.md` - confirmed live this session via the Tribunal's own decision file-number prefix `Nur` at `hpdt.org.nz`, and via a specific 2023 HPDT nurse-misconduct decision (censure and suspension for spreading COVID-19 misinformation) found in this session's search results. The Tribunal's sanction powers (cancellation, suspension up to three years, conditions up to three years, censure, fines up to NZ$30,000, costs orders) are the same HPCAA s101 powers described in `mcnz.md` - not nurse-specific.

## Appeal route and forum

Same route as `mcnz.md`: appeal to the **High Court** under HPCAA Part 5, generally within 20 working days, with further appeal to the **Court of Appeal** limited to points of law. Confirmed live this session by an HPDT decision PDF for a nursing case citing HPCAA s101(1) penalty provisions, consistent with the shared cross-profession statutory basis.

## Primary sources checked

- Search-engine synthesis of `nursingcouncil.org.nz/Public/NCNZ/Concerns.aspx`, `nursingcouncil.org.nz/Public/NCNZ/concerns-section/Fitness_to_practice.aspx`, and the Council's Professional Conduct Committee process pages (all returned HTTP 403 to direct WebFetch this session - see sourcing note below)
- `hpdt.org.nz` (cross-profession Tribunal scope, confirmed via `Nur`-prefixed decision file numbers)
- A specific 2023 HPDT nurse-discipline decision (censure/suspension, COVID-19 misinformation) surfaced in live search results, corroborating that nurses are in fact disciplined through this Tribunal in practice, not just in theory
- `mcnz.org.nz` and HPCAA-citing sources listed in `mcnz.md`, for the shared statutory scaffolding

## Sourcing note - direct fetch blocked

`nursingcouncil.org.nz` returned HTTP 403 Forbidden to direct WebFetch on every page attempted this session (`/Public/NCNZ/Concerns.aspx`, `/Public/NCNZ/concerns-section/Fitness_to_practice.aspx`). Everything above sourced from that domain is therefore via **search-engine synthesis of that domain's content**, not a direct page read - a weaker form of live verification than `WebFetch` alone would give, though still checked this session (per this repository's rule) rather than recalled from training data. Before relying on this profile for anything requiring exact procedural wording, re-attempt a direct fetch of `nursingcouncil.org.nz` (a different network path or a cached/mirrored copy may succeed where this session's fetch did not) or ask the Council directly.

## What is NOT in this profile

No independently page-read text from `nursingcouncil.org.nz` - see the sourcing note above. No case-by-case Nursing Council or HPDT decision database - this is a procedural/structural profile only, consistent with `COMMUNITY_REVIEWED` (not `MAINTAINER VERIFIED`).
