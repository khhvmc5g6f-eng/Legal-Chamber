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
- Python 3.9+ if you want to run `scripts/deadline_calculator.py` / `scripts/citation_lint.py` directly rather than having an agent invoke them.
- No other runtime dependency. Nothing in this repo calls a paid legal database. Where a skill can use a live connector (e.g. CourtListener for US federal case law, if that MCP server is connected in your session), it says so and degrades to "ask the user for the source" if the connector isn't available.

## First run

Say something like:

```
Review my employment tribunal case using Full Chambers.
```

`legal-work` will ask for jurisdiction (no auto-detection is implemented, see `docs/HONEST_STATUS.md`) and matter type, then open a matter workspace under `matters/<MATTER-ID>/` in your project (created on first use, gitignored by default, see `.gitignore`).
