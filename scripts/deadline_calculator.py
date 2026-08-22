#!/usr/bin/env python3
"""Deterministic business-day-aware deadline calculator.

This is arithmetic, not legal judgement: it computes a date N "days" after a
trigger date under a caller-supplied rule (calendar days or business days,
with an optional holiday list), and reports how it got there. It does NOT
know what rule applies in any jurisdiction - the caller must supply
`--rule-source` for the record, and the actual rule (calendar vs business
days, which holidays, whether the count includes or excludes day zero) must
come from a verified primary source, not from this script's defaults.

Usage:
    python3 deadline_calculator.py --trigger 2026-01-15 --days 21 \
        --unit business --holidays 2026-01-19 --rule-source "UNVERIFIED - example only"

    python3 deadline_calculator.py --selftest
"""

import argparse
import datetime
import sys


def parse_date(s):
    return datetime.date.fromisoformat(s)


def add_calendar_days(start, days):
    return start + datetime.timedelta(days=days)


def add_business_days(start, days, holidays):
    """Move forward `days` business days from `start` (start not counted).
    `days` of 0 returns `start` unchanged, even if `start` itself falls on a
    weekend/holiday - this function only counts steps, it does not validate
    that the starting point is a business day. Negative `days` moves backward."""
    holidays = set(holidays or [])
    current = start
    step = 1 if days >= 0 else -1
    remaining = abs(days)
    while remaining > 0:
        current = current + datetime.timedelta(days=step)
        if current.weekday() < 5 and current not in holidays:
            remaining -= 1
    return current


def roll_to_next_business_day(d, holidays):
    """If `d` falls on a weekend or a holiday, move forward to the next
    business day. This is a distinct, jurisdiction-specific rule (e.g. many
    court-procedure rules do this for calendar-day deadlines, some don't) -
    it is never applied automatically, only when the caller opts in with
    `--roll-if-non-business`, because assuming it by default would itself be
    an unverified legal assumption baked into arithmetic."""
    holidays = set(holidays or [])
    while d.weekday() >= 5 or d in holidays:
        d = d + datetime.timedelta(days=1)
    return d


def calculate(trigger_date, days, unit, holidays, inclusive_of_trigger=False, roll_if_non_business=False):
    holidays = [parse_date(h) if isinstance(h, str) else h for h in (holidays or [])]
    base = trigger_date
    effective_days = days - 1 if inclusive_of_trigger else days
    if unit == "calendar":
        result = add_calendar_days(base, effective_days)
        if roll_if_non_business:
            result = roll_to_next_business_day(result, holidays)
    elif unit == "business":
        result = add_business_days(base, effective_days, holidays)
    else:
        raise ValueError("unit must be 'calendar' or 'business'")
    return result


