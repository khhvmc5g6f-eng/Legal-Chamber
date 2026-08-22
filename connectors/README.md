# Connectors

Abstraction layer notes for research data sources. This repository does not hard-code credentials or a required commercial database - it documents which connector to reach for, per jurisdiction, and what to do when none is available.

## What's actually connected in a Claude Code session (not this repo's doing - session-dependent)

| Source | Status | Notes |
|---|---|---|
| CourtListener (RECAP dockets, opinions, judges, oral arguments) | Usable if the session has this MCP server connected | US federal + some state coverage. See `../jurisdictions/us-federal/README.md`. |
| Official legislation/judgment sites (legislation.gov.uk, BAILII/Find Case Law, AustLII, CanLII, NZLII, Légifrance, BOE, EUR-Lex, etc.) | Reachable via WebSearch/WebFetch in a Claude Code session | Not a dedicated connector - live web research each time, and each jurisdiction pack names the specific sites to prefer. |
| Westlaw / Lexis / vLex / HeinOnline | Not connected in this build | Would require the user's own subscription and an MCP/API integration this repository does not ship. |

## Additional open APIs identified but not yet wired in (checked live via WebSearch on 2026-08-22, not yet integrated as a connector)

| Source | Coverage | Access | Confidence |
|---|---|---|---|
| Find Case Law (National Archives) | UK court/tribunal judgments as structured data (LegalDocML XML), Open Justice Licence, commercial reuse permitted | No key needed - REST-ish endpoints, docs at `nationalarchives.github.io/ds-find-caselaw-docs/public` | Verified live this session |
| legislation.gov.uk data API | UK primary legislation - full text, XML/RDF/Atom feeds | No key needed - append `.data.xml` / `.data.feed` / `.data.rdf` to any legislation URL, docs at `legislation.github.io/data-documentation` | Verified live this session |
| EUR-Lex / CELLAR SPARQL endpoint | EU treaties, regulations, directives, decisions, CJEU rulings as RDF | Public SPARQL endpoint needs no key; the fuller EUR-Lex web-services layer needs registration | Verified live this session |
| Légifrance (via PISTE, run by DILA) | French codes, statutes, consolidated law | Free registration required at `piste.gouv.fr` | Verified live this session |
| Federal Register API (US) | US federal regulatory notices/rules, 1994-present | No key needed | Verified live this session |
| Regulations.gov API (US) | US federal rulemaking dockets and public comments | Free API key via `api.data.gov` | Verified live this session |
| CanLII API | Canadian federal + provincial case law and legislation metadata | Read-only REST API, but requires applying for a key and explaining project scope - not instantly open | Verified live this session |

None of these are wired into a jurisdiction pack's live-verification story yet beyond the note above - adding one means: (1) updating the relevant `../jurisdictions/<slug>/README.md` "primary sources" section with the exact endpoint, (2) deciding whether it needs a stored API key (this repo has no secrets-handling mechanism, so a keyed connector would need the user's own environment to supply it, never committed here), and (3) writing the actual request/parse logic if a Python helper is wanted rather than relying on an agent's own WebFetch. Not built in this pass - flagging as the concrete next step for widening verified coverage, per `../docs/HONEST_STATUS.md`'s roadmap.

## Principle

Never hard-code a requirement for a specific commercial database. If a connector is available in the running session, use it and say so. If not, fall back to WebSearch/WebFetch against the jurisdiction pack's named primary sources, or say `NO_VERIFIED_AUTHORITY_LOCATED` and ask the user to supply sources, rather than silently degrading to unverified recall.

## Status

Genuinely usable today: the CourtListener note above, and the general WebSearch/WebFetch fallback (which depends on the session actually running those tools, not on anything this repository provides). Everything else in the original spec's "research provider abstraction" (a formal plugin interface for new connectors) is unbuilt - see `../docs/HONEST_STATUS.md`.
