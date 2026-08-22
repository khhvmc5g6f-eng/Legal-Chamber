---
jurisdiction: European Union (supranational)
legal_system: sui generis - treaty-based supranational law overlaying member states' own civil/common-law systems
verification_status: STRUCTURAL_DRAFT
last_reviewed: 2026-08-22
reviewer: added during a stress-test pass after a live matter simulation found the gap - no member-state pack (e.g. France, Spain) can substitute for EU-level authority
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

## What is NOT in this pack

No populated CJEU case-law database. No verified article-level text of any Regulation/Directive beyond naming them. No regulator profile - see `../../regulators/README.md`, which is deliberately empty pending real profiles (CNIL, and other national data-protection authorities acting as GDPR's "one-stop-shop" lead supervisory authority mechanism, are not documented here).
