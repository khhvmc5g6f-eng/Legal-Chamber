#!/usr/bin/env python3
"""Deterministic cross-matter conflict-of-interest name matcher.

`schemas/matter.schema.json`'s `conflict_check` field records each matter's
parties, related entities, and opposing counsel - and D-09 in
`DEFECT_REGISTER.md` found a real matter proceed to substantive work with
`conflict_check.cleared: false` and both parties unnamed, because nothing
actually gated on it. Even where a single matter's own gate is respected,
nothing has ever checked a name against every OTHER matter this workspace
holds - the actual conflict-of-interest question ("have we acted against
this party before, or for them in a matter now adverse to them"). This is
exact and near-exact name matching across files, not legal judgement about
whether a match is a real conflict, so it belongs here per CLAUDE.md's
"deterministic tools first" principle. A name match is a flag to review, not
an automatic finding of a disqualifying conflict - only a human (or the
matter's own `cleared_by`) can actually clear one.

Usage:
    python3 check_conflicts.py matters/
    python3 check_conflicts.py matters/ --candidate "Jane Doe" "Acme Corp"
    python3 check_conflicts.py --selftest
"""

import argparse
import glob
import json
import os
import re
import sys

_NAME_ROLE_FIELDS = ("parties", "related_entities", "opposing_counsel")


def _normalize_name(raw):
    """Lowercase, collapse whitespace, strip common corporate suffixes and
    punctuation, so "Acme Corp." and "ACME CORP" are recognised as the same
    name without needing exact byte-for-byte equality - real conflict checks
    fail on exactly this kind of cosmetic mismatch if done naively."""
    name = raw.strip().lower()
    name = re.sub(r"[.,]", "", name)
    name = re.sub(r"\s+", " ", name)
    name = re.sub(r"\b(ltd|limited|llc|inc|incorporated|plc|corp|corporation|llp|co)\b\.?$", "", name).strip()
    return name


def _iter_matter_names(matters_root):
    """Yields (matter_id, role, normalized_name, original_name, matter_json_path)
    for every name recorded in every matter's conflict_check block."""
    for path in glob.glob(os.path.join(matters_root, "*", "intake", "matter.json")):
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError):
            continue
        matter_id = data.get("matter_id") or os.path.basename(os.path.dirname(os.path.dirname(path)))
        conflict_check = data.get("conflict_check")
        if not isinstance(conflict_check, dict):
            continue
        for role in _NAME_ROLE_FIELDS:
            for name in conflict_check.get(role, []) or []:
                if not isinstance(name, str) or not name.strip():
                    continue
                yield matter_id, role, _normalize_name(name), name, path


def find_cross_matter_matches(matters_root):
    """Returns a list of finding dicts, one per normalised name that appears
    in more than one distinct matter's conflict_check block."""
    by_name = {}
    for matter_id, role, norm, original, path in _iter_matter_names(matters_root):
        by_name.setdefault(norm, []).append({"matter_id": matter_id, "role": role, "name": original, "path": path})

    findings = []
    for norm, occurrences in by_name.items():
        matter_ids = {o["matter_id"] for o in occurrences}
        if len(matter_ids) > 1:
            findings.append({"normalized_name": norm, "occurrences": occurrences})
    return findings


def check_candidate(matters_root, candidate_names):
    """Returns a list of finding dicts for a proposed new matter's own
    candidate party/entity names, checked against every EXISTING matter -
    the actual pre-engagement conflict check, before a new matter directory
    even exists yet."""
    existing = list(_iter_matter_names(matters_root))
    findings = []
    for candidate in candidate_names:
        norm = _normalize_name(candidate)
        hits = [
            {"matter_id": matter_id, "role": role, "name": original, "path": path}
            for matter_id, role, existing_norm, original, path in existing
            if existing_norm == norm
        ]
        if hits:
            findings.append({"candidate": candidate, "normalized_name": norm, "occurrences": hits})
    return findings


