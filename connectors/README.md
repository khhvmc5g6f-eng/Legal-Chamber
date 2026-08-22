# Connectors

Abstraction layer notes for research data sources. This repository does not hard-code credentials or a required commercial database - it documents which connector to reach for, per jurisdiction, and what to do when none is available.

## What's actually connected in a Claude Code session (not this repo's doing - session-dependent)

| Source | Status | Notes |
|---|---|---|
| CourtListener (RECAP dockets, opinions, judges, oral arguments) | Usable if the session has this MCP server connected | US federal + some state coverage. See `../jurisdictions/us-federal/README.md`. |
| Official legislation/judgment sites (legislation.gov.uk, BAILII/Find Case Law, AustLII, CanLII, NZLII, Légifrance, BOE, EUR-Lex, etc.) | Reachable via WebSearch/WebFetch in a Claude Code session | Not a dedicated connector - live web research each time, and each jurisdiction pack names the specific sites to prefer. |
| Westlaw / Lexis / vLex / HeinOnline | Not connected in this build | Would require the user's own subscription and an MCP/API integration this repository does not ship. |

**BAILII specifically is read-only, single-document access at most.** Its own `robots.txt` disallows `/eu`, `/ew`, `/ie`, `/je`, `/nie`, `/scot`, `/sh`, `/uk`, `/wales`, `/worldlii` - most of its actual content directories - for every user agent, and its terms of use prohibit bulk downloading and scraping "by software agents compiling knowledge bases." A block from BAILII (typically HTTP 403) is final: do not retry via a proxy, cache, archive mirror, or any other workaround - see `../docs/OPERATING_RULES.md`'s "Verification hierarchy for authority." Fall back to a citing judgment on Find Case Law that quotes/applies the same case instead, or mark the citation `UNVERIFIED`.

