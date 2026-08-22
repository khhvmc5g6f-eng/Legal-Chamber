# Interim Applications

A decision framework for applications a court/tribunal decides before trial/final hearing - some can end all or part of a matter outright, others manage how it proceeds. Naming and specific tests/thresholds (what strike-out actually requires, the exact summary-judgment standard, the American Cyanamid-style injunction test or its jurisdiction's equivalent) are jurisdiction-specific and not verified here - check the relevant `../jurisdictions/<slug>/README.md` and the applicable procedural rules before relying on this as more than a structural checklist. This gap was named explicitly in `../docs/HONEST_STATUS.md` ("no interim-application or case-management layer exists") - this file narrows, but does not close, that gap: it gives the four archetypes a decision structure, not verified jurisdiction-specific content.

## The four archetypes

Most interim applications are one of these, or a combination:

1. **Strike-out** - the claim/defence should be removed without examining its merits, because of a defect in the pleading itself (no reasonable grounds, an abuse of process, non-compliance with a rule/order). Decided on the pleaded case, not the evidence.
2. **Summary judgment** - the claim/defence should be decided now because, even taking the evidence at its highest for the losing side, there's no real prospect of success on it and no other compelling reason for a trial. Decided with reference to evidence, unlike strike-out.
3. **Interim injunction** - a party needs the court/tribunal to require or prohibit an act *before* the substantive dispute is finally decided, because waiting would cause harm that can't adequately be remedied by damages later. Usually involves cross-undertakings in damages and a balance-of-convenience/harm assessment.
4. **Case management directions** - not dispositive at all: timetabling, disclosure scope, expert permission (`../skills/legal-litigation/SKILL.md` Step 5), consolidation/split trials, or a stay. Decides how the matter proceeds, not who wins.

Don't conflate these - each has a different evidential basis, a different standard the applicant must meet, and (in most jurisdictions) different costs consequences for getting it wrong.

## Decision framework, per application

```
APPLICATION TYPE: strike-out | summary judgment | interim injunction | case management
WHAT'S BEING SOUGHT: (precise - not "dismiss the claim," but the exact order sought)
JURISDICTION'S ACTUAL TEST: (verify live - do not recall from memory)
EVIDENTIAL BASIS NEEDED: (pleading only / witness evidence / expert evidence - varies by type above)
TIMING: (many jurisdictions gate these behind a stage of the proceedings, or require the substantive
  defence/reply to have been filed first - check before assuming an application can be made now)
COSTS EXPOSURE: (an unsuccessful interim application commonly carries its own adverse costs order,
  separate from the eventual outcome of the substantive claim - factor this into whether to bring it)
CROSS-UNDERTAKING (injunctions only): (what the applicant is committing to if the injunction turns
  out to have been wrongly granted)
LIKELY OUTCOME IF GRANTED / IF REFUSED: (what actually changes procedurally either way)
```

## Before bringing any of these

- Check `../schemas/issue.schema.json`'s `case_killer` flag from `../skills/legal-litigation/SKILL.md` Step 2 - a strike-out or summary judgment application is usually *how* a case-killer point identified there actually gets put before the court, not a separate analysis from scratch.
- Calculate any application-specific deadline (time to respond, evidence-filing deadline) with `../scripts/deadline_calculator.py` and a real `--rule-source`, not from memory - see `../skills/legal-litigation/SKILL.md` Step 4.
- Run the remedy-first check (`../skills/legal-litigation/SKILL.md` Step 3) before an interim injunction application specifically - confirm the final relief actually available would justify the interim measure sought; a disproportionate interim application invites both refusal and an adverse costs order.
- Filing-readiness (`../docs/QUALITY_GATES.md` Gate 13) applies to an interim application exactly as it does to the substantive claim - it is its own document with its own formal requirements, not an informal request.

## Status

This is a decision framework and checklist, not a jurisdiction-verified engine. It does not model: the exact procedural rule number or test wording for any jurisdiction (verify live, every time), judicial discretion factors beyond naming that they exist, multi-application case management conference agendas, or the interaction between a pending interim application and a stay/settlement negotiation (cross-reference `../skills/legal-negotiation/SKILL.md` for that). See `../docs/HONEST_STATUS.md`.
