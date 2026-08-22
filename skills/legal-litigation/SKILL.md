---
name: legal-litigation
description: Claims, defences, applications, trial preparation, and skeleton arguments in a court or tribunal. Use once jurisdiction, facts, evidence, and research are underway and the task is building or testing the actual case for a court/tribunal process.
---

# legal-litigation

## 0. Day-one triage - before any element-by-element work

Do these first, not as step 2 of a longer sequence - a real solicitor checks them in the first hour precisely because each one can moot everything that follows:

- **Limitation/time-bar.** Calculate it now, with `../../scripts/deadline_calculator.py` and a real `--rule-source` from the jurisdiction pack, not as part of the general case-killer sweep in step 2 below. If limitation has expired or is close, that governs everything else about how this matter proceeds.
- **Client care and costs information.** Before substantive work begins, has the client been given (or does this response need to include) costs information: funding basis (fixed fee, hourly, CFA, DBA, litigation funding), a costs estimate or budget, and who's paying if the matter is lost? This is a file-opening compliance obligation in most jurisdictions, not an optional extra - if it hasn't happened, flag it rather than proceeding as if only the legal analysis matters.
- **Pre-action protocol / ADR check.** Has the applicable pre-action protocol (if the jurisdiction has one) been complied with, and has mediation or another ADR route been considered or attempted? Skipping this has direct costs consequences in many jurisdictions even if the underlying claim is strong. Cross-reference `../legal-negotiation/SKILL.md` for the ADR/settlement analysis itself - this step is the gate that decides whether it's needed before proceeding, not a substitute for running it.

## 1. Build the issue tree

For each cause of action or defence, use `../../schemas/issue.schema.json`: elements, burden (legal/evidential/reverse), standard of proof, authority, facts required, evidence available and missing, opposition's likely position. Never analyse "the case" as one undifferentiated blob - element-by-element is what makes a gap visible.

## 2. Case-killer check

Beyond limitation (already checked in step 0), check for anything else capable of ending the matter regardless of the merits: jurisdiction, standing, res judicata, exclusion clause, statutory bar, failure to exhaust an alternative remedy, immunity, a mandatory procedural requirement not met. Mark these `case_killer: true` on the relevant issue record.

## 3. Remedy-first check

Ask before drafting the substantive argument: if every liability argument succeeds, what does the decision-maker actually have power to grant? Don't build an elaborate argument toward a remedy that isn't available - check `../legal-prospects/SKILL.md`'s remedy dimension early, not last.

## 4. Procedure

Deadlines and filing requirements come from the jurisdiction pack (`../../jurisdictions/<slug>/README.md`) and, where a specific date is needed, `../../scripts/deadline_calculator.py` with a real `--rule-source` - never recalled from memory. Filing-readiness (court, case number, parties, page/word limits, statement of truth, exhibits, service) is a checklist, not a vibe - see `../../docs/QUALITY_GATES.md` Gate 13. Include court/filing fees (and any fee remission scheme available) in the procedural picture, not just deadlines - a case can stall on an unbudgeted issue fee as easily as on a missed date.

## 5. Expert evidence, if the matter needs it

If the matter turns on anything outside ordinary legal or factual knowledge (causation, valuation, technical standards, medical opinion), flag the need for expert evidence now rather than late: identify the question the expert needs to answer, the applicable duty-to-the-court/independence rule for the jurisdiction, and any disclosure obligations for expert reports. Keep expert evidence distinct from advocacy - see `../legal-evidence/SKILL.md`'s witness-knowledge separation, which applies equally here (an expert's opinion is not a lawyer's argument dressed up with a credential attached).

## 6. Adversarial testing

Before relying on the case theory, run at least the first two stages of `../../workflows/five-hearing-adversarial.md` (justiciability/pleadability, then doctrinal/authority challenge) even if not doing the full five-hearing workflow. Escalate to the full workflow for anything `L4` or above. Note that workflow's own "before hearing 1" caveat: it tests argument and evidence quality, it does not model interim applications, disclosure timing, or case management - track those procedurally in step 4, not through the adversarial workflow.

## 7. Case theory coherence

Keep legal theory, fact theory, evidence theory, and remedy theory consistent with each other - a change in one (e.g. conceding a fact to strengthen credibility) has to be checked against the others, not made in isolation.

## Correspondence discipline

If this matter produces correspondence (not just court documents), every piece must be clearly marked `without prejudice` or open before it's sent - see `../../docs/OPERATING_RULES.md`'s confidentiality classifications. Never let negotiating content bleed into an open letter, or vice versa; `../legal-draft/SKILL.md` enforces this at the drafting stage, but it starts with knowing which register a given piece of correspondence is in before writing it.

## Hand off

- Need the opposing side built out properly, in an isolated context → `../legal-moot/SKILL.md`.
- Need the actual document → `../legal-draft/SKILL.md`.
- Need prospects stated → `../legal-prospects/SKILL.md`.
- Anticipating or facing an appeal → `../legal-appeal/SKILL.md`.
- Pre-action ADR/settlement strategy itself → `../legal-negotiation/SKILL.md`.