**AustLII specifically bars AI/automated use in its own published usage policy** - not just a robots.txt block but an explicit term ("AI-related or automated purposes" are named as not permitted). Do not build a scraper or connector against AustLII; if Australian case law needs verifying, the honest answer today is `UNVERIFIED` pending either an authorized-access arrangement or a future Federal Register of Legislation connector for statute text (no equivalent exists yet for AustLII's case-law holdings).

## Additional open APIs identified but not yet wired in (checked live via WebFetch/WebSearch, not yet integrated as a connector)

| Source | Coverage | Access | Confidence |
|---|---|---|---|
| Find Case Law (National Archives) | UK court/tribunal judgments as structured data (LegalDocML XML) | No key needed for reading/citing a specific judgment - REST-ish endpoints, docs at `nationalarchives.github.io/ds-find-caselaw-docs/public`. **Correction to an earlier version of this file: the Open Justice Licence covers single-document reuse, but its own text states "you need to apply for a licence to do computational analysis of Find Case Law records" - bulk/computational use is NOT covered by the same free-reuse terms as reading one judgment.** A connector built against this source should fetch per-citation, never in bulk, without a separate licence. | Verified live, license text re-checked and corrected |
| judiciary.uk | Practice Directions and guidance - **has a genuine structured WordPress REST API** (`wp-json/wp/v2/`) with dedicated `guidance` and `judgment` post types, not just an HTML document library as an earlier pass assumed | No key confirmed needed for reads; exact reuse terms for the content itself not independently confirmed, treat as OGL-equivalent pending a direct check | Verified live that the API exists; licence terms unconfirmed |
| legislation.gov.uk data API | UK primary legislation - full text, XML/RDF/Atom feeds | No key needed - append `.data.xml` / `.data.feed` / `.data.rdf` to any legislation URL, docs at `legislation.github.io/data-documentation`. The dataset's own docs admit it "is not yet complete" - don't assume full coverage. | Verified live |
| eCFR API (`ecfr.gov`) | Live, current-as-of-date text of the US Code of Federal Regulations | No key needed - public domain (US government work) | Verified live, endpoint hit directly and returned real content |
| GovInfo API (`api.govinfo.gov`) | US Code (USLM XML), Federal Register, Statutes at Large, Congressional bills/reports, CFR | Free key via `api.data.gov` signup - public domain data, but the API *client* repo (`github.com/usgpo/api`) itself has no clear license, so don't vendor its code without checking that separately from the data | Verified live |
| Judilibre (Cour de cassation, France) | Pseudonymized decisions of France's highest ordinary court, structured (facts/arguments/reasoning/ruling) | Open Licence 2.0, OAuth2 registration via `piste.gouv.fr` - sandbox and production endpoints both documented at `github.com/Cour-de-cassation/judilibre-search` | Verified live |
| Légifrance (via PISTE, run by DILA) | French codes, statutes, consolidated law, plus Conseil d'État/Conseil constitutionnel case law | Free registration required at `piste.gouv.fr`, OAuth2, stable since April 2023 | Verified live |
| CanLII API | Canadian federal + provincial case law and legislation metadata, including citation graphs | Read-only REST API, but requires applying for a key by email and explaining project scope - not instantly open | Verified live (official docs at `github.com/canlii/API_documentation`) |
| Justice Laws bulk XML (Canada) | Consolidated federal Acts and Regulations, updated roughly biweekly | Fully open - GitHub-mirrored (`github.com/justicecanada/laws-lois-xml`), no key | Verified via search corroboration |
| New Zealand Legislation Developer API | Acts, Legislative Instruments, Bills | Free key via email request; the API's own maintainers label it "Version Zero" - a pre-release/feedback-stage contract, not a stable guarantee | Verified via search corroboration |
| BOE Open Data API (Spain) | Consolidated Spanish legislation, daily gazette summaries | Appears to need no key (GET-based REST, XML/JSON) - strong search corroboration but not independently fetched live, re-confirm directly before treating as fully verified | Medium-high confidence, not directly fetched |
| EUR-Lex / CELLAR (SPARQL + REST webservices) | EU treaties, regulations, directives, decisions, CJEU rulings, plus ECLI/ELI identifiers | Public SPARQL endpoint needs no key; the fuller EUR-Lex web-services layer needs registration; exact current reuse-licence wording should be re-fetched directly before being cited as settled | Verified live, licence text needs a follow-up re-check |
| Federal Register API (US) | US federal regulatory notices/rules, 1994-present | No key needed | Verified live |
| Regulations.gov API (US) | US federal rulemaking dockets and public comments | Free API key via `api.data.gov` | Verified live |

**Confirmed NOT to have a usable public API, don't attempt one:** AustLII (usage policy explicitly bars automated/AI use, see above), NZLII (no API found, likely inherits AustLII's affiliated policy though not independently confirmed for NZLII's own terms), legislation.gov.au (document-by-document only, no public API found despite searching), CENDOJ/Spain case law (free search only - its own regulation explicitly prohibits bulk/commercial reuse without a formal CGPJ request), CURIA/InfoCuria (relaunched January 2026, still explicitly no bulk download or public API per its own site).

**ECLI (European Case Law Identifier)** - confirmed real, current, and actively governed across all 27 EU member states, not deprecated. `scripts/citation_lint.py`'s `ecli` pattern now recognises the shape (`ECLI:XX:court:year:id`) across the France, Spain, and EU jurisdiction packs at once - shape recognition only, the same caveat as every other pattern in that file: it doesn't confirm the underlying decision exists or holds what it's cited for.

None of the sources above are wired into a jurisdiction pack's live-verification story as a formal connector yet (CourtListener remains the only one with that status) - adding one means: (1) updating the relevant `../jurisdictions/<slug>/README.md` "primary sources" section with the exact endpoint, (2) deciding whether it needs a stored API key (this repo has no secrets-handling mechanism, so a keyed connector would need the user's own environment to supply it, never committed here), and (3) writing the actual request/parse logic if a Python helper is wanted rather than relying on an agent's own WebFetch. Canada (CanLII) and France (Judilibre) are the strongest near-term candidates - both have real, documented, structurally CourtListener-like APIs.

## Principle

Never hard-code a requirement for a specific commercial database. If a connector is available in the running session, use it and say so. If not, fall back to WebSearch/WebFetch against the jurisdiction pack's named primary sources, or say `NO_VERIFIED_AUTHORITY_LOCATED` and ask the user to supply sources, rather than silently degrading to unverified recall.

## Status

Genuinely usable today: the CourtListener note above, and the general WebSearch/WebFetch fallback (which depends on the session actually running those tools, not on anything this repository provides). Everything else in the original spec's "research provider abstraction" (a formal plugin interface for new connectors) is unbuilt - see `../docs/HONEST_STATUS.md`.
