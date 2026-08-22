---
name: legal-regulatory
description: Regulator investigations, disciplinary proceedings, and enforcement responses. Use when a regulator or professional body (not a court) is the decision-maker.
---

# legal-regulatory

## Identify the regulator and its actual powers

Before anything else: which regulator, under what statutory/professional power, at what stage (informal inquiry, formal investigation, allegation, decision, appeal)? Do not assume a regulator's procedure mirrors court procedure - most regulatory regimes have their own rules, and often lighter procedural protections than a court process; check the regulator's own published procedure rather than assuming.

## Allegation matrix

For each allegation:

```
Allegation → applicable rule → particulars → supporting evidence →
undermining evidence → admissions → disputes → defence → mitigation
```

## Keep liability and mitigation separate

Mitigation material must never leak into the liability response as an unintended admission. Draft them as clearly separated sections/documents, and check the liability response doesn't concede anything the mitigation section assumes.

## Deadlines

Regulatory response deadlines are often short and strict - check them against the regulator's own published rules (not the general court-procedure pack for the jurisdiction) and `../../scripts/deadline_calculator.py` with a real `--rule-source`.

## Sanction range and appeal rights

State the actual range of outcomes the regulator can impose and the appeal route, before assessing strategy - see the remedy-first principle in `../legal-litigation/SKILL.md`, which applies here too.

## Hand off

- Need the actual response document → `../legal-draft/SKILL.md`.
- Facing an appeal from a regulatory decision → `../legal-appeal/SKILL.md`.
