#!/usr/bin/env python3
"""Legal Chamber CLI - `legal <verb> ...`.

Two genuinely different kinds of subcommand live here, and this file is
honest about which is which rather than blurring the line:

DETERMINISTIC (real, run entirely in this script, no model involved):
    init, status, validate, lint, deadline, verify-refs, verify-persistence,
    jurisdictions, gates, bundle

REASONING-DEPENDENT (this script cannot do these itself - a bare Python
script has no legal judgement; it shells out to a live Claude Code
invocation of the actual skill file, or - if the `claude` CLI isn't on
PATH - prints the exact guidance to run manually instead of pretending to
have done the work):
    intake, jurisdiction, facts, evidence, chronology, research,
    authorities, analyse, draft, review, oppose, moot, appeal, prospects,
    verify

Usage:
    python3 legal_cli.py init MATTER-001 --type litigation --jurisdiction "England & Wales"
    python3 legal_cli.py status MATTER-001
    python3 legal_cli.py validate
    python3 legal_cli.py research MATTER-001 "is the limitation period an issue here"
    python3 legal_cli.py --selftest
"""

import argparse
import glob
import json
import os
import shutil
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STANDARD_SUBDIRS = [
    "intake", "facts", "evidence", "chronology", "issues", "research",
    "authorities", "drafts", "opposition", "moot", "procedure", "costs",
    "prospects", "final",
]

REASONING_VERBS = {
    "intake": ("skills/legal-work/SKILL.md", "run intake classification and jurisdiction resolution for this matter"),
    "jurisdiction": ("agents/jurisdiction/ROLE.md", "resolve jurisdiction for this matter, asking rather than inferring"),
    "facts": ("agents/evidence/ROLE.md", "build or update the Fact Ledger for this matter"),
    "evidence": ("agents/evidence/ROLE.md", "build or update the Evidence Ledger for this matter"),
    "chronology": ("agents/evidence/ROLE.md", "build or update the chronology for this matter"),
    "research": ("skills/legal-research/SKILL.md", "run bidirectional legal research for this matter"),
    "authorities": ("skills/legal-authorities/SKILL.md", "verify a specific authority for this matter"),
    "analyse": ("skills/legal-litigation/SKILL.md", "build or review the issue tree and case theory for this matter"),
    "draft": ("skills/legal-draft/SKILL.md", "produce a document for this matter"),
    "review": ("skills/legal-review/SKILL.md", "review the current draft/reasoning for this matter"),
    "oppose": ("agents/opposition/ROLE.md", "build the strongest reasonable opposing case for this matter"),
    "moot": ("skills/legal-moot/SKILL.md", "stress-test the case theory for this matter"),
    "appeal": ("skills/legal-appeal/SKILL.md", "run appellate vulnerability analysis for this matter"),
    "prospects": ("skills/legal-prospects/SKILL.md", "assess prospects for this matter"),
    "verify": ("skills/legal-verify/SKILL.md", "run the full verification pass over the current draft for this matter"),
}


def matter_dir(matter_id):
    return os.path.join(REPO_ROOT, "matters", matter_id)


# ---------------------------------------------------------------------------
# Deterministic commands
# ---------------------------------------------------------------------------

