# Regulators

Regulator profiles: statutory/professional powers, procedure, sanction range, appeal route. Used by `../skills/legal-regulatory/SKILL.md` and `../agents/regulatory/ROLE.md`.

## Status

**33 real profiles exist**, all `COMMUNITY_REVIEWED`, not yet `MAINTAINER VERIFIED` — see `../GOVERNANCE.md`'s pack verification levels. This list is the authoritative current count (rewritten 2026-08-22 to consolidate several concurrent same-day editing passes — see each file's own frontmatter for its individual `reviewer`/sourcing note and "What is NOT in this profile" section rather than trusting a summary here for verification detail):

- **Original three**: `cnil.md` (France, data protection), `ico.md` (UK, data protection), `ftc.md` (US, privacy/data-security enforcement).
- **UK healthcare** (9): `gmc.md` (doctors), `nmc.md` (nurses/midwives), `hcpc.md` (allied health), `gphc.md` (pharmacy, Great Britain only), `gdc.md` (dentistry), `mhra.md` (medicines/devices — a product-safety regulator, not a fitness-to-practise body), `cqc.md` (England, provider quality), `his.md` (Scotland, provider quality — a materially different statutory model from CQC), `hiw.md` (Wales, provider quality — different again from both).
- **US healthcare** (4): `fda.md` (medicines/devices, federal), `dea.md` (controlled substances, federal), `fsmb.md` (a coordinating body, not a licensing authority — Medical Board of California used as the worked state example), `ncsbn.md` (same coordinating-body treatment for nursing, California Board of Registered Nursing as the example). `joint-commission.md` not built — `jointcommission.org` blocked automated fetch, remains EXPERIMENTAL.
- **Canadian healthcare** (4): `health-canada.md` (medicines/devices, the one genuinely federal piece), `cpso.md` (Ontario physicians, worked example), `cno.md` (Ontario nurses), `college-des-medecins-quebec.md` (Québec's structurally different professional-order model). No single national physician/nurse regulator — licensure is provincial.
- **Australian healthcare** (3): `ahpra.md` (the administrative body for the unified national scheme — Board decides, AHPRA administers), `medical-board-australia.md` (the National Board that actually decides doctor cases), `tga.md` (medicines/devices, federal). `ahpra.md` also covers the 2023 cosmetic-surgery reforms.
- **New Zealand healthcare** (4): `mcnz.md` (doctors), `nursing-council-nz.md` (nurses), `hdc.md` (Health and Disability Commissioner — a consumer-complaint body, distinct from the profession councils), `medsafe.md` (medicines/devices).
- **French healthcare** (5): `ordre-des-medecins.md` (CNOM, doctors), `ordre-infirmiers.md` (ONI, nurses), `ansm.md` (medicines/devices), `has.md` (standards/certification, not disciplinary), `ars-note.md` (short note on the regional ARS facility-inspection layer, not a full template profile).
- **Spanish healthcare** (3): `cgcom.md` (national/regional Colegio split for doctors), `consejo-general-enfermeria.md` (same split for nurses), `aemps.md` (medicines/devices, national).

Every other regulator remains **EXPERIMENTAL** with no profile built. See `../docs/HONEST_STATUS.md`. Several files note specific fields left `UNVERIFIED` (exact penalty figures, appeal routes for un-researched sub-jurisdictions, etc.) where a primary source could not be directly read this session — check the individual file before relying on a specific number.

## What a regulator profile should contain, when one is added

```
Regulator name
Jurisdiction
Statutory basis for its power
Investigation stages (informal inquiry → formal investigation → allegation → decision → appeal)
Procedural rules (own published rules, not assumed to mirror court procedure)
Sanction range
Appeal route and forum
Primary source
Last checked / reviewer
```

## Contributing one

Follow `../GOVERNANCE.md`'s sourcing requirements. A regulator profile built from general impression rather than the regulator's own published rules is not acceptable - the whole point of this file existing separately from a jurisdiction pack is that regulatory procedure is often quite different from ordinary court procedure and easy to get wrong by assumption.
