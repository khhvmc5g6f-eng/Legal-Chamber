---
jurisdiction: England & Wales
legal_system: common-law
verification_status: STRUCTURAL_DRAFT
last_reviewed: 2026-08-22
reviewer: initial repository build (not independently re-checked by a second reviewer)
---

# England & Wales

See `docs/HONEST_STATUS.md` for what `STRUCTURAL_DRAFT` means. In short: the structure below is believed accurate as general knowledge of how this legal system is organised; no specific case, statutory pinpoint, or procedural deadline in this file has been checked against a primary source in this build.

## Court / tribunal hierarchy (civil, headline)

```
UK Supreme Court (final appellate court for E&W civil matters)
  └── Court of Appeal (Civil Division)
        └── High Court (King's Bench Division / Chancery Division / Family Division)
              └── County Court
Employment Appeal Tribunal
  └── Employment Tribunal
First-tier Tribunal / Upper Tribunal (regulatory, immigration, tax, etc.)
```

Criminal hierarchy (headline, not relied upon for criminal matter work in this build - `legal-litigation`'s criminal support is jurisdiction-pack-gated and this pack does not yet cover it beyond this structural note):

```
UK Supreme Court
  └── Court of Appeal (Criminal Division)
        └── Crown Court (indictable/either-way, on appeal from Magistrates')
              └── Magistrates' Court (summary offences, first hearings)
```

## Authority hierarchy

Binding: decisions of a higher court in the same hierarchy (Supreme Court binds all; Court of Appeal binds High Court and below; a High Court decision binds County Court but not another High Court judge, who instead treats it as persuasive). Persuasive: decisions of courts of coordinate jurisdiction, Privy Council decisions, and decisions from other common-law jurisdictions (Australia, Canada, etc.). Distinguish ratio decidendi (binding) from obiter dicta (persuasive at most) - this pack does not assert which parts of any specific case are ratio vs obiter; that is a per-case check.

## Citation style

**OSCOLA** (Oxford University Standard for Citation of Legal Authorities) is the standard style for academic and much practitioner work. Case citation shape: `Party v Party [Year] Court CaseNumber` (neutral citation, e.g. `[2023] UKSC 12`) or `Party v Party [Year] Volume Reports Page` for a law-report citation. Statute citation: `Short Title Year, s X`.

## Governing statutes/codes (named, not summarised)

England & Wales does not have a single civil or criminal code; law is a mix of statute and case law. Key procedural instruments by name only (content not verified in this pack): the Civil Procedure Rules (civil litigation), the Criminal Procedure Rules (criminal litigation), the Employment Tribunals Rules of Procedure. Do not assert a specific rule number or deadline from memory - verify live.

## Primary sources to check against

- `legislation.gov.uk` - official legislation database
- `caselaw.nationalarchives.gov.uk` (Find Case Law, successor to BAILII for many purposes) / `bailii.org` - judgments
- `judiciary.uk` - Practice Directions, guidance
- Official Civil Procedure Rules site (`justice.gov.uk` / `civilprocedurerules...`) for CPR text

## What is NOT in this pack

No populated Authority Graph, no verified statutory pinpoint, no verified procedural deadline. See `docs/OPERATING_RULES.md` for what must happen before any of those can be asserted as fact in a matter.