def cmd_init(args):
    mdir = matter_dir(args.matter_id)
    if os.path.exists(mdir):
        print(f"matters/{args.matter_id}/ already exists - not overwriting. Use 'status' to inspect it.")
        return 1
    # Only create intake/ up front. Pre-creating all 14 standard subdirectories
    # empty was tried and reverted - it made every fresh matter immediately
    # trigger 13 empty-directory findings from verify_matter_persistence.py,
    # inconsistent with how matters actually grow in practice (a subdirectory
    # appears only once something real is written into it, per the matters
    # generated during the 2026-08-22 stress test). Other subdirectories get
    # created organically by whichever skill/role first writes into them.
    os.makedirs(os.path.join(mdir, "intake"), exist_ok=True)
    matter_record = {
        "matter_id": args.matter_id,
        "matter_type": args.type or "advisory",
        "jurisdiction": [{"country": args.jurisdiction, "legal_system": "UNKNOWN", "confidence": "asserted-by-user"}] if args.jurisdiction else [],
        "complexity_tier": args.tier or "L1",
        "status": "INTAKE",
        "confidentiality": "CONFIDENTIAL",
        "conflict_check": {"cleared": False},
    }
    with open(os.path.join(mdir, "intake", "matter.json"), "w", encoding="utf-8") as f:
        json.dump(matter_record, f, indent=2)
    print(f"Created matters/{args.matter_id}/intake/ and matter.json. Other subdirectories (facts/, research/, etc.) "
          f"are created only once a skill/role actually writes into them - see skills/legal-work/SKILL.md Step 3.")
    print("conflict_check.cleared is false - clear it (or knowingly waive it) before substantive work proceeds, per skills/legal-work/SKILL.md Step 3.")
    print(f"Next: python3 {sys.argv[0]} intake {args.matter_id} \"<describe the matter>\"")
    return 0


def cmd_status(args):
    mdir = matter_dir(args.matter_id)
    if not os.path.isdir(mdir):
        print(f"matters/{args.matter_id}/ does not exist. Run 'init' first.")
        return 1
    print(f"=== matters/{args.matter_id}/ ===")
    ref_script = os.path.join(REPO_ROOT, "scripts", "verify_matter_refs.py")
    persist_script = os.path.join(REPO_ROOT, "scripts", "verify_matter_persistence.py")
    rc = 0
    for label, script in [("cross-reference integrity", ref_script), ("claimed-vs-persisted outputs", persist_script)]:
        print(f"\n--- {label} ---")
        result = subprocess.run([sys.executable, script, mdir], capture_output=True, text=True)
        print(result.stdout.strip())
        if result.returncode != 0:
            rc = 1
    return rc


def cmd_validate(_args):
    print("=== schema validity ===")
    rc = 0
    for path in glob.glob(os.path.join(REPO_ROOT, "schemas", "*.schema.json")):
        try:
            with open(path, encoding="utf-8") as f:
                json.load(f)
            print(f"OK: {os.path.relpath(path, REPO_ROOT)}")
        except (OSError, json.JSONDecodeError) as e:
            print(f"FAIL: {os.path.relpath(path, REPO_ROOT)}: {e}")
            rc = 1

    print("\n=== deterministic script selftests ===")
    for script in ["citation_lint.py", "deadline_calculator.py", "verify_matter_refs.py", "verify_matter_persistence.py"]:
        path = os.path.join(REPO_ROOT, "scripts", script)
        result = subprocess.run([sys.executable, path, "--selftest"], capture_output=True, text=True)
        print(f"{script}: {result.stdout.strip()}")
        if result.returncode != 0:
            rc = 1
    return rc


def cmd_lint(args):
    script = os.path.join(REPO_ROOT, "scripts", "citation_lint.py")
    result = subprocess.run([sys.executable, script] + args.files)
    return result.returncode


def cmd_deadline(args):
    script = os.path.join(REPO_ROOT, "scripts", "deadline_calculator.py")
    result = subprocess.run([sys.executable, script] + args.rest)
    return result.returncode


def cmd_verify_refs(args):
    script = os.path.join(REPO_ROOT, "scripts", "verify_matter_refs.py")
    result = subprocess.run([sys.executable, script, matter_dir(args.matter_id)])
    return result.returncode


def cmd_verify_persistence(args):
    script = os.path.join(REPO_ROOT, "scripts", "verify_matter_persistence.py")
    result = subprocess.run([sys.executable, script, matter_dir(args.matter_id)])
    return result.returncode


