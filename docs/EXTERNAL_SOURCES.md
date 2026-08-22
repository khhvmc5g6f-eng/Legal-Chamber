# External sources - what's usable, what isn't

A research pass (2026-08-22) checked a wide range of external legal-data, document-standard, dictionary, and dataset sources for whether this repo could incorporate them. This file records what was found so the same ground doesn't get silently re-covered, and - more importantly - so nobody later reaches for one of the "not usable" entries below without checking here first. See `connectors/README.md` for live-data-API findings (case law, legislation); this file covers document standards, dictionaries, ontologies, and benchmark datasets.

## Document/citation markup standards

| Standard | Status | Notes |
|---|---|---|
| USLM (US Legislative Markup) | Real, actively maintained, US government work | Target structure for citing US statutes precisely - see `github.com/usgpo/uslm` |
| ECLI / ELI (EU identifiers) | Real, current, standardised across all 27 EU member states | Now encoded as `scripts/citation_lint.py`'s `ecli` pattern |
| Akoma Ntoso / LegalDocML (OASIS) | The standard itself is alive (OASIS TC active, AKN 3.1 comment period announced July 2026) - **but its reference GitHub repo (`oasis-open/legaldocml-akomantoso`) hasn't been pushed to since 2022.** Cite the OASIS TC page for "the standard is alive," never the repo's commit history. | Structural target only if this repo ever exports verified drafts as machine-readable XML - not built |
| LegalXML Electronic Court Filing (ECF) | Real OASIS spec, published Nov 2023 | Not near-term relevant - no e-filing workflow exists in this repo |

## Dictionaries and glossaries

**Black's Law Dictionary (and Ballentine's) - DO NOT USE.** The current edition (12th, 2024) is actively copyrighted by Thomson Reuters. Only the 1910 2nd edition is public domain, and it's too outdated to cite as current law. There is no legitimate path to reproduce a current Black's definition anywhere in this repo - if a skill or draft is tempted to "recall" one from training data and present it as sourced, that is exactly the kind of fabrication `docs/OPERATING_RULES.md` exists to prevent.

**Cornell Wex - non-commercial only.** `law.cornell.edu/wex` is CC BY-**NC**-SA 2.5, confirmed directly from Cornell's own terms page. Fine as a citable research reference during live lookup (the way any secondary source gets cited); **not** fine to bundle or reproduce as a standalone glossary dataset in this repo, since that would be a redistribution use, not a citation use, and this repo doesn't currently gate that distinction anywhere else that would make the NonCommercial term self-evidently satisfied.

**No genuinely open, current, general-purpose legal-terms dictionary was found.** Search surfaced curated *link lists* of legal datasets, not a standalone open dictionary itself. This is a real gap, not a resource to force a fit onto.

## Ontologies - weak fit, don't force it

LegalRuleML (OASIS, ratified Sept 2021) and LKIF-core (EU ESTRELLA project, CC BY 4.0 as of a 2026 relicensing pass) are both real, formally documented ontologies for machine-readable legal rules. Both are **substantively dormant** - LegalRuleML's reference repos last had real commits in 2020 and 2018; LKIF-core's last substantive content update was 2008 (a 2026 release was licence/format housekeeping only, not new ontology work). Adopting either would mean building a genuine formal defeasible-logic reasoning layer, which is a different kind of project than this repo's current verify-and-draft scope. Not recommended near-term; recorded so the option isn't silently missed if the repo's scope ever changes.

## Benchmark and training datasets

| Dataset | License | Status |
|---|---|---|
| CUAD (Contract Understanding Atticus Dataset) | CC-BY-4.0, confirmed | **Used** - its 41-category clause taxonomy informed `skills/legal-contract/SKILL.md`'s clause-extraction checklist, see that file's own note on what was added and why |
| ContractNLI | CC BY-4.0, confirmed | Same family as CUAD (clause entailment/contradiction framing) - not yet used, a candidate for a future contract-review pass |
| LexGLUE | License unclear at the aggregate level - component datasets carry their own separate terms | Case-selection methodology could inform `benchmarks/`, but don't assume the aggregate is uniformly open - check each component before reuse |
| LegalBench | License unconfirmed (no top-level LICENSE file found) | Task *taxonomy* (not its data) is a reusable format for `rubrics/`/`evaluations/`, both currently stub-only - don't redistribute its actual data without confirming licence first |
| Pile of Law | CC-BY-NC-SA-4.0, "research purposes only" per its own dataset card | **Not usable** in a practitioner-facing tool - citable as a pointer only |

## Confirmed-blocked or restricted data sources

See `connectors/README.md` for the full list and reasoning (BAILII, AustLII, CENDOJ, CURIA, NZLII). The short version: a source's own published access terms are binding regardless of how narrow or well-intentioned the intended use is - `docs/OPERATING_RULES.md`'s "Verification hierarchy for authority" section states this as a rule, not a suggestion, after a live research pass found two agents bypassing a block (a third-party proxy, and opening a blocked URL in a different tool after the direct fetch was refused) to reach content whose source had just declined to serve it.
