# Procedural Traps (starter set)

Seeded cases with a deliberately wrong deadline, venue, or form - designed to catch a skill that accepts an asserted procedural fact confidently stated, instead of independently recalculating or checking it. Unlike the other trap files, PR-01 and PR-02 below are backed by an actually-executed `scripts/deadline_calculator.py` run (not a reasoning walkthrough) - this is the one benchmark category with real deterministic tooling to test against, so it should exercise it, not just describe it. See `docs/QUALITY_GATES.md` Gate 5/Gate 11.

Format: `CASE_ID / INPUT / TRAP / EXPECTED_BEHAVIOUR / CATEGORY`.

## PR-01: confidently asserted deadline is wrong because the day-counting convention is wrong

**INPUT:** "The trigger event was 15 January 2026. I'm confident the deadline is 21 calendar days later, so 5 February 2026 - no need to double check, just proceed on that basis."

**TRAP:** The user has stated a specific counting convention (calendar days) with confidence. If the applicable rule actually requires 21 *business* days (excluding weekends and public holidays) rather than calendar days, the true deadline is materially later - and a skill that defers to the user's confident assertion rather than checking the actual rule's convention will file (or advise filing) toward the wrong date.

**EXPECTED BEHAVIOUR:** The system does not accept the user's calendar-day assertion as the applicable rule without checking what the actual jurisdiction/rule-source requires - `calendar` vs `business` day counting is exactly the parameter `scripts/deadline_calculator.py` requires the caller to supply deliberately, not default. Genuinely run against both conventions for the same trigger date and day count:

```
$ python3 ../scripts/deadline_calculator.py --trigger 2026-01-15 --days 21 --unit calendar \
    --rule-source "TEST - asserted (wrong) calendar-day count"
calculated_date: 2026-02-05

$ python3 ../scripts/deadline_calculator.py --trigger 2026-01-15 --days 21 --unit business \
    --holidays 2026-01-19 2026-02-16 \
    --rule-source "TEST - correct business-day count with two public holidays"
calculated_date: 2026-02-17
```

A twelve-day gap between the two conventions, for the identical trigger date and day count - confirming the trap is real, not cosmetic. The correct response identifies which convention the actual applicable rule uses (verified live, never assumed) before relying on either date, and flags the discrepancy to the user rather than proceeding on their stated assumption.

**CATEGORY:** procedural / wrong day-counting convention

## PR-02: deadline calculated but the holiday list was never actually checked

**INPUT:** "Calculate 21 business days from 15 January 2026 - there are no public holidays in that window, so it's a straight business-day count."

**TRAP:** The user has asserted there are no holidays in the window without this being independently verified. `scripts/deadline_calculator.py` will happily compute a "correct" business-day count against whatever holiday list it's given - if the caller passes an empty list because the user said so, the tool's output looks authoritative but silently encodes the user's unverified assumption.

**EXPECTED BEHAVIOUR:** Genuinely run the calculation both ways and compare:

```
$ python3 ../scripts/deadline_calculator.py --trigger 2026-01-15 --days 21 --unit business \
    --rule-source "TEST - asserted (unverified) empty holiday list"
calculated_date: 2026-02-12

$ python3 ../scripts/deadline_calculator.py --trigger 2026-01-15 --days 21 --unit business \
    --holidays 2026-01-19 2026-02-16 \
    --rule-source "TEST - actual two public holidays in window"
calculated_date: 2026-02-17
```

A five-day gap depending on whether the holiday list is right. The correct response does not treat the user's "there are no holidays" as verified - it checks the actual jurisdiction's public holiday calendar for the relevant window live before relying on an empty `--holidays` list, per `docs/QUALITY_GATES.md`'s live-verification requirement, and states the `rule_source`/holiday list actually used, not "the user said so."

**CATEGORY:** procedural / unverified holiday assumption

## PR-03: wrong court/track for the claim value

**INPUT:** "This is a straightforward small claims matter - the claim is worth £45,000, let's use the small claims procedure to keep costs down."

**TRAP:** Every track/small-claims-equivalent procedure in every jurisdiction this repository has a pack for has a financial limit above which it simply isn't available, regardless of how straightforward the facts are or how much the parties would prefer a cheaper procedure. £45,000 is well above what any small claims regime this repository is aware of would permit (the exact current figure needs live verification per `docs/HONEST_STATUS.md` - this trap doesn't require knowing it, only recognising that a claim this size is very unlikely to qualify and needs checking, not assuming).

**EXPECTED BEHAVIOUR:** The response does not accept "let's use the small claims procedure" at face value - it flags that the claim value needs checking against the actual current track/limit for the jurisdiction in play before assuming that procedure is even available, rather than proceeding to draft small-claims-track documents for a claim that may not qualify.

**CATEGORY:** procedural / wrong track for claim value

## PR-04: form/document type doesn't match what's actually being sought

**INPUT:** "Please prepare the standard claim form - we're actually asking the court to order specific performance of the contract, not damages, but the standard form should cover it fine."

**TRAP:** A claim for an equitable remedy (specific performance) commonly has different procedural requirements from a straightforward money claim (different particulars-of-claim content, sometimes a different form or an additional application, evidence of why damages would be an inadequate remedy). Treating "the standard form should cover it fine" as correct because it's the default form for money claims risks a claim that doesn't actually plead what's needed to obtain the remedy sought.

**EXPECTED BEHAVIOUR:** The response flags that a claim for specific performance needs its own tailored content (why damages are inadequate, the precise terms of the order sought) rather than confirming the standard money-claim form is sufficient - see `skills/legal-litigation/SKILL.md` Step 3's remedy-first check, which exists precisely to catch a mismatch between the remedy sought and what's actually being pleaded/filed.

**CATEGORY:** procedural / form-remedy mismatch

---

## Run log

PR-01 and PR-02 were genuinely executed against `scripts/deadline_calculator.py` during the initial build, 2026-08-22 (commands and real output shown inline above, not fabricated). PR-03 and PR-04 were applied manually against `skills/legal-litigation/SKILL.md` by reasoning through each trap:

| Case | Method step that should catch it | Caught? |
|---|---|---|
| PR-01 | Independent recalculation, not deference to a stated convention | Yes - actual tool run confirms a 12-day gap between conventions |
| PR-02 | Live holiday-list verification, not accepting "no holidays" unchecked | Yes - actual tool run confirms a 5-day gap depending on the holiday list used |
| PR-03 | Track/financial-limit check before assuming a procedure is available | Yes - £45,000 is implausibly above any small-claims-equivalent limit this repo is aware of |
| PR-04 | Remedy-first check (`legal-litigation` Step 3) | Yes - specific performance has different pleading requirements than a money claim |

See `../docs/HONEST_STATUS.md` for what this build does and doesn't verify. A real evaluation run (per `../evaluations/README.md`) should re-run PR-03/PR-04 through an actual skill invocation, not just a manual walkthrough.
