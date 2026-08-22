---
regulator: DEA (Drug Enforcement Administration)
jurisdiction: United States (federal)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added alongside fda.md, fsmb.md, and ncsbn.md to give US healthcare regulation an honest, non-unified profile — DEA is the one federal body with real, direct authority over controlled-substance *prescribing*, which is otherwise easy to leave out if a spec only covers state medical/nursing boards. Sourced via live browser fetches against dea.gov, deadiversion.usdoj.gov, law.cornell.edu, and ecfr.gov, not recalled from training data. Several direct dea.gov and deadiversion.usdoj.gov URLs returned bot-style 403/404s to the automated WebFetch tool but rendered normally through an interactive browser session in the same sourcing session — noted because it affected sourcing method, not source reliability.
---

# DEA

This profile covers DEA's role regulating the manufacture, distribution, and — the piece most relevant to a clinical-software spec — the **prescribing** of controlled substances by individual practitioners. It does not cover DEA's much larger criminal drug-trafficking enforcement mission, which shares the same agency but is out of scope for a healthcare-regulator profile, consistent with how `ftc.md` scopes out FTC's antitrust mission.

## Statutory basis and mission

Per `dea.gov/about/mission` (checked 2026-08-22), DEA's mission is "to enforce the controlled substances laws and regulations of the United States" and to prosecute (or support prosecution of) those involved in illicit manufacture, growing, or distribution of controlled substances, alongside non-enforcement programs to reduce availability of illicit drugs. Listed among DEA's primary responsibilities on the same page: "Enforcement of the provisions of the Controlled Substances Act as they pertain to the manufacture, distribution, and dispensing of legally produced controlled substances" — this is the clause under which practitioner registration and prescribing oversight sits, distinct from DEA's separate criminal-trafficking responsibilities listed on the same page.

The governing statute is the **Controlled Substances Act (CSA)**, Title 21 US Code. Per `dea.gov/drug-information/csa` (checked 2026-08-22): the CSA "places all substances which were in some manner regulated under existing federal law into one of five schedules," based on "the substance's medical use, potential for abuse, and safety or dependence liability." Scheduling/rescheduling proceedings are governed by **CSA Section 201, 21 U.S.C. § 811**, and may be initiated by DEA, HHS, or by petition from an interested party (manufacturer, medical or pharmacy association, public-interest group, state/local government, or an individual citizen). Section 811(c) lists eight required factors, including actual/relative abuse potential, pharmacological effect, current scientific knowledge, abuse history and pattern, public-health risk, and dependence liability.

## The five schedules

Per `dea.gov/drug-information/drug-scheduling` (checked 2026-08-22): drugs are classified into five schedules by "acceptable medical use" and "abuse or dependency potential." Schedule I has the highest abuse potential and, per the site, "no currently accepted medical use" (examples given: heroin, LSD, marijuana/cannabis, MDMA, methaqualone, peyote) — meaning Schedule I substances are, by DEA's own framework, not part of the legitimate-prescribing system this profile otherwise covers. Schedule II drugs (examples given: fentanyl, oxycodone, methadone, hydromorphone, methamphetamine, Adderall, Ritalin) have "high potential for abuse" with severe dependence risk but a recognized medical use, and are the schedule most relevant to routine clinical prescribing oversight. Schedules III-V step down in abuse potential (examples given for III: ketamine, anabolic steroids, low-dose codeine combinations; for IV: Xanax, Valium, Ambien, tramadol; for V: low-dose antidiarrheal/antitussive/analgesic preparations).

The DEA page notes a substance need not be formally scheduled to be treated as Schedule I for criminal prosecution if it meets the "controlled substance analogue" definition (21 U.S.C. § 802(32)(A)), scheduled under § 813.

## Practitioner registration

