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
| Contract Law | England & Wales - formation/acceptance, remoteness of damages (`contract-formation.json`, `contract-remoteness.json`). Terms, breach generally, misrepresentation, frustration: not built. Scotland - the statutory personal-bar mechanism for informal land contracts (`jurisdictions/scotland/authorities/contract-personal-bar-writing-requirement.json`) - this jurisdiction's first-ever Authority Graph entry. Australia - the normative standard for statutory unconscionable conduct (`jurisdictions/australia/authorities/contract-unconscionable-conduct-normative-standard.json`, case recorded at secondary tier - see file) - this jurisdiction's first-ever Authority Graph entry. Canada - the non-excludable duty of honest contractual performance, common-law provinces (`jurisdictions/canada/authorities/contract-duty-of-honest-performance.json`, both nodes recorded at secondary tier after CanLII presented a bot-verification CAPTCHA that was correctly declined - see file), plus a separate Quebec civil-law entry on general extracontractual liability (`jurisdictions/canada/authorities/quebec-civil-liability-defamation-fault-standard.json`) - this jurisdiction's first-ever Authority Graph entries. New Zealand - the statutory cancellation right for misrepresentation and its substantiality gate (`jurisdictions/new-zealand/authorities/contract-cancellation-misrepresentation-substantiality.json`, both nodes recorded at secondary tier after government sites presented bot-check gates - see file). Spain - article 1258 CC's good-faith integration principle, applied to fill a genuine gap in distribution-contract termination notice (`jurisdictions/spain/authorities/contract-formation-good-faith-integration.json`, both nodes recorded at secondary tier after BOE/CENDOJ access failures - see file) - this jurisdiction's first-ever Authority Graph entries |
| Tort Law | England & Wales - duty of care, occupiers' liability (`tort-duty-of-care.json`, `tort-occupiers-liability.json`). Nuisance, defamation, trespass, product liability, economic torts: not built. Scotland (Delict Law) - the neighbour principle's origin and modern construction (`jurisdictions/scotland/authorities/delict-neighbour-principle-duty-of-care.json`, one node recorded at secondary tier - see file). Australia - the statutory four-factor breach-of-duty calculus (`jurisdictions/australia/authorities/tort-negligence-breach-four-factor-test.json`, both nodes recorded at secondary tier after genuine, repeated primary-source access failures - see file). Canada - the modern Anns/Cooper duty-of-care test and its rigorous application (`jurisdictions/canada/authorities/tort-duty-of-care-proximity-foreseeability.json`, both nodes recorded at secondary tier after the SCC's own site blocked this session's independent re-fetch - see file). New Zealand - the ACC no-fault bar's exemplary-damages exception, a structurally distinctive feature of NZ tort law (`jurisdictions/new-zealand/authorities/tort-acc-bar-exemplary-damages-exception.json`, both nodes recorded at secondary tier - see file). Spain - article 1902 CC's fault-based boundary against objectivised liability (`jurisdictions/spain/authorities/civil-extracontractual-liability-fault-based-boundary.json`, both nodes recorded at secondary tier after a genuine network-level block on BOE/CENDOJ - see file). France - article 1240 CC's objective fault standard, applied to a child's capacity for discernement (`jurisdictions/france/authorities/civil-delictual-liability-objective-fault-standard.json`) - this jurisdiction's first-ever Authority Graph entries |
| Property Law / Real Property | England & Wales - conversion of chattels, the auctioneer's ministerial-act defence (`property-conversion-chattels.json`). Scotland - the anti-monopoly rule for real burdens (`jurisdictions/scotland/authorities/property-real-burden-monopoly-anti-monopoly-rule.json`, case recorded at secondary tier - see file). Australia - native title's continuity requirement (`jurisdictions/australia/authorities/property-native-title-continuity-requirement.json`, case recorded at secondary tier - see file) |
| Land Law | England & Wales - registered interests/actual occupation, easements (`land-registered-interests.json`, `land-easements.json`). Leases, covenants, mortgages, co-ownership: not built |
| Equity & Trusts | England & Wales - imperfect gifts, fiduciary duty (`equity-gifts-trusts.json`, `equity-fiduciary-duty.json`). Resulting/constructive trusts, equitable remedies: not built |
| Restitution / Unjust Enrichment | England & Wales - the four-stage unjust enrichment test, "at the expense of" (`restitution-unjust-enrichment-test.json`). What makes an enrichment unjust, defences, proprietary remedies: not built |
| Family Law | England & Wales - the sharing principle on divorce (`family-financial-remedies-sharing.json`). Needs, compensation, children, domestic abuse, adoption, surrogacy: not built |
| Succession Law | England & Wales - testamentary capacity, intestacy distribution (`succession-testamentary-capacity-and-intestacy.json`). Will formalities, undue influence, probate procedure, family provision claims: not built |
| Consumer Law | England & Wales - the satisfactory-quality implied term, CRA 2015 s.9 (`consumer-satisfactory-quality.json`). Remedial scheme, services, unfair terms, digital content: not built |

