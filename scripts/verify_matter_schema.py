#!/usr/bin/env python3
"""Deterministic schema-conformance checker for a matter workspace's own JSON records.

CI's `schema-validation` job (`.github/workflows/ci.yml`) only checks that the
schema files under `schemas/*.schema.json` are themselves well-formed JSON
Schema documents - it has never checked that a real matter's actual records
(`facts/facts.json`, `evidence/evidence.json`, etc.) conform to those schemas.
Nothing else in this repository does either. This is arithmetic (does this
record have its required fields, does an enum-typed field hold a value that
enum actually allows), not legal judgement, so it belongs here per CLAUDE.md's
"deterministic tools first" principle rather than being left to an agent's
own diligence.

None of this repository's schemas declare `additionalProperties: false`, so a
field name the schema doesn't recognise is not a schema violation under
Draft-07 semantics - only a possible typo or drift. This script therefore
reports two severities: schema VIOLATIONS (missing required field, wrong
type, value outside a declared enum - real schema breaks, non-zero exit) and
UNKNOWN FIELD notices (not in the schema's declared properties - reported for
visibility, does not fail the run on its own).

Usage:
    python3 verify_matter_schema.py matters/MATTER-ID
    python3 verify_matter_schema.py --selftest
"""

import argparse
import glob
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Which files under a matter directory should conform to which schema, and
# how to find the list of record objects inside that file (a bare list, or
# a dict value reached by one of these keys).
RECORD_TYPES = [
    # (schema file, file globs relative to matter_dir, is_single_object)
    ("matter.schema.json", ["intake/matter.json", "matter.json"], True),
    ("fact.schema.json", ["facts/facts.json", "facts.json"], False),
    ("evidence.schema.json", ["evidence/evidence.json", "facts/evidence.json"], False),
    ("chronology.schema.json", ["chronology/chronology.json"], False),
    ("issue.schema.json", ["issues/issues.json"], False),
    ("authority.schema.json", ["authorities/authorities.json"], False),
    ("deadline.schema.json", ["procedure/deadlines.json", "deadlines/deadlines.json"], False),
]

_LIST_KEYS = ("items", "facts", "evidence", "events", "issues", "authorities", "deadlines")


def _load_schema(schema_name):
    path = os.path.join(REPO_ROOT, "schemas", schema_name)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _extract_items(data):
    """A record file is either a bare JSON array, or a dict holding the array
    under one of a few conventional keys - mirrors verify_matter_refs.py's
    same lenient unwrapping so the two scripts agree on what "a record" means."""
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in _LIST_KEYS:
            if isinstance(data.get(key), list):
                return data[key]
    return None


def _validate_record(record, schema, path, index_label):
    violations = []
    unknown = []
    properties = schema.get("properties", {})

    for field in schema.get("required", []):
        if field not in record:
            violations.append(f"{path} [{index_label}]: missing required field {field!r}")

    for field, value in record.items():
        if field not in properties:
            unknown.append(f"{path} [{index_label}]: unknown field {field!r} not in {schema.get('title', '?')} schema")
            continue
        spec = properties[field]
        expected_type = spec.get("type")
        if expected_type == "string" and not isinstance(value, str):
            violations.append(f"{path} [{index_label}]: field {field!r} should be a string, got {type(value).__name__}")
        elif expected_type == "array" and not isinstance(value, list):
            violations.append(f"{path} [{index_label}]: field {field!r} should be an array, got {type(value).__name__}")
        elif expected_type == "boolean" and not isinstance(value, bool):
            violations.append(f"{path} [{index_label}]: field {field!r} should be a boolean, got {type(value).__name__}")
        elif expected_type == "object" and not isinstance(value, dict):
            violations.append(f"{path} [{index_label}]: field {field!r} should be an object, got {type(value).__name__}")
        if "enum" in spec and value is not None and value not in spec["enum"]:
            violations.append(f"{path} [{index_label}]: field {field!r} = {value!r} is not one of {spec['enum']}")

    return violations, unknown


