---
jurisdiction: Australia
legal_system: common-law (federal)
verification_status: STRUCTURAL_DRAFT
last_reviewed: 2026-08-22
reviewer: initial repository build; corrected 2026-08-22 by an independent fact-check pass (see docs/HONEST_STATUS.md) - Family Court of Australia error fixed; a populated Authority Graph was added the same day via four parallel-agent research passes, each independently re-verified against a live primary source (where reachable) by the orchestrating session before being written - see "Populated Authority Graph" below
---

# Australia

See `docs/HONEST_STATUS.md`. Australia is a federation - Commonwealth (federal) law sits alongside 6 state and 2 territory systems, each with their own courts and much of their own substantive law. This pack covers federal/Commonwealth structure and the general state-court pattern; it does not verify any specific state's content.

## Court hierarchy (headline)

```
High Court of Australia (final appellate court for the whole federation, state and federal matters)
  └── Federal Court of Australia (federal first instance + some appellate, general/commercial/admin matters)
  └── Federal Circuit and Family Court of Australia (FCFCOA - family law and general federal work;
        formed 1 September 2021 by the merger of the former Family Court of Australia and the
        Federal Circuit Court - the "Family Court of Australia" no longer exists as a standalone court)
  └── State/Territory Supreme Courts (Court of Appeal division + trial division)
        └── State/Territory District/County Courts (mid-tier)
              └── State/Territory Magistrates'/Local Courts
```

## Authority hierarchy

The High Court binds all Australian courts. A state Court of Appeal binds courts below it within that state; other states' intermediate appellate decisions are persuasive, not binding, though Australian courts give considerable weight to intermediate-appellate consistency across states (the "Farah Constructions" convention of following other states' Courts of Appeal absent a plainly wrong result) - this pack does not assert the current status of that convention without a per-matter check.

## Citation style

**AGLC** (Australian Guide to Legal Citation) is the standard style. Case citation shape uses medium-neutral citation, e.g. `Party v Party [2023] HCA 12`. Statute citation: `Short Title Year (Jurisdiction) s X`.

## Governing statutes/codes (named, not summarised)

No single federal code; Commonwealth Acts plus state/territory Acts plus common law. Key procedural instruments by name only: Federal Court Rules, and each state's own Uniform Civil Procedure Rules or equivalent (naming conventions differ by state).

## Primary sources to check against

- `austlii.edu.au` (AustLII) - legislation and case law across federal and state jurisdictions
- `legislation.gov.au` - official Commonwealth legislation
- Each state/territory's official legislation site and court site

## Populated Authority Graph

`authorities/` holds four doctrinal files across four subjects - Australia's first Authority Graph content in this repository, each researched live this session against Commonwealth and federal court primary sources.

| File | Subject | Lead case |
|---|---|---|
| `authorities/contract-unconscionable-conduct-normative-standard.json` | Contract Law - the normative standard for statutory unconscionable conduct | *ACCC v Lux Distributors Pty Ltd* [2013] FCAFC 90 |
| `authorities/tort-negligence-breach-four-factor-test.json` | Tort Law - the statutory four-factor breach-of-duty calculus | *Tapp v Australian Bushmen's Campdraft & Rodeo Association Ltd* [2022] HCA 11 |
| `authorities/property-native-title-continuity-requirement.json` | Property Law - native title's "substantially uninterrupted" continuity requirement | *Members of the Yorta Yorta Aboriginal Community v Victoria* [2002] HCA 58 |
| `authorities/criminal-conspiracy-intention-not-recklessness.json` | Criminal Law - the intention element of Commonwealth conspiracy | *The Queen v LK; The Queen v RK* (2010) 241 CLR 177 |

Deliberately narrow, matching the same one-or-two-doctrinal-points-per-file discipline used throughout this repository's other jurisdictions - four real starting points, not a survey. A significant access-pattern finding is worth naming here: AustLII, jade.io, and the High Court's own eresources/download routes returned HTTP 403 or unusable timeouts to automated fetch across dozens of URL attempts spanning all four research passes - far more consistently blocked than England & Wales's or Scotland's primary sources. Three of the four case nodes (Tort, Property, Criminal) are consequently recorded at `VERIFIED_SECONDARY_SOURCE`, corroborated instead via independent, professionally-authored secondary sources (academic case notes, law-firm commentary, official bench books) that themselves pin-cite the primary judgment's paragraphs - never via a third-party reader-proxy, which this repository's access-terms rule excludes. Each file states this honestly rather than presenting a secondary-sourced quote as a primary read. One research pass (Property Law) also caught and discarded an unreliable WebSearch-synthesized claim about a case's bench composition that included a Justice who had not yet been appointed to the High Court at the time of the judgment.

## What is NOT in this pack

No state-specific substantive content verified beyond the four Authority Graph entries above. No verified procedural deadline.
