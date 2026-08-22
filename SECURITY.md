# Security Policy

## Scope

This repository ships prompt-based skills, JSON Schemas, markdown reference packs, and two small dependency-free Python scripts (`scripts/deadline_calculator.py`, `scripts/citation_lint.py`). It has no server component, no database, and makes no network calls of its own.

## Sensitive data handling

- `matters/` (per-matter workspaces created when the skill runs) is gitignored by default and must never be committed, see `.gitignore` and `CLAUDE.md`. Matter workspaces can contain privileged, confidential, or personal data.
- This repository defines confidentiality/privilege *classifications* (`docs/OPERATING_RULES.md`) but does not itself implement encryption, access control, or retention enforcement, those are the responsibility of whatever environment a matter workspace lives in. Do not treat this repo's classification labels as a substitute for actual access controls.
- No telemetry, analytics, or external calls are made by anything in this repository. Any research connector (e.g. CourtListener) is used only through the invoking session's own MCP configuration, never hardcoded with credentials here.

## Reporting a vulnerability

Open a private security advisory on GitHub (Security → Advisories → Report a vulnerability) rather than a public issue, for anything involving:

- a way for matter data to leak into this public repository or its history
- a prompt-injection path that causes a skill to bypass a quality gate or the human-review requirement
- any credential or token accidentally committed

We will acknowledge within a reasonable time and, if the report is a real issue, patch and credit you (unless you ask not to be credited) before public disclosure.

## Not a substitute for legal or information-security advice

Nothing in this repository is legal advice, and using it does not create a legal review or advice relationship with its maintainers. See `README.md` and `docs/HONEST_STATUS.md`.
