---
regulator: TGA (Therapeutic Goods Administration)
jurisdiction: Australia (federal — one regulator for the whole country, no state-level equivalent)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added alongside ahpra.md and medical-board-australia.md, sourced via live WebSearch against tga.gov.au and corroborating secondary/legal sources — tga.gov.au's own pages timed out or were not directly fetchable this session, so this profile is search-corroborated rather than page-fetched
---

# TGA

The sixth regulator profile in this repository, following `ico.md`'s format — see `README.md`. Unlike AHPRA and the Medical Board of Australia (which regulate practitioners), the TGA regulates **products** — medicines, medical devices, biologicals, and (as of recent legislative scope) vaping goods. It is a purely federal body: Australia has no state-level equivalent to the TGA, in contrast to the state-based professional-regulation layer described in `ahpra.md`.

## Statutory basis

The TGA operates under the **Therapeutic Goods Act 1989 (Cth)**, part of the Australian Government Department of Health, Disability and Ageing. Per the TGA's own site content returned in search results (checked 2026-08-22 — tga.gov.au's pages themselves timed out on direct fetch this session, so this is corroborated via search-engine-returned excerpts of the TGA's own published wording, not a directly rendered primary page): the Act is "the primary legislative framework for regulating the quality, safety, efficacy, and availability of therapeutic goods in Australia."

## What it regulates

- **Medicines** — from over-the-counter products (e.g. paracetamol) to prescription medicines.
- **Medical devices** — from simple products (bandages, surgical masks) to complex implantable devices.
- **Biologicals** and **blood and blood products**.
- **Vaping goods** (per a corroborating secondary regulatory-summary source checked this session — not independently confirmed against TGA's own page).

Before a therapeutic good can be supplied in or exported from Australia, it must be **registered, listed, or included on the Australian Register of Therapeutic Goods (ARTG)**, unless a specific exemption applies. Medicines are registered or listed depending on risk; medical devices are "included."

**Distinct from PBS funding** — this is the point flagged in `../jurisdictions/src/registry.ts`'s `australia` entry and worth restating precisely: TGA/ARTG approval is a **safety and efficacy** gate. Whether a medicine is then subsidised for patients is a completely separate decision made through the **Pharmaceutical Benefits Scheme (PBS)**. A medicine can be TGA-approved and not PBS-funded, and the two processes should never be conflated in advice to a client.

## Regulatory functions

Per corroborating search results checked this session:

- **Pre-market assessment** — assessing new medicines and medical devices before they can be supplied.
- **Post-market monitoring** — tracking safety once a product is on the market and acting on emerging safety signals (adverse event reporting, recalls).
- **Compliance and enforcement** — per the TGA's own "Compliance and enforcement" page content returned in search results, the TGA "monitors and enforces compliance ... for the import, export, manufacture, advertising, and supply of therapeutic goods," prioritising matters involving public safety, serious breaches of the Act, or repeated/wilful non-compliance.

## Sanction range (enforcement, not disciplinary)

Unlike AHPRA/the Medical Board (which sanction individual practitioners), the TGA's enforcement tools act on products, conduct, and entities — manufacturers, sponsors, advertisers — not on a practitioner's registration to practise:

- **Infringement notices** — an on-the-spot financial penalty for certain breaches, without needing to go to court, per the TGA's own "Compliance and enforcement" content returned in search results.
- **Civil penalty proceedings in court** — for serious or repeated non-compliance. A corroborating secondary legal source (a law-firm enforcement-trends summary, checked this session) cites the largest civil penalty obtained to date as **AUD $22 million**, against Medtronic Australasia, for supplying its Infuse Bone Graft Kit while it was not included on the ARTG — **this specific figure is a secondary-source citation of a reported court outcome, not independently confirmed against a court judgment or TGA media release this session**, and should be checked against the primary judgment before being relied on in any matter.
- **Advertising enforcement** — the TGA specifically calls out advertising and supply of unapproved therapeutic goods as an ongoing enforcement focus area.

## Appeal route

**UNVERIFIED this session.** No search or fetch this session confirmed the specific appeal/review pathway for a TGA regulatory decision (e.g. internal reconsideration, Administrative Review Tribunal — the body that replaced the AAT in 2024 — or judicial review in the Federal Court). This is a genuine gap in this profile rather than a guessed answer: do not assume any of those routes applies to a specific TGA decision type without checking tga.gov.au directly.

## What is NOT in this profile

No independently re-verified primary text of the Therapeutic Goods Act 1989 itself. No confirmed appeal/review route (see above — flagged, not guessed). No detail on the TGA's ARTG listing/registration procedural stages beyond the high-level description above, since tga.gov.au's own procedural pages could not be directly fetched this session (timeouts). No case-by-case TGA enforcement-action database. See `ahpra.md` and `medical-board-australia.md` for the practitioner-regulation side of Australian healthcare regulation, which the TGA is deliberately distinct from.
