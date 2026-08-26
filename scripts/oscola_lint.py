#!/usr/bin/env python3
"""Lint deterministic OSCOLA 5 citation-format mistakes.

This checks text shape only. It cannot establish that an authority exists,
is current, or supports the proposition for which it is cited. Those
questions still require the live primary-source verification workflow in
docs/OPERATING_RULES.md.

Usage:
    python3 scripts/oscola_lint.py draft.md [other.md ...]
    python3 scripts/oscola_lint.py --json draft.md
    python3 scripts/oscola_lint.py --selftest
"""

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    column: int
    rule: str
    message: str
    excerpt: str


@dataclass(frozen=True)
class Rule:
    code: str
    pattern: re.Pattern
    message: str


COURT_CODE = (
    r"(?:UKSC|UKPC|UKUT|UKFTT|EWCA\s+(?:Civ|Crim)|"
    r"EWHC(?:\s+[A-Za-z]{2,10})?|EWCOP|EWFC)"
)

RULES = (
    Rule(
        "OSC001",
        re.compile(r"\b[A-Z][A-Za-z'’-]+\s+v\.\s+[A-Z][A-Za-z'’-]+"),
        "Use 'v' without a full stop in an English case name.",
    ),
    Rule(
        "OSC002",
        re.compile(rf"(?<!\[)\b(?:19|20)\d{{2}}\s+{COURT_CODE}\s+\d+\b"),
        "Put the year of a UK neutral citation in square brackets.",
    ),
    Rule(
        "OSC003",
        re.compile(
            r"\b[A-Z][A-Za-z'’& -]+\s+Act\s+\d{4},?\s+sections?\s+\d",
            re.IGNORECASE,
        ),
        "Use 's' for one section or 'ss' for multiple sections.",
    ),
    Rule(
        "OSC004",
        re.compile(
            r"\b[A-Z][A-Za-z'’& -]+\s+(?:Regulations|Order|Rules)\s+"
            r"\d{4},\s*(?!SI\b)\d{4}/\d+\b"
        ),
        "Prefix a statutory instrument number with 'SI'.",
    ),
    Rule(
        "OSC005",
        re.compile(
            rf"\[\d{{4}}\]\s+{COURT_CODE}\s+\d+[^\n]{{0,45}}"
            r"\b(?:at\s+)?(?:para\.?|p\.?)\s*\d+",
            re.IGNORECASE,
        ),
        "Use square brackets for a case paragraph pinpoint, for example [42].",
    ),
    Rule(
        "OSC006",
        re.compile(
            r"(?:\[\d{4}\]\s+\d+\s+[A-Z][A-Za-z ]+\s+\d+|"
            r"\([^)]*\d{4}\))\s*,?\s*pp?\.\s*\d+",
            re.IGNORECASE,
        ),
        "Omit 'p' or 'pp' before an OSCOLA pinpoint.",
    ),
    Rule(
        "OSC007",
        re.compile(r"\b(?:op\.?\s+cit\.?|loc\.?\s+cit\.?)\b", re.IGNORECASE),
        "Use an OSCOLA cross-citation or 'ibid' instead of 'op cit' or 'loc cit'.",
    ),
    Rule(
        "OSC008",
        re.compile(
            r"\b[A-Z][A-Za-z'’.-]+(?:\s+[A-Z][A-Za-z'’.-]+)*,?\s+"
            r'\"[^\"\n]+\"\s+[\[(]\d{4}[\])]'
        ),
        "Use single quotation marks around an article or chapter title.",
    ),
    Rule(
        "OSC009",
        re.compile(r"(?<![<(])https?://[^\s>)]+"),
        "Enclose a standalone web address in angle brackets and add an accessed date where OSCOLA requires one.",
    ),
)

FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
FOOTNOTE = re.compile(r"^\s*(?:\[\^[^]]+\]:|\d+\.)\s+(.+)$")


def lint_text(text, path="<text>"):
    findings = []
    in_fence = False
    fence_char = None
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        fence = FENCE.match(raw_line)
        if fence:
            marker = fence.group(1)[0]
            if not in_fence:
                in_fence, fence_char = True, marker
            elif marker == fence_char:
                in_fence, fence_char = False, None
            continue
        if in_fence:
            continue

        for rule in RULES:
            for match in rule.pattern.finditer(raw_line):
                findings.append(
                    Finding(
                        path=str(path),
                        line=line_number,
                        column=match.start() + 1,
                        rule=rule.code,
                        message=rule.message,
                        excerpt=match.group(0).strip(),
                    )
                )

        footnote = FOOTNOTE.match(raw_line)
        if footnote:
            body = footnote.group(1).rstrip()
            if body and not re.search(r"[.!?]['’\"]?$", body):
                findings.append(
                    Finding(
                        path=str(path),
                        line=line_number,
                        column=len(raw_line.rstrip()),
                        rule="OSC010",
                        message="End an OSCOLA footnote with punctuation.",
                        excerpt=body[-80:],
                    )
                )
    return findings


def lint_file(path):
    return lint_text(Path(path).read_text(encoding="utf-8"), path=path)


def selftest():
    failures = []
    bad = """Smith v. Jones 2023 UKSC 12
Roe v Bloggs [2024] EWCA Civ 8, para 4
Data Protection Act 2018, section 4
Example Regulations 2024, 2024/123
1. A Smith, \"Useful Article\" (2025) 84 MLR 120
[^2]: See op cit
```
Fake v. Code 2024 UKSC 7
```
"""
    found = lint_text(bad)
    codes = {finding.rule for finding in found}
    expected = {
        "OSC001",
        "OSC002",
        "OSC003",
        "OSC004",
        "OSC005",
        "OSC007",
        "OSC008",
        "OSC010",
    }
    missing = expected - codes
    if missing:
        failures.append(f"missing expected rules: {sorted(missing)}")
    if any(f.excerpt == "Fake v. Code 2024 UKSC 7" for f in found):
        failures.append("linted content inside a fenced code block")

    good = """*Smith v Jones* [2023] UKSC 12, [4].
Data Protection Act 2018, s 4.
Example Regulations 2024, SI 2024/123.
1. A Smith, ‘Useful Article’ (2025) 84 MLR 120.
[^2]: *Smith* (n 1) [8].
"""
    good_findings = lint_text(good)
    if good_findings:
        failures.append(f"false positives on valid examples: {good_findings}")

    if failures:
        print("SELFTEST FAILED:")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("SELFTEST OK (OSCOLA 5 shape checks passed)")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("files", nargs="*")
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()

    if args.selftest:
        return selftest()
    if not args.files:
        parser.error("supply at least one file, or --selftest")

    findings = []
    failed_to_read = []
    for path in args.files:
        try:
            findings.extend(lint_file(path))
        except (OSError, UnicodeError) as error:
            failed_to_read.append({"path": path, "error": str(error)})

    if args.as_json:
        print(
            json.dumps(
                {
                    "version": "oscola-5",
                    "findings": [asdict(finding) for finding in findings],
                    "errors": failed_to_read,
                },
                indent=2,
            )
        )
    else:
        for finding in findings:
            print(
                f"{finding.path}:{finding.line}:{finding.column}: "
                f"{finding.rule} {finding.message}"
            )
            print(f"    {finding.excerpt}")
        for error in failed_to_read:
            print(f"{error['path']}: ERROR {error['error']}", file=sys.stderr)
        if not findings and not failed_to_read:
            print("OSCOLA lint passed: no deterministic format issues found.")
    return 1 if findings or failed_to_read else 0


if __name__ == "__main__":
    sys.exit(main())