def cmd_jurisdictions(args):
    jdir = os.path.join(REPO_ROOT, "jurisdictions")
    if args.slug:
        path = os.path.join(jdir, args.slug, "README.md")
        if not os.path.exists(path):
            print(f"No pack for '{args.slug}'. Run without an argument to list available slugs.")
            return 1
        with open(path, encoding="utf-8") as f:
            print(f.read())
        return 0

    print("Available jurisdiction packs (see docs/HONEST_STATUS.md for what STRUCTURAL_DRAFT actually means):\n")
    for entry in sorted(os.listdir(jdir)):
        readme = os.path.join(jdir, entry, "README.md")
        if not os.path.isfile(readme):
            continue
        status = "UNKNOWN"
        with open(readme, encoding="utf-8") as f:
            for line in f:
                if line.startswith("verification_status:"):
                    status = line.split(":", 1)[1].strip()
                    break
        print(f"  {entry:20s} {status}")
    return 0


def cmd_gates(_args):
    path = os.path.join(REPO_ROOT, "docs", "QUALITY_GATES.md")
    with open(path, encoding="utf-8") as f:
        print(f.read())
    return 0


def cmd_bundle(args):
    mdir = matter_dir(args.matter_id)
    if not os.path.isdir(mdir):
        print(f"matters/{args.matter_id}/ does not exist.")
        return 1
    out_dir = args.out or os.path.join(mdir, "final", "bundle")
    os.makedirs(out_dir, exist_ok=True)
    copied = 0
    for sub in ("drafts", "final", "authorities"):
        src = os.path.join(mdir, sub)
        if not os.path.isdir(src):
            continue
        for root, _dirs, files in os.walk(src):
            for name in files:
                src_path = os.path.join(root, name)
                if os.path.commonpath([src_path, out_dir]) == out_dir:
                    continue
                dst_path = os.path.join(out_dir, f"{sub}__{name}")
                shutil.copy2(src_path, dst_path)
                copied += 1
    print(f"Copied {copied} file(s) from drafts/, final/, and authorities/ into {os.path.relpath(out_dir, REPO_ROOT)}.")
    print("This is a literal file collection, not a curated authorities bundle - deciding which authorities are "
          "actually relied upon (per docs/OPERATING_RULES.md's authorities-bundle rule) requires legal judgement; "
          "use 'legal draft' or the legal-draft skill directly for that.")
    return 0


# ---------------------------------------------------------------------------
# Reasoning-dependent commands
# ---------------------------------------------------------------------------

def cmd_reasoning_verb(verb, args):
    skill_file, task_description = REASONING_VERBS[verb]
    mdir_rel = f"matters/{args.matter_id}" if args.matter_id else None
    extra = " ".join(args.rest) if args.rest else ""

    prompt_lines = [
        f"Read {skill_file} in this repository and follow its actual instructions to {task_description}.",
    ]
    if mdir_rel:
        prompt_lines.append(f"Matter workspace: {mdir_rel}/ (create it first with 'legal init {args.matter_id}' if it doesn't exist).")
    if extra:
        prompt_lines.append(f"Additional instruction: {extra}")
    prompt = " ".join(prompt_lines)

    claude_bin = shutil.which("claude")
    if not claude_bin:
        print(f"This is a reasoning-dependent step - '{verb}' requires an actual legal-reasoning pass, which this "
              f"bare script cannot perform itself, and the 'claude' CLI was not found on PATH to run it for you.")
        print(f"\nRun this yourself in Claude Code:\n\n  {prompt}\n")
        return 2

    print(f"Invoking Claude Code non-interactively for '{verb}' (this may take a while and will use API credits)...")
    result = subprocess.run([claude_bin, "--print", prompt], cwd=REPO_ROOT)
    return result.returncode


# ---------------------------------------------------------------------------


