---
jurisdiction: United States - Federal
legal_system: common-law
verification_status: STRUCTURAL_DRAFT
last_reviewed: 2026-08-22
reviewer: initial repository build (not independently re-checked by a second reviewer)
---

# United States - Federal

See `docs/HONEST_STATUS.md`. This pack covers the **federal** system only. Each of the 50 states plus DC and the territories has its own separate court system, procedural rules, and much of its own substantive law (contract, tort, property, family, most criminal law) - a federal-only pack must never be used to answer a state-law question. State packs are not built in this version; treat any state-law question as `NO VERIFIED AUTHORITY LOCATED` until a state pack exists or live research is done.

## Court hierarchy

```
Supreme Court of the United States
  └── U.S. Courts of Appeals (13 circuits: 1st-11th, D.C. Circuit, Federal Circuit)
        └── U.S. District Courts (94 districts; trial courts of general federal jurisdiction)
Specialized: U.S. Tax Court, U.S. Court of Federal Claims, U.S. bankruptcy courts (units of the district courts), agency ALJs with their own appeal routes
```

## Authority hierarchy

Binding: Supreme Court binds all federal (and state) courts on federal-law questions; a Court of Appeals decision binds the district courts within its own circuit only (a circuit split is a real and recurring phenomenon - never assume one circuit's holding binds another). Persuasive: out-of-circuit Court of Appeals decisions, district court decisions generally (even within the same circuit, one district judge's decision does not bind another).

## Citation style

**Bluebook** is the standard style. Case citation shape: `Party v. Party, Volume Reporter Page (Court Year)`, e.g. `Smith v. Jones, 123 F.4th 456 (9th Cir. 2024)`. Statute citation: `Title U.S.C. § Section`.

## Governing statutes/codes (named, not summarised)

United States Code (federal statutes, organized by Title), Code of Federal Regulations (federal agency regulations). Key procedural instruments by name only: Federal Rules of Civil Procedure (FRCP), Federal Rules of Criminal Procedure, Federal Rules of Evidence, Federal Rules of Appellate Procedure, and each district's own Local Rules.

## Live verification capability - CourtListener

**This is the one jurisdiction pack in this build with a genuine live research connector available in a Claude Code session that has the CourtListener MCP server connected.** Use it instead of relying on training-data recall:

- `search` across RECAP dockets, opinions, judges, and oral arguments.
- `get_endpoint_schema` + `call_endpoint` for structured lookups on a specific docket, cluster, court, or party once you have an ID from `search`.
- Field names differ between `search` results (camelCase, e.g. `caseName`) and the REST API (`snake_case`, e.g. `case_name`) - check the schema before reusing a field name across tools.

A citation is not verified merely because CourtListener's index contains something matching the party names - confirm court, date, and that the retrieved opinion actually supports the proposition it is being cited for, per `docs/OPERATING_RULES.md`.

## Primary sources to check against

- CourtListener (`courtlistener.com`) - via the MCP connector above, or directly
- `govinfo.gov` - official U.S. Code, CFR, and court opinions
- Each circuit's and district's own official site for local rules

## What is NOT in this pack

No state-law coverage. No verified procedural deadline - FRCP/local-rule deadlines must be checked live.

## Populated Authority Graph (starter)

`authority-graph.json` in this directory is the repository's first real, populated Authority Graph entry - 2 cases, 1 verified `FOLLOWS` edge, on the Computer Fraud and Abuse Act's "exceeds authorized access" question (*United States v. Nosal*, 676 F.3d 854 (9th Cir. 2012) (en banc), and *Van Buren v. United States*, 593 U.S. 374 (2021)). Every field, including the edge itself, was verified live against CourtListener on 2026-08-22, not recalled from training data - see the file's own `verification_method` field. It is deliberately narrow (one doctrinal question, not a general database) rather than broad-but-unverified - see `docs/HONEST_STATUS.md`.