def selftest():
    failures = []

    # Calendar days: 10 calendar days after 2026-01-01 (Thursday) = 2026-01-11
    r = calculate(datetime.date(2026, 1, 1), 10, "calendar", [])
    if r != datetime.date(2026, 1, 11):
        failures.append(f"calendar case: expected 2026-01-11, got {r}")

    # Business days: 5 business days after Friday 2026-01-02 skipping weekend
    # 2026-01-02 is a Friday. +1 biz day -> Mon 2026-01-05, +5 -> Fri 2026-01-09
    r = calculate(datetime.date(2026, 1, 2), 5, "business", [])
    if r != datetime.date(2026, 1, 9):
        failures.append(f"business-day case: expected 2026-01-09, got {r}")

    # Business days with a holiday inserted
    r = calculate(datetime.date(2026, 1, 2), 5, "business", [datetime.date(2026, 1, 5)])
    if r != datetime.date(2026, 1, 12):
        failures.append(f"business-day+holiday case: expected 2026-01-12, got {r}")

    # Weekend never counted as a business day
    r = calculate(datetime.date(2026, 1, 2), 1, "business", [])
    if r.weekday() >= 5:
        failures.append(f"weekend leaked into business-day result: {r}")

    # inclusive_of_trigger: trigger date itself counts as day 1
    # 2026-01-01 is day 1, so 10 inclusive calendar days lands on 2026-01-10, not -11
    r = calculate(datetime.date(2026, 1, 1), 10, "calendar", [], inclusive_of_trigger=True)
    if r != datetime.date(2026, 1, 10):
        failures.append(f"inclusive_of_trigger case: expected 2026-01-10, got {r}")

    # days=0 returns the trigger date unchanged
    r = calculate(datetime.date(2026, 1, 2), 0, "calendar", [])
    if r != datetime.date(2026, 1, 2):
        failures.append(f"days=0 case: expected trigger date unchanged, got {r}")
    r = calculate(datetime.date(2026, 1, 2), 0, "business", [])
    if r != datetime.date(2026, 1, 2):
        failures.append(f"days=0 business case: expected trigger date unchanged, got {r}")

    # negative days moves backward
    r = calculate(datetime.date(2026, 1, 15), -10, "calendar", [])
    if r != datetime.date(2026, 1, 5):
        failures.append(f"negative calendar days case: expected 2026-01-05, got {r}")

    # roll_if_non_business: a calendar deadline landing on a weekend rolls forward
    # 2026-01-02 (Friday) + 1 calendar day = 2026-01-03 (Saturday) -> rolls to 2026-01-05 (Monday)
    r = calculate(datetime.date(2026, 1, 2), 1, "calendar", [], roll_if_non_business=True)
    if r != datetime.date(2026, 1, 5):
        failures.append(f"roll_if_non_business case: expected 2026-01-05, got {r}")
    # without the flag, the same calculation lands on the Saturday unrolled
    r = calculate(datetime.date(2026, 1, 2), 1, "calendar", [])
    if r != datetime.date(2026, 1, 3):
        failures.append(f"unrolled calendar case: expected 2026-01-03 (Saturday, unrolled), got {r}")

    if failures:
        print("SELFTEST FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("SELFTEST OK (10/10 checks passed)")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--trigger", help="ISO date the clock starts, e.g. 2026-01-15")
    p.add_argument("--days", type=int, help="Number of days")
    p.add_argument("--unit", choices=["calendar", "business"], default="calendar")
    p.add_argument("--holidays", nargs="*", default=[], help="ISO dates excluded when --unit business")
    p.add_argument("--inclusive-of-trigger", action="store_true", help="Count the trigger date itself as day 1")
    p.add_argument("--roll-if-non-business", action="store_true",
                    help="Calendar mode only: if the result lands on a weekend/holiday, roll forward to the "
                         "next business day. This is a jurisdiction-specific rule, never applied by default.")
    p.add_argument("--rule-source", default="UNVERIFIED", help="Record what rule this calculation is under - do not omit")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()

    if args.selftest:
        sys.exit(selftest())

    if not args.trigger or args.days is None:
        p.error("--trigger and --days are required unless --selftest is passed")

    trigger = parse_date(args.trigger)
    result = calculate(trigger, args.days, args.unit, args.holidays, args.inclusive_of_trigger, args.roll_if_non_business)

    print(f"trigger_date: {trigger.isoformat()}")
    print(f"days: {args.days} ({args.unit})")
    print(f"holidays_excluded: {args.holidays}")
    print(f"roll_if_non_business: {args.roll_if_non_business}")
    print(f"rule_source: {args.rule_source}")
    print(f"calculated_date: {result.isoformat()}")
    if args.rule_source == "UNVERIFIED":
        suggested_confidence = "ESTIMATE"
    else:
        suggested_confidence = "CALCULATED_UNVERIFIED_RULE"
    print(f"suggested schemas/deadline.schema.json confidence value: {suggested_confidence}")
    if args.rule_source == "UNVERIFIED":
        print("WARNING: --rule-source was not supplied. This tool has no way to enforce that the record you "
              "write down matches this warning - if you set confidence to VERIFIED_AGAINST_PRIMARY_SOURCE "
              "anyway, that is a false record. Only that value is appropriate once a human has actually "
              "checked this calculation's rule against a primary source, not merely run this script.",
              file=sys.stderr)


if __name__ == "__main__":
    main()