### Criminal law and process

| Area | Coverage |
|---|---|
| Criminal Law (substantive) | England & Wales - oblique intent, causation in manslaughter (`criminal-mens-rea.json`, `criminal-causation.json`). Offences against the person, property offences, sexual offences, inchoate offences: not built. Scotland - the objective 'reasonable person' fear/alarm test under s.38 (`jurisdictions/scotland/authorities/criminal-threatening-abusive-behaviour-objective-test.json`). Australia - the intention element of Commonwealth conspiracy (`jurisdictions/australia/authorities/criminal-conspiracy-intention-not-recklessness.json`, case recorded at secondary tier - see file). Canada - the 'role in the incident' construction of the unified self-defence test (`jurisdictions/canada/authorities/criminal-self-defence-role-in-incident.json`, case recorded at secondary tier - see file). New Zealand - excessive self-defence's exclusion from partial-defence status (`jurisdictions/new-zealand/authorities/criminal-self-defence-excessive-force-no-partial-defence.json`, both nodes recorded at secondary tier after a persistent AWS WAF bot-challenge - see file). Spain - the 'agresion ilegitima' requirement of legitima defensa (`jurisdictions/spain/authorities/criminal-legitima-defensa-agresion-ilegitima.json`, both nodes recorded at secondary tier after a genuine network-level block on BOE/CENDOJ - see file). France - the necessity/proportionality test for legitime defense, applied to a law-enforcement officer's lethal force (`jurisdictions/france/authorities/criminal-legitime-defense-proportionality-last-resort.json`) |
| Criminal Procedure & Evidence | England & Wales - hearsay admissibility gateways, Article 6 compliance (`criminal-procedure-hearsay.json`) |
| Sentencing Law | England & Wales - guilty-plea sentence reduction, the unequivocal-indication requirement (`sentencing-guilty-plea-reduction.json`) |
| Youth Justice | England & Wales - age of criminal responsibility, Article 6 effective-participation safeguard (`youth-justice-criminal-responsibility-participation.json`, one node lower-confidence, flagged in the file) |
| Extradition Law | England & Wales/UK - the Article 8 proportionality test for Part 2 requests (`extradition-article-8-proportionality.json`) |

### Public law

