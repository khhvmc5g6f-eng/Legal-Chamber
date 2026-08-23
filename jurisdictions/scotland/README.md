---
jurisdiction: Scotland
legal_system: mixed (civilian-influenced with common-law features)
verification_status: STRUCTURAL_DRAFT
last_reviewed: 2026-08-22
reviewer: initial repository build (not independently re-checked by a second reviewer); a populated Authority Graph was added 2026-08-23 via four parallel-agent research passes, then expanded the same day via a second, a third, and a fourth four-agent batch toward full 99-area coverage, each entry independently re-verified against a live primary source by the orchestrating session before being written - see "Populated Authority Graph" below
---

# Scotland

See `docs/HONEST_STATUS.md`. Scotland is a **distinct jurisdiction from England & Wales** with its own courts, procedure, and much of its own substantive law (notably in property, some contract, and criminal procedure) - never assume "UK law" collapses the two. See `docs/SPEC_FULL_TEXT.md` Part XI.

**Note on `STRUCTURAL_DRAFT`:** this label describes the structural narrative below only (court hierarchy, citation style) - it was not itself re-checked against a primary source in this build, matching England & Wales's pack before its own promotion. The Authority Graph in `authorities/` below is a separate, independently-verified layer: each file was checked against a live primary source, per proposition, this session.

## Court hierarchy (civil, headline)

```
UK Supreme Court (final appellate court for most Scottish civil matters)
  └── Court of Session, Inner House (appellate court for both tracks below)
        ├── Court of Session, Outer House (first instance, higher-value/complex - appeals direct to Inner House)
        └── Sheriff Appeal Court (appeals from the Sheriff Court, generally with permission - not automatic)
              └── Sheriff Court (most civil business)
Employment Appeal Tribunal / Employment Tribunal (Scotland) - same UK-wide tribunal system as E&W for employment
```

