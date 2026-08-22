#!/usr/bin/env python3
"""Deterministic claimed-vs-persisted output checker for a matter workspace.

A live stress test (2026-08-22, see DEFECT_REGISTER.md D-03/D-08) found
matters where a stage's own summary claimed a document existed - a case
theory, a completed essay, a full hearing history - that was never actually
written to matters/<ID>/. The root cause (no agent role had Write access)
is fixed, but nothing deterministic backstops the instruction-level check
in agents/quality/ROLE.md. This script is that backstop: it maps a matter's
own declared `status` (schemas/matter.schema.json) to the workspace
subdirectories that status implies should be non-empty, and flags any that
are missing or empty. It is arithmetic over the filesystem, not legal
judgement - it cannot tell you whether a file's CONTENT is any good, only
whether something claiming to exist actually does.

Usage:
    python3 verify_matter_persistence.py matters/MATTER-ID
    python3 verify_matter_persistence.py --selftest
"""

import argparse
import json
import os
import sys

STANDARD_SUBDIRS = [
    "intake", "facts", "evidence", "chronology", "issues", "research",
    "authorities", "drafts", "opposition", "moot", "procedure", "costs",
    "prospects", "final",
]

# Matter lifecycle status (workflows/matter-lifecycle.md) -> subdirectories
# that status implies must already have at least one real file in them.
# Cumulative: a later status implies everything an earlier one did, plus more.
STATUS_EXPECTATIONS = {
    "INTAKE": ["intake"],
    "RESEARCHING": ["intake", "facts", "research"],
    "DRAFTING": ["intake", "facts", "research", "drafts"],
    "REVIEWING": ["intake", "facts", "research", "drafts"],
    "ADVERSARIAL_REVIEW": ["intake", "facts", "research", "drafts", "opposition"],
    "HUMAN_REVIEW_PENDING": ["intake", "facts", "research", "drafts", "final"],
    "VERIFIED_FOR_FILING": ["intake", "facts", "research", "drafts", "final"],
    "CLOSED": ["intake", "final"],
}


def _dir_is_empty(path):
    if not os.path.isdir(path):
        return True
    for _root, _dirs, files in os.walk(path):
        if files:
            return False
    return True


def _read_matter_status(matter_dir):
    candidates = [
        os.path.join(matter_dir, "intake", "matter.json"),
        os.path.join(matter_dir, "matter.json"),
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                with open(path, encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, dict) and "status" in data:
                    return data["status"]
            except (OSError, json.JSONDecodeError):
                continue
    return None


def verify_matter(matter_dir):
    """Returns (findings, status) - findings is a list of human-readable strings."""
    findings = []

    if not os.path.isdir(matter_dir):
        return [f"{matter_dir} does not exist"], None

    status = _read_matter_status(matter_dir)

    present_but_empty = []
    for sub in STANDARD_SUBDIRS:
        sub_path = os.path.join(matter_dir, sub)
        if os.path.isdir(sub_path) and _dir_is_empty(sub_path):
            present_but_empty.append(sub)
    for sub in present_but_empty:
        findings.append(f"{sub}/ exists but is empty - a stage created the directory without writing anything into it")

    if status:
        expected = STATUS_EXPECTATIONS.get(status)
        if expected is None:
            findings.append(f"matter status \"{status}\" is not a recognised value from matter.schema.json's status enum - cannot check expectations for it")
        else:
            for sub in expected:
                sub_path = os.path.join(matter_dir, sub)
                if not os.path.isdir(sub_path):
                    findings.append(f"status is \"{status}\", which implies {sub}/ should exist, but the directory is entirely absent")
                elif _dir_is_empty(sub_path):
                    findings.append(f"status is \"{status}\", which implies {sub}/ should have real content, but it is empty")
    else:
        findings.append("no readable status found in intake/matter.json - cannot check status-implied expectations, only emptiness of existing directories")

    return findings, status


def selftest():
    import tempfile
    failures = []

    with tempfile.TemporaryDirectory() as tmp:
        matter_dir = os.path.join(tmp, "MATTER-001")
        os.makedirs(os.path.join(matter_dir, "intake"))
        os.makedirs(os.path.join(matter_dir, "facts"))
        os.makedirs(os.path.join(matter_dir, "drafts"))  # deliberately left empty
        with open(os.path.join(matter_dir, "intake", "matter.json"), "w") as f:
            json.dump({"matter_id": "MATTER-001", "status": "DRAFTING"}, f)
        with open(os.path.join(matter_dir, "facts", "facts.json"), "w") as f:
            json.dump([{"fact_id": "F-001"}], f)

        findings, status = verify_matter(matter_dir)
        if status != "DRAFTING":
            failures.append(f"did not read status correctly, got {status}")
        if not any("drafts/" in f and "empty" in f for f in findings):
            failures.append(f"did not flag the empty drafts/ directory implied by DRAFTING status - findings were: {findings}")
        if not any("research" in f for f in findings):
            failures.append(f"did not flag missing research/ implied by DRAFTING status - findings were: {findings}")
        if any("intake/" in f and "empty" in f for f in findings) or any("facts/" in f and "empty" in f for f in findings):
            failures.append(f"false positive on intake/ or facts/, both of which have real content - findings were: {findings}")

        # a matter with no status file at all should still report, not crash
        matter_dir2 = os.path.join(tmp, "MATTER-002")
        os.makedirs(matter_dir2)
        findings2, status2 = verify_matter(matter_dir2)
        if status2 is not None:
            failures.append("expected no status for a matter with no matter.json")
        if not findings2:
            failures.append("expected at least the 'no readable status' finding for a status-less matter")

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

    findings, status = verify_matter(args.matter_dir)
    print(f"matter: {args.matter_dir}")
    print(f"declared status: {status or 'UNKNOWN'}")
    if findings:
        print(f"FINDINGS ({len(findings)}):")
        for f in findings:
            print(f"  - {f}")
        sys.exit(1)
    print("No claimed-but-missing outputs found for this matter's declared status.")


if __name__ == "__main__":
    main()
