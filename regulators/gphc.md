---
regulator: GPhC (General Pharmaceutical Council)
jurisdiction: Great Britain (England, Wales, Scotland) - NOT Northern Ireland, which has its own separate regulator (the Pharmaceutical Society of Northern Ireland); regulates individual pharmacists and pharmacy technicians and registers pharmacy premises
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added alongside hcpc.md to build out the UK healthcare-regulator set, sourced via live WebSearch against pharmacyregulation.org, not recalled from training data
---

# GPhC

The seventh regulator profile in this repository - see `README.md`. Note the jurisdictional scope carefully: unlike GMC, NMC, HCPC, and GDC (all UK-wide), the GPhC covers **Great Britain only** - Northern Ireland pharmacists are regulated separately by the Pharmaceutical Society of Northern Ireland, which is not covered by this profile.

## Statutory basis

The GPhC is the statutory regulator of pharmacists, pharmacy technicians, and registered pharmacy premises in Great Britain, under the **Pharmacy Order 2010** (a statutory instrument). It sets standards for pharmacy professionals and pharmacy premises and maintains the register. Adjudication of fitness-to-practise allegations against individuals is carried out by its own **Fitness to Practise Committee (FtPC)**, sitting in-house (structurally similar to the NMC's model, not delegated to a separately branded tribunal service the way the GMC and HCPC delegate to the MPTS/HCPTS).

## Investigation stages

Per `pharmacyregulation.org` (checked 2026-08-22): the GPhC's own material describes an **Investigating Committee (IC)** stage ahead of any FtPC referral - the IC can close a case with no further action, or close it after giving advice or a formal warning (recorded on the register), or refer the case to the FtPC. At an FtPC hearing (heard by a panel of three: a chair, a registered pharmacy professional, and a lay member), the committee follows a **three-stage process**: (1) findings of fact on any disputed facts, using the civil standard of proof ("balance of probabilities"); (2) whether the facts found amount to a ground of impairment, and whether fitness to practise is currently impaired; (3) determination of the appropriate outcome/sanction.

## Sanction range

Per the sources checked, in ascending order: **advice** or a **warning** (recorded on the register, used where conduct was unacceptable but posed no risk to patients or the public); **conditions of practice** (restricting registration for up to 3 years, e.g. requiring retraining or supervision); **suspension** (up to 12 months, with return to practice dependent on a mandatory review hearing and remediation evidence); and **removal** from the register (reserved for conduct - particularly dishonesty or sexual misconduct - so serious that no period of remediation could restore public confidence). A removed pharmacist may apply for restoration five years after removal takes effect.

## Appeal route and forum

Per `legislation.gov.uk`'s text of the Pharmacy Order 2010 and corroborating secondary legal sources (checked 2026-08-22): under **Article 58** of the Order, a pharmacy professional can appeal an FtPC decision to the **High Court**, within **28 days** of notification. Grounds are legal ones - error of law, procedural unfairness, or a sanction that was wrong or seriously unjust because of serious procedural or other irregularity - broadly the same "wrong or unjust" merits-adjacent standard used across the UK's health-professional appeal regimes. Separately, the **Professional Standards Authority** (the same oversight body that scrutinises GMC, NMC, HCPC, and GDC decisions) can itself refer a GPhC decision to the High Court if it considers a sanction insufficient to protect the public - mirroring the GMC's section 40A mechanism functionally, even though it sits with the PSA rather than the GPhC itself for this particular regulator.

## Primary sources checked

- `pharmacyregulation.org/patients-and-public/reporting-concerns/investigating-concerns/what-fitness-practise-committee-does` and related pages on how concerns are handled (indexed via WebSearch)
- `pharmacyregulation.org` "Good decision making: Fitness to Practise hearings and outcomes guidance" (dated March 2024 per the indexed snippet)
- `legislation.gov.uk/ukdsi/2010/9780111487358/article/56` (Pharmacy Order 2010 text, indexed via WebSearch, for Article 58's numbering as reported in secondary sources)
- Secondary legal-sector sources (GPhC Defence Barristers, Probity and Ethics, LexisNexis UK guidance note) cross-checked for the 28-day window and PSA referral mechanism

## What is NOT in this profile

The Article 58 citation for the appeal provision was reported consistently across secondary sources but the Order's text itself was not directly opened and read this session - treat the specific Article number as `COMMUNITY_REVIEWED`, not independently re-verified against the primary legislative text. No verified detail on pharmacy **premises** registration/inspection (a separate GPhC function from individual fitness to practise, not covered here). No case-by-case FtPC decision database - this is a procedural/structural profile only.