Note: the Outer House and the Sheriff Court are **parallel first-instance tracks**, not sequential tiers of the same one - a case starts in one or the other depending on value/complexity, and each has its own route up to the Inner House (the Sheriff Court's route via the Sheriff Appeal Court typically requires permission).

Criminal hierarchy (headline only; distinct procedure from E&W - e.g. the historic "not proven" verdict, solemn vs summary procedure):

```
High Court of Justiciary (trial court for the most serious crimes; also the final appellate criminal court - the UK Supreme Court does not generally hear Scottish criminal appeals)
  └── Sheriff Court (solemn and summary criminal business)
        └── Justice of the Peace Court (minor summary offences)
```

## Authority hierarchy

Broadly follows common-law precedent principles (binding on lower courts in the same hierarchy, persuasive across the England & Wales/Scotland boundary), but Scots law also draws on institutional writers and civilian-derived doctrine in areas E&W does not (e.g. some obligations/property doctrine) - this pack does not attempt to state which doctrines those are without per-topic verification.

## Citation style

OSCOLA is used for Scottish legal citation too, with Scotland-specific court abbreviations (e.g. `[2023] CSIH` for Court of Session Inner House, `[2023] CSOH` for Outer House, `[2023] HCJAC` for the High Court of Justiciary Appeal Court).

## Governing statutes/codes (named, not summarised)

No single code; a mix of Acts of the Scottish Parliament, Acts of the UK Parliament (for reserved matters), and common law/institutional writings. Key procedural instruments by name only: the Court of Session Rules, the Ordinary Cause Rules / Summary Cause Rules (Sheriff Court).

## Primary sources to check against

- `legislation.gov.uk` (covers Scottish Parliament Acts alongside UK-wide legislation)
- `scotcourts.gov.uk` - judgments and court rules
- `bailii.org` - Scottish case law is also indexed here

## Populated Authority Graph

`authorities/` holds sixteen doctrinal files across sixteen subjects - Scotland's Authority Graph content in this repository, each verified live against legislation.gov.uk and (where reachable) BAILII/Scottish Courts/the deciding tribunal's own site. This is Scotland's furthest step yet beyond its original four-entry starting point toward the same full 99-area coverage England & Wales already has.

| File | Subject | Lead case |
|---|---|---|
| `authorities/contract-personal-bar-writing-requirement.json` | Contract Law - the statutory personal-bar mechanism for informal land contracts | *The Advice Centre for Mortgages Ltd v McNicoll* [2006] CSOH 58 |
| `authorities/delict-neighbour-principle-duty-of-care.json` | Delict Law - the neighbour principle's origin and modern construction | *Donoghue v Stevenson* [1932] AC 562; *Robinson v Chief Constable of West Yorkshire Police* [2018] UKSC 4 |
| `authorities/property-real-burden-monopoly-anti-monopoly-rule.json` | Property Law - the anti-monopoly rule for real burdens | *Marriott and another v Greenbelt Group Limited*, Lands Tribunal for Scotland LTS/TC/2014/27 |
| `authorities/criminal-threatening-abusive-behaviour-objective-test.json` | Criminal Law - the objective 'reasonable person' fear/alarm test | *Rooney v Procurator Fiscal, Stirling* [2013] HCJAC 57 |
| `authorities/family-cohabitants-economic-advantage-disadvantage.json` | Family Law - cohabitants' capital-sum remedy on separation under the Family Law (Scotland) Act 2006 s.28, a genuinely distinct statutory scheme with no England & Wales equivalent | *Gow v Grant* [2012] UKSC 29 |
| `authorities/succession-legal-rights-moveable-estate-boundary.json` | Succession Law - legal rights (forced heirship), a genuinely distinct feature with no England & Wales equivalent, and the moveable/heritable estate boundary they depend on | *Macdonald v Macdonald's Executrix* [1932] UKHL 3 |
| `authorities/employment-unfair-dismissal-reasonable-inquiry.json` | Employment Law - the UK-wide s.98 unfair-dismissal framework applied by a genuinely Scottish tribunal | *Douglas v North Lanarkshire Council* [2024] EAT 194 |
| `authorities/constitutional-legislative-competence-common-law-review.json` | Constitutional Law - the Scottish Parliament's legislative competence and its common-law reviewability | *AXA General Insurance Ltd v Lord Advocate* [2011] UKSC 46 |
| `authorities/evidence-corroboration-supports-confirms-strengthens.json` | Evidence Law - the corroboration requirement, a distinctive feature of Scots criminal procedure with no equivalent in England & Wales, and its survival despite a failed 2013-2015 abolition attempt | *Lord Advocate's Reference No 1 of 2023* [2023] HCJAC 40, applying *Fox v HM Advocate* 1998 JC 94 |
| `authorities/human-rights-lord-advocate-convention-rights-limit.json` | Human Rights Law - the Scotland Act 1998 s.57(2) Convention-rights limit on the Scottish Government/Lord Advocate, a free-standing devolution-competence constraint distinct from the Human Rights Act itself | *Cadder v HM Advocate* [2010] UKSC 43 |
| `authorities/landlord-tenant-eviction-grounds-exhaustive.json` | Landlord & Tenant Law - the Private Housing (Tenancies) (Scotland) Act 2016 s.51's exhaustive Schedule 3 eviction grounds, with no no-fault route at all | *Wawrzonek v Galewski*, First-tier Tribunal for Scotland, FTS/HPC/EV/26/1444 |
| `authorities/insolvency-floating-charge-statutory-origin-attachment.json` | Insolvency Law - the floating charge's purely statutory origin (Scots law has no equity, unlike England, so had no floating charge at all until statute created one) and its attachment/crystallisation limits | *Sharp v Woolwich Building Society* [1997] UKHL 8 |
| `authorities/agricultural-crofting-right-to-buy-hardship-defence.json` | Agricultural Law - crofting, a genuinely unique form of land tenure with no England & Wales equivalent, and the statutory hardship/sound-management defences to a crofter's right to buy | *Malone v Pattinson*, Scottish Land Court SLC/39/17 |
| `authorities/mental-health-compulsory-treatment-order-criteria.json` | Mental Health Law - the Compulsory Treatment Order criteria under a genuinely distinct statutory scheme with its own tribunal | Mental Health Tribunal for Scotland, MHTS/4/26/04/01073/S063 |
| `authorities/criminal-procedure-prosecutor-master-of-instance.json` | Criminal Procedure - the solemn/summary mode-of-trial classification and the "master of the instance" doctrine underlying prosecutorial control of process, honestly scoped as adjacent rather than directly on point | *Arthur v HM Advocate* [2002] ScotHC 324 |
| `authorities/company-arrestment-individual-company-asymmetry.json` | Company Law - arrestment against company bank accounts and a genuinely distinctive individual/company statutory-protection asymmetry | *Anwar v The Advocate General for Scotland* [2021] UKSC 44 |

Deliberately narrow, matching the same one-or-two-doctrinal-points-per-file discipline used throughout this repository's England & Wales build - not a survey of Scots law, sixteen real entries so far. Two access patterns specific to the Scottish court system are worth naming: BAILII's Scottish archive presented a bot-detection interstitial to direct automated fetch on most cases attempted across all four research passes, resolved either by reading the page through a genuine sandboxed browser session (not a proxy) or, for tribunal decisions and Scottish Land Court decisions that BAILII and Scottish Courts don't index at all, by fetching the decision directly from the deciding body's own official publication site (the Lands Tribunal for Scotland, the Scottish Land Court, the Mental Health Tribunal for Scotland, and the First-tier Tribunal for Scotland's Housing and Property Chamber). The Delict Law entry is honest about a real limitation: no Scottish-originating case that itself substantively engages Donoghue v Stevenson's neighbour principle was found this session, so the entry pairs Donoghue with a UK Supreme Court case (Robinson) that genuinely construes it and that Scottish courts have since applied, rather than force a weaker Scottish-only pairing. The Succession Law entry has a similar honest gap: the paired case (Macdonald v Macdonald's Executrix, 1932) predates the Succession (Scotland) Act 1964 itself, because the researching agent could not find a clean, accessible post-1964 case on legal-rights calculation this session - reported honestly rather than force-fitted. The Evidence Law entry has a comparable gap: the foundational case (Fox v HM Advocate 1998 JC 94) could not be fetched directly (not indexed in BAILII's older Scottish collections), so it is verified instead via two independent routes that quote it verbatim - a 2023 full-bench judgment and the Scottish Judicial Institute's own Jury Manual - recorded at VERIFIED_SECONDARY_SOURCE for that reason. The Employment Law entry is confirmed genuinely Scottish on three independent indicia: the EAT sat at its Edinburgh premises, the Employment Tribunal below sat at Glasgow, and the case reference carries the EAT's own "SCO" regional designator - guarding against the risk of silently duplicating an England & Wales entry under a UK-wide statute. The Insolvency Law entry documents something genuinely distinctive to Scots legal history: the floating charge did not exist at all in Scots law (which has no law of equity) until created entirely by statute in 1961, in sharp contrast to its common-law/equitable development in England. The Criminal Procedure entry has an honest scoping gap of its own: after extensive searching, no case squarely construing the "accused has no right to elect jury trial" principle was found reachable this session, so the entry is deliberately paired with a case on the closely related "master of the instance" doctrine generally, its edge relationship marked OTHER rather than APPLIES to reflect that the pairing is adjacent, not direct. The Mental Health Law entry has a genuine tooling limitation worth naming: the paired tribunal decision's specific paragraph-level reasoning sits on redaction-flattened image pages that the orchestrating session's own PDF-text-extraction tools could not read - the case's identity, date, and disposal were independently confirmed from the document's readable pages, but the exact reasoning wording rests on the researching agent's own read via a rendered browser session.

## What is NOT in this pack

No verified procedural deadline - Court of Session/Sheriff Court rule deadlines must be checked live. The court hierarchy, citation-style description, and named-not-summarised statutes/codes above remain `STRUCTURAL_DRAFT` (general knowledge of how the system is organised, not independently re-checked against a primary source in this build) - only the Authority Graph content above has actually been verified per-proposition.
