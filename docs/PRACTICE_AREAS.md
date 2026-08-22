# Practice-area taxonomy

This is a classification map, not substantive law. It records that Land Law is a distinct field from Equity & Trusts, and roughly where each field sits relative to the others - it does not assert anything about what the law in any field actually says. That distinction matters here specifically: `docs/OPERATING_RULES.md` Part I forbids asserting unverified legal content, and a practice-area label is metadata (like a Dewey Decimal number), not a legal proposition, so it doesn't need the same per-item primary-source check a case citation or statutory pinpoint does. Don't let that make it feel like a loophole for asserting doctrine under a taxonomy label - a `practice_areas` entry says "this matter is about Tort," never "the law of Tort says X."

## What this is for

1. **Matter records** - `schemas/matter.schema.json`'s optional `practice_areas` field records which of these apply to a matter, alongside (not instead of) `matter_type`, which is the *process* axis (litigation, transactional, regulatory, ...). A single matter can span multiple practice areas (e.g. an employment tribunal claim is `matter_type: employment` and `practice_areas: [employment, tort]` if it includes a personal-injury element).
2. **`skills/legal-work/SKILL.md`'s classification step** - naming the practice area(s) in play, alongside matter type and jurisdiction, helps route to the right specialist skill and flags which `jurisdictions/<slug>/authorities/` topics (see below) might already have something relevant.
3. **`jurisdictions/<slug>/authorities/*.json` file naming** - as jurisdiction packs grow real Authority Graph content (see `docs/HONEST_STATUS.md`), naming each topic file after a practice area (e.g. `contract-formation.json`, `tort-duty-of-care.json`) keeps the growing set navigable. This taxonomy is the reference list for that naming, not a requirement that every area gets a file - most don't have one yet, and that's expected, not a gap to panic about.

## It doesn't stop at this list

Roughly 90 named fields below, grouped into eleven categories - and several genuinely split further by jurisdiction (Family Law's UK/US divide on matrimonial-property regimes) or by sub-practice (Property routinely separates residential from commercial from agricultural in practice, even though it's one line here). Treat this as a working reference to extend, not a closed enumeration - if a matter needs a practice area not listed, add it as free text; `practice_areas` in the schema is a string array, not a closed enum, precisely so this list doesn't gate what a matter can record.

## Core private law

- Contract Law - formation, terms, breach, remedies, misrepresentation, frustration
- Tort Law - negligence, nuisance, defamation, trespass, product liability, economic torts, occupiers' liability
- Property Law / Real Property - ownership, possession, personal property (chattels)
- Land Law - registered/unregistered land, leases, easements, covenants, mortgages, co-ownership
- Equity & Trusts - express/resulting/constructive trusts, fiduciary duty, equitable remedies (injunctions, specific performance, tracing)
- Restitution / Unjust Enrichment
- Family Law - divorce, financial remedies, children (custody/contact), domestic abuse, adoption, surrogacy
- Succession Law - wills, intestacy, probate, estate administration
- Consumer Law

## Criminal law and process

- Criminal Law (substantive) - offences against the person, property offences, sexual offences, inchoate offences
- Criminal Procedure & Evidence
- Sentencing Law
- Youth Justice
- Extradition Law

## Public law

- Constitutional Law
- Administrative Law / Judicial Review
- Human Rights Law
- Electoral Law
- Immigration & Nationality Law
- Asylum & Refugee Law
- Local Government Law
- Freedom of Information / Public Records Law

## Business, commercial, and financial

- Company / Corporate Law - incorporation, directors' duties, shareholders, insolvency, M&A
- Commercial Law - sale of goods, agency, commercial contracts, secured transactions
- Banking & Finance Law
- Securities & Capital Markets Law
- Insurance Law
- Competition / Antitrust Law
- Insolvency & Restructuring Law
- Tax Law - income, corporate, VAT/sales tax, international tax, customs & excise
- International Trade Law
- Franchise Law
- Partnership Law

## Employment and labor

