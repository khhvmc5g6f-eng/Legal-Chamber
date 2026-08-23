---
jurisdiction: France
legal_system: civil-law
verification_status: STRUCTURAL_DRAFT
last_reviewed: 2026-08-22
reviewer: initial repository build (not independently re-checked by a second reviewer); a populated Authority Graph was added the same day via four parallel-agent research passes, each independently re-verified against a live primary source by the orchestrating session before being written - see "Populated Authority Graph" below
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

## Populated Authority Graph

`authorities/` holds four doctrinal files across four subjects - France's first Authority Graph content in this repository. Each entry quotes the original French code text and case reasoning verbatim, with an English paraphrase, following the civilian doctrinal method described above (starting from the code article, not from precedent).

| File | Subject | Lead case |
|---|---|---|
| `authorities/civil-delictual-liability-objective-fault-standard.json` | Civil Liability - article 1240 CC's objective fault standard, not dependent on the actor's capacity for *discernement* | *Cass. Ass. plén.*, 9 mai 1984 (arrêt *Derguini*), n° 80-93.481 |
| `authorities/criminal-legitime-defense-proportionality-last-resort.json` | Criminal Law - the necessity/proportionality test of *légitime défense* under article 122-5, applied to a law-enforcement officer's lethal force | *Cass. crim.*, 9 janvier 2018, n° 16-86.552 |
| `authorities/labour-dismissal-cause-reelle-serieuse.json` | Employment Law - the *cause réelle et sérieuse* threshold for personal-reason dismissal, and an employer's prior toleration not barring reliance on it later | *Cass. soc.*, 12 juin 2024, n° 23-14.292 |
| `authorities/administrative-detournement-de-pouvoir.json` | Administrative Law/Judicial Review - the *détournement de pouvoir* ground, a distinctively French ground of review with no direct common-law equivalent | *CE*, 26 novembre 1875, n° 47544 (known in doctrine as arrêt "Pariset") |

Deliberately narrow, matching the same one-or-two-doctrinal-points-per-file discipline used throughout this repository's other jurisdictions. Unlike Spain's research passes, France's sourcing was clean: `legifrance.gouv.fr`'s codes and jurisprudence databases fetched successfully on every attempt across all four research passes, with no network-level block, DNS failure, or CAPTCHA gate encountered at all - all four entries are `VERIFIED_PRIMARY_SOURCE` on every node, a direct counterpoint to Spain's genuine BOE/CENDOJ access constraints. The one honesty note worth recording: the *détournement de pouvoir* file's foundational 1875 judgment is anonymised in the primary Légifrance text (the applicant appears only as "le sieur X..."), and the doctrinal name "Pariset" is a secondary-literature convention not present in the primary source itself - recorded as such rather than presented as text that appears in the judgment. The researching agent also investigated and correctly rejected a second candidate case (*Barel*, CE Ass., 28 mai 1954) once direct verification showed its actual annulment ground was *erreur de droit*, not *détournement de pouvoir*.

## What is NOT in this pack

No verified procedural deadline. No verified content beyond the four entries above - Civil Procedure, Commercial Law, and the remaining Administrative Law/Judicial Review grounds (incompétence, vice de forme, violation de la loi) all remain unbuilt.
