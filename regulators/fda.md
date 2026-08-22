---
regulator: FDA (Food and Drug Administration)
jurisdiction: United States (federal)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added as part of a batch of US healthcare regulator profiles (alongside dea.md, fsmb.md, ncsbn.md) requested specifically to model US healthcare regulation honestly — the US has no single national professional licensing regulator, so this profile covers the one piece of US healthcare regulation that genuinely IS a single federal body: medicines and medical devices. Sourced via live browser fetches against fda.gov and law.cornell.edu, not recalled from training data. Two direct fda.gov URLs (the FD&C Act overview page and the "Laws Enforced by FDA" page) returned bot-style 404s to the automated WebFetch tool but rendered normally through an interactive browser session in the same sourcing session — flagging this because it affected the sourcing method, not because it casts doubt on the content once rendered.
---

# FDA

This profile covers the FDA's role regulating drugs, biologics, and medical devices — the medicines/devices piece of US healthcare regulation. It does not cover FDA's food, cosmetics, tobacco, or veterinary-product jurisdiction, which are real but out of scope for a healthcare-regulator profile. See `README.md` for what a regulator profile should contain, and see `ncsbn.md`/`fsmb.md` for the companion honest treatment of why the US has no equivalent single national body for *professional* (physician/nurse) licensure.

## Statutory basis

Per `fda.gov/regulatory-information/laws-enforced-fda` (checked 2026-08-22): the Pure Food and Drug Act of 1906 was "the first of more than 200 laws" now enforced by FDA. The core statute is the **Federal Food, Drug, and Cosmetic Act of 1938 (FD&C Act)**, passed after a toxic elixir killed 107 people; it "completely overhauled the public health system," authorizing FDA "to demand evidence of safety for new drugs, issue standards for food, and conduct factory inspections." Per `fda.gov/regulatory-information/laws-enforced-fda/federal-food-drug-and-cosmetic-act-fdc-act` (checked 2026-08-22), the FD&C Act and its amending statutes are codified into **Title 21, Chapter 9 of the United States Code**.

Two amendments verified on the same page are load-bearing for the drugs/devices scope of this profile:

- The **Kefauver-Harris Amendments of 1962** — passed after the European thalidomide tragedy — "strengthened the rules for drug safety and required manufacturers to prove their drugs' effectiveness," not merely their safety.
- The **Medical Device Amendments of 1976** — passed after a US Senate finding that faulty devices caused "10,000 injuries, including 731 deaths" — "applied safety and effectiveness safeguards to new devices" for the first time. This 1976 date is itself load-bearing elsewhere in FDA device regulation: it is the cutoff for "preamendments" devices in the 510(k) framework below.

Per the same page, FDA today "regulates $1 trillion worth of products a year," and "ensures the safety and effectiveness of all drugs, biological products ... medical devices, and animal drugs and feed" — the drugs/devices scope of this profile sits inside that broader mandate, which also covers food and cosmetics (out of scope here).

## Drug approval pathway

Per `fda.gov/drugs/types-applications/new-drug-application-nda` (checked 2026-08-22): "Since 1938, every new drug has been the subject of an approved NDA before U.S. commercialization." The **New Drug Application (NDA)** is "the vehicle through which drug sponsors formally propose that the FDA approve a new pharmaceutical for sale and marketing in the U.S.," incorporating data from the animal studies and human clinical trials conducted under an **Investigational New Drug (IND)** application. The NDA must let an FDA reviewer decide: whether the drug is safe and effective for its proposed use(s) and whether benefits outweigh risks; whether the proposed labeling is appropriate; and whether the manufacturing methods and quality controls are adequate.

This profile did not independently re-verify, this session, the separate ANDA (generic, abbreviated) pathway under FD&C Act section 505(j) or the BLA (biologics) pathway beyond what appeared in search-engine summaries of `ecfr.gov` and `fda.gov` pages — both are real FDA pathways per general FDA structure, but are `UNVERIFIED` at the same live-primary-source standard as the NDA pathway above, and should not be treated as checked to the same depth.