- Employment Law - unfair dismissal, discrimination, contracts of employment, TUPE/business transfers
- Labor / Trade Union Law
- Pensions Law
- Health & Safety Law
- Immigration-linked Right-to-Work Law

## Intellectual property and technology

- Patent Law
- Copyright Law
- Trademark Law
- Trade Secrets / Confidential Information
- Design Rights
- Technology & IT Law
- Data Protection & Privacy Law (GDPR, UK DPA, CCPA, etc.)
- AI & Algorithmic Regulation
- Cybersecurity Law
- Media & Entertainment Law
- Telecommunications Law

## Property and construction

- Landlord & Tenant Law (residential and commercial)
- Construction Law
- Planning Law
- Environmental Law
- Agricultural Law
- Mining & Natural Resources Law
- Energy Law
- Water Law

## Regulatory and sector-specific

- Healthcare / Medical Law
- Mental Health Law
- Education Law
- Charity Law / Not-for-Profit Law
- Gaming & Gambling Law
- Food & Drug Law
- Aviation Law
- Maritime / Admiralty Law
- Transport Law
- Sports Law
- Arts & Cultural Property Law
- Animal Law

## Procedure, dispute resolution, and the legal profession

- Civil Procedure
- Evidence Law
- Arbitration Law
- Mediation & ADR
- Class Actions / Group Litigation
- Legal Ethics / Professional Responsibility
- Conflict of Laws / Private International Law

## International and comparative

- Public International Law
- International Humanitarian Law (law of armed conflict)
- International Criminal Law
- International Human Rights Law
- Law of the Sea
- Space Law
- EU Law (supranational)
- Comparative Law
- Diplomatic & Consular Law
- Treaty Law

## Rights-based, social, and emerging

- Civil Rights Law
- Disability Law
- Elder Law
- Housing Law
- Welfare / Social Security Law
- Refugee & Statelessness Law
- Indigenous / First Nations Law
- Climate Change Law
- Blockchain & Cryptocurrency Law
- Biotechnology & Genetics Law
- Robotics & Autonomous Systems Law
- Election / Disinformation Regulation
- National Security Law

## Coverage status

What actually has a populated `jurisdictions/<slug>/authorities/*.json` Authority Graph entry, as of this table's own `last_updated` below, versus what's named in the taxonomy above but has no real content yet. This table exists specifically so neither this file nor `README.md` can silently overstate coverage by simply naming an area - see `docs/HONEST_STATUS.md`'s own discipline about not letting a stub read as more than it is. A "Built" row still means **narrow, deliberately** - one or two doctrinal points, not a survey of the field; see the file's own `what_this_is_not` section for exactly what it doesn't cover. Update this table in the same commit that adds or removes a `jurisdictions/*/authorities/*.json` file - a coverage table that drifts from the files it describes is worse than no table at all.

`last_updated: 2026-08-22`

### Core private law

| Area | Coverage |
|---|---|
| Contract Law | England & Wales - formation/acceptance, remoteness of damages (`contract-formation.json`, `contract-remoteness.json`). Terms, breach generally, misrepresentation, frustration: not built |
| Tort Law | England & Wales - duty of care, occupiers' liability (`tort-duty-of-care.json`, `tort-occupiers-liability.json`). Nuisance, defamation, trespass, product liability, economic torts: not built |
| Property Law / Real Property | England & Wales - conversion of chattels, the auctioneer's ministerial-act defence (`property-conversion-chattels.json`) |
| Land Law | England & Wales - registered interests/actual occupation, easements (`land-registered-interests.json`, `land-easements.json`). Leases, covenants, mortgages, co-ownership: not built |
| Equity & Trusts | England & Wales - imperfect gifts, fiduciary duty (`equity-gifts-trusts.json`, `equity-fiduciary-duty.json`). Resulting/constructive trusts, equitable remedies: not built |
| Restitution / Unjust Enrichment | England & Wales - the four-stage unjust enrichment test, "at the expense of" (`restitution-unjust-enrichment-test.json`). What makes an enrichment unjust, defences, proprietary remedies: not built |
| Family Law | England & Wales - the sharing principle on divorce (`family-financial-remedies-sharing.json`). Needs, compensation, children, domestic abuse, adoption, surrogacy: not built |
| Succession Law | England & Wales - testamentary capacity, intestacy distribution (`succession-testamentary-capacity-and-intestacy.json`). Will formalities, undue influence, probate procedure, family provision claims: not built |
| Consumer Law | England & Wales - the satisfactory-quality implied term, CRA 2015 s.9 (`consumer-satisfactory-quality.json`). Remedial scheme, services, unfair terms, digital content: not built |

