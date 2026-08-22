---
jurisdiction: Canada
legal_system: mixed (common-law federal + provinces, except Quebec which is civil-law for private law)
verification_status: STRUCTURAL_DRAFT
last_reviewed: 2026-08-22
reviewer: initial repository build (not independently re-checked by a second reviewer)
---

# Canada

See `docs/HONEST_STATUS.md`. Canada is a federation with 10 provinces and 3 territories. **Quebec is a civil-law jurisdiction for private law** (its own Civil Code of Quebec), while the rest of Canada is common-law - never apply common-law reasoning structures to a Quebec private-law question. Criminal law is federal (Criminal Code of Canada) and applies uniformly, but procedure and civil law are provincial.

## Court hierarchy (headline)

```
Supreme Court of Canada (final appellate court for the whole federation)
  └── Federal Court of Appeal / Provincial Courts of Appeal
        └── Federal Court / Provincial Superior Courts (trial courts of general/inherent jurisdiction)
              └── Provincial/Territorial Courts (lower-tier, including most criminal first appearances)
```

## Authority hierarchy

The Supreme Court of Canada binds all Canadian courts. A provincial Court of Appeal binds courts below it within that province; other provinces' appellate decisions are persuasive. Quebec's Court of Appeal decisions on private-law (civil-law) matters do not transpose to common-law provinces and vice versa.

## Citation style

**McGill Guide** (Canadian Guide to Uniform Legal Citation) is the standard style. Case citation shape uses neutral citation, e.g. `Party v Party, 2023 SCC 12`. Statute citation: `Short Title, Statute Volume Reference, c Chapter, s Section`.

## Governing statutes/codes (named, not summarised)

Criminal Code of Canada (federal, uniform). Civil Code of Quebec (Quebec private law only). Common-law provinces: no single civil code; provincial statutes plus common law. Key procedural instruments by name only: each province's own Rules of Civil Procedure (naming and numbering differ by province), the Federal Courts Rules.

## Primary sources to check against

- `canlii.org` (CanLII) - federal and provincial legislation and case law
- `laws-lois.justice.gc.ca` - official federal statutes
- Each province's own official legislation site (e.g. Quebec's `legisquebec.gouv.qc.ca`) and court site

## Live verification capability - CanLII API (documented, not yet wired)

CanLII has a real, documented read-only REST API (`github.com/canlii/API_documentation`, confirmed live via direct fetch 2026-08-22) - case browsing/metadata, citation graphs (what cites what, structurally similar to CourtListener's `opinions-cited`), and legislation browsing. **Access requires a free API key obtained by emailing CanLII and describing the project's scope - not a self-serve signup**, so this repository cannot obtain one autonomously; a human needs to request it. Constraints once obtained: HTTPS only, 10MB max response, 10,000 results/request cap. Once a key exists, wiring this in means: (1) confirming the exact endpoint shapes against the live docs (they may have changed since this check), (2) deciding where the key is supplied (this repo has no secrets-handling mechanism - it would need to come from the user's own environment, never committed here), (3) documenting the connector here the way `../us-federal/README.md` documents CourtListener. See `../../connectors/README.md` for the full cross-jurisdiction connector inventory.

## What is NOT in this pack

No province-specific procedural content verified. No populated Authority Graph. No verified procedural deadline. No Quebec civil-law doctrinal depth beyond noting it is a distinct system.