## Medical device pathways

Verified live via `fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k` and `.../premarket-approval-pma` (both checked 2026-08-22):

- **510(k) (Premarket Notification).** Required for most Class I, II, and III devices not requiring a PMA. A 510(k) "is a premarket submission made to FDA to demonstrate that the device to be marketed is ... substantially equivalent[] to a legally marketed device (section 513(i)(1)(A) FD&C Act)." The comparison device is called the "predicate" — any legally marketed device may serve as one, most often a device recently cleared under 510(k) itself, or a "preamendments device" legally marketed before **May 28, 1976** (the Medical Device Amendments cutoff). FDA issues a clearance letter, not an approval; the SE determination "is usually made within 90 days." If FDA finds the device not substantially equivalent, the applicant may resubmit with new data, seek a Class I/II designation via De Novo, file a reclassification petition, or file a PMA instead.
- **PMA (Premarket Approval).** "The FDA process of scientific and regulatory review to evaluate the safety and effectiveness of Class III medical devices" — devices that "support or sustain human life, are of substantial importance in preventing impairment of human health, or which present a potential, unreasonable risk of illness or injury." Required under **section 515 of the FD&C Act**; the governing regulation is **21 CFR Part 814**. PMA is described on FDA's own page as "the most stringent type of device marketing application required by FDA" — approval, not just clearance, is required before marketing, based on FDA finding "sufficient valid scientific evidence to assure that the device is safe and effective for its intended use(s)." A Class III device that fails to meet PMA requirements is "considered to be adulterated under section 501(f) of the FD&C Act and may not be marketed."
- **De Novo classification.** Referenced on both pages above as the route for a novel device with no valid predicate, letting FDA classify it into Class I or II (rather than defaulting it into Class III) under **section 513(f)(2) of the FD&C Act** where general (or general and special) controls are judged sufficient to assure safety and effectiveness. A device classified via De Novo can itself become a predicate for future 510(k)s. This profile did not independently re-fetch a dedicated De Novo FDA page this session beyond what appears cross-referenced on the 510(k)/PMA pages verified above; the De Novo description here is `COMMUNITY_REVIEWED` at the same level as the rest of this section, not independently re-verified against its own dedicated source page.

## What is NOT in this profile

No ANDA/BLA-specific primary-source verification beyond what is cross-referenced above. No coverage of FDA's food, cosmetics, tobacco, or animal-drug jurisdiction. No coverage of FDA's inspection/enforcement powers (warning letters, seizure, injunction, criminal referral) — this profile is a premarket-pathway profile, not an enforcement profile; DEA's enforcement/registration model in `dea.md` is a closer analogue to what an FDA *enforcement* profile would need to cover, and that gap should be treated as open rather than assumed covered. No independent verification of the De Novo process's own dedicated FDA guidance page. No verification of the FDA's post-market surveillance or recall authority. Two fda.gov URLs (see reviewer note above) needed an interactive browser fetch rather than the automated WebFetch tool to render — noted for anyone re-verifying this profile who hits the same 404 with a plain automated fetch.

## Primary sources checked

- `fda.gov/regulatory-information/laws-enforced-fda` — FD&C Act history, Kefauver-Harris and Medical Device Amendments, scope of FDA's $1 trillion/year regulatory footprint
- `fda.gov/regulatory-information/laws-enforced-fda/federal-food-drug-and-cosmetic-act-fdc-act` — FD&C Act codification into Title 21 Chapter 9 USC
- `fda.gov/drugs/types-applications/new-drug-application-nda` — NDA process, IND linkage, the three key FDA-reviewer decisions
- `fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k` — 510(k) process, substantial equivalence standard, predicate devices, 1976 preamendments cutoff
- `fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-approval-pma` — PMA process, Class III scope, 21 CFR Part 814, section 515/501(f) FD&C Act citations