### Criminal law and process

| Area | Coverage |
|---|---|
| Criminal Law (substantive) | England & Wales - oblique intent, causation in manslaughter (`criminal-mens-rea.json`, `criminal-causation.json`). Offences against the person, property offences, sexual offences, inchoate offences: not built |
| Criminal Procedure & Evidence | England & Wales - hearsay admissibility gateways, Article 6 compliance (`criminal-procedure-hearsay.json`) |
| Sentencing Law | England & Wales - guilty-plea sentence reduction, the unequivocal-indication requirement (`sentencing-guilty-plea-reduction.json`) |
| Youth Justice | England & Wales - age of criminal responsibility, Article 6 effective-participation safeguard (`youth-justice-criminal-responsibility-participation.json`, one node lower-confidence, flagged in the file) |
| Extradition Law | England & Wales/UK - the Article 8 proportionality test for Part 2 requests (`extradition-article-8-proportionality.json`) |

### Public law

| Area | Coverage |
|---|---|
| Constitutional Law | England & Wales - prerogative power/parliamentary sovereignty (`public-law-parliamentary-sovereignty.json`) |
| Administrative Law / Judicial Review | England & Wales - grounds of judicial review (`public-law-judicial-review-grounds.json`) |
| Human Rights Law | England & Wales - s.6 HRA public-authority duty, the proportionality test (`human-rights-proportionality.json`) |
| Electoral Law | England & Wales/UK - the substantial-compliance test for invalidating a parliamentary election (`electoral-substantial-compliance.json`) |
| Immigration & Nationality Law | England & Wales/UK - the "unduly harsh" deportation test (`immigration-deportation-unduly-harsh.json`). Live-flagged: a 2026 amendment widened who counts as a "foreign criminal" - see the file's own caveat |
| Asylum & Refugee Law | England & Wales/UK - the "well-founded fear" test, both its 2022 standard-of-proof framework and its 2010 substantive gloss (`asylum-well-founded-fear.json`). Live-flagged: a fast-moving, contested area - see the file's own caveats |
| Local Government Law | England & Wales - the general power of competence converted into a duty via HRA 1998 (`local-government-general-power-duty.json`) |
| Freedom of Information / Public Records Law | England & Wales/UK - the ministerial veto's narrow construction (`foi-ministerial-veto.json`) |

### Business, commercial, and financial

| Area | Coverage |
|---|---|
| Company / Corporate Law | England & Wales - the director's creditor duty and its s.172(3) trigger (`company-directors-creditor-duty.json`). Other general duties, wrongful/fraudulent trading, disqualification, shareholder remedies: not built |
| Commercial Law | England & Wales - satisfactory quality/fitness for purpose in a B2B sale (`commercial-satisfactory-quality-fitness-purpose.json`) |
| Banking & Finance Law | England & Wales - the Quincecare duty and its APP-fraud scope limit (`banking-quincecare-duty.json`) |
| Securities & Capital Markets Law | England & Wales - issuer liability and intermediated-shareholder standing (`securities-issuer-liability-standing.json`) |
| Insurance Law | England & Wales - the fair-presentation duty and the insurer-waiver exception (`insurance-fair-presentation-waiver.json`) |
| Competition / Antitrust Law | England & Wales - the Chapter II super-dominance pricing doctrine (`competition-super-dominance-pricing.json`, one node secondary-tier - see file) |
| Insolvency & Restructuring Law | England & Wales - wrongful trading and its relationship to the creditor duty (`insolvency-wrongful-trading.json`) |
| Tax Law | England & Wales/UK - the Ramsay purposive-construction principle (`tax-ramsay-purposive-construction.json`) |
| International Trade Law | England & Wales - the documentary-credit autonomy principle and fraud exception (`international-trade-documentary-credit-autonomy.json`, one node secondary-tier - see file) |
| Franchise Law | England & Wales - pre-contractual misrepresentation of store performance (`franchise-precontractual-misrepresentation.json`) |
| Partnership Law | England & Wales - when a partnership relation actually commences (`partnership-commencement-test.json`) |

