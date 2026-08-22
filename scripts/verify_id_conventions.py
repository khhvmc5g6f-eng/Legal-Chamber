#!/usr/bin/env python3
"""Deterministic ID-convention checker for a matter workspace, per docs/ID_CONVENTIONS.md.

That file fixes a default prefix and zero-padding convention per record type
(F-001, EX-014, AUTH-007, and so on) specifically because a long-running
matter worked across multiple sessions or agents will otherwise produce
colliding or malformed IDs with nothing to catch it. Nothing previously
checked that the convention was actually followed - this is a plain regex
and set-membership check, not legal judgement, so it belongs here per
CLAUDE.md's "deterministic tools first" principle.

Checks two things per record type, matter-wide (across every file that type's
records live in):
  1. FORMAT - every ID matches its documented prefix and zero-padding shape.
  2. DUPLICATES - no ID is reused by two different records of the same type.

A matter that has adopted its own convention instead (docs/ID_CONVENTIONS.md
allows this, stated once in that matter's intake/ record) is out of scope for
this script - it only checks the documented default.

Usage:
    python3 verify_id_conventions.py matters/MATTER-ID
    python3 verify_id_conventions.py --selftest
"""

import argparse
import glob
import json
import os
import re
import sys

# (id field name, glob patterns under matter_dir, expected regex, human label)
# Hearing IDs are documented as H-1 through H-5 with no stated zero-padding
# requirement (docs/ID_CONVENTIONS.md's own example), so they get a looser
# pattern than the zero-padded-to-3 rule that applies to every other type.
ID_RULES = [
    ("fact_id", ["facts/facts.json", "facts.json"], re.compile(r"^F-\d{3,}$"), "Fact"),
    ("evidence_id", ["evidence/evidence.json", "facts/evidence.json"], re.compile(r"^EX-\d{3,}$"), "Evidence"),
    ("authority_id", ["authorities/authorities.json"], re.compile(r"^AUTH-\d{3,}$"), "Authority"),
    ("issue_id", ["issues/issues.json"], re.compile(r"^ISS-\d{3,}$"), "Issue"),
    ("deadline_id", ["procedure/deadlines.json", "deadlines/deadlines.json"], re.compile(r"^DL-\d{3,}$"), "Deadline"),
    ("event_id", ["chronology/chronology.json"], re.compile(r"^CHR-\d{3,}$"), "Chronology event"),
    ("conclusion_id", ["**/conclusions.json"], re.compile(r"^CONC-\d{3,}$"), "Conclusion"),
    ("draft_id", ["**/drafts.json"], re.compile(r"^DRAFT-\d{3,}$"), "Draft"),
    ("hearing_id", ["moot/hearing-*.json", "**/hearing-*.json"], re.compile(r"^H-\d+$"), "Hearing"),
]


def _iter_records(matter_dir, globs):
    for pattern in globs:
        for path in glob.glob(os.path.join(matter_dir, pattern), recursive=True):
            try:
                with open(path, encoding="utf-8") as f:
                    data = json.load(f)
            except (OSError, json.JSONDecodeError):
                continue
            if isinstance(data, list):
                items = data
            elif isinstance(data, dict):
                items = None
                for v in data.values():
                    if isinstance(v, list):
                        items = v
                        break
                if items is None and any(k.endswith("_id") for k in data):
                    items = [data]  # a single-object record file, e.g. one hearing per file
                if items is None:
                    items = []
            else:
                items = []
            for item in items:
                if isinstance(item, dict):
                    yield path, item


def verify_matter(matter_dir):
    """Returns (findings, checked_count)."""
    if not os.path.isdir(matter_dir):
        return [f"{matter_dir} does not exist"], 0

    findings = []
    checked = 0

    for field, globs, pattern, label in ID_RULES:
        seen = {}  # id -> path where it was first seen
        for path, record in _iter_records(matter_dir, globs):
            if field not in record:
                continue
            record_id = str(record[field])
            checked += 1
            if not pattern.match(record_id):
                findings.append(f"{path}: {label} id {record_id!r} does not match the documented format {pattern.pattern}")
            if record_id in seen:
                findings.append(f"{path}: {label} id {record_id!r} is a duplicate - already used in {seen[record_id]}")
            else:
                seen[record_id] = path

    return findings, checked


def selftest():
    import tempfile

    failures = []

    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(os.path.join(tmp, "facts"))
        with open(os.path.join(tmp, "facts", "facts.json"), "w") as f:
            json.dump(
                [
                    {"fact_id": "F-001", "proposition": "well-formed"},
                    {"fact_id": "F-1", "proposition": "not zero-padded"},
                    {"fact_id": "FACT-002", "proposition": "wrong prefix"},
                    {"fact_id": "F-003", "proposition": "first of a duplicate pair"},
                    {"fact_id": "F-003", "proposition": "second of a duplicate pair"},
                ],
                f,
            )

        findings, checked = verify_matter(tmp)

        if checked != 5:
            failures.append(f"expected 5 records checked, got {checked}")
        if not any("F-1" in f and "format" in f for f in findings):
            failures.append(f"did not flag non-zero-padded F-1 - findings were: {findings}")
        if not any("FACT-002" in f for f in findings):
            failures.append(f"did not flag wrong-prefix FACT-002 - findings were: {findings}")
        if not any("F-003" in f and "duplicate" in f for f in findings):
            failures.append(f"did not flag duplicate F-003 - findings were: {findings}")
        if any("F-001" in f for f in findings):
            failures.append(f"false positive on well-formed, unique F-001 - findings were: {findings}")

    nonexistent = os.path.join(tempfile.gettempdir(), "verify-id-conventions-selftest-does-not-exist")
    findings, checked = verify_matter(nonexistent)
    if not findings:
        failures.append("nonexistent matter directory silently reported clean - should be a hard failure")

    if failures:
        print("SELFTEST FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("SELFTEST OK (all checks passed)")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("matter_dir", nargs="?", help="Path to a matters/MATTER-ID directory")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()

    if args.selftest:
        sys.exit(selftest())

    if not args.matter_dir:
        p.error("supply a matter directory, or --selftest")

    findings, checked = verify_matter(args.matter_dir)
    print(f"Checked {checked} IDs in {args.matter_dir}")
    if findings:
        print(f"ID CONVENTION ISSUES ({len(findings)}):")
        for f in findings:
            print(f"  - {f}")
        sys.exit(1)
    print("No ID convention issues found.")


if __name__ == "__main__":
    main()
