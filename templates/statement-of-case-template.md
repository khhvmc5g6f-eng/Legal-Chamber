# Statement of Case / Pleading (jurisdiction-agnostic skeleton)

> Delete this note. This skeleton does not include any jurisdiction's actual required form, numbering convention, statement-of-truth wording, or page/word limit - check the applicable court/tribunal rule live and use its exact required form, per `../skills/legal-draft/SKILL.md` Step 6 and `../docs/QUALITY_GATES.md` Gate 13. "Statement of case" covers particulars of claim, defence, reply, counterclaim, or their jurisdiction's equivalent name - use whichever this document actually is.

**Court/tribunal:** [ ]
**Claim/case number:** [ ]
**Parties:** [Claimant/Applicant] v [Defendant/Respondent]
**Document:** [Particulars of Claim / Defence / Reply / Counterclaim / other - state which]

## 1. Parties

State who each party is and, where relevant to a pleaded issue (capacity, corporate status, jurisdiction), why that matters - not just names.

## 2. Facts relied on

Numbered paragraphs, one factual proposition per paragraph, in a logical (usually chronological) order. Every fact here must trace to `../schemas/fact.schema.json` with a real status (`ESTABLISHED`/`ADMITTED`/`DISPUTED`/etc, per `../docs/OPERATING_RULES.md`'s fact status vocabulary) - a pleaded fact with no evidential basis is a liability, not a placeholder to fill in later.

1. [ ]
2. [ ]

## 3. Legal basis / cause(s) of action (or defences)

For each cause of action or defence, trace to `../schemas/issue.schema.json`: the elements, which paragraph(s) above establish each element, and the authority relied on (verified per `../skills/legal-authorities/SKILL.md`, never asserted from memory). Do not plead a cause of action whose elements the facts pleaded above don't actually support - see `../skills/legal-draft/SKILL.md`'s argument-map step.

| Cause of action/defence | Element | Supporting fact para(s) | Authority |
|---|---|---|---|
| | | | |

## 4. Remedy sought

State precisely what's being asked for - see `../skills/legal-litigation/SKILL.md` Step 3's remedy-first check (don't plead toward a remedy the decision-maker doesn't actually have power to grant). Include any interim relief sought separately, with its own basis - see `../workflows/interim-applications.md`.

## 5. Statement of truth

[Insert the exact required wording for the applicable jurisdiction and forum - do not improvise this.]

## Before filing

- Run `python3 ../scripts/citation_lint.py <this file>` and fix what it flags - see `../docs/STYLE_GUIDE.md`.
- Confirm every fact/authority reference above resolves to a real record on the matter, not a placeholder left unfilled.
- Check the correspondence/confidentiality register if any part of this document's content originated in without-prejudice communications - see `../docs/OPERATING_RULES.md`'s confidentiality classifications; without-prejudice content must never appear in an open pleading.
