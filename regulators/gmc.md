---
regulator: GMC (General Medical Council)
jurisdiction: United Kingdom (England, Wales, Scotland, Northern Ireland - one regulator for all four; the tribunal function sits with the MPTS, a statutory committee of the GMC operating at arm's length)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added alongside ico.md/cnil.md/ftc.md to build out the UK healthcare-regulator set, sourced via live WebSearch against gmc-uk.org, mpts-uk.org, and named secondary legal-sector sources (direct WebFetch of gmc-uk.org and mpts-uk.org pages returned HTTP 403 this session; findings below rest on search-engine-indexed snippets of those official pages plus corroborating secondary sources, not on a fetched full page - see "What is NOT in this profile")
---

# GMC

The fourth regulator profile in this repository, and the first of the UK's individual-practitioner healthcare fitness-to-practise regulators - see `README.md`.

## Statutory basis

The GMC is the UK-wide statutory regulator of doctors (and, since 2024, physician associates and anaesthesia associates), under the **Medical Act 1983** (as amended). It keeps the register of licensed medical practitioners and sets standards of practice, education, and conduct (`Good Medical Practice`). Adjudication of fitness-to-practise allegations is carried out by the **Medical Practitioners Tribunal Service (MPTS)**, a statutory committee of the GMC established in 2012 specifically to separate investigation/prosecution (done by the GMC) from adjudication (done by the MPTS), which operates "at arm's length" from the GMC's own decision-making.

## Investigation stages

Per `gmc-uk.org` and corroborating secondary legal sources (checked 2026-08-22): a case can originate from a third-party complaint (patient, employer, police), self-referral by the doctor, or the GMC opening its own investigation. The broad stages are:

- **Triage** - initial assessment of whether a concern falls within the GMC's remit and criteria for investigation.
- **Provisional enquiry** (where used) - a limited initial review to decide whether a full investigation should open.
- **Formal investigation** - the GMC sends a "Rule 7 letter" (under the Fitness to Practise Rules 2004) setting out the allegation and giving the doctor 28 days to respond; evidence, expert opinion, and clinical advice are gathered.
- **Case examiner decision** - two case examiners (one medical, one lay) review the evidence and decide whether to close the case, issue a warning, agree undertakings, or refer it to the MPTS.
- **MPTS tribunal hearing** - an independent Medical Practitioners Tribunal (a panel separate from the GMC) determines the facts, whether the doctor's fitness to practise is impaired, and any sanction. The MPTS also runs separate **interim orders tribunals** (which can restrict practice pending the outcome of a full investigation), and review, restoration, and non-compliance hearings.

The GMC investigates and prosecutes; the MPTS adjudicates independently - these are institutionally separate functions even though the MPTS is legally a GMC committee.

## Sanction range

Per the sources checked, where impairment is found an MPT can impose, in ascending order of severity: **a warning** (recorded but not restricting practice), **undertakings**, **conditions on registration** (up to 3 years, reviewed), **suspension** (up to 12 months, reviewed before expiry), or **erasure** from the register (permanent removal, reserved for the most serious cases - dishonesty, sexual misconduct, violence, or conduct fundamentally incompatible with continued registration). Panels apply MPTS sanctions guidance and must select the least restrictive sanction sufficient to protect patients and maintain public confidence.

## Appeal route and forum

Per secondary legal-sector sources summarising the Medical Act 1983 (checked 2026-08-22): a doctor found impaired can appeal an MPT decision under **section 40** of the Medical Act 1983 to the **High Court** (England & Wales), **Court of Session** (Scotland), or **High Court of Justice in Northern Ireland**, within **28 days** of notification. Section 40 appeals are generally treated as a rehearing, with the Court able to dismiss the appeal, allow it and quash the direction, substitute its own direction, or remit to the MPT. Separately, under **section 40A** (added by later amendment), the **GMC itself** can appeal an MPT decision it considers insufficient for public protection - a narrower, review-basis appeal, not a rehearing. This is a materially asymmetric appeal structure: the doctor's own appeal right is broader than the GMC's.

## Primary sources checked

- `gmc-uk.org` pages on "How we make decisions about a doctor's fitness to practise" and related fitness-to-practise guidance (indexed content reviewed via WebSearch; direct WebFetch blocked with HTTP 403 this session)
- `mpts-uk.org` pages on hearing types, appeals, and sanctions guidance (indexed content reviewed via WebSearch; direct WebFetch blocked with HTTP 403 this session)
- Secondary legal-sector summaries of Medical Act 1983 sections 40 and 40A (5SAH, Kings View Chambers, Doctors Defence Service, Burton Copeland, Regulation Resolution) cross-checked against each other for consistency on the 28-day time limit and court venues

## What is NOT in this profile

No text of the Fitness to Practise Rules 2004 was directly read this session (procedural detail above is drawn from secondary summaries of it, not the rules themselves). Direct WebFetch of `gmc-uk.org` and `mpts-uk.org` returned HTTP 403 in this session, so nothing here is drawn from a fully fetched official page - it rests on search-engine-indexed snippets of those pages, which is a materially weaker check than an actual page fetch; a maintainer should re-attempt a direct fetch (or manual browse) before upgrading this past `COMMUNITY_REVIEWED`. No verified position on the newer physician associate/anaesthesia associate fitness-to-practise regime beyond the fact that the GMC took on their regulation in December 2024 - not researched in this session. No case-by-case MPTS decision database - this is a procedural/structural profile only.