Per `deadiversion.usdoj.gov/drugreg/reg_apps/pract-state-lic-require.html` and `deadiversion.usdoj.gov/drugreg/registration.html` (both checked 2026-08-22), and consistent with the general rule (documented across multiple DEA Diversion Control Division FAQ pages checked this session): a **DEA registration is a condition of, not a substitute for, state authority** — a practitioner must hold current authority under state law to prescribe controlled substances before DEA registration is available, and DEA relies on state licensing boards to make that underlying competency determination. A practitioner must generally obtain a **separate DEA registration for each state** in which they maintain an office or practice location; the registration is not portable across states even though it is a federal number. Renewal uses **DEA Form 224a** and, per the current registration page, registrants must keep an active email address on file to receive renewal notices (checked page did not show a definitive "renew every 3 years" statement in the rendered text this session; that figure — commonly cited elsewhere, including in `21 CFR 1301.13(e)(1)(iv)` — is `UNVERIFIED` at the primary-source-this-session standard, since this profile did not independently render the eCFR text of that specific subsection). Since June 27, 2023, practitioners have been required to attest to a one-time, eight-hour controlled-substance training requirement (imposed by the MATE Act, part of the Consolidated Appropriations Act 2023) when applying for or renewing a registration; this specific requirement is drawn from a `deadiversion.usdoj.gov` FAQ search summary rather than a fully rendered primary page this session, so it should be treated as `COMMUNITY_REVIEWED` rather than `MAINTAINER VERIFIED` pending a direct re-fetch.

## Denial, suspension, and revocation of registration

Per `law.cornell.edu/uscode/text/21/824` (checked 2026-08-22, current US Code text): under **21 U.S.C. § 824(a)**, the Attorney General (in practice, DEA acting under delegated authority) may suspend or revoke a registration on finding the registrant has:

1. materially falsified an application;
2. been convicted of a felony under the CSA or an equivalent state/federal drug law;
3. had a state license or registration suspended, revoked, or denied by competent state authority, such that the registrant is "no longer authorized by State law" to handle controlled substances — this is the mechanism that ties DEA registration status directly to the outcome of a *state* medical/nursing board disciplinary proceeding, making DEA's registration decision derivative of state licensure action rather than an independent first-line competency judgment;
4. committed acts rendering the registration "inconsistent with the public interest"; or
5. been excluded from a federal healthcare program under 42 U.S.C. § 1320a-7(a).

**Procedure (§ 824(c)):** before denial, revocation, or suspension, the registrant must be served an order to show cause, stating the basis and specific legal citations, directing appearance "not less than 30 days after" service, and notifying the registrant of the opportunity to submit a corrective action plan before that date. Proceedings run under the federal Administrative Procedure Act (5 U.S.C. subchapter II of chapter 5) and are independent of any parallel criminal prosecution.

**Immediate suspension (§ 824(d)):** the Attorney General may suspend a registration simultaneously with instituting show-cause proceedings, without the normal 30-day process, on a finding of "imminent danger to the public health or safety" — defined in the statute as a substantial likelihood, absent immediate suspension, of death, serious bodily harm, or controlled-substance abuse resulting from the registrant's failure to maintain effective diversion controls or otherwise comply with CSA obligations. This suspension continues through the full proceedings, including judicial review, unless earlier withdrawn or dissolved by a court.

## Civil penalty amounts (verified current, inflation-adjusted)

Per `ecfr.gov/current/title-28/chapter-I/part-85/section-85.5`, Table 1 (current text checked 2026-08-22, showing Title 28 "up to date as of 8/20/2026," figures effective for penalties assessed after July 3, 2025): CSA civil penalties under **21 U.S.C. § 842(c)** vary sharply by violation type, and are not a single figure:

- **General CSA prohibited-act violations** (§ 842(c)(1)(A), covering § 842(a) violations other than the recordkeeping/reporting/opioid categories below) — **$82,950 per violation**.
- **Recordkeeping/reporting violations** (§ 842(c)(1)(B)(i), covering § 842(a)(5), (10), (17) — failure to keep required records, furnish reports, or report theft/loss of controlled substances) — a lower ceiling of **$19,246 per violation**.
- **Opioid-specific failures** under the SUPPORT for Patients and Communities Act (§ 842(c)(1)(B)(ii)) — **$124,825**.
- **Anabolic-steroid false labeling**, importer/exporter/manufacturer/distributor level (§ 842(c)(1)(C)) — **$664,740 per violation**; at the retail level (§ 842(c)(1)(D)) — a much lower **$1,330 per violation**.
- **Reckless-disregard distribution of laboratory supplies to a business** (§ 842(c)(2)(C)) — **$498,517**.
- **Opioid failures by a registered manufacturer or distributor** (§ 842(c)(2)(D)) — **$624,123**.
- **Maintaining drug-involved premises** (21 U.S.C. § 856(d)) — **$459,687**.
- **Controlled Substance Import Export Act violations** (21 U.S.C. § 961(1)) — **$91,245**.

These are the DOJ-published maximums per violation; each is a distinct statutory hook, not a single unified "CSA penalty," and a single course of conduct can implicate more than one at once (e.g., a registrant with both a recordkeeping failure and a separate substantive prohibited act).

## Appeal route and forum

Per `law.cornell.edu/uscode/text/21/877` (checked 2026-08-22): "any person aggrieved by a final decision of the Attorney General" (in practice, DEA's Administrator, acting under delegation) may petition for review in the **US Court of Appeals for the District of Columbia Circuit, or the circuit where the person's principal place of business is located**, within **30 days** of notice of the decision. Findings of fact by the Attorney General, "if supported by substantial evidence, shall be conclusive" — the same substantial-evidence-for-facts framing this repository's `ftc.md` profile found for the FTC's own administrative appeal route, though the statutory text as fetched does not itself spell out the standard of review for the Attorney General's legal conclusions, so that point is `UNVERIFIED` here rather than assumed, consistent with `ftc.md`'s own treatment of the identical gap.

## What is NOT in this profile

No independent verification of the exact 3-year registration renewal period (commonly cited but not independently re-rendered from `21 CFR 1301.13` this session — flagged above, not assumed). No coverage of DEA's criminal drug-trafficking enforcement mission, which is real but out of scope for a healthcare-regulator profile. No coverage of DEA's separate authority over manufacturers, distributors, importers, and exporters as opposed to prescribing practitioners, beyond the civil-penalty table above (which does cover some manufacturer/distributor-specific penalty tiers). No independent verification of the MATE Act training-requirement mechanics beyond a search-engine summary of a DEA FAQ page. No coverage of state-level controlled-substance regulation layered on top of DEA registration (e.g., state PDMP reporting duties, state-specific second-license requirements referenced on the practitioner state-license-requirements page) — that is real and materially varies by state, and belongs in state-level jurisdiction packs (see `../jurisdictions/`), not asserted here.

## Primary sources checked

- `dea.gov/about/mission` — DEA mission statement and enumerated primary responsibilities
- `dea.gov/drug-information/csa` — CSA structure, five-schedule framework, § 811 scheduling factors and petitioners
- `dea.gov/drug-information/drug-scheduling` — Schedule I-V definitions and examples
- `deadiversion.usdoj.gov/drugreg/reg_apps/pract-state-lic-require.html` — state-license-as-precondition table (one-license vs. second-CS-license states)
- `deadiversion.usdoj.gov/drugreg/registration.html` — DEA Form 224a renewal mechanics, required active email
- `law.cornell.edu/uscode/text/21/824` — full text of 21 U.S.C. § 824(a)-(d): grounds, show-cause procedure, immediate suspension
- `law.cornell.edu/uscode/text/21/877` — full text of 21 U.S.C. § 877: judicial review, 30-day window, substantial-evidence standard for facts
- `ecfr.gov/current/title-28/chapter-I/part-85/section-85.5` — current (as of 8/20/2026) DOJ inflation-adjusted civil penalty table, § 842(c) and related CSA penalty lines