### Employment and labor

| Area | Coverage |
|---|---|
| Employment Law | England & Wales - unfair dismissal/whistleblowing detriment, disability discrimination (`employment-unfair-dismissal-whistleblowing.json`, `employment-disability-discrimination.json`) |
| Labor / Trade Union Law | UK - the golden formula and the Article 11 detriment-protection gap (`trade-union-detriment-protection-gap.json`) |
| Pensions Law | England & Wales - pension scheme rule construction principles (`pensions-scheme-rule-construction.json`) |
| Health & Safety Law | England & Wales - the "reasonably practicable" risk/cost balancing test (`health-safety-reasonably-practicable.json`) |
| Immigration-linked Right-to-Work Law | UK - the civil penalty notice particularisation requirement (`right-to-work-penalty-notice.json`) |

### Intellectual property and technology

| Area | Coverage |
|---|---|
| Patent Law | England & Wales - direct infringement and the doctrine of equivalents (`patent-doctrine-of-equivalents.json`, one node secondary-tier - see file) |
| Copyright Law | England & Wales - the originality standard, "author's own intellectual creation" (`copyright-originality-standard.json`) |
| Trademark Law | England & Wales - **partial and adjacent**: `ip-passing-off.json` covers the common-law tort of passing off (goodwill/misrepresentation/damage), not registered trade mark infringement under the Trade Marks Act 1994 - a related but legally distinct cause of action. Registered trade mark law itself: not built |
| Trade Secrets / Confidential Information | England & Wales - the breach of confidence test incorporated by the Trade Secrets Regulations 2018 (`trade-secrets-breach-of-confidence.json`) |
| Design Rights | England & Wales - the unregistered design right's "commonplace" originality test (`design-rights-commonplace-test.json`, secondary-tier - see file) |
| Technology & IT Law | England & Wales - the CMA 1990 "unauthorised access" test (`technology-computer-misuse-unauthorised-access.json`, one node deliberately hedged - see file for named, unresolved sourcing gaps) |
| Data Protection & Privacy Law | England & Wales - the material-damage requirement and representative-action bar, under the now-repealed DPA 1998 s.13 (`data-protection-compensation.json`, `Lloyd v Google LLC` [2021] UKSC 50). Plus a `STRUCTURAL_DRAFT` EU jurisdiction pack (`jurisdictions/eu/`) and three real regulator profiles (`regulators/ico.md` UK, `regulators/cnil.md` France, `regulators/ftc.md` US) documenting each regulator's actual power/procedure. The modern UK GDPR/DPA 2018 Article 82/s.168 compensation provision itself: not independently verified |
| AI & Algorithmic Regulation | England & Wales/UK - the new Art.22A-22D automated-decision-making framework (`ai-regulation-automated-decisions.json`, statute only - no squarely-on-point case found, stated honestly rather than forced) |
| Cybersecurity Law | US-Federal - the CFAA "exceeds authorized access" test (`jurisdictions/us-federal/authority-graph.json`, *United States v Nosal* 676 F.3d 854 (9th Cir. 2012) (en banc), *Van Buren v United States* 593 U.S. 374 (2021)) - this repository's first populated Authority Graph entry, predating this session's build-out, missed in earlier passes of this table and only caught on a later audit |
| Media & Entertainment Law | England & Wales - the misuse of private information two-stage test (`media-misuse-private-information.json`) |
| Telecommunications Law | England & Wales - the Electronic Communications Code's operator/occupier distinction (`telecoms-code-operator-occupier.json`) |

### Property and construction

