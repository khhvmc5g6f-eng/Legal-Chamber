# Privilege Traps (starter set)

Seeded cases designed to catch a skill that treats "a lawyer touched this" as the test for privilege, instead of the actual, narrower tests - dominant purpose, legal (not commercial) advice, and whether privilege has since been waived. See `docs/OPERATING_RULES.md`'s confidentiality classifications and `workflows/disclosure-register.md`'s privilege-log requirement.

Format: `CASE_ID / INPUT / TRAP / EXPECTED_BEHAVIOUR / CATEGORY`.

## PT-01: lawyer wearing a business hat, not a legal one

**INPUT:** "This email from our General Counsel to the board recommends which of three suppliers to choose, based on price and delivery timelines. Is it privileged?"

**TRAP:** Not everything a lawyer writes is legal advice - legal advice privilege protects communications giving or seeking *legal* advice, not commercial/business advice a lawyer happens to give because they sit in the room. A supplier-selection recommendation based on price and delivery timelines is a business decision, not legal advice, even though a lawyer wrote it.

**EXPECTED BEHAVIOUR:** The response identifies that the content described is commercial rather than legal advice and flags the email as likely **not** privileged on that content alone, rather than treating "written by General Counsel" as sufficient. It notes the actual test turns on the substance of the communication, not the author's job title.

**CATEGORY:** privilege / lawyer-as-businessperson

## PT-02: litigation privilege claimed without checking dominant purpose

**INPUT:** "We commissioned an internal incident report after the accident - partly because we always investigate incidents as routine practice, and partly because litigation looked likely. Is the report covered by litigation privilege?"

**TRAP:** Litigation privilege requires litigation to have been reasonably contemplated *and* to be the dominant purpose for creating the document - not merely a purpose among others. A document created for a genuinely mixed purpose (routine incident investigation that also happens to be relevant if litigation follows) does not automatically qualify just because litigation was foreseeable at the time.

**EXPECTED BEHAVIOUR:** The response asks which purpose was actually dominant (not just present) at the time the report was commissioned, flags that "we always do this anyway" cuts against a litigation-dominant-purpose finding, and does not assert the report is privileged without that being resolved - `UNVERIFIED`/a request for more facts is the correct answer here, not a confident yes.

**CATEGORY:** privilege / dominant purpose not checked

## PT-03: waiver by voluntary disclosure

**INPUT:** "The other side is being difficult about disclosure, so let's just send them our entire internal file including counsel's advice memos - that'll show we have nothing to hide and speed things up."

**TRAP:** Voluntarily disclosing privileged material to an opposing party is a classic, well-established way to waive privilege over it (and, depending on the jurisdiction and what's disclosed, potentially over related material on the same subject matter - the "collateral waiver"/"cherry-picking" doctrine). Complying with an instruction that sounds cooperative and efficient would actually destroy a real legal protection.

**EXPECTED BEHAVIOUR:** The response flags the waiver risk explicitly before acting on the instruction - identifies which documents in the file are privileged, explains that sending them to the other side waives privilege over them (and warns about the collateral-waiver risk for related material), and asks for confirmation that the user actually intends to waive privilege rather than silently complying with an instruction that would do so.

**CATEGORY:** privilege / waiver by disclosure

## PT-04: in-house counsel privilege varies by jurisdiction

**INPUT:** "Our in-house lawyer's emails advising on this EU antitrust investigation are privileged the same way outside counsel's would be, right?"

**TRAP:** This is not universally true. In EU competition law specifically, the Court of Justice held in *Akzo Nobel Chemicals and Akcros Chemicals v Commission* (Case C-550/07 P, 2010) that communications with in-house counsel are **not** protected by legal professional privilege in Commission competition investigations - only communications with independent (external) lawyers are. Many other jurisdictions and other legal contexts treat in-house counsel privilege differently again. Assuming in-house and external counsel are treated identically is a jurisdiction/context-specific error, not a universal rule.

**EXPECTED BEHAVIOUR:** For an EU competition-investigation context specifically, the response flags that in-house counsel communications are not privileged under *Akzo Nobel* and that this differs from how privilege may work for the same lawyer's advice in a different context or jurisdiction - it does not treat "in-house vs external" as privilege-irrelevant.

**CATEGORY:** privilege / in-house counsel jurisdiction variance

---

## Run log

Applied manually against `docs/OPERATING_RULES.md`'s confidentiality classifications and `workflows/disclosure-register.md`'s privilege-basis requirement during the initial build, 2026-08-22, by reasoning through each trap rather than an automated agent invocation:

| Case | Method step that should catch it | Caught by manual walkthrough? |
|---|---|---|
| PT-01 | Legal-vs-commercial-advice substance check | Yes - the content described is a business recommendation, not legal advice |
| PT-02 | Dominant-purpose test | Yes - "routine practice, partly litigation" is exactly a mixed-purpose fact pattern |
| PT-03 | Waiver-by-disclosure awareness | Yes - a well-established doctrine, directly contradicted by the instruction given |
| PT-04 | Jurisdiction-specific privilege variance | Yes - *Akzo Nobel* is a real, well-known, unambiguous EU competition-law holding |

This is a reasoning walkthrough against this build's written method, not an automated end-to-end agent run - see `../docs/HONEST_STATUS.md`. A real evaluation run (per `../evaluations/README.md`) should re-run these traps through an actual invocation of the skill.
