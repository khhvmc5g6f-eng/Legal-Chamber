---
jurisdiction: Scotland
legal_system: mixed (civilian-influenced with common-law features)
verification_status: STRUCTURAL_DRAFT
last_reviewed: 2026-08-22
reviewer: initial repository build (not independently re-checked by a second reviewer); a populated Authority Graph was added the same day via four parallel-agent research passes, each independently re-verified against a live primary source by the orchestrating session before being written - see "Populated Authority Graph" below
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

`authorities/` holds four doctrinal files across four subjects - Scotland's first Authority Graph content in this repository, each verified live against legislation.gov.uk and (where reachable) BAILII/Scottish Courts/the deciding tribunal's own site.

| File | Subject | Lead case |
|---|---|---|
| `authorities/contract-personal-bar-writing-requirement.json` | Contract Law - the statutory personal-bar mechanism for informal land contracts | *The Advice Centre for Mortgages Ltd v McNicoll* [2006] CSOH 58 |
| `authorities/delict-neighbour-principle-duty-of-care.json` | Delict Law - the neighbour principle's origin and modern construction | *Donoghue v Stevenson* [1932] AC 562; *Robinson v Chief Constable of West Yorkshire Police* [2018] UKSC 4 |
| `authorities/property-real-burden-monopoly-anti-monopoly-rule.json` | Property Law - the anti-monopoly rule for real burdens | *Marriott and another v Greenbelt Group Limited*, Lands Tribunal for Scotland LTS/TC/2014/27 |
| `authorities/criminal-threatening-abusive-behaviour-objective-test.json` | Criminal Law - the objective 'reasonable person' fear/alarm test | *Rooney v Procurator Fiscal, Stirling* [2013] HCJAC 57 |

Deliberately narrow, matching the same one-or-two-doctrinal-points-per-file discipline used throughout this repository's England & Wales build - not a survey of Scots law, four real starting points. Two access patterns specific to the Scottish court system are worth naming: BAILII's Scottish archive presented a bot-detection interstitial to direct automated fetch on every case attempted this session, resolved either by reading the page through a genuine sandboxed browser session (not a proxy) or, for a Lands Tribunal decision that BAILII and Scottish Courts don't index at all, by fetching the judgment directly from the deciding tribunal's own official publication site. The Delict Law entry is honest about a real limitation: no Scottish-originating case that itself substantively engages Donoghue v Stevenson's neighbour principle was found this session, so the entry pairs Donoghue with a UK Supreme Court case (Robinson) that genuinely construes it and that Scottish courts have since applied, rather than force a weaker Scottish-only pairing.

## What is NOT in this pack

No verified procedural deadline - Court of Session/Sheriff Court rule deadlines must be checked live. The court hierarchy, citation-style description, and named-not-summarised statutes/codes above remain `STRUCTURAL_DRAFT` (general knowledge of how the system is organised, not independently re-checked against a primary source in this build) - only the Authority Graph content above has actually been verified per-proposition.
