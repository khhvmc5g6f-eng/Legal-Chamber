#!/usr/bin/env python3
"""Deterministic citation-shape and house-style linter.

This is pattern matching, not legal judgement. It cannot tell you whether a
citation is real - only whether its shape matches a recognised pattern, and
whether the surrounding prose violates this project's house style (see
docs/STYLE_GUIDE.md). A citation that passes this linter still requires the
verification steps in docs/OPERATING_RULES.md before it can be relied upon.

Usage:
    python3 citation_lint.py path/to/file.md [path/to/other.md ...]
    python3 citation_lint.py --selftest
"""

import argparse
import re
import sys

EM_DASH = "—"

# Fixed phrases matched literally (word-boundary, case-insensitive). Kept as
# ONE list so a phrase added here is always enforced - a previous version had
# a second, separately-maintained regex list that silently drifted out of
# sync with this one.
STOCK_PHRASES = [
    "it is important to note",
    "it is worth noting",
    "it is crucial to",
    "in today's",
    "delve into",
    "delve deeper",
    "a nuanced approach",
    "a multifaceted",
    "robust framework",
]
# (readable label, compiled regex) pairs - the label is what gets reported in
# findings, since re.escape()'d patterns are unreadable (it backslash-escapes
# spaces too) and shouldn't leak into user-facing output.
STOCK_REGEXES = [(phrase, re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)) for phrase in STOCK_PHRASES]
# Structural patterns that need their own regex rather than a literal phrase:
STOCK_REGEXES += [
    ("not merely...but", re.compile(r"\bnot merely\b.{0,40}\bbut\b", re.IGNORECASE)),
    ("not only...but also", re.compile(r"\bnot only\b.{0,40}\bbut also\b", re.IGNORECASE)),
]

CITATION_PATTERNS = {
    # UK neutral citation - court code may be one word (UKSC, EWHC, UKUT) or
    # two (EWCA Civ, EWCA Crim, EWHC Comm), e.g. [2023] UKSC 12 / [2023] EWCA Civ 456.
    "uk_neutral": re.compile(r"\[\d{4}\]\s+[A-Z]{2,10}(?:\s+[A-Za-z]{2,10})?\s+\d+"),
    "eu_case": re.compile(r"[Cc]-\d+/\d{2,4}"),
    # US reporter citation - the reporter abbreviation itself often contains
    # digits (F.2d, F.3d, F.4th, F. Supp. 2d), so the character class must
    # allow them; volume/page stay digit-only either side of it. The trailing
    # parenthetical is "(Court Year)" for circuit/district citations (e.g.
    # "(9th Cir. 1969)") but just "(Year)" for the US Reports - allow any
    # non-paren text before the 4-digit year rather than requiring the year alone.
    "us_reporter": re.compile(r"\d+\s+[A-Z][A-Za-z0-9.'\s]{1,20}\d+\s*\([^()]*\d{4}\)"),
}


# Matches a fence of 3+ backticks and its closing fence of the SAME length,
# per CommonMark (a longer inner fence, e.g. 4 backticks wrapping a 3-backtick
# example, is not closed by the first 3-backtick run it contains).
FENCED_CODE_BLOCK = re.compile(r"(`{3,})[^\n]*\n.*?\n\1`*", re.DOTALL)


def _strip_fenced_code_blocks(text):
    """Remove fenced code blocks entirely for the prose-only checks (double
    space, stock phrasing, quotation-mark mixing) - ASCII diagrams and JSON
    examples legitimately use multi-space alignment that isn't a house-style
    violation, and counts here don't need to preserve position. Citation-shape
    detection and em-dash detection still run against the original,
    unstripped text."""
    return FENCED_CODE_BLOCK.sub(" ", text)


def lint_text(text):
    findings = []
    prose = _strip_fenced_code_blocks(text)

    em_dash_count = text.count(EM_DASH)
    if em_dash_count:
        findings.append(f"em_dash: {em_dash_count} occurrence(s) - house style prohibits em dashes (docs/STYLE_GUIDE.md)")

    # Mid-line only - leading indentation for nested markdown lists is not a
    # house-style violation, only an accidental double space within a sentence.
    double_space_count = len(re.findall(r"(?<=\S)[^\S\n]{2,}", prose))
    if double_space_count:
        findings.append(f"double_space: {double_space_count} occurrence(s)")

    straight_quotes = prose.count('"')
    curly_quotes = prose.count("“") + prose.count("”")
    if straight_quotes and curly_quotes:
        findings.append(f"mixed_quotation_marks: {straight_quotes} straight + {curly_quotes} curly - pick one convention")

    for label, rx in STOCK_REGEXES:
        matches = rx.findall(prose)
        if matches:
            findings.append(f"stock_phrase '{label}': {len(matches)} occurrence(s)")

    citations_found = {}
    for name, rx in CITATION_PATTERNS.items():
        matches = rx.findall(text)
        if matches:
            citations_found[name] = matches

    return findings, citations_found


def lint_file(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    findings, citations = lint_text(text)
    return findings, citations


def selftest():
    failures = []

    bad_text = "This is bad — it has an em dash. It is important to note that this is not merely wrong but also flagged."
    findings, _ = lint_text(bad_text)
    joined = " ".join(findings)
    if "em_dash" not in joined:
        failures.append("did not flag em dash in bad_text")
    if "it is important to note" not in joined.lower():
        failures.append("did not flag stock phrase in bad_text")
    if "not merely" not in joined.lower():
        failures.append("did not flag 'not merely...but' construction")

    good_text = "This is a clean sentence with no house-style violations at all."
    findings, _ = lint_text(good_text)
    if findings:
        failures.append(f"false positive(s) on clean text: {findings}")

    citation_text = "See Smith v Jones [2023] UKSC 12 and Case C-45/21."
    _, citations = lint_text(citation_text)
    if "uk_neutral" not in citations:
        failures.append("did not detect UK neutral citation shape")
    if "eu_case" not in citations:
        failures.append("did not detect EU case citation shape")

    if failures:
        print("SELFTEST FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("SELFTEST OK (all checks passed)")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("files", nargs="*")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()

    if args.selftest:
        sys.exit(selftest())

    if not args.files:
        p.error("supply at least one file, or --selftest")

    exit_code = 0
    for path in args.files:
        findings, citations = lint_file(path)
        print(f"--- {path} ---")
        if citations:
            for name, matches in citations.items():
                print(f"  citation shapes ({name}): {matches}")
        if findings:
            exit_code = 1
            for f in findings:
                print(f"  FLAG: {f}")
        if not findings and not citations:
            print("  no findings")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
