---
regulator: Health Canada
jurisdiction: Canada (federal)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added as the genuinely-national piece of Canada's healthcare regulatory picture - professional licensure and discipline in Canada is provincial (see cpso.md, cno.md, college-des-medecins-quebec.md), but medicines and medical device regulation is federal and single-national; sourced via live WebSearch against canada.ca and laws-lois.justice.gc.ca, not recalled from training data
---

# Health Canada

The fourth regulator profile in this repository, following `ico.md`'s format - see `README.md`. Unlike `cnil.md`, `ico.md`, and `ftc.md` (all data-protection/privacy regulators), this profile covers a products regulator - Health Canada's role in approving and policing pharmaceutical drugs and medical devices. It is deliberately narrow: Health Canada also regulates cannabis, tobacco and vaping products, pest control products, controlled substances, and much more, none of which is covered here.

**Why this profile exists in a Canadian healthcare context**: Canada has no single national physician or nurse regulator - see `cpso.md`, `cno.md`, and `college-des-medecins-quebec.md` for the provincial professional colleges that actually license and discipline clinicians. Health Canada is the one piece of Canadian healthcare regulation that genuinely is national and single, which is why it gets its own profile rather than being folded into a provincial one.

## Statutory basis

Per `canada.ca` (checked 2026-08-22, via live WebSearch quoting Health Canada's own "Regulating health products" page - direct WebFetch to canada.ca returned HTTP 403 this session, see note under Primary sources checked): Health Canada is the federal regulatory authority for the sale of pharmaceutical drugs and medical devices in Canada, acting under the **Food and Drugs Act** and its subordinate **Food and Drug Regulations** and **Medical Devices Regulations**. Within Health Canada, the Health Products and Food Branch (HPFB) is the operating unit that reviews, approves, and monitors these products.

Health Canada is the **sole federal drug- and device-approval authority** - there is no provincial equivalent that separately approves a drug or device for sale. Provinces and territories instead decide, after Health Canada approval, which approved products to fund through their own public drug formularies (see the `canada`, `canada-ontario`, `canada-quebec`, and `canada-british-columbia` entries in `virtual-hospital`'s jurisdiction registry) - do not conflate Health Canada market authorisation with a province's funding/formulary decision, the same distinction already drawn for Australia's TGA/PBS and New Zealand's Medsafe/Pharmac in that registry.

## Regulatory stages (not "investigation stages" in the professional-discipline sense)

Health Canada is a products regulator, not a complaint-driven professional-discipline body, so its process doesn't map onto the informal-inquiry → formal-investigation → allegation → decision → appeal shape used elsewhere in this directory. Per sources checked, its lifecycle approach runs:

- **Pre-market review** - a drug requires a Notice of Compliance (and, for most products, a Drug Identification Number) before sale; a medical device requires a device licence (for higher-risk Class II-IV devices) or establishment licensing (lower-risk Class I), under a risk-based classification system.
- **Post-market surveillance** - adverse event and incident reporting through MedEffect Canada / Canada Vigilance, safety signal review, and mandatory reporting obligations on manufacturers.
- **Compliance and enforcement action** - inspections (including good manufacturing practice inspections), recall orders, mandatory label or packaging changes, licence suspension or cancellation, and administrative monetary penalties or prosecution for non-compliance.

## Sanction range

Per `laws-lois.justice.gc.ca` and `canada.ca` guidance on the **Protecting Canadians from Unsafe Drugs Act ("Vanessa's Law")**, which amended the Food and Drugs Act (checked 2026-08-22): Health Canada/the Minister of Health can order a mandatory recall of a therapeutic product believed to present a serious or imminent risk of injury, order label or packaging changes, and compel information or further testing. Penalties for non-compliance with these orders include fines of **up to $5,000,000 per day** (replacing a prior $5,000 maximum), with courts retaining discretion to impose even higher fines where a violation was intentional or reckless, alongside potential imprisonment for offences under the Act. As of 22 June 2023, Vanessa's Law's powers extend to natural health products as well as conventional drugs and devices (their "therapeutic product" definition was broadened). `UNVERIFIED`: the exact administrative-monetary-penalty (AMP) tariff amounts under the specific AMP regulations (as opposed to the statutory maximum court-imposed fine) were not independently confirmed this session - check `canada.ca`'s AMP regulations directly before relying on a specific per-violation AMP figure.

## Appeal route and forum

This is structurally different from the tribunal-based appeal routes in `cpso.md`, `cno.md`, and `college-des-medecins-quebec.md`. Health Canada is a federal government department exercising statutory/ministerial authority, not an independent adjudicative tribunal - so there is no dedicated appeal board equivalent to HPARB or Quebec's Tribunal des professions. A refusal, suspension, or other adverse regulatory decision (e.g. a Notice of Compliance refusal, a device licence refusal, a recall order) is challenged by way of **judicial review at the Federal Court**, with further appeal to the **Federal Court of Appeal**. Per multiple reported Federal Court decisions checked this session (e.g. proceedings concerning Notice of Compliance refusals and biosimilar "second person" determinations), this is the live, actually-used route, not just a theoretical one.

## Primary sources checked

- `canada.ca/en/health-canada/corporate/mandate/regulatory-role/what-health-canada-regulates-1/health-products.html` (Health Canada's own description of its regulatory role) - content surfaced and directly quoted via live WebSearch this session; direct WebFetch and `rtk curl` to this and related `canada.ca` pages returned HTTP 403 / connection failures this session (canada.ca appears to be blocking this session's fetch tooling), so this profile relies on WebSearch's own live retrieval and quotation of the canada.ca text rather than a direct page fetch - flagged here for transparency rather than silently treated as equivalent to a direct fetch.
- `canada.ca/en/health-canada/services/drugs-health-products/legislation-guidelines/protecting-canadians-unsafe-drugs-act-vanessa-law-amendments-food-drugs-act.html` and `laws-lois.justice.gc.ca/eng/annualstatutes/2014_24/page-1.html` (Vanessa's Law penalty provisions)
- `canada.ca` guidance on the power to recall or require assessments/tests/studies under Vanessa's Law
- Reported Federal Court and Federal Court of Appeal decisions on Notice of Compliance and natural-health-product licensing judicial review (confirms the judicial-review appeal route in practice)
- `canada.ca/en/health-canada/services/drug-health-product-review-approval.html` (drug/device review and approval overview)

## What is NOT in this profile

No verified current text of the Food and Drugs Act's or Medical Devices Regulations' specific provisions (named by title only). No confirmed AMP tariff schedule figures (only the statutory court-fine maximum under Vanessa's Law was verified). No coverage of Health Canada's non-medicines/devices remits (cannabis, tobacco/vaping, pest control products, consumer product safety, radiation-emitting devices, First Nations and Inuit health) - out of scope for this profile. No case-by-case Health Canada enforcement-action database - this is a procedural/structural profile, consistent with `../GOVERNANCE.md`'s `COMMUNITY_REVIEWED` (not yet `MAINTAINER VERIFIED`) standard.
