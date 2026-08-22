# Regulators

Regulator profiles: statutory/professional powers, procedure, sanction range, appeal route. Used by `../skills/legal-regulatory/SKILL.md` and `../agents/regulatory/ROLE.md`.

## Status

**One real profile exists: `cnil.md`** (France's data-protection regulator), added after a live stress test's regulatory-mode matter demonstrated exactly what shape one needs to be, sourced from `cnil.fr` and `conseil-etat.fr` directly. `COMMUNITY_REVIEWED`, not yet `MAINTAINER VERIFIED` - see `../GOVERNANCE.md`'s pack verification levels. Every other regulator remains **EXPERIMENTAL** with no profile built. See `../docs/HONEST_STATUS.md`.

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
