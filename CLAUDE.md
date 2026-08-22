# Instructions for Claude working in this repository

This file governs Claude Code sessions editing *this repository's own source*. It is distinct from `skills/legal-work/SKILL.md`, which governs Claude when it is *using* Legal Chamber to do legal work for an end user.

## Non-negotiable rules

1. **Never write a jurisdiction pack, authority entry, or citation as if verified when it wasn't checked against a primary source in this session.** If you can't check it, write `UNVERIFIED` and say what would need to happen to verify it. This applies to your own commits exactly as it applies to the skill's runtime output, see `docs/OPERATING_RULES.md`.
2. **Never commit anything under `matters/`.** It's gitignored for a reason, real matter data (facts, evidence, privileged material) must never enter this public repository's history. If you find matter data staged, unstage it and ask before proceeding.
3. **Jurisdiction pack changes need a primary source.** Adding or editing anything in `jurisdictions/*/authorities.md`, `*/procedure.md`, or `*/citation.md` requires citing where you got it (official legislation site, official court site, or a named secondary source) and updating that pack's `VERIFICATION_STATUS` honestly, see `docs/OPERATING_RULES.md` Part CLX and `GOVERNANCE.md`.
4. **Style rules apply to this repo's own prose too.** No em dashes, no stock AI-prose phrasing, UK English by default unless a file is jurisdiction-specific US content, see `docs/STYLE_GUIDE.md`.
5. **Keep `docs/HONEST_STATUS.md` current.** If you add real capability, move the corresponding line from "not real yet" to "real." If you add a stub, don't let README or HONEST_STATUS overstate it.
6. **Before adding a new top-level skill, agent role, or jurisdiction, check whether an existing one already covers it.** This repo grows by depth (real verified content in existing packs) more than by breadth (more jurisdictions with only structural stubs), see the roadmap in `docs/HONEST_STATUS.md`.

## Working conventions

- Each `skills/*/SKILL.md` stays small (progressive disclosure), link out to `agents/`, `jurisdictions/`, `schemas/`, and `workflows/` rather than inlining their content.
- JSON Schemas in `schemas/` are the source of truth for record shape. If a workflow doc describes a field a schema doesn't have, fix the schema, don't let them drift.
- Deterministic logic (dates, arithmetic, citation-pattern checks) belongs in `scripts/`, not in a skill's prose instructions, see `docs/OPERATING_RULES.md` "deterministic tools first."
- Run `scripts/citation_lint.py`, `scripts/deadline_calculator.py --selftest`, `scripts/verify_matter_refs.py --selftest`, and `scripts/verify_matter_persistence.py --selftest` before committing changes that touch citation, deadline, schema cross-reference, or matter-persistence logic.
