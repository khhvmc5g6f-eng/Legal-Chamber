---
jurisdiction: European Union (supranational)
legal_system: sui generis - treaty-based supranational law overlaying member states' own civil/common-law systems
verification_status: STRUCTURAL_DRAFT
last_reviewed: 2026-08-23
reviewer: added during a stress-test pass after a live matter simulation found the gap - no member-state pack (e.g. France, Spain) can substitute for EU-level authority; a populated Authority Graph was added 2026-08-23 via four parallel-agent research passes, each independently re-verified against a live primary source by the orchestrating session before being written - see "Populated Authority Graph" below
---

# European Union

See `docs/HONEST_STATUS.md`. This pack exists because EU law is **directly applicable and supranational** - a country pack like `../france/README.md` or `../spain/README.md` covers that country's own courts and domestic law, but cannot substitute for EU-level instruments (Regulations, which apply directly without national implementing legislation) or EU-level authority (the Court of Justice of the European Union). Do not answer an EU-law question (GDPR, competition law, free movement, etc.) using only a member state's pack - both levels are usually in play.

## Court hierarchy

```
Court of Justice of the European Union (CJEU), composed of:
  Court of Justice - preliminary rulings (referred from national courts), direct actions,
                     and appeals from the General Court
  General Court - first instance for most direct actions (competition, state aid, trade mark,
                  actions against EU institutions)
```

National courts are not part of this hierarchy but interact with it constantly via the preliminary reference procedure (Article 267 TFEU) - a national court can (and sometimes must) refer a question of EU law to the CJEU before deciding a case itself.

## Authority hierarchy

Treaties (TEU, TFEU, Charter of Fundamental Rights) rank highest, then Regulations (directly applicable in every member state without national implementing legislation - GDPR is a Regulation), then Directives (bind member states as to the result to be achieved, but require national implementing legislation - a Directive's exact effect in a given country depends on how that country implemented it, so check the national implementing law too), then Decisions (binding on those to whom addressed). CJEU rulings on the interpretation of EU law bind national courts within their scope - this is closer to binding precedent than most EU member states' own domestic doctrine (see `../france/README.md`'s note that French domestic jurisprudence is not formally binding in the common-law sense - CJEU rulings on EU law are a distinct, more binding layer on top of that).

## Citation style

CJEU cases are cited by case number and party names, e.g. `Case C-311/18, Data Protection Commissioner v Facebook Ireland Ltd (Schrems II), EU:C:2020:559` - the `EU:C:` identifier is the European Case Law Identifier (ECLI) and is the most reliable pinpoint. Regulations/Directives are cited by type, number, and year, e.g. `Regulation (EU) 2016/679 (GDPR)`.

## Governing instruments relevant across most matters (named, not summarised)

Treaty on European Union (TEU), Treaty on the Functioning of the European Union (TFEU), Charter of Fundamental Rights of the European Union. Regulation (EU) 2016/679 (General Data Protection Regulation) is the most commonly relevant Regulation for data-protection matters - see `../france/README.md` for how this interacts with French-specific data-protection law (CNIL, the French Data Protection Act) rather than replacing it.

## Primary sources to check against

- `curia.europa.eu` - CJEU judgments and case law
- `eur-lex.europa.eu` - official consolidated EU legislation (see `../../connectors/README.md` for the public SPARQL/CELLAR endpoint, verified live)
- Each relevant national data-protection or sectoral regulator's own site for how a Regulation/Directive was actually implemented or applied domestically (e.g. `cnil.fr` for France)

## Populated Authority Graph

`authorities/` holds four foundational entries - the EU's first Authority Graph content in this repository, added the same day the last other jurisdiction (France) closed out, making this the ninth and final jurisdiction pack in this repository to move off zero.

| File | Subject | Lead case |
|---|---|---|
| `authorities/primacy-of-eu-law-costa-v-enel.json` | Constitutional - the primacy of EU law over conflicting national law | *Costa v ENEL*, Case 6/64 |
| `authorities/free-movement-mutual-recognition-cassis-de-dijon.json` | Free Movement of Goods - TFEU art.34 and the mutual-recognition principle | *Cassis de Dijon*, Case 120/78 |
| `authorities/competition-abuse-of-dominance-intel-as-efficient-competitor.json` | Competition - TFEU art.102 and the as-efficient-competitor test for loyalty rebates | *Intel v Commission*, C-413/14 P |
| `authorities/data-protection-international-transfers-schrems-ii.json` | Data Protection - GDPR arts.45-46's international-transfer mechanisms | *Schrems II*, C-311/18 |

All four entries are `VERIFIED_PRIMARY_SOURCE` on every node. `curia.europa.eu`'s own InfoCuria document viewer returned only a JS-rendering shell to a plain fetch on two of the four cases (Intel, Schrems II) - not a CAPTCHA or bot-block, a client-side rendering requirement - worked around with a genuine in-session rendered-browser session for Intel, and with `eur-lex.europa.eu`'s official case-law mirror of the same judgment for Schrems II and Costa v ENEL, both equally official primary sources rather than a proxy substitute. The GDPR Regulation text and the Schrems II judgment - both very long documents - also repeatedly defeated the fetch tooling's page-processing step, which truncated before reaching articles 45-46 or the operative part on every attempt; worked around by fetching the same official EUR-Lex PDF renditions directly and extracting the text locally, never by routing around the block with a third-party reader-proxy. Costa v ENEL is a deliberate single-node, zero-edge entry: primacy is a judge-made doctrine with no standalone operative Treaty article to pair it with - Declaration No 17 concerning primacy, itself independently verified this session, does no more than recall the doctrine and name this judgment as its origin.

## What is NOT in this pack

No verified article-level text of any Directive (only the GDPR Regulation and two Treaty articles have been checked). One national data-protection regulator profile now exists - see `../../regulators/cnil.md` for France - but no other member state's supervisory authority is documented, and the GDPR "one-stop-shop" lead-supervisory-authority mechanism itself is not separately explained here. Free movement of persons, services, and capital; state aid; merger control; and the direct-effect doctrine (a related but distinct concept from primacy) all remain unbuilt.
