# Limitation / time-bar, M1-KESTREL

Per `skills/legal-litigation/SKILL.md` step 0: calculated first, before any element-by-element work, because it can moot everything else.

## Primary sources checked live this session (2026-08-22)

Not taken from `jurisdictions/england-wales/README.md` (STRUCTURAL_DRAFT, explicitly not a source of verified deadlines). Checked directly against `legislation.gov.uk`:

- **ERA 1996 s.111(2)(a)**: unfair dismissal complaint must be presented "before the end of the period of three months beginning with the effective date of termination," subject to (b) such further period as the tribunal considers reasonable where presentation within three months was not reasonably practicable. Covers heads (1) ordinary unfair dismissal, (2) automatic unfair dismissal (s.103A dismissal for making a protected disclosure), and whistleblowing detriment under s.48 (same three-month/"reasonably practicable" structure, s.48 not independently refetched this session but is part of the same Part V/X time-limit scheme s.111 sits in - flagged `UNVERIFIED` at the pinpoint level for s.48 itself, only s.111 was fetched verbatim).
- **ERA 1996 s.207B**: defines Day A (contact ACAS under Employment Tribunals Act 1996 s.18A) and Day B (receipt of EC certificate). The period from the day after Day A to Day B is not counted towards the limitation period, and if the limitation period would otherwise expire between Day A and one month after Day B, it is extended to the end of that one-month-after-Day-B point instead.
- **Equality Act 2010 s.123**: discrimination claims (heads 4-7: disability discrimination, failure to make reasonable adjustments, discrimination arising from disability, victimisation) must be brought within three months of the act complained of, or such other period as the tribunal thinks just and equitable - a materially different (wider) discretion than unfair dismissal's "reasonably practicable" test. A continuing-act rule applies conduct extending over a period is treated as done at the end of the period.

None of the above three fetches asserted the further case-law gloss that the "three months" period is conventionally calculated as ending the day before the numerically corresponding date in the third month (the `Dedman`/`University of Cambridge v Murray` line) - that refinement was not independently re-verified this session and is marked `UNVERIFIED` here rather than assumed.

## What could not be calculated to an exact date, and why

The facts given fix only relative offsets, not calendar dates:

- EDT: "2 months 3 weeks before this instruction" (instruction date 2026-08-22) - an *estimate*, not an admitted or documented date. Counting back gives approximately **2026-06-01**, but "2 months 3 weeks" is not a precise unit and the real EDT should come from a termination letter or HR record, not from arithmetic on a vague phrase.
- ACAS EC certificate ("Day B"): "1 week after dismissal" - on the estimated EDT, approximately **2026-06-08**.
- ACAS EC contact date ("Day A"): **not stated at all**. Section 207B's calculation needs Day A, not just Day B, and it is impossible to know how much of the primary period was actually "stopped" without it.

## Illustrative calculation only (F-002/F-003 assumptions), run via `scripts/deadline_calculator.py`

```
python3 scripts/deadline_calculator.py --trigger 2026-06-01 --days 92 --unit calendar \
  --rule-source "UNVERIFIED - illustrative only, see procedure/limitation.md"
-> calculated_date: 2026-09-01
```

This used 92 calendar days as a stand-in for "three months" because **the script has no month-denominated mode** - it only accepts `--days` in calendar or business units (see `Router/jurisdiction defect notes.md` item 2). Ninety-two days is not the same calculation as "three months beginning with 1 June," and depending on which months are actually spanned the true statutory date could land a few days earlier or later than this script can express. This output is not being relied on for anything beyond illustrating the mechanism; the actual limitation date must be recalculated once a real EDT is known, ideally by a tool (or a human) that does calendar-month arithmetic, not day-counting.

Even on the illustrative EDT, today (2026-08-22) is inside the primary period either way (2 months 3 weeks < 3 months), so on the facts as given **the primary unfair-dismissal/whistleblowing time limit has very likely NOT yet expired** - but this is a `REASONABLE`, not `VERIFIED`, conclusion, resting on an assumed EDT and an approximated day-count. It should be re-run the moment a real EDT is confirmed.

## What must happen before this is filed on

1. Get the actual EDT and actual ACAS Day A date from primary documents (dismissal letter, ACAS EC certificate itself - the certificate states both Day A and Day B).
2. Re-run the limitation calculation for both the ERA 1996 (unfair dismissal/whistleblowing) and separately the Equality Act 2010 (discrimination) time limits - they are governed by different statutory tests (reasonably practicable vs just and equitable) even though both nominally run three months, so a single shared deadline record is not safe to use for both claim families.
3. Confirm whether any ACAS EC exemption applies (none apparent on the facts given).
4. Treat this as `case_killer: true` on the relevant `issue.schema.json` records until 1-3 are done, per `legal-litigation/SKILL.md` step 2.

## Addendum, 2026-08-22 (second session) - do not assume the statutory 3-month period is about to be extended

Research this session (`research/research_log.md`) found consistent secondary-source reporting (Impact Employment Law, Thompsons, Make UK, Didlaw, GA Solicitors, Brightmine - not independently cross-checked against legislation.gov.uk this session, so `VERIFIED_SECONDARY_SOURCE` only) that the Employment Rights Act 2025 s.152 and Sch 12 extend the primary Employment Tribunal time limit from three months to six months, but **only for claims where the act or failure complained of falls on or after 1 October 2026**.

On the estimated EDT in this matter (approximately 2026-06-01, itself only an `ASSUMED` fact per F-002), the dismissal and any related detriments predate 1 October 2026. The extended six-month period would **not** apply to this matter even once in force - the three-month (or "reasonably practicable"/"just and equitable" extended) period calculated above remains the operative test. This is flagged because it would be an easy, wrong assumption to make given how close the current instruction date (2026-08-22) is to the 1 October 2026 in-force date - the temptation to think "the new six-month rule will apply by the time this is filed" does not survive checking what date the extension actually keys off (the date of the act complained of, not the date of filing or of the rule coming into force).