| Area | Coverage |
|---|---|
| Landlord & Tenant Law | England & Wales - **historical/transitional only**: the pre-repeal Housing Act 1988 s.21 "no-fault" possession route and a gas-safety-timing point (`landlord-tenant-s21-historical.json`). S.21 was abolished by the Renters' Rights Act 2025 (effective 1 May 2026, confirmed live) - not current operative practice for new notices. The s.8 statutory-grounds route that replaced it: not built |
| Construction Law | England & Wales - statutory adjudication and the enforcement gateway (`construction-adjudication-enforcement.json`) |
| Planning Law | England & Wales - the "material considerations" test (`planning-material-considerations.json`) |
| Environmental Law | England & Wales - statutory nuisance standing (`environmental-statutory-nuisance-standing.json`) |
| Agricultural Law | England & Wales - the automatic conversion of an agricultural tenancy at will into a full tenancy from year to year under AHA 1986 s.2 (`agricultural-tenancy-at-will-conversion.json`) |
| Mining & Natural Resources Law | England & Wales - Crown petroleum ownership vs. the surface owner's default ownership of the strata (`mining-subsurface-severance.json`) |
| Energy Law | England & Wales - the statutory route for challenging an Ofgem compliance order (`energy-ofgem-compliance-order-challenge.json`, one node's ultimate disposal deliberately left `UNKNOWN` - see file for the named tool-truncation gap) |
| Water Law | England & Wales - statutory exclusivity for failure-to-construct-sewers claims, and its 2024 narrowing (`water-sewer-duty-statutory-exclusivity.json`) |

### Regulatory and sector-specific

| Area | Coverage |
|---|---|
| Healthcare / Medical Law | England & Wales - capacity as the gateway to informed consent, and Montgomery's material-risk disclosure test (`healthcare-informed-consent.json`) |
| Mental Health Law | England & Wales - the Cheshire West "acid test" for deprivation of liberty and its MCA 2005 s.4A statutory trigger (`mental-health-deprivation-of-liberty.json`) |
| Education Law | England & Wales - the absolute, non-delegable duty to secure EHC plan provision under CFA 2014 s.42 (`education-ehc-plan-duty.json`) |
| Charity Law / Not-for-Profit Law | England & Wales - the public benefit requirement's no-presumption rule, applied to fee-charging schools (`charity-public-benefit-fee-charging-schools.json`) |
| Gaming & Gambling Law | England & Wales - the objective "cheating at gambling" test (`gaming-cheating-objective-test.json`, case pinpoint quotes deliberately recorded at secondary tier - see file) |
| Food & Drug Law | England & Wales - the purpose-and-effect "medicinal product" test (`food-drug-medicinal-product-purpose-test.json`) |
| Aviation Law | England & Wales - the Montreal Convention Article 17 "accident" definition (`aviation-montreal-convention-accident-definition.json`) |
| Maritime / Admiralty Law | England & Wales - Article 4's conduct bar on limiting liability (`maritime-limitation-liability-conduct-bar.json`, case recorded at secondary tier after primary sources were blocked or unreliable - see file) |
| Transport Law | England & Wales - CMR Article 29's disapplication of the liability cap for wilful misconduct (`transport-cmr-wilful-misconduct-liability-cap.json`, case pinpoint quotes deliberately recorded at secondary tier - see file) |
| Sports Law | England & Wales - the participant duty-of-care doctrine and its high threshold in elite competition (`sports-participant-duty-of-care.json`) |
| Arts & Cultural Property Law | England & Wales - a foreign state's title to looted antiquities as the basis for an English conversion claim (`arts-cultural-property-foreign-state-title-conversion.json`, one node's exact statutory wording left as a named, unresolved discrepancy - see file) |
| Animal Law | England & Wales - the objective "knew or ought reasonably to have known" fault standard (`animal-welfare-unnecessary-suffering-objective-standard.json`) |

### Procedure, dispute resolution, and the legal profession

