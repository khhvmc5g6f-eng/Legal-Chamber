---
jurisdiction: France
legal_system: civil-law
verification_status: STRUCTURAL_DRAFT
last_reviewed: 2026-08-22
reviewer: initial repository build (not independently re-checked by a second reviewer)
---

# France

See `docs/HONEST_STATUS.md`. **Do not apply common-law reasoning structures here.** French law is organised around a strict separation between the ordinary judiciary (private law and criminal matters) and the administrative order (claims against public administration), each with its own supreme court - this split has no equivalent in most common-law systems and is easy to get wrong by analogy.

## Court hierarchy (headline)

```
ORDINARY ORDER (private law, criminal)                ADMINISTRATIVE ORDER (public law)
Cour de cassation (highest ordinary court)             Conseil d'État (highest administrative court, also government adviser)
  └── Cours d'appel                                       └── Cours administratives d'appel
        └── Tribunaux judiciaires (civil) /                     └── Tribunaux administratifs
            Tribunaux de police / correctionnels (criminal)

Conseil constitutionnel - constitutional review, separate from both orders, not a general court of appeal
```

A jurisdictional dispute over which order a claim belongs to is itself resolved by the **Tribunal des conflits** - a real and non-obvious procedural trap if the wrong order is chosen.

## Authority hierarchy / doctrinal method

Primary sources rank: the Constitution, ratified treaties/EU law - see `../eu/README.md`, which this pack does not duplicate - (which under Article 55 of the Constitution take precedence over ordinary statute), codified statute (*lois*, organised into codes: Code civil, Code pénal, Code de commerce, Code du travail, etc.), then regulations (*décrets*, *arrêtés*). Case law (*jurisprudence*) is not formally binding precedent - French courts are not bound by their own prior decisions in the common-law sense - but a consistent line of Cour de cassation or Conseil d'État decisions (*jurisprudence constante*) carries strong practical authority and departing from it invites cassation. *Doctrine* (academic commentary) is a genuine, actively cited secondary source shaping how codal provisions are understood.

## Citation style

French legal citation differs from OSCOLA/Bluebook: statutes/codes are cited by article number within the named code (e.g. `art. 1240 C. civ.`), and case law by court, chamber, and date (e.g. `Cass. civ. 1re, 15 janv. 2023, n° 21-12.345`) or by ECLI identifier for more recent decisions.

## Governing codes (named, not summarised)

Code civil (1804, much amended - notably the 2016 reform of the law of obligations), Code pénal, Code de procédure civile, Code de procédure pénale, Code du travail, Code de commerce. Content not verified in this pack - check the current consolidated text live.

## Primary sources to check against

- `legifrance.gouv.fr` - official consolidated legislation and case law
- `conseil-etat.fr` / `courdecassation.fr` - official decisions of the two supreme courts
- `conseil-constitutionnel.fr` - constitutional decisions

For data-protection/regulatory matters specifically, see `../../regulators/cnil.md` - a real, sourced profile of CNIL's investigation stages, sanction range, and appeal route (to the Conseil d'État, not an ordinary court).

## Live verification capability - Judilibre and Légifrance/PISTE (documented, not yet wired)

Two real, documented APIs exist. **Judilibre** (`github.com/Cour-de-cassation/judilibre-search`, Cour de cassation's own open API) publishes pseudonymized decisions with structured sections (facts/arguments/reasoning/ruling) - confirmed live 2026-08-22. **Légifrance/PISTE** (DILA) covers codes, consolidated legislative/regulatory text, JORF, and Conseil d'État/Conseil constitutionnel/appellate case law - confirmed live and stable since April 2023. Both require free registration and OAuth2 authentication via `piste.gouv.fr` - **a human needs to complete that registration**, this repository cannot obtain credentials autonomously. Once a credential exists, wiring either in means: (1) re-confirming the exact endpoint shapes against the live docs, (2) supplying the credential from the user's own environment (never committed here, this repo has no secrets-handling mechanism), (3) documenting the connector here the way `../us-federal/README.md` documents CourtListener. See `../../connectors/README.md` for the full cross-jurisdiction connector inventory.

## What is NOT in this pack

No populated jurisprudence database. No verified article-level code content. No verified procedural deadline.
