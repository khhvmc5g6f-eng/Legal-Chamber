#!/usr/bin/env python3
"""Legal Chamber programmatic API - importable Python functions, not just a CLI.

This module exists because docs/SPEC_FULL_TEXT.md Part CLXXII names a
function-shaped API (createMatter(), resolveJurisdiction(), buildProofGraph(),
etc.) as a stated goal, and until now only bin/legal existed. Every function
here is honest about whether it's deterministic or reasoning-dependent - see
scripts/legal_cli.py's own docstring for the same distinction, which this
module reuses rather than re-implementing.

DETERMINISTIC (real, run entirely here):
    create_matter, get_matter_status, ingest_fact, ingest_evidence,
    build_proof_graph, check_filing_gates

REASONING-DEPENDENT (delegates to a live Claude Code invocation via
scripts/legal_cli.py's existing subprocess pattern, or raises clearly if
`claude` isn't available - never fakes legal judgement in pure Python):
    resolve_jurisdiction, research_issue, verify_authority, draft_document,
    run_adversarial_review, calculate_prospects

Usage as a library:

    import legal_api
    legal_api.create_matter("MATTER-001", matter_type="litigation", jurisdiction="England & Wales")
    graph = legal_api.build_proof_graph("MATTER-001")

Usage as a script:

    python3 legal_api.py --selftest
"""

import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import legal_cli  # noqa: E402  (reuse its REPO_ROOT, matter_dir, and reasoning-verb dispatch)


class LegalChamberError(Exception):
    """Raised for a deterministic-function precondition failure - never for a legal judgement call."""


class ReasoningRequiredError(LegalChamberError):
    """Raised when a caller asks this module to do something only a live model invocation can do."""


def _load_json(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _matter_dir(matter_id):
    return legal_cli.matter_dir(matter_id)


# ---------------------------------------------------------------------------
# Deterministic functions
# ---------------------------------------------------------------------------

def create_matter(matter_id, matter_type=None, jurisdiction=None, tier=None):
    """Create a new matter workspace. Returns the matter record dict.
    Raises LegalChamberError if the matter already exists - this function
    never silently overwrites a matter."""
    mdir = _matter_dir(matter_id)
    if os.path.exists(mdir):
        raise LegalChamberError(f"matters/{matter_id}/ already exists - use get_matter_status() to inspect it")

    class _Args:
        pass
    args = _Args()
    args.matter_id = matter_id
    args.type = matter_type
    args.jurisdiction = jurisdiction
    args.tier = tier
    rc = legal_cli.cmd_init(args)
    if rc != 0:
        raise LegalChamberError(f"create_matter({matter_id!r}) failed - see stdout above")
    return _load_json(os.path.join(mdir, "intake", "matter.json"))


def get_matter_status(matter_id):
    """Returns a dict: {matter_record, ref_findings, persistence_findings}.
    Real, deterministic checks - not a legal assessment of the matter's merits."""
    mdir = _matter_dir(matter_id)
    if not os.path.isdir(mdir):
        raise LegalChamberError(f"matters/{matter_id}/ does not exist")

    ref_script = os.path.join(legal_cli.REPO_ROOT, "scripts", "verify_matter_refs.py")
    persist_script = os.path.join(legal_cli.REPO_ROOT, "scripts", "verify_matter_persistence.py")

    sys.path.insert(0, os.path.dirname(ref_script))
    import verify_matter_refs
    import verify_matter_persistence

    ref_findings, ref_checked = verify_matter_refs.verify_matter(mdir)
    persist_findings, status = verify_matter_persistence.verify_matter(mdir)

    return {
        "matter_id": matter_id,
        "matter_record": _load_json(os.path.join(mdir, "intake", "matter.json")),
        "declared_status": status,
        "cross_reference_findings": ref_findings,
        "cross_references_checked": ref_checked,
        "persistence_findings": persist_findings,
    }


def _append_record(matter_id, subdir, filename, required_id_field, record):
    if required_id_field not in record:
        raise LegalChamberError(f"record is missing required field '{required_id_field}'")
    mdir = _matter_dir(matter_id)
    if not os.path.isdir(mdir):
        raise LegalChamberError(f"matters/{matter_id}/ does not exist - call create_matter() first")
    target_dir = os.path.join(mdir, subdir)
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, filename)
    existing = _load_json(path, default=[])
    if not isinstance(existing, list):
        raise LegalChamberError(f"{path} does not contain a JSON array - refusing to guess how to merge into it")
    existing_ids = {item.get(required_id_field) for item in existing if isinstance(item, dict)}
    if record[required_id_field] in existing_ids:
        raise LegalChamberError(f"{required_id_field} {record[required_id_field]!r} already exists in {path} - "
                                 f"this function appends new records, it does not update existing ones")
    existing.append(record)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2)
    return record