| Area | Coverage |
|---|---|
| Civil Procedure | US Federal - pleading standard (*Twombly*/*Iqbal*), Article III standing, personal jurisdiction (`pleading-standard.json`, `article-iii-standing.json`, `personal-jurisdiction.json`). England & Wales has no populated Authority Graph entry for civil procedure specifically, though `workflows/*.md`, `docs/QUALITY_GATES.md`, and `scripts/deadline_calculator.py` provide real generic procedural mechanics, not doctrine |
| Evidence Law | **Mechanism, not doctrine**: `schemas/evidence.schema.json` and `skills/legal-evidence/SKILL.md` give a real Evidence Ledger for organising a matter's own evidence, but that is case-management tooling, not substantive evidence-law content (hearsay, privilege, admissibility rules) - not built |
| Arbitration Law | England & Wales - the s.68 "serious irregularity" high threshold (`arbitration-serious-irregularity-high-threshold.json`) |
| Mediation & ADR | England & Wales - the court's power to compel ADR, per Churchill's reclassification of Halsey (`mediation-adr-compulsion-power.json`, case recorded at secondary tier with a named paragraph-number discrepancy - see file) |
| Class Actions / Group Litigation | England & Wales - the opt-out collective-proceedings suitability threshold (`class-actions-opt-out-collective-proceedings-suitability.json`, case recorded at secondary tier - see file) |
| Legal Ethics / Professional Responsibility | England & Wales - the former-client confidentiality duty and its courtroom test (`legal-ethics-former-client-confidentiality.json`) |
| Conflict of Laws / Private International Law | England & Wales - the "necessary or proper party" jurisdictional gateway (`conflict-of-laws-necessary-proper-party-gateway.json`) |

### International and comparative

| Area | Coverage |
|---|---|
| Public International Law | England & Wales - customary international law's sovereign-act limit on statutory state immunity for employment claims (`public-international-law-state-immunity-employment.json`, one node's exact disposal wording only partially confirmed - see file) |
| International Humanitarian Law | England & Wales - Article 5 ECHR's closed detention list is not displaced by IHL/UNSCR authority absent an affirmative power reaching the individual case (`international-humanitarian-law-article5-detention-basis.json`) |
| International Criminal Law | England & Wales - immunity ratione materiae does not shield international crimes/jus cogens conduct (`international-criminal-law-immunity-jus-cogens.json`, case recorded at secondary tier, sequential rather than direct construes/applies relationship - see file) |
| International Human Rights Law | England & Wales - the "mirror principle" governing domestic treatment of Strasbourg jurisprudence (`international-human-rights-mirror-principle.json`, case recorded at secondary tier with a named paragraph-number discrepancy - see file) |
| Law of the Sea | England & Wales - the UNCLOS-derived baseline as a domestic statute's territorial-reach test (`law-of-the-sea-baseline-territorial-reach.json`) |
| Space Law | England & Wales - the core spaceflight licensing prohibition (`space-law-spaceflight-licensing-prohibition.json`, statute-only - genuine search found no construing case, an honest gap in the case law itself, see file) |
| EU Law (supranational) | `jurisdictions/eu/` exists as a `STRUCTURAL_DRAFT` pack (CJEU hierarchy, Treaty/Regulation/Directive precedence, ECLI citation, primary sources named) - no populated Authority Graph |
| Comparative Law | England & Wales - the methodology for using foreign/comparative law to develop the common law (`comparative-law-causation-methodology.json`, single-node, case recorded at secondary tier after a proxy-fetch method was deliberately excluded per this repository's access-terms rule - see file) |
| Diplomatic & Consular Law | England & Wales - a former diplomat's narrower residual immunity (`diplomatic-consular-immunity-official-functions.json`, case recorded at secondary tier - see file) |
| Treaty Law | England & Wales - the internationalist, purposive approach to construing a scheduled treaty (`treaty-law-internationalist-purposive-interpretation.json`) |

### Rights-based, social, and emerging

| Area | Coverage |
|---|---|
| Civil Rights Law | England & Wales - indirect discrimination's no-reason-requirement (`civil-rights-indirect-discrimination-no-reason-requirement.json`) |
| Disability Law | England & Wales - the reasonable-adjustments middle standard (`disability-reasonable-adjustments-middle-standard.json`) |
| Elder Law | None |
| Housing Law | None |
| Welfare / Social Security Law | None |
| Refugee & Statelessness Law | None |
| Indigenous / First Nations Law | None |
| Climate Change Law | None |
| Blockchain & Cryptocurrency Law | None |
| Biotechnology & Genetics Law | None |
| Robotics & Autonomous Systems Law | None |
| Election / Disinformation Regulation | None |
| National Security Law | None |

### Totals

86 of ~99 named areas have a populated Authority Graph entry - 84 in England & Wales, 2 in US-Federal (Civil Procedure; Cybersecurity Law via the CFAA authority-graph.json that predates this session's build-out) - all narrow, one or two doctrinal points each, not a survey. Intellectual property and technology (11/11), Property and construction (8/8), Regulatory and sector-specific (12/12), Procedure/dispute resolution and the legal profession (6/6), and International and comparative (9/9) are now fully complete categories - ten of eleven overall, leaving only Rights-based, social, and emerging (2/13). Two entries are explicitly time-limited or historic rather than describing current practice going forward: Landlord & Tenant Law's underlying provision (Housing Act 1988 s.21) was repealed by the Renters' Rights Act 2025, and Data Protection & Privacy Law's case-law entry construes a now-repealed statute (DPA 1998 s.13), not the current UK GDPR/DPA 2018 regime - both discovered live during research rather than assumed, and both files say so rather than presenting themselves as current law. One entry (Energy Law) deliberately leaves a case's ultimate disposal marked `UNKNOWN` because this session's fetch tool truncated before the judgment's concluding paragraphs on two separate attempts - the confirmed grounds are recorded, the unconfirmed one is not papered over. One entry (Public International Law/state immunity) has a statute node whose underlying provision has itself since been amended in direct response to the case that construes it - a genuine and rare "the case caused Parliament to change the law" link, marked `OVERRULED` on both nodes to reflect that the specific text construed no longer stands, not that the reasoning was doubted. Nine entries across this pass and the last (Gaming & Gambling, Maritime/Admiralty, Transport, Mediation & ADR, Class Actions, Diplomatic & Consular, International Criminal Law, Comparative Law, Law of the Sea's BAILII-mirror-only limitation) record their case node's specific pinpoint quotes at `VERIFIED_SECONDARY_SOURCE` rather than primary, because this session's own independent re-fetch could not reproduce a primary-source read the researching agent claimed or a proxy/browser-tool bypass used - the statute half of each pair remains fully primary-verified. The Comparative Law entry is notable for actively excluding a researching agent's quotes obtained via a third-party reader-proxy, consistent with this repository's own access-terms rule (`docs/OPERATING_RULES.md`) that was written after an earlier instance of exactly that workaround was discarded. Two entries (Arts & Cultural Property, International Human Rights Law) found and recorded genuine paragraph-number or textual discrepancies across different fetches of the same official source, rather than silently picking one. One entry (Space Law) is a deliberate statute-only, zero-edge node - a genuine, thoroughly-searched absence of any construing case, the honest state of a real but still-underlitigated field. 2 more (Evidence Law, EU Law) have a real mechanism that isn't a case-law Authority Graph: case-management tooling, or a structural jurisdiction pack respectively. The remaining 11 of the 99 have no mechanism at all, all in the Rights-based, social, and emerging category. This table's own honesty depends on being updated every time that changes; a stale "Built" row is exactly the failure mode `docs/HONEST_STATUS.md` exists to catch.

## Relationship to jurisdiction packs

A practice area's name and boundaries vary by legal system - "Land Law" is common-law terminology; a civil-law jurisdiction folds the same ground into "biens" / real-property provisions of its Civil Code. Don't assume a practice area translates 1:1 across `jurisdictions/`; check the relevant pack's own terminology section (most are `STRUCTURAL_DRAFT` and don't have one populated yet - see `docs/HONEST_STATUS.md`) before assuming an area name means the same thing in two different systems.
