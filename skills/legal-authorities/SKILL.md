---
name: legal-authorities
description: Verify one specific citation or authority - does it exist, what does it actually hold, does it support the proposition it's being cited for. Use for a narrow "check this citation" request, as distinct from legal-research's broader open-ended research.
---

# legal-authorities

A focused version of the verification hierarchy in `../../docs/OPERATING_RULES.md`, for a single authority rather than a whole research question.

## Checklist

1. **Existence** - search the citation string and the party names independently. A hit only inside another AI-generated document does not count.
2. **Identity match** - court, date, and jurisdiction as claimed. Watch for case-name collisions: same-name parties, appeals of the same matter, consolidated cases, anonymised decisions, and cross-jurisdiction namesakes. For a US court name specifically, `python3 ../../scripts/verify_court_name.py "<name>"` checks it against a real, vendored table (courts-db, 2,809 records) before you assume a court name is genuine - it only confirms the name is a known one, not that this specific case was decided there.
3. **Proposition match** - does this authority actually establish what it's being cited for? Specifically rule out: dicta presented as ratio, a dissent presented as the majority, counsel's submission presented as the court's holding, an overturned first-instance decision, or a different statutory regime/jurisdiction than the one in play.
4. **Currency** - has it been overruled, distinguished into irrelevance, or superseded by legislation? State `LAW_AS_OF` for the check.
5. **Treatment** - record what's known (followed/distinguished/overruled/criticised) and `UNKNOWN` for what isn't.

Record the result with `../../schemas/authority.schema.json`, `verification_status` set honestly, and `verified_at` stamped. If any step fails, the output is `NO_VERIFIED_AUTHORITY_LOCATED` or `UNVERIFIED` - never a downgraded-but-still-asserted version of the citation.

## Output shape

```
CITATION: <as given>
STATUS: VERIFIED_PRIMARY_SOURCE | VERIFIED_SECONDARY_SOURCE | UNVERIFIED | NO_VERIFIED_AUTHORITY_LOCATED
COURT / DATE / JURISDICTION: ...
PROPOSITION CHECKED: ...
DOES IT HOLD THAT: yes / no / partially, because ...
TREATMENT: ...
SOURCE: ...
```
