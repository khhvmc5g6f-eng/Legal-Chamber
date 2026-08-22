#!/usr/bin/env python3
"""Deterministic US reporter citation-year plausibility checker.

scripts/citation_lint.py already checks whether a US reporter citation's
*abbreviation* is real (vendored from Free Law Project's reporters-db,
scripts/data/reporters.json). It never checks the *year* against that same
data - but reporters-db also records each edition's real start/end date
(e.g. "A." ran 1885-1938, "A.2d" 1938-2010, "A.3d" 2010-present). A citation
naming a real reporter abbreviation but a year outside that edition's actual
run (a case "reported" in A.3d in 1990, three decades before A.3d existed)
is exactly the shape a fabricated or garbled citation would take, and
nothing previously checked it. This is a date-range lookup, not legal
judgement, so it belongs here per CLAUDE.md's "deterministic tools first"
principle - like citation_lint.py itself, it is a plausibility check, not a
truth check: a plausible year does not mean the case exists, only that this
one automatic reason to doubt it doesn't apply.

Usage:
    python3 verify_citation_years.py path/to/draft.md [more files...]
    python3 verify_citation_years.py --selftest
"""

import argparse
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import citation_lint  # noqa: E402  (reuse its US-reporter shape pattern and normalisation)

_REPORTERS_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "reporters.json")
_YEAR_RE = re.compile(r"\((?:[^()]*?\s)?(\d{4})\)\s*$")

_edition_ranges_cache = None


def _load_edition_ranges():
    """Map normalised edition abbreviation -> (start_year, end_year_or_None).

    Keyed on the specific edition (e.g. "a.3d"), not the reporter family
    (e.g. "A."), because different editions of the same reporter have
    different, non-overlapping date ranges - collapsing them would defeat
    the entire point of this check."""
    global _edition_ranges_cache
    if _edition_ranges_cache is not None:
        return _edition_ranges_cache
    ranges = {}
    try:
        with open(_REPORTERS_DATA_PATH, encoding="utf-8") as f:
            data = json.load(f)
        for entries in data.values():
            for entry in entries:
                for edition, span in entry.get("editions", {}).items():
                    start = span.get("start")
                    end = span.get("end")
                    if not start:
                        continue
                    start_year = int(start[:4])
                    end_year = int(end[:4]) if end else None
                    key = citation_lint._normalize_reporter(edition)
                    # A reporter name can legitimately map to more than one
                    # historical publisher/edition record - widen to the
                    # union of all ranges sharing this exact edition key
                    # rather than overwriting, so a real citation isn't
                    # flagged just because it hit the narrower of two entries.
                    if key in ranges:
                        prev_start, prev_end = ranges[key]
                        start_year = min(start_year, prev_start)
                        if prev_end is None or end_year is None:
                            end_year = None
                        else:
                            end_year = max(end_year, prev_end)
                    ranges[key] = (start_year, end_year)
    except (OSError, json.JSONDecodeError):
        pass
    _edition_ranges_cache = ranges
    return ranges


def check_text(text, current_year=None):
    """Returns a list of finding strings for implausible citation years."""
    if current_year is None:
        current_year = datetime.datetime.now().year
    ranges = _load_edition_ranges()
    findings = []
    for m in citation_lint._US_REPORTER_WITH_GROUP.finditer(text):
        full_match = m.group(0)
        reporter_raw = m.group(1)
        year_match = _YEAR_RE.search(full_match)
        if not year_match:
            continue
        year = int(year_match.group(1))
        edition_key = citation_lint._normalize_reporter(reporter_raw)
        if edition_key not in ranges:
            continue  # unrecognised reporter is citation_lint.py's job, not this check's
        start_year, end_year = ranges[edition_key]
        if year < start_year:
            findings.append(
                f"implausible_citation_year: {full_match.strip()!r} - {reporter_raw.strip()!r} did not begin "
                f"until {start_year}, but the citation gives {year}"
            )
        elif end_year is not None and year > end_year:
            findings.append(
                f"implausible_citation_year: {full_match.strip()!r} - {reporter_raw.strip()!r} ended in "
                f"{end_year}, but the citation gives {year}"
            )
        elif year > current_year:
            findings.append(
                f"implausible_citation_year: {full_match.strip()!r} - {year} is in the future "
                f"(current year is {current_year})"
            )
    return findings


def selftest():
    failures = []

    ranges = _load_edition_ranges()
    if not ranges:
        failures.append("reporters-db data file failed to load (scripts/data/reporters.json) - year checking is silently disabled")

    # A.3d only started in 2010 - citing it for a 1990 case is implausible.
    too_early = check_text("See Smith v Jones, 12 A.3d 456 (1990).", current_year=2026)
    if not any("1990" in f for f in too_early):
        failures.append(f"did not flag a pre-1938 A.3d citation as implausible - findings were: {too_early}")

    # A. (first series) ended in 1938 - citing it for a 2005 case is implausible.
    too_late = check_text("See Smith v Jones, 12 A. 456 (2005).", current_year=2026)
    if not any("2005" in f for f in too_late):
        failures.append(f"did not flag a post-1938 first-series A. citation as implausible - findings were: {too_late}")

    # A real, in-range citation must not false-positive.
    real = check_text("See Roe v Wade, 410 U.S. 113 (1973).", current_year=2026)
    if real:
        failures.append(f"false positive on a genuinely in-range US Reports citation - findings were: {real}")

    # A citation dated in the future is implausible regardless of reporter range.
    future = check_text("See Smith v Jones, 12 U.S. 456 (2099).", current_year=2026)
    if not any("future" in f for f in future):
        failures.append(f"did not flag a future-dated citation - findings were: {future}")

    if failures:
        print("SELFTEST FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("SELFTEST OK (all checks passed)")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("files", nargs="*", help="Markdown/text files to check")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()

    if args.selftest:
        sys.exit(selftest())

    if not args.files:
        p.error("supply at least one file, or --selftest")

    exit_code = 0
    for path in args.files:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        findings = check_text(text)
        print(f"--- {path} ---")
        if not findings:
            print("  no findings")
            continue
        for finding in findings:
            print(f"  {finding}")
        exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