def ingest_fact(matter_id, fact_record):
    """Append one record to facts/facts.json, shaped per schemas/fact.schema.json.
    Does not validate legal content - only that fact_id is present and unique.
    Real schema validation (types, enums) is the caller's responsibility, or
    run scripts/legal_cli.py validate for the schema files themselves."""
    return _append_record(matter_id, "facts", "facts.json", "fact_id", fact_record)


def ingest_evidence(matter_id, evidence_record):
    """Append one record to evidence/evidence.json, shaped per schemas/evidence.schema.json."""
    return _append_record(matter_id, "evidence", "evidence.json", "evidence_id", evidence_record)


def build_proof_graph(matter_id):
    """Build a real dependency graph from a matter's existing fact/evidence/
    issue/authority records, by following the ID cross-references those
    records already declare (fact_ids_required, evidence_available_ids,
    authority_ids, etc. - see docs/ID_CONVENTIONS.md). This is pure graph
    construction over data that already exists in the matter - it does not
    invent a relationship that isn't already recorded, and it does not
    assess whether the graph shows a strong or weak case (that is
    schemas/conclusion.schema.json's proof_status field, set by whoever
    built the conclusion, not by this function).

    Returns {"nodes": [...], "edges": [...]} - nodes are every fact/
    evidence/issue/authority record found; edges are (from_id, to_id,
    via_field) for every cross-reference that actually resolves.
    """
    mdir = _matter_dir(matter_id)
    if not os.path.isdir(mdir):
        raise LegalChamberError(f"matters/{matter_id}/ does not exist")

    nodes = {}
    id_field_by_type = {"fact": "fact_id", "evidence": "evidence_id", "issue": "issue_id", "authority": "authority_id"}
    file_globs = {
        "fact": ["facts/facts.json"],
        "evidence": ["evidence/evidence.json", "facts/evidence.json"],
        "issue": ["issues/issues.json"],
        "authority": ["authorities/authorities.json"],
    }
    for node_type, globs in file_globs.items():
        id_field = id_field_by_type[node_type]
        for pattern in globs:
            for path in glob.glob(os.path.join(mdir, pattern)):
                data = _load_json(path, default=[])
                # Real agent-generated files sometimes wrap the array in a dict with
                # metadata fields (AI_GENERATED, VERIFICATION_STATUS, matter_id, ...)
                # rather than being a bare JSON array - found by testing this function
                # against real stress-test matter data, not assumed. Unwrap the same
                # way scripts/verify_matter_refs.py already does.
                if isinstance(data, dict):
                    data = data.get("items", data.get("facts", data.get("evidence", data.get("issues", data.get("authorities", [])))))
                if not isinstance(data, list):
                    continue
                for item in data:
                    if isinstance(item, dict) and id_field in item:
                        nodes[item[id_field]] = {"id": item[id_field], "type": node_type, "record": item}

    edges = []
    reference_fields = [
        ("fact_ids", ), ("evidence_ids", ), ("contrary_evidence_ids", ),
        ("authority_ids", ), ("fact_ids_required", ), ("evidence_available_ids", ),
    ]
    for node_id, node in nodes.items():
        record = node["record"]
        # issue.schema.json nests these under elements[]
        elements = record.get("elements") if isinstance(record.get("elements"), list) else []
        scan_targets = [record] + [e for e in elements if isinstance(e, dict)]
        for target in scan_targets:
            for (field,) in reference_fields:
                values = target.get(field)
                if not isinstance(values, list):
                    continue
                for ref_id in values:
                    if ref_id in nodes:
                        edges.append({"from": node_id, "to": ref_id, "via_field": field})

    return {
        "matter_id": matter_id,
        "nodes": list(nodes.values()),
        "edges": edges,
        "node_count": len(nodes),
        "edge_count": len(edges),
    }


