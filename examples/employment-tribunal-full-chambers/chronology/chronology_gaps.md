# Chronology gaps, M1-KESTREL

Per `skills/legal-evidence/SKILL.md`'s chronology section: actively look for gaps where a document or event would be expected but isn't there. This matter has several events the scenario names as existing, but none of them carry any date information at all - not even an offset - so none of them can be placed on `chronology.json` without inventing a date that isn't supported by anything supplied. Listing them here, rather than fabricating a placeholder date, is itself the finding:

| Alleged event | Related facts | Why it cannot be placed on the timeline |
|---|---|---|
| Protected disclosure(s) | F-009, F-010 | No date, approximate period, or even a "before/after dismissal" ordering is stated. |
| Disciplinary process (start, hearing(s), outcome) | F-011, F-012 | Stated only as "preceded termination" - no date and no distance-from-dismissal is given, unlike the dismissal and ACAS EC dates which at least have offsets. |
| Occupational health referral(s)/report(s) | F-015, F-016 | Existence alleged only; no date. |
| Sickness absence period(s) | F-017, F-018 | Existence alleged only; no date range or pattern. |
| Contradictory internal emails | F-013, F-014 | Existence alleged only; no date, sender, or recipient. |
| ACAS EC "Day A" (first contact with ACAS) | F-004 | Only "Day B" (the certificate date, CHR-002) is given; Day A is not stated at all. |

**Consequence for causation analysis**: several of the claim heads in `issues/issues.json` (automatic unfair dismissal, whistleblowing detriment, discrimination arising from disability, victimisation) turn on temporal and causal sequencing between these undated events and the dismissal - which disclosure/adjustment-request/protected-act came first, and how close in time it sat to the disciplinary process or dismissal. None of that can be assessed from the facts as supplied. This is recorded as a fact-gap (see the relevant `UNKNOWN` facts above) and reflected in `proof_status: UNSUPPORTED` on the corresponding issue elements, not resolved by assumption.

**Schema note**: `schemas/chronology.schema.json` requires `date` on every event, with `date_certainty` (including an `UNKNOWN` enum value) only qualifying how firm that date is - there is no way to add a record for something known to exist but for which literally zero date information exists, without either (a) omitting it from the chronology file entirely (what has been done here) or (b) putting a non-ISO placeholder string in a field documented as "ISO date". See `intake/router_defect_notes.md` item 5 for this flagged as a schema defect.