def selftest():
    import tempfile
    failures = []

    with tempfile.TemporaryDirectory() as tmp:
        old_root = globals()["REPO_ROOT"]
        try:
            globals()["REPO_ROOT"] = tmp
            os.makedirs(os.path.join(tmp, "scripts"))
            # copy the real deterministic scripts in so subprocess calls resolve
            for name in ["citation_lint.py", "deadline_calculator.py", "verify_matter_refs.py", "verify_matter_persistence.py"]:
                shutil.copy2(os.path.join(old_root, "scripts", name), os.path.join(tmp, "scripts", name))

            class Args:
                pass
            a = Args()
            a.matter_id = "SELFTEST-001"
            a.type = "litigation"
            a.jurisdiction = "England & Wales"
            a.tier = "L2"
            rc = cmd_init(a)
            if rc != 0:
                failures.append(f"cmd_init returned {rc}")
            if not os.path.isdir(os.path.join(tmp, "matters", "SELFTEST-001", "intake")):
                failures.append("init did not create the intake/ subdirectory")
            if not os.path.exists(os.path.join(tmp, "matters", "SELFTEST-001", "intake", "matter.json")):
                failures.append("init did not write intake/matter.json")

            b = Args()
            b.matter_id = "SELFTEST-001"
            rc = cmd_status(b)
            # status may exit 1 if the (empty, freshly-initted) matter has expected-but-missing dirs for its
            # status - that's correct behaviour being exercised, not a selftest failure, so only check it ran.
        finally:
            globals()["REPO_ROOT"] = old_root

    if failures:
        print("SELFTEST FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("SELFTEST OK (all checks passed)")
    return 0


def build_parser():
    p = argparse.ArgumentParser(prog="legal", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--selftest", action="store_true")
    sub = p.add_subparsers(dest="command")

    sp = sub.add_parser("init", help="Create a new matter workspace (deterministic)")
    sp.add_argument("matter_id")
    sp.add_argument("--type", choices=["research", "litigation", "administrative-public-law", "criminal", "employment", "regulatory", "transactional", "advisory", "negotiation-adr", "academic"])
    sp.add_argument("--jurisdiction")
    sp.add_argument("--tier", choices=["L1", "L2", "L3", "L4", "L5", "L6"])

    sp = sub.add_parser("status", help="Show a matter's persistence/cross-reference gate results (deterministic)")
    sp.add_argument("matter_id")

    sub.add_parser("validate", help="Validate all schemas and run all deterministic script selftests (deterministic)")

    sp = sub.add_parser("lint", help="Run the citation/house-style linter (deterministic)")
    sp.add_argument("files", nargs="+")

    sp = sub.add_parser("deadline", help="Run the deadline calculator - pass its own flags after --")
    sp.add_argument("rest", nargs=argparse.REMAINDER)

    sp = sub.add_parser("verify-refs", help="Check cross-referenced IDs resolve within a matter (deterministic)")
    sp.add_argument("matter_id")

    sp = sub.add_parser("verify-persistence", help="Check claimed outputs exist on disk for a matter (deterministic)")
    sp.add_argument("matter_id")

    sp = sub.add_parser("jurisdictions", help="List jurisdiction packs and their verification status (deterministic)")
    sp.add_argument("slug", nargs="?")

    sub.add_parser("gates", help="Print the quality gates (deterministic)")

    sp = sub.add_parser("bundle", help="Collect a matter's drafts/final/authorities files into one folder (deterministic, not curated)")
    sp.add_argument("matter_id")
    sp.add_argument("--out")

    for verb, (_skill, desc) in REASONING_VERBS.items():
        sp = sub.add_parser(verb, help=f"[reasoning-dependent] {desc}")
        sp.add_argument("matter_id", nargs="?")
        sp.add_argument("rest", nargs=argparse.REMAINDER)

    return p


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.selftest:
        sys.exit(selftest())

    if not args.command:
        parser.print_help()
        sys.exit(1)

    deterministic = {
        "init": cmd_init, "status": cmd_status, "validate": cmd_validate, "lint": cmd_lint,
        "deadline": cmd_deadline, "verify-refs": cmd_verify_refs, "verify-persistence": cmd_verify_persistence,
        "jurisdictions": cmd_jurisdictions, "gates": cmd_gates, "bundle": cmd_bundle,
    }
    if args.command in deterministic:
        sys.exit(deterministic[args.command](args))
    elif args.command in REASONING_VERBS:
        sys.exit(cmd_reasoning_verb(args.command, args))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