def selftest():
    import tempfile

    failures = []

    with tempfile.TemporaryDirectory() as tmp:
        for matter_id, party in [("M-A", "Acme Corp"), ("M-B", "ACME CORP."), ("M-C", "Unrelated Party Ltd")]:
            d = os.path.join(tmp, matter_id, "intake")
            os.makedirs(d)
            with open(os.path.join(d, "matter.json"), "w") as f:
                json.dump(
                    {
                        "matter_id": matter_id,
                        "conflict_check": {"parties": [party], "related_entities": [], "opposing_counsel": [], "cleared": False},
                    },
                    f,
                )

        findings = find_cross_matter_matches(tmp)

        if len(findings) != 1:
            failures.append(f"expected exactly 1 cross-matter name match (Acme Corp vs ACME CORP.), got {len(findings)}: {findings}")
        else:
            matter_ids = {o["matter_id"] for o in findings[0]["occurrences"]}
            if matter_ids != {"M-A", "M-B"}:
                failures.append(f"cross-matter match should span M-A and M-B only, got {matter_ids}")

        if any("unrelated" in f["normalized_name"] for f in findings):
            failures.append("false-matched the genuinely unrelated party into a conflict")

        # Corporate-suffix normalisation itself, isolated from the cross-matter logic above.
        if _normalize_name("Acme Corp") != _normalize_name("ACME CORP."):
            failures.append("corporate-suffix/casing normalisation did not treat 'Acme Corp' and 'ACME CORP.' as equal")

        # --candidate mode: a proposed new matter's names checked against existing matters.
        candidate_findings = check_candidate(tmp, ["Acme Corporation", "Someone Else Entirely"])
        if len(candidate_findings) != 1 or candidate_findings[0]["candidate"] != "Acme Corporation":
            failures.append(f"--candidate mode did not correctly match 'Acme Corporation' against existing 'Acme Corp'/'ACME CORP.' - got {candidate_findings}")
        if any(f["candidate"] == "Someone Else Entirely" for f in candidate_findings):
            failures.append("--candidate mode false-matched a genuinely new, unrelated candidate name")

    # An empty matters/ directory (or one with no conflict_check data) must
    # report cleanly, not crash or false-positive.
    with tempfile.TemporaryDirectory() as empty_tmp:
        findings = find_cross_matter_matches(empty_tmp)
        if findings:
            failures.append(f"false positive on an empty matters/ directory - findings were: {findings}")

    if failures:
        print("SELFTEST FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("SELFTEST OK (all checks passed)")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("matters_root", nargs="?", help="Path to the matters/ directory")
    p.add_argument("--candidate", nargs="+", metavar="NAME", help="Check these candidate name(s) against every existing matter, instead of scanning matters/ against itself")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()

    if args.selftest:
        sys.exit(selftest())

    if not args.matters_root:
        p.error("supply the matters/ directory, or --selftest")

    if args.candidate:
        findings = check_candidate(args.matters_root, args.candidate)
        print(f"Checked {len(args.candidate)} candidate name(s) against {args.matters_root}")
        if findings:
            print(f"POSSIBLE CONFLICTS ({len(findings)}):")
            for f in findings:
                print(f"  - {f['candidate']!r} matches existing record(s):")
                for o in f["occurrences"]:
                    print(f"      {o['matter_id']} ({o['role']}): {o['name']!r} - {o['path']}")
            sys.exit(1)
        print("No possible conflicts found.")
        return

    findings = find_cross_matter_matches(args.matters_root)
    print(f"Scanned conflict_check records under {args.matters_root}")
    if findings:
        print(f"POSSIBLE CROSS-MATTER CONFLICTS ({len(findings)}):")
        for f in findings:
            print(f"  - {f['normalized_name']!r} appears in:")
            for o in f["occurrences"]:
                print(f"      {o['matter_id']} ({o['role']}): {o['name']!r}")
        sys.exit(1)
    print("No cross-matter name matches found.")


if __name__ == "__main__":
    main()
