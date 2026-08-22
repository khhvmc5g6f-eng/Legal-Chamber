# Agent Roster

Legal Chambers' agent roles live under `agents/<role>/` as prompt specifications. They are invoked through Claude Code's Agent tool, each role's `ROLE.md` becomes (or informs) the prompt for a fresh subagent context, never a persona bolted onto the same context doing everything else.

## Independence rule

A single agent context must never be the sole:

- **researcher**
- **drafter**
- **opposition**
- **judge**
- **final reviewer**

for the same proposition. Adversarial roles (`counsel` vs `opposition`, `judiciary`) always run in separate contexts from the roles whose work they're checking. See `workflows/five-hearing-adversarial.md`.

## Roles

| Directory | Function |
|---|---|
| `agents/intake/` | Classifies the incoming request, extracts matter type and jurisdiction signal, does **not** research or draft. |
| `agents/jurisdiction/` | Resolves which jurisdiction pack(s) apply; flags multi-jurisdiction / conflict-of-laws issues. |
| `agents/research/` | Runs supporting **and** disconfirming searches for each material proposition; logs both in the research log. |
| `agents/evidence/` | Builds the Fact Ledger and Evidence Ledger; flags contradictions and missing-but-expected documents. |
| `agents/solicitors/` | Constructs the strongest sustainable case from verified law, fact, and evidence, instructing/research/litigation/evidence/procedure/remedies/drafting sub-functions described in one file for now (see the file's own TODO on splitting further). |
| `agents/counsel/` | Independently challenges the solicitor team's work before it goes further. |
| `agents/opposition/` | Runs in an isolated context; instructed to build the strongest **reasonable** case for the other side, not a strawman. |
| `agents/judiciary/` | Simulated decision-maker for the five-hearing adversarial workflow; may decide against the user. |
| `agents/academic/` | Marking-panel roles for academic mode (knowledge, analysis, research, critical evaluation, structure, external examiner). |
| `agents/transactional/` | Contract/due-diligence specific reasoning (clause dependency mapping, red-flag detection). |
| `agents/regulatory/` | Regulatory/disciplinary matter reasoning (allegation matrix, mitigation vs liability separation). |
| `agents/negotiation/` | Interests/BATNA/WATNA/settlement modelling, explicitly kept separate from legal-merits reasoning. |
| `agents/quality/` | Runs the quality gates (`docs/QUALITY_GATES.md`) and the citation/fact audits before any output is offered for human review. |

## Status

Every role file in this build is a genuine, usable prompt specification. None has yet been run through the benchmark suite in `benchmarks/` end-to-end, see `docs/HONEST_STATUS.md`. Treat these as a strong first draft of each role's guardrails, not as validated.