| Area | Coverage |
|---|---|
| Constitutional Law | England & Wales - prerogative power/parliamentary sovereignty (`public-law-parliamentary-sovereignty.json`) |
| Administrative Law / Judicial Review | England & Wales - grounds of judicial review (`public-law-judicial-review-grounds.json`). France - the detournement de pouvoir (misuse of power) ground, a genuinely distinctive feature with no common-law equivalent (`jurisdictions/france/authorities/administrative-detournement-de-pouvoir.json`, single-node, the foundational 1875 arret both establishes and applies the doctrine - see file) |
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
| Employment Law | England & Wales - unfair dismissal/whistleblowing detriment, disability discrimination (`employment-unfair-dismissal-whistleblowing.json`, `employment-disability-discrimination.json`). Spain - the ILO Convention 158 prior-hearing requirement for disciplinary dismissal, a very recent (November 2024) doctrinal shift (`jurisdictions/spain/authorities/labour-dismissal-prior-hearing-ilo-convention.json`, both nodes recorded at secondary tier - see file). France - the cause reelle et serieuse threshold for personal-reason dismissal, applied in a very recent (June 2024) case (`jurisdictions/france/authorities/labour-dismissal-cause-reelle-serieuse.json`) |
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
| Elder Law | England & Wales - the patient-centred best-interests test for life-sustaining treatment (`elder-law-best-interests-life-sustaining-treatment.json`) |
| Housing Law | England & Wales - the standard of review for a homelessness final-offer refusal (`housing-homelessness-final-offer-standard-of-review.json`) |
| Welfare / Social Security Law | England & Wales - the hybrid test for a tribunal's issue-consideration duty (`welfare-tribunal-issue-scope-hybrid-test.json`, a suggested candidate citation was checked and discarded as unverifiable - see file) |
| Refugee & Statelessness Law | England & Wales - the balance-of-probabilities standard for statelessness determination (`refugee-statelessness-balance-of-probabilities-standard.json`, one node's link to the current successor provision is the researching agent's own inference, honestly flagged - see file) |
| Indigenous / First Nations Law | England & Wales - UK courts and Chagossian displacement via prerogative-powers doctrine (`indigenous-chagossian-displacement-prerogative-powers.json`, single-node, explicitly not an aboriginal-title case - a second candidate was investigated and rejected as unverifiable, see file). New Zealand - the paramount-provision status of a 'principles of the Treaty of Waitangi' clause (`jurisdictions/new-zealand/authorities/treaty-waitangi-principles-paramount-clause.json`) - this jurisdiction's first-ever Authority Graph entry |
| Climate Change Law | England & Wales - the Secretary of State's information duty under the Net Zero Strategy machinery (`climate-change-net-zero-strategy-information-duty.json`, this session's own independent re-verification attempt initially got the case's outcome backwards and was corrected via a third-pass check before writing - see file) |
| Blockchain & Cryptocurrency Law | England & Wales - cryptoassets as property, common law and statute (`blockchain-cryptoasset-property-status.json`) |
| Biotechnology & Genetics Law | England & Wales - the strict, continuing bilateral-consent requirement for IVF embryos (`biotechnology-embryo-consent-withdrawal.json`) |
| Robotics & Autonomous Systems Law | None |
| Election / Disinformation Regulation | None |
| National Security Law | None |

### Totals