def verify_matter(matter_dir):
    """Returns (violations, unknowns, checked_count)."""
    if not os.path.isdir(matter_dir):
        return [f"{matter_dir} does not exist"], [], 0

    violations = []
    unknown = []
    checked = 0

    for schema_name, globs, single in RECORD_TYPES:
        schema = _load_schema(schema_name)
        for rel in globs:
            for path in glob.glob(os.path.join(matter_dir, rel)):
                try:
                    with open(path, encoding="utf-8") as f:
                        data = json.load(f)
                except (OSError, json.JSONDecodeError) as e:
                    violations.append(f"{path}: could not parse as JSON ({e})")
                    continue

                if single:
                    records = [data] if isinstance(data, dict) else None
                else:
                    records = _extract_items(data)

                if records is None:
                    violations.append(f"{path}: expected a {'single object' if single else 'list of records'}, got {type(data).__name__}")
                    continue

                for i, record in enumerate(records):
                    if not isinstance(record, dict):
                        violations.append(f"{path} [{i}]: record is not a JSON object")
                        continue
                    checked += 1
                    label = record.get("fact_id") or record.get("evidence_id") or record.get("event_id") or record.get("issue_id") or record.get("authority_id") or record.get("deadline_id") or record.get("matter_id") or str(i)
                    v, u = _validate_record(record, schema, path, label)
                    violations.extend(v)
                    unknown.extend(u)

    return violations, unknown, checked


def selftest():
    import tempfile

    failures = []

    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(os.path.join(tmp, "facts"))
        # A fact missing its required "materiality" field, one with a bad enum
        # value, one that's entirely valid, and one with an unrecognised field.
        with open(os.path.join(tmp, "facts", "facts.json"), "w") as f:
            json.dump(
                [
                    {"fact_id": "F-001", "proposition": "x", "status": "ESTABLISHED"},
                    {"fact_id": "F-002", "proposition": "y", "status": "NOT_A_REAL_STATUS", "materiality": "HIGH"},
                    {"fact_id": "F-003", "proposition": "z", "status": "ESTABLISHED", "materiality": "LOW"},
                    {"fact_id": "F-004", "proposition": "w", "status": "ESTABLISHED", "materiality": "LOW", "totally_made_up_field": "oops"},
                ],
                f,
            )

        violations, unknown, checked = verify_matter(tmp)

        if checked != 4:
            failures.append(f"expected 4 records checked, got {checked}")
        if not any("F-001" in v and "materiality" in v for v in violations):
            failures.append(f"did not flag F-001's missing required 'materiality' field - violations were: {violations}")
        if not any("F-002" in v and "NOT_A_REAL_STATUS" in v for v in violations):
            failures.append(f"did not flag F-002's invalid enum value - violations were: {violations}")
        if any("F-003" in v for v in violations):
            failures.append(f"false positive on valid record F-003 - violations were: {violations}")
        if not any("F-004" in u and "totally_made_up_field" in u for u in unknown):
            failures.append(f"did not flag F-004's unknown field as an advisory notice - unknown was: {unknown}")
        if any("F-004" in v for v in violations):
            failures.append("an unknown field must be advisory only, not a hard violation (no additionalProperties:false in these schemas)")

    # A nonexistent matter directory must be a hard failure, never a clean pass -
    # matches the convention verify_matter_refs.py and verify_matter_persistence.py
    # already use.
    nonexistent = os.path.join(tempfile.gettempdir(), "verify-matter-schema-selftest-does-not-exist")
    violations, unknown, checked = verify_matter(nonexistent)
    if not violations:
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

    violations, unknown, checked = verify_matter(args.matter_dir)
    print(f"Checked {checked} records in {args.matter_dir}")
    if unknown:
        print(f"UNKNOWN FIELDS, advisory only ({len(unknown)}):")
        for u in unknown:
            print(f"  - {u}")
    if violations:
        print(f"SCHEMA VIOLATIONS ({len(violations)}):")
        for v in violations:
            print(f"  - {v}")
        sys.exit(1)
    print("No schema violations found.")


if __name__ == "__main__":
    main()
