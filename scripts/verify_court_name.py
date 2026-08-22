#!/usr/bin/env python3
"""Deterministic US court-name/abbreviation lookup.

This is name recognition, not legal judgement. It tells you whether a court
name or abbreviation is a real, known one in the vendored table - it says
nothing about whether a specific case was actually decided by that court,
which still requires CourtListener or an equivalent primary source, per
docs/OPERATING_RULES.md. Use it as a sanity check before writing a `court`
field into an authority.schema.json entry, or when a court name appears in
drafted text and you want to confirm it's not a garbled/invented one.

US-only (courts-db's coverage): don't use this to check a UK/EU/other
jurisdiction's court name - it will report "not found" for every one of
those, which is a coverage gap, not evidence the name is wrong.

Usage:
    python3 verify_court_name.py "Court of Appeals for the Ninth Circuit"
    python3 verify_court_name.py "S.D.N.Y." "Alabama Circuit Courts"
    python3 verify_court_name.py --selftest
"""

import argparse
import json
import re
import sys
from pathlib import Path

_COURTS_DATA_PATH = Path(__file__).resolve().parent / "data" / "courts.json"
_courts_cache = None


def _normalize(raw):
    """Collapse whitespace, lowercase, and strip one trailing period - court
    abbreviations are written interchangeably with or without a final full
    stop ("S.D.N.Y" and "S.D.N.Y." both appear in real use), and courts-db's
    own stored literal doesn't consistently include one, so an exact-match
    lookup that's sensitive to it misses genuine hits. Does not strip
    internal periods (S.D.N.Y's own periods are untouched) - only a single
    trailing one."""
    normalized = re.sub(r"\s+", " ", raw.strip()).lower()
    return normalized[:-1] if normalized.endswith(".") else normalized


def load_courts():
    """Lazily load and cache the vendored courts-db table (list of court
    records). Returns an empty list (rather than raising) if the data file
    is missing, so a stale checkout degrades to "nothing found" instead of
    crashing."""
    global _courts_cache
    if _courts_cache is not None:
        return _courts_cache
    try:
        with open(_COURTS_DATA_PATH, "r", encoding="utf-8") as f:
            _courts_cache = json.load(f)
    except (OSError, json.JSONDecodeError):
        _courts_cache = []
    return _courts_cache


# Characters that never appear in a literal US court name but are exactly
# the ones courts-db's genuine regex entries use for their own machinery -
# quantifiers (? * + {n,m}), alternation (|), character classes ([ ]),
# escape sequences (\), and template-variable interpolation (${...}, the $
# alone is enough to catch it). Deliberately NOT included: '.' and '(' ')'
# - both are extremely common in real, literal court abbreviations
# ("S.D.N.Y.", "New York Supreme Court (other)"), and an earlier version of
# this check treated ANY period or parenthesis as a regex signal, silently
# dropping dozens of genuine literal abbreviations from lookup - including
# the exact example in this file's own usage docstring below. Validated
# against the full vendored table: with this narrower character set, zero
# of the ~4,150 entries kept as "literal" still contain a wildcard (.*),
# optional-comma (,?), or brace-quantifier ({n,m}) construct.
_REGEX_METACHAR = re.compile(r"[?*+{}|\[\]\\$]")


def _candidate_names(court):
    """Every string this court record could plausibly be looked up by:
    its full name, its short abbreviation, and every literal string in its
    regex list (courts-db's regex entries are almost always plain literal
    alternatives, not real patterns with metacharacters - a literal
    match is normalized and used as-is; an entry containing a real regex
    metacharacter, per _REGEX_METACHAR above, is skipped for exact lookup
    rather than mis-treated as a plain string)."""
    names = []
    if court.get("name"):
        names.append(court["name"])
    if court.get("name_abbreviation"):
        names.append(court["name_abbreviation"])
    for pattern in court.get("regex") or []:
        if not _REGEX_METACHAR.search(pattern):
            names.append(pattern)
    return names


def lookup_court(name):
    """Return the matching court record dict, or None. Exact match
    (case/whitespace-insensitive) against name, name_abbreviation, or any
    plain-literal regex alternative - not a fuzzy/partial match, since a
    partial match on a court name is exactly the kind of false confidence
    this tool exists to avoid."""
    target = _normalize(name)
    for court in load_courts():
        for candidate in _candidate_names(court):
            if _normalize(candidate) == target:
                return court
    return None


def selftest():
    failures = []

    courts = load_courts()
    if not courts:
        failures.append("courts-db data file failed to load (scripts/data/courts.json)")
    elif len(courts) < 1000:
        failures.append(f"suspiciously few court records loaded: {len(courts)}")

    known_examples = ["Alabama Circuit Courts", "Supreme Court of the United States"]
    for name in known_examples:
        if lookup_court(name) is None:
            failures.append(f"known court name not found: {name!r}")

    if lookup_court("The Made Up Court of Nowhere") is not None:
        failures.append("fabricated court name incorrectly matched")

    # A literal abbreviation containing a period or parenthesis must still
    # be found - an earlier version of _REGEX_METACHAR treated '.' and '('/')'
    # as regex signals and silently dropped every such literal, including
    # this exact example from the tool's own usage docstring.
    if lookup_court("S.D.N.Y") is None:
        failures.append("literal abbreviation containing periods not found (S.D.N.Y)")
    if lookup_court("S.D.N.Y.") is None:
        failures.append("trailing-period variant not found (S.D.N.Y.) - normalization regression")
    if lookup_court("New York Supreme Court (other)") is None:
        failures.append("literal name containing parentheses not found")

    # A genuine regex entry (containing courts-db template variables or
    # quantifiers) must still be correctly excluded from literal lookup,
    # not accidentally treated as a literal string after the metachar fix.
    genuinely_regex_only = "${usa} (Circuit )?(Courts? )?(of Appeals?(,|.)? ?)?(for the )?(Ninth,? )(Circuit)?"
    if lookup_court(genuinely_regex_only) is not None:
        failures.append("a genuine regex pattern was matched as if it were a literal name")

    if lookup_court("alabama circuit courts") is None:
        failures.append("lookup should be case-insensitive")

    if failures:
        print("SELFTEST FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("SELFTEST OK (all checks passed)")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("names", nargs="*")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()

    if args.selftest:
        sys.exit(selftest())

    if not args.names:
        p.error("supply at least one court name, or --selftest")

    exit_code = 0
    for name in args.names:
        court = lookup_court(name)
        if court:
            print(
                f"FOUND: {name!r} -> {court.get('name')} (id={court.get('id')}, "
                f"jurisdiction={court.get('jurisdiction', 'n/a')}, system={court.get('system', 'n/a')}, "
                f"level={court.get('level') or 'n/a'})"
            )
        else:
            print(f"NOT FOUND: {name!r} - not a recognised US court name/abbreviation in this table (US-only coverage; a non-US court will always report this)")
            exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