def check_filing_gates(matter_id):
    """Mechanically checkable subset of docs/QUALITY_GATES.md's 13 gates.
    Returns {gate_number: {"checkable_here": bool, "passed": bool|None, "note": str}}.
    Gates requiring legal judgement (most of them) are marked checkable_here=False
    with passed=None - this function never claims to fully automate a gate that
    needs a human or an agent's judgement, per agents/quality/ROLE.md."""
    mdir = _matter_dir(matter_id)
    if not os.path.isdir(mdir):
        raise LegalChamberError(f"matters/{matter_id}/ does not exist")

    matter_record = _load_json(os.path.join(mdir, "intake", "matter.json"), default={})
    facts = _load_json(os.path.join(mdir, "facts", "facts.json"), default=[])
    issues = _load_json(os.path.join(mdir, "issues", "issues.json"), default=[])

    gates = {}
    gates[1] = {
        "checkable_here": True,
        "passed": bool(matter_record.get("jurisdiction")),
        "note": "jurisdiction established" if matter_record.get("jurisdiction") else "matter.json has no jurisdiction set",
    }
    facts_with_status = [f for f in facts if isinstance(f, dict) and f.get("status")]
    gates[2] = {
        "checkable_here": True,
        "passed": bool(facts) and len(facts_with_status) == len(facts),
        "note": f"{len(facts_with_status)}/{len(facts)} facts have a status field" if facts else "no facts recorded yet",
    }
    gates[3] = {
        "checkable_here": True,
        "passed": bool(issues),
        "note": f"{len(issues)} issue(s) recorded" if issues else "no issues recorded yet",
    }
    for n in (4, 5, 6, 8, 9, 10, 12, 13):
        gates[n] = {"checkable_here": False, "passed": None, "note": "requires legal/factual judgement - see docs/QUALITY_GATES.md and agents/quality/ROLE.md"}
    gates[7] = {
        "checkable_here": True,
        "passed": all(bool(i.get("elements")) for i in issues) if issues else None,
        "note": "every issue has at least one element with evidence fields" if issues else "no issues to check",
    }
    gates[11] = {"checkable_here": True, "passed": None, "note": "run scripts/citation_lint.py against the actual draft to check this - not assessed here without a draft path"}

    return {"matter_id": matter_id, "gates": gates,
            "reminder": "VERIFIED_FOR_FILING is set only by a human reviewer - this function never sets it, per agents/quality/ROLE.md"}


# ---------------------------------------------------------------------------
# Reasoning-dependent functions - delegate to legal_cli's existing pattern
# ---------------------------------------------------------------------------

def _reasoning_call(verb, matter_id, extra_instruction=""):
    class _Args:
        pass
    args = _Args()
    args.matter_id = matter_id
    args.rest = [extra_instruction] if extra_instruction else []
    rc = legal_cli.cmd_reasoning_verb(verb, args)
    if rc == 2:
        raise ReasoningRequiredError(
            f"'{verb}' requires live legal reasoning that this function cannot perform itself, and the "
            f"'claude' CLI was not found on PATH to run it for you - see the printed guidance above for "
            f"the exact prompt to run yourself in Claude Code."
        )
    return rc == 0


def resolve_jurisdiction(matter_id, instruction=""):
    return _reasoning_call("jurisdiction", matter_id, instruction)


def research_issue(matter_id, instruction=""):
    return _reasoning_call("research", matter_id, instruction)


def verify_authority(matter_id, instruction=""):
    return _reasoning_call("authorities", matter_id, instruction)


def draft_document(matter_id, instruction=""):
    return _reasoning_call("draft", matter_id, instruction)