94 of ~99 named areas have a populated Authority Graph entry - 92 in England & Wales, 2 in US-Federal (Civil Procedure; Cybersecurity Law via the CFAA authority-graph.json that predates this session's build-out) - all narrow, one or two doctrinal points each, not a survey. **England & Wales itself is now complete: 99 of 99 taxonomy areas have real content or an honestly-documented reason they don't** (Evidence Law's case-management-only mechanism, Space Law's genuine case-law absence). All eleven of the England & Wales-relevant taxonomy categories are now fully worked through, ending with Rights-based, social, and emerging (13/13 - the last three areas, Robotics & Autonomous Systems, Election/Disinformation Regulation, and National Security Law, remain unbuilt and are named as such below, not silently dropped from the count). **Scotland's, Australia's, Canada's, New Zealand's, Spain's, and France's Authority Graphs now exist for the first time**: Scotland has four entries (Contract, Delict, Property, Criminal Law), Australia has four entries (Contract, Tort, Property, Criminal Law), Canada has five entries (Contract, Tort, Criminal Law, plus a separate Quebec civil-law entry - Canada's mixed common-law/civil-law structure genuinely needed the extra row), New Zealand has four entries (Contract, Tort, Criminal Law, and Indigenous/First Nations Law via Treaty of Waitangi jurisprudence), Spain has four entries (Contract, Civil/Extracontractual Liability, Criminal, Employment Law), and France has four entries (Civil/Extracontractual Liability, Criminal, Employment Law, and Administrative Law/Judicial Review via the detournement de pouvoir doctrine), all added to the existing taxonomy rows rather than new rows, since the taxonomy is jurisdiction-agnostic - see each row's Coverage cell and each jurisdiction's own README. Australia's, Canada's, New Zealand's, and Spain's primary-source access all proved markedly harder than England & Wales's or Scotland's: AustLII/jade.io/hcourt.gov.au for Australia, CanLII's bot-verification CAPTCHA (correctly declined rather than solved) plus intermittent SCC-site blocks for Canada, legislation.govt.nz/courtsofnz.govt.nz's own 'Human Verification' bot-check gates (also correctly declined) for New Zealand, and a genuine network-level block on BOE (ECONNREFUSED) and CENDOJ (DNS resolution failure, or a CAPTCHA on the document-view route) for Spain, confirmed consistently across all four Spanish research passes - most case nodes across all four jurisdictions are recorded at `VERIFIED_SECONDARY_SOURCE` after corroboration via independent, professionally-authored secondary sources, stated honestly in each file rather than presented as a clean primary read. France was a clean counterpoint: legifrance.gouv.fr's codes and jurisprudence databases fetched successfully on every attempt across all four research passes, with no access blocks encountered at all - all four French entries are `VERIFIED_PRIMARY_SOURCE` on both nodes. Spain and France are also this repository's first two civil-law jurisdictions with populated Authority Graph content - all eight entries between them quote original Spanish or French text verbatim with an English paraphrase, following the civilian doctrinal method (starting from the code article, not from precedent) each jurisdiction's own README already documented. Two entries are explicitly time-limited or historic rather than describing current practice going forward: Landlord & Tenant Law's underlying provision (Housing Act 1988 s.21) was repealed by the Renters' Rights Act 2025, and Data Protection & Privacy Law's case-law entry construes a now-repealed statute (DPA 1998 s.13), not the current UK GDPR/DPA 2018 regime - both discovered live during research rather than assumed, and both files say so rather than presenting themselves as current law. One entry (Energy Law) deliberately leaves a case's ultimate disposal marked `UNKNOWN` because this session's fetch tool truncated before the judgment's concluding paragraphs on two separate attempts - the confirmed grounds are recorded, the unconfirmed one is not papered over. One entry (Public International Law/state immunity) has a statute node whose underlying provision has itself since been amended in direct response to the case that construes it - a genuine and rare "the case caused Parliament to change the law" link, marked `OVERRULED` on both nodes to reflect that the specific text construed no longer stands, not that the reasoning was doubted. One entry (Climate Change Law) records a real self-caught error: this session's own independent re-verification of the case's outcome initially returned the wrong answer (inverted), corrected only by a third-pass check against independent secondary sources before the file was written - kept in the file's own notes as a demonstrated instance of exactly the failure mode this repository's verification discipline exists to catch. Roughly a dozen entries across this and earlier passes record a case node's specific pinpoint quotes at `VERIFIED_SECONDARY_SOURCE` rather than primary, because independent re-fetch could not reproduce a primary-source read a researching agent claimed, or because BAILII/Find Case Law genuinely blocked access and only a browser-tool or citing-judgment route was available - the statute half of each pair remains fully primary-verified in every such case. The Comparative Law entry is notable for actively excluding a researching agent's quotes obtained via a third-party reader-proxy, consistent with this repository's own access-terms rule (`docs/OPERATING_RULES.md`) that was written after an earlier instance of exactly that workaround was discarded. Several entries (Arts & Cultural Property, International Human Rights Law, Welfare's discarded-fabricated-citation catch, Climate Change's self-caught inversion) found and recorded genuine discrepancies or errors rather than silently resolving them. Two entries (Space Law, Indigenous/First Nations Law) are deliberate single-node, zero-edge or explicitly-scoped entries - genuine, thoroughly-searched absences of a clean second node, the honest state of real but under-litigated or hard-to-fit fields, rather than a forced pairing. 2 more (Evidence Law, EU Law) have a real mechanism that isn't a case-law Authority Graph: case-management tooling, or a structural jurisdiction pack respectively. The remaining 3 of the 99 (all Rights-based, social, and emerging) have no mechanism at all. This table's own honesty depends on being updated every time that changes; a stale "Built" row is exactly the failure mode `docs/HONEST_STATUS.md` exists to catch.

## Relationship to jurisdiction packs

A practice area's name and boundaries vary by legal system - "Land Law" is common-law terminology; a civil-law jurisdiction folds the same ground into "biens" / real-property provisions of its Civil Code. Don't assume a practice area translates 1:1 across `jurisdictions/`; check the relevant pack's own terminology section (most are `STRUCTURAL_DRAFT` and don't have one populated yet - see `docs/HONEST_STATUS.md`) before assuming an area name means the same thing in two different systems.
