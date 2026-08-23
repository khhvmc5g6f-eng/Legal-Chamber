---
jurisdiction: Spain
legal_system: civil-law
verification_status: STRUCTURAL_DRAFT
last_reviewed: 2026-08-22
reviewer: initial repository build (not independently re-checked by a second reviewer); a populated Authority Graph was added the same day via four parallel-agent research passes, each independently re-verified where reachable against a live primary source by the orchestrating session before being written - see "Populated Authority Graph" below
---

# Spain

See `docs/HONEST_STATUS.md`. **Do not apply common-law reasoning structures here** (`docs/OPERATING_RULES.md`, "civil law mode"). Codified statute is the primary source of law; case law (*jurisprudencia*) informs interpretation and, in the case of the Supreme Court's *doctrina reiterada* (settled repeated case law, generally two or more consistent rulings), carries real interpretive weight, but the doctrinal method starts from the code text and its systematic structure, not from working outward from precedent. Spain is also organised into 17 Autonomous Communities, several of which have their own civil-law regimes (*derechos forales/civiles autonómicos*, e.g. Catalonia, Aragón, the Basque Country, Navarre, Galicia, Balearic Islands) that displace the general Civil Code in their territory for the matters they cover - this pack does not verify any autonomous-community-specific content.

## Court hierarchy (headline)

```
Tribunal Constitucional (Constitutional Court - constitutional review, not part of the ordinary judiciary)
Tribunal Supremo (Supreme Court - highest ordinary court, organised into five chambers: civil, criminal, administrative, labour/social, military)
  └── Tribunales Superiores de Justicia (one per Autonomous Community - appellate + some first instance for regional-law matters)
        └── Audiencias Provinciales (provincial appellate courts, civil and criminal)
              └── Juzgados de Primera Instancia / Juzgados de lo Penal / Juzgados de lo Social (first-instance courts by subject matter)
```

## Authority hierarchy / doctrinal method

Primary sources rank: the Constitution, EU law where applicable (Spain is an EU member state - see `../eu/README.md`, not duplicated here), then the Civil Code (*Código Civil*) and other codes (*Código Penal*, *Código de Comercio*, etc.) and statutes (*leyes orgánicas* then *leyes ordinarias*), then regulations (*reglamentos*). *Jurisprudencia* from the Tribunal Supremo is not formally binding precedent in the common-law sense, but *doctrina reiterada* is treated as authoritative guidance on how a code provision is to be interpreted, and departing from it requires justification. *Doctrina* (academic legal commentary) is a genuine, citable secondary source in Spanish practice, not merely persuasive colour.

## Citation style

Spanish legal citation conventions differ from OSCOLA/Bluebook: statutes are cited by name and date (e.g. `Código Civil, art. 1902`), and case law by court, chamber, date, and *número de recurso* or ECLI identifier (e.g. `STS 123/2023, de 15 de enero`).

## Governing codes (named, not summarised)

Código Civil (1889, much amended), Código Penal, Ley de Enjuiciamiento Civil (LEC - civil procedure), Ley de Enjuiciamiento Criminal (LECrim - criminal procedure), Estatuto de los Trabajadores (labour). Content not verified in this pack - check the current consolidated text live.

## Primary sources to check against

- `boe.es` (Boletín Oficial del Estado) - official consolidated legislation
- `poderjudicial.es` (CENDOJ) - official case-law database
- Autonomous-community official gazettes for regional civil-law regimes

## Populated Authority Graph

`authorities/` holds four doctrinal files across four subjects - Spain's first Authority Graph content in this repository, and this repository's first civil-law jurisdiction with populated content. Each entry quotes the original Spanish code text and case reasoning verbatim, with an English paraphrase, following the civilian doctrinal method described above (starting from the code article, not from precedent).

| File | Subject | Lead case |
|---|---|---|
| `authorities/contract-formation-good-faith-integration.json` | Contract/Obligations - article 1258 CC's good-faith integration principle | *STS 801/2025*, de 20 de mayo de 2025 |
| `authorities/civil-extracontractual-liability-fault-based-boundary.json` | Civil Liability - article 1902 CC's fault-based boundary against objectivised liability | *STS 149/2007*, de 22 de febrero de 2007 |
| `authorities/criminal-legitima-defensa-agresion-ilegitima.json` | Criminal Law - the *agresión ilegítima* requirement of *legítima defensa* | *STS 140/2010* (Sala de lo Penal) |
| `authorities/labour-dismissal-prior-hearing-ilo-convention.json` | Employment Law - the ILO Convention 158 prior-hearing requirement for disciplinary dismissal | *STS 1250/2024* (Sala de lo Social, Pleno) |

Deliberately narrow, matching the same one-or-two-doctrinal-points-per-file discipline used throughout this repository's other jurisdictions. The dominant access-pattern finding this session, confirmed consistently across all four research passes: **boe.es returned a connection-level `ECONNREFUSED` error, and poderjudicial.es/cendoj.poderjudicial.es returned DNS resolution failure (`ENOTFOUND`)**, or presented a CAPTCHA bot-detection gate on the document-view route specifically. This is a genuine network-level block on these two government domains from this environment, not a source-specific 403/404 or a quality judgment on the sources themselves. Per this repository's rules, no research pass attempted a proxy workaround. Each instead corroborated its statutory and case-law content via multiple independent secondary sources (Iberley, Conceptos Jurídicos, vLex, academic case notes, law-firm commentary), and - where a case was live-fetchable at the metadata level (CENDOJ's search-results page, or the Poder Judicial press page) but not at the full-text level - recorded the metadata as primary-verified and the substantive quotes as secondary-corroborated, a split-tier honesty pattern unique to this jurisdiction's access constraints. This session's own independent WebSearch corroboration further confirmed every node's core substance before each file was written.

## What is NOT in this pack

No verified procedural deadline. No autonomous-community-specific civil law content beyond the general Código Civil entries above.