def run_adversarial_review(matter_id, instruction=""):
    return _reasoning_call("oppose", matter_id, instruction)


def calculate_prospects(matter_id, instruction=""):
    return _reasoning_call("prospects", matter_id, instruction)


# ---------------------------------------------------------------------------


def selftest():
    import shutil
    import tempfile
    failures = []

    with tempfile.TemporaryDirectory() as tmp:
        old_root = legal_cli.REPO_ROOT
        try:
            legal_cli.REPO_ROOT = tmp
            os.makedirs(os.path.join(tmp, "scripts"))
            for name in ["citation_lint.py", "deadline_calculator.py", "verify_matter_refs.py", "verify_matter_persistence.py"]:
                shutil.copy2(os.path.join(old_root, "scripts", name), os.path.join(tmp, "scripts", name))

            record = create_matter("API-TEST-001", matter_type="litigation", jurisdiction="England & Wales", tier="L2")
            if record.get("matter_id") != "API-TEST-001":
                failures.append(f"create_matter did not return the expected record: {record}")

            try:
                create_matter("API-TEST-001")
                failures.append("create_matter did not raise on a duplicate matter id")
            except LegalChamberError:
                pass

            ingest_fact("API-TEST-001", {"fact_id": "F-001", "proposition": "the contract was signed", "status": "ESTABLISHED", "materiality": "HIGH"})
            ingest_fact("API-TEST-001", {"fact_id": "F-002", "proposition": "payment was withheld", "status": "USER_ASSERTED", "materiality": "HIGH"})
            try:
                ingest_fact("API-TEST-001", {"fact_id": "F-001", "proposition": "duplicate", "status": "ESTABLISHED", "materiality": "LOW"})
                failures.append("ingest_fact did not raise on a duplicate fact_id")
            except LegalChamberError:
                pass

            os.makedirs(os.path.join(tmp, "matters", "API-TEST-001", "issues"), exist_ok=True)
            with open(os.path.join(tmp, "matters", "API-TEST-001", "issues", "issues.json"), "w") as f:
                json.dump([{"issue_id": "ISS-001", "description": "breach of contract",
                            "elements": [{"element": "breach", "burden": "LEGAL", "standard": "balance of probabilities",
                                          "fact_ids_required": ["F-001", "F-002"]}],
                            "priority": "HIGH"}], f)

            graph = build_proof_graph("API-TEST-001")
            if graph["node_count"] < 3:
                failures.append(f"build_proof_graph found too few nodes: {graph}")
            edge_targets = {(e["from"], e["to"]) for e in graph["edges"]}
            if ("ISS-001", "F-001") not in edge_targets or ("ISS-001", "F-002") not in edge_targets:
                failures.append(f"build_proof_graph did not find the fact_ids_required edges: {graph['edges']}")

            status = get_matter_status("API-TEST-001")
            if status["matter_id"] != "API-TEST-001":
                failures.append(f"get_matter_status returned wrong matter_id: {status}")

            gates = check_filing_gates("API-TEST-001")
            if not gates["gates"][1]["passed"]:
                failures.append(f"Gate 1 should pass (jurisdiction was set): {gates}")
            if gates["gates"][2]["passed"] is not True:
                failures.append(f"Gate 2 should pass (both facts have a status): {gates}")
            if gates["gates"][4]["checkable_here"] is not False:
                failures.append("Gate 4 should be marked not mechanically checkable")

            # Force the no-`claude`-available path deterministically, rather than actually
            # invoking a live model call from inside a selftest (which would be slow, cost
            # tokens, and be non-deterministic depending on the machine running the test).
            real_which = legal_cli.shutil.which
            legal_cli.shutil.which = lambda _name: None
            try:
                resolve_jurisdiction("API-TEST-001")
                failures.append("resolve_jurisdiction should have raised ReasoningRequiredError with no claude CLI available")
            except ReasoningRequiredError:
                pass
            finally:
                legal_cli.shutil.which = real_which
        finally:
            legal_cli.REPO_ROOT = old_root

    if failures:
        print("SELFTEST FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("SELFTEST OK (all checks passed)")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    print(__doc__)
