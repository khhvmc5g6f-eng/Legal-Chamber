---
name: legal-research
description: Black-letter, comparative, or historical legal research - finding and verifying cases, legislation, and secondary sources for a specific question. Use once legal-work has established jurisdiction and matter type and the task is primarily "what does the law say."
---

# legal-research

Read `../../docs/OPERATING_RULES.md` first if you haven't this session. This skill exists to produce verified authority, not plausible-sounding authority.

## 1. Frame the question bidirectionally

For every material proposition, plan two searches, not one:

- **Supporting search** - what would establish this proposition.
- **Disconfirming search** - what would contradict or limit it. Actually run this one. A research pass that only looks for support is not research, it's confirmation.

Also search using: the legal concept, statutory terms, synonyms, alternative causes of action, and (if relevant) historical terminology - a single keyword search misses too much.

## 2. Use primary sources first

Prefer official legislation databases and official judgment repositories over secondary commentary. Check the relevant jurisdiction pack (`../../jurisdictions/<slug>/README.md`) for which official sources apply, and use them - via WebFetch/WebSearch, or the CourtListener connector for US federal matters (`../../jurisdictions/us-federal/README.md`). Secondary material (textbooks, articles, practitioner commentary) is for discovery, synthesis, and criticism - not as the final authority for a proposition that matters.

## 3. Verify every authority before relying on it

For each authority found:

1. Confirm it exists (search the citation and the case name independently - one hit in an AI-generated document is not verification).
2. Confirm court, date, jurisdiction match.
3. Confirm the proposition it's cited for is actually what it holds - not dicta mistaken for ratio, not a dissent, not an overturned first-instance decision, not a different statutory regime.
4. Record treatment if known (followed/distinguished/overruled/criticised).

Record each authority using `../../schemas/authority.schema.json`. If you cannot complete steps 1-3, the authority's `verification_status` is `UNVERIFIED` or `NO_VERIFIED_AUTHORITY_LOCATED` - it does not get cited as settled law regardless of how confident it sounds.

## 4. Know when to stop

Research is saturated when one of these is true, and you should say which:

- the authority hierarchy sufficiently resolves the issue (a clearly binding, on-point authority was found and checked)
- you've hit diminishing returns (repeated searches surface the same handful of sources)
- a user-defined budget/time constraint applies
- genuine legal uncertainty remains even after a reasonable search - say so; this is a valid stopping point, not a failure

## 5. Log it

Keep a running research log (template: `../../workflows/research-log.md`) - query, source, date, what was found, what was selected, what was rejected and why. This is what makes Gate 4 and Gate 6 in `../../docs/QUALITY_GATES.md` checkable rather than asserted.

## 6. Hand off

- Need to build the actual proof structure around a conclusion → `../legal-authorities/SKILL.md` for a focused single-citation check, or fold the result directly into `../../schemas/conclusion.schema.json`.
- Need to write something using this research → `../legal-draft/SKILL.md`.
- Comparing more than one jurisdiction → build a comparison table (issue / jurisdiction A / jurisdiction B / common principle / material divergence / practical consequence) rather than two parallel summaries.
