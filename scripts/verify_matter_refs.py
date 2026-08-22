#!/usr/bin/env python3
"""Deterministic cross-reference integrity checker for a matter workspace.

Legal Chamber's schemas cross-reference each other by ID string (a chronology
event's fact_ids, an issue's fact_ids_required/evidence_available_ids, a
draft's change_log authority_id, and so on - see docs/ID_CONVENTIONS.md).
Nothing previously checked that those IDs actually resolve to a real record
in the matter - a stress test found this gap directly. This is arithmetic
(does ID X appear as a real record elsewhere), not legal judgement, so it
belongs here rather than in a skill's prose instructions per CLAUDE.md's
"deterministic tools first" principle.

Usage:
    python3 verify_matter_refs.py matters/MATTER-ID
    python3 verify_matter_refs.py --selftest
"""

import argparse
import glob
import json
import os
import sys

# Which files under a matter directory hold which record type, and which
# fields on OTHER records are expected to point at that record type's IDs.
RECORD_GLOBS = {
    "fact": ["facts/facts.json"],
    "evidence": ["evidence/evidence.json", "facts/evidence.json"],
    "chronology": ["chronology/chronology.json"],
    "issue": ["issues/issues.json"],
    "authority": ["authorities/authorities.json"],
}

REFERENCE_FIELDS = [
    # (source file glob pattern, field name, target record type)
    ("chronology/chronology.json", "fact_ids", "fact"),
    ("chronology/chronology.json", "evidence_ids", "evidence"),
    ("issues/issues.json", "authority_ids", "authority"),
    ("fact*.json", "evidence_ids", "evidence"),
    ("fact*.json", "contrary_evidence_ids", "evidence"),
]


def _load_records(matter_dir, globs):
    """Collect every object's own id-like field value from the given files."""
    ids = set()
    for pattern in globs:
        for path in glob.glob(os.path.join(matter_dir, pattern)):
            try:
                with open(path, encoding="utf-8") as f:
                    data = json.load(f)
            except (OSError, json.JSONDecodeError):
                continue
            items = data if isinstance(data, list) else data.get("items", data.get("facts", data.get("evidence", data.get("events", data.get("issues", data.get("authorities", []))))))
            if not isinstance(items, list):
                continue
            for item in items:
                if not isinstance(item, dict):
                    continue
                for key in ("fact_id", "evidence_id", "event_id", "issue_id", "authority_id"):
                    if key in item:
                        ids.add(str(item[key]))
    return ids


def _collect_referenced_ids(matter_dir, field_pattern, field_name):
    referenced = []
    for path in glob.glob(os.path.join(matter_dir, "**", field_pattern), recursive=True):
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError):
            continue
        items = data if isinstance(data, list) else data.get("items", [])
        if isinstance(data, dict) and not items:
            for v in data.values():
                if isinstance(v, list):
                    items = v
                    break
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            values = item.get(field_name)
            if isinstance(values, list):
                for v in values:
                    referenced.append((path, field_name, str(v)))
            elif values:
                referenced.append((path, field_name, str(values)))
    return referenced


def verify_matter(matter_dir):
    """Returns (findings, checked_count) - findings is a list of broken-reference strings."""
    known_ids = {
        rtype: _load_records(matter_dir, globs) for rtype, globs in RECORD_GLOBS.items()
    }
    all_known = set()
    for ids in known_ids.values():
        all_known |= ids

    findings = []
    checked = 0
    for pattern, field_name, target_type in REFERENCE_FIELDS:
        for path, field, ref_id in _collect_referenced_ids(matter_dir, pattern, field_name):
            checked += 1
            if ref_id not in all_known:
                findings.append(f"{path}: {field}=\"{ref_id}\" does not match any known {target_type} record id in this matter")
    return findings, checked


def selftest():
    import tempfile
    failures = []

    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(os.path.join(tmp, "facts"))
        os.makedirs(os.path.join(tmp, "chronology"))
        with open(os.path.join(tmp, "facts", "facts.json"), "w") as f:
            json.dump([{"fact_id": "F-001", "proposition": "x"}], f)
        with open(os.path.join(tmp, "chronology", "chronology.json"), "w") as f:
            json.dump([{"event_id": "CHR-001", "description": "y", "fact_ids": ["F-001", "F-999"]}], f)

        findings, checked = verify_matter(tmp)
        if checked == 0:
            failures.append("selftest did not check any references - harness broken")
        if not any("F-999" in f for f in findings):
            failures.append(f"did not flag the dangling reference to F-999 - findings were: {findings}")
        if any("F-001" in f for f in findings):
            failures.append(f"false positive on the valid reference F-001 - findings were: {findings}")

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
    print(f"Checked {checked} cross-references in {args.matter_dir}")
    if findings:
        print(f"BROKEN ({len(findings)}):")
        for f in findings:
            print(f"  - {f}")
        sys.exit(1)
    print("No broken cross-references found.")


if __name__ == "__main__":
    main()
