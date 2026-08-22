---
regulator: Medsafe (New Zealand Medicines and Medical Devices Safety Authority)
jurisdiction: New Zealand (national - one regulator, no sub-national variation)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added to complete the New Zealand set alongside mcnz.md, nursing-council-nz.md, and hdc.md, sourced via live WebFetch/WebSearch against medsafe.govt.nz and legislation-tracking sources, not recalled from training data
---

# Medsafe

The seventh regulator profile in this repository, following `ico.md`'s format - see `README.md`. Medsafe is not a standalone statutory body in the way the other profiles in this set are - it is a business unit inside a government ministry - which materially changes its "statutory basis" and accountability structure below.

## Statutory basis

Medsafe is the **New Zealand Medicines and Medical Devices Safety Authority**, operating as a **business unit of the Ministry of Health**, accountable through the Ministry to the Minister of Health - confirmed live via `medsafe.govt.nz/other/about.asp` (fetched 2026-08-22). It is not a Crown entity or independent regulator in the way the ICO or CNIL are; it sits inside the Ministry's own organisational structure.

It administers the **Medicines Act 1981** and the **Medicines Regulations 1984** for medicines, related products (food/dentifrice/cosmetic items with a secondary therapeutic use), controlled drugs used as medicines, and (via a distinct, lighter-touch regime - see below) medical devices.

### The Therapeutic Products Act 2023 was passed, then repealed - do not assume it is in force

This is worth flagging explicitly because it is exactly the kind of recent legislative churn that is easy to get wrong from training data. Per live search results this session (checked against `legislation.govt.nz`'s own tracked Act status and law-firm legal-update summaries, since direct WebFetch of `legislation.govt.nz` itself returned HTTP 403 in this session - see sourcing note):

- The **Therapeutic Products Act 2023** was enacted to eventually replace the Medicines Act 1981, but was **repealed on 18 December 2024** by section 3 of the **Therapeutic Products Act Repeal Act 2024 (2024 No 55)**, following a change of government.
- As a result, the **Medicines Act 1981 and its regulations continue to apply** to medicines and medical devices, and the Dietary Supplements Regulations 1985 continue to govern some natural health products.
- The Ministry of Health is developing a **new Medical Products Bill** intended to eventually replace the Medicines Act 1981, and a separate standalone bill was agreed in September 2024 for natural health products - both `UNVERIFIED` as to current drafting/enactment status; check `legislation.govt.nz` and `health.govt.nz` directly before relying on this for any live matter, since bill status changes fast and this session could not directly fetch either site.

## Regulatory scope and mechanism - medicines vs. devices are NOT the same regime

- **Medicines**: pharmacological-effect products for therapeutic use, regulated for market entry, safety, and quality under the Medicines Act 1981 framework.
- **Medical devices**: regulated through a **notification-based** scheme, not a premarket-approval scheme - confirmed live this session via search results on Medsafe's **WAND** (Web Assisted Notification of Devices) database, established under the Medicines (Database of Medical Devices) Regulations 2003. Per those results: "there is no approval system for medical devices under the Medicines Act 1981" - importers, exporters, and local manufacturers must notify their device to WAND, generally within 30 days of the device being supplied in New Zealand, and must hold documentation supporting the device's safety and effectiveness (which can include recognition of an existing approval from a body such as the EU, Health Canada, or the US FDA) that Medsafe can request. A New Zealand-based Sponsor is required for overseas companies without a local presence, and is the sole liaison to Medsafe. This is a materially lighter-touch, post-market-oriented mechanism compared with a premarket-approval regulator like the US FDA or the EU's MDR regime - do not describe Medsafe's device oversight as an "approval" process.

## Distinct from Pharmac funding

Medsafe's authorisation of a medicine (that it may lawfully be supplied/marketed in New Zealand) is a **separate question** from whether Pharmac (the government's separate pharmaceutical-funding agency) chooses to fund it on the Pharmaceutical Schedule. A medicine can be Medsafe-authorised without being Pharmac-funded, and this distinction is already correctly flagged in `virtual-hospital/jurisdictions/src/registry.ts`'s `new-zealand` entry - this profile confirms rather than contradicts that.

## Sanction range / enforcement powers

`UNVERIFIED` in this session - this session's sources described Medsafe's regulatory mechanism (notification for devices, Act/Regulations-based control for medicines) but did not surface a clear, citable description of Medsafe's own direct enforcement/penalty powers (e.g. product recalls, prosecutions under the Medicines Act, infringement notices). Do not assume a sanction range without checking the Medicines Act 1981 directly.

## Appeal route and forum

`UNVERIFIED` in this session - not established. Given Medsafe's status as a Ministry business unit rather than an independent statutory tribunal-adjacent body, any appeal route is likely to run through general administrative/judicial review of a Ministry decision rather than a dedicated tribunal, but this was not confirmed against a primary source this session and should not be relied on.

## Primary sources checked

- `medsafe.govt.nz/other/about.asp` (fetched live - organisational status, governing legislation as understood by Medsafe's own "about" page, which does not itself mention the Therapeutic Products Act at all)
- Live search results on the Therapeutic Products Act 2023's repeal (`legislation.govt.nz`'s own tracked status, `simpsongrierson.com` and `beehive.govt.nz` legal/government updates on the Therapeutic Products Act Repeal Act 2024)
- Live search results on the WAND medical-device notification database and its regulatory basis (Medicines (Database of Medical Devices) Regulations 2003)

## Sourcing note - direct fetch blocked for legislation and Ministry pages

`legislation.govt.nz` and `health.govt.nz/regulation-legislation/medicines-control` both returned HTTP 403 Forbidden to direct WebFetch this session. The legislative-status claims above (Therapeutic Products Act repeal, Medicines Act 1981 continuing in force, Medical Products Bill in development) are therefore sourced via search-engine synthesis of those domains' content and of law-firm/government commentary, not a direct primary-text read. This is still a same-session live check per this repository's rule, but is weaker than a direct fetch - re-verify against `legislation.govt.nz` directly before relying on this for a live matter with a hard deadline tied to the legislative status.

## What is NOT in this profile

No confirmed enforcement/penalty powers. No confirmed appeal route. No independently-read primary legislative text (Medicines Act 1981, Therapeutic Products Act Repeal Act 2024) - see sourcing note above. No case-by-case Medsafe decision or product-recall database - this is a procedural/structural profile only, consistent with `COMMUNITY_REVIEWED` (not `MAINTAINER VERIFIED`).
