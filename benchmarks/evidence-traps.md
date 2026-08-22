# Evidence Traps (starter set)

Seeded cases designed to catch a skill that treats a bundle of evidence as internally consistent and complete by default, instead of actively checking for contradictions, missing documents, and hearsay dressed up as personal knowledge. See `skills/legal-evidence/SKILL.md` and `workflows/disclosure-register.md`.

Format: `CASE_ID / INPUT / TRAP / EXPECTED_BEHAVIOUR / CATEGORY`.

## ET-01: seeded contradiction between two witness statements

**INPUT:** "Witness A's statement says: 'I was in the office by 8am and saw the delivery arrive at 8:15am.' Witness B's statement says: 'I let the delivery driver in myself at around 9am - the office was empty when I arrived.' Please summarise what happened for the timeline."

**TRAP:** These two accounts directly contradict each other on both the delivery time (8:15am vs. ~9am) and whether the office was occupied at the relevant time. A summarisation task, taken literally, invites blending both into one smooth narrative rather than flagging that they can't both be true.

**EXPECTED BEHAVIOUR:** The response identifies and states the contradiction explicitly rather than silently reconciling or picking one account to report as "the" timeline - per `skills/legal-evidence/SKILL.md`'s cross-reference discipline, a chronology entry built from contradictory sources needs a `DISPUTED` or `CONTRADICTED` status (`docs/OPERATING_RULES.md`'s fact status vocabulary), not a single confident merged account.

**CATEGORY:** evidence / seeded contradiction

## ET-02: missing document logically implied by what's disclosed

**INPUT:** "Here's the disclosed email: 'Please see the attached signed contract and the pricing schedule for your records.' The bundle only contains the email itself - no attachments."

**TRAP:** The email explicitly references two attachments (a signed contract, a pricing schedule) that are not present in what was actually disclosed. Treating the email alone as "the document" and moving on misses that something referenced is missing from the record entirely.

**EXPECTED BEHAVIOUR:** The response flags the two missing attachments explicitly as a gap to chase, rather than treating the disclosed email as complete - per `skills/legal-evidence/SKILL.md`'s missing-document detection and `workflows/disclosure-register.md`'s `family` field (attachments and their cover email should share one, so an incomplete family is visible). It does not infer or assume the contents of the missing documents from context.

**CATEGORY:** evidence / missing document

## ET-03: hearsay drafted to read like personal knowledge

**INPUT:** "Draft witness statement paragraph from these notes: 'The claimant definitely knew about the defect before purchase - everyone in the office was talking about it that week.'"

**TRAP:** "Everyone in the office was talking about it" is the witness reporting what other people said, not something the witness personally observed the claimant knowing. A statement drafted as "the claimant definitely knew" states a fact about the claimant's own state of mind as if from personal knowledge, when the actual source is office gossip/hearsay at best - a real vulnerability if put into a formal statement unchanged.

**EXPECTED BEHAVIOUR:** Per `skills/legal-evidence/SKILL.md`'s witness-knowledge separation and `templates/witness-statement-template.md`'s paragraph-by-paragraph content rule, the drafted paragraph does not assert the claimant's actual knowledge as fact from personal observation - it states what the witness personally heard/observed (office conversation happening) and does not convert that into a conclusion about what the claimant knew, flagging the distinction to the person providing the instructions rather than smoothing over it in the draft.

**CATEGORY:** evidence / hearsay presented as personal knowledge

## ET-04: exhibit reference doesn't match the bundle

**INPUT:** "The witness statement refers to 'Exhibit JD-3, the signed lease agreement.' The evidence bundle has exhibits JD-1, JD-2, and JD-4 - there is no JD-3."

**TRAP:** A numbering gap in an exhibit sequence referenced by a witness statement is exactly the kind of bundle-integrity problem that's easy to skim past if the task is framed as "check the witness statement reads well" rather than "check the bundle is actually complete and consistent with what's cited."

**EXPECTED BEHAVIOUR:** The response flags the missing JD-3 exhibit explicitly - either it was never disclosed, was misnumbered, or the statement's reference is wrong - rather than assuming JD-4 is "close enough" or silently proceeding as if the lease agreement is present. Per `workflows/disclosure-register.md`'s bundle assembly step, exhibit numbering gaps are a defensible-bundle problem, not a cosmetic one.

**CATEGORY:** evidence / bundle integrity gap

---

## Run log

Applied manually against `skills/legal-evidence/SKILL.md` and `workflows/disclosure-register.md` during the initial build, 2026-08-22, by reasoning through each trap rather than an automated agent invocation:

| Case | Method step that should catch it | Caught by manual walkthrough? |
|---|---|---|
| ET-01 | Cross-reference / contradiction detection | Yes - the two accounts are directly, unambiguously inconsistent |
| ET-02 | Missing-document detection | Yes - both attachments are explicitly named in the email but absent from the bundle |
| ET-03 | Witness-knowledge separation | Yes - "everyone was talking about it" is reported speech, not personal observation of the claimant's knowledge |
| ET-04 | Bundle/exhibit-numbering integrity check | Yes - a gap in a referenced exhibit sequence is directly checkable against what's disclosed |

This is a reasoning walkthrough against this build's written method, not an automated end-to-end agent run - see `../docs/HONEST_STATUS.md`. A real evaluation run (per `../evaluations/README.md`) should re-run these traps through an actual invocation of the skill.
