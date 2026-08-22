# Install

## As a Claude Code plugin

```bash
claude plugin install <this-repo-url>
```

or, from a local clone:

```bash
claude plugin install /path/to/legal-chamber
```

This registers `skills/legal-work` (and the other 15 skills) as invocable skills, and makes `agents/*` role specs available for the Agent tool to use as prompts.

## As a bare skill directory

If you don't want the full plugin, copy or symlink `skills/legal-work/` into your project's own skill search path (e.g. a `.claude/skills/` directory), and copy the `jurisdictions/`, `schemas/`, `scripts/`, and `docs/` directories alongside it, `legal-work` reads them by relative path.

## Requirements

- Claude Code (or a compatible Agent Skills runtime).
- Python 3.9+ if you want to run `scripts/deadline_calculator.py` / `scripts/citation_lint.py` / `scripts/verify_matter_refs.py` / `scripts/verify_matter_persistence.py` / `scripts/legal_cli.py` directly rather than having an agent invoke them.
- No other runtime dependency. Nothing in this repo calls a paid legal database. Where a skill can use a live connector (e.g. CourtListener for US federal case law, if that MCP server is connected in your session), it says so and degrades to "ask the user for the source" if the connector isn't available.

## Optional: the `legal` CLI

`bin/legal` (a thin wrapper around `scripts/legal_cli.py`) gives you a command-line entry point matching the original spec's verb list. Some of it is real, deterministic tooling that needs no model at all; the rest shells out to a live Claude Code invocation of the actual skill (or prints the exact prompt to run yourself, if the `claude` CLI isn't on your PATH) - `scripts/legal_cli.py`'s own docstring is explicit about which verb is which, since a bare Python script cannot do legal reasoning itself and this repo does not pretend otherwise.

```bash
./bin/legal init MATTER-001 --type litigation --jurisdiction "England & Wales"   # deterministic
./bin/legal status MATTER-001                                                    # deterministic
./bin/legal validate                                                              # deterministic - runs every schema + script check
./bin/legal jurisdictions                                                         # deterministic - lists packs and their verification status
./bin/legal research MATTER-001 "is there a limitation issue here"                # reasoning-dependent - invokes Claude Code, or prints guidance
```

## Optional: the Python API

`scripts/legal_api.py` exposes the same deterministic capability as importable functions, plus one genuinely new one - `build_proof_graph(matter_id)`, which constructs a real dependency graph (which facts/evidence/authorities an issue actually relies on) by following the ID cross-references a matter's own JSON records already declare. Nothing here assesses whether a case is strong - it only shows what's actually linked to what.

```python
import sys; sys.path.insert(0, "scripts")
import legal_api

legal_api.create_matter("MATTER-001", matter_type="litigation", jurisdiction="England & Wales")
legal_api.ingest_fact("MATTER-001", {"fact_id": "F-001", "proposition": "...", "status": "USER_ASSERTED", "materiality": "HIGH"})
graph = legal_api.build_proof_graph("MATTER-001")
```

## First run

Say something like:

```
Review my employment tribunal case using Full Chambers.
```

`legal-work` will ask for jurisdiction (no auto-detection is implemented, see `docs/HONEST_STATUS.md`) and matter type, then open a matter workspace under `matters/<MATTER-ID>/` in your project (created on first use, gitignored by default, see `.gitignore`).
