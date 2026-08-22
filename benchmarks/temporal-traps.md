# Temporal Traps (starter set)

Seeded cases where the same question has a different correct answer depending on `LAW_AS_OF` date, or where a fact that was once current has since gone stale - designed to catch a skill that answers from a fixed mental snapshot of "the law" instead of checking currency for the date actually in play. See `schemas/matter.schema.json`'s `jurisdiction[].law_as_of` field and `docs/OPERATING_RULES.md`'s currency/treatment requirements.

Format: `CASE_ID / INPUT / TRAP / EXPECTED_BEHAVIOUR / CATEGORY`.

## TT-01: a figure that changes periodically, asked with no date

**INPUT:** "What's the current small claims track financial limit in England & Wales?"

**TRAP:** Procedural thresholds like this are set by statutory instrument and have been revised more than once historically. A system that recalls a number from training data and states it as current, without checking it against a live primary source for today's date, will eventually be wrong regardless of what the number happens to be right now - this trap tests the *behaviour* (check before asserting), not any specific figure, deliberately, since asserting a specific "correct" figure here would itself violate this repository's own no-recall rule.

**EXPECTED BEHAVIOUR:** The system does not state a specific number from memory. It either checks the current Civil Procedure Rules/practice direction live and cites the primary source with a check date, or states plainly that the current figure needs live verification and offers to do that - per Gate 5/Gate 11 in `docs/QUALITY_GATES.md`.

**CATEGORY:** temporal / stale-figure recall

## TT-02: a major regime change, question spans the boundary

**INPUT:** "We're an England & Wales company relying on an EU Regulation that applied directly in UK law. Does it still apply the same way today as it did five years ago?"

**TRAP:** The United Kingdom left the EU (31 January 2020, with a transition period ending 31 December 2020), after which directly-applicable EU law was converted into "retained EU law" (later relabelled and partially amended as "assimilated law" under the Retained EU Law (Revocation and Reform) Act 2023) rather than continuing to apply exactly as before. A system that treats "it's an EU Regulation, it applies directly" as still true without qualification, for a UK matter today, is answering pre-Brexit law as if it were current.

**EXPECTED BEHAVIOUR:** The response flags that the legal mechanism by which the Regulation applies changed after the transition period ended, that the current UK-domestic version may have since been amended or revoked independently of any change to the original EU instrument, and that the current status needs to be checked against the UK's own statute book (legislation.gov.uk) rather than assumed to mirror EU law's current text.

**CATEGORY:** temporal / regime change spanning the question

## TT-03: this repository's own "current" tag taken as permanent

**INPUT:** "Your own authority graph says *Van Buren v. United States* is `GOOD_LAW_CURRENT` - so I can rely on that without checking further, right?"

**TRAP:** `jurisdictions/us-federal/authority-graph.json` records `treatment: GOOD_LAW_CURRENT` with a `verified_at` timestamp from when the check was actually performed (2026-08-22). That tag describes the case's status *as of that check*, not a permanent fact - a system that treats a stored `GOOD_LAW_CURRENT` value as good indefinitely, without noticing how much time has passed since `verified_at`, will eventually serve stale information from its own supposedly-verified data.

**EXPECTED BEHAVIOUR:** The response distinguishes "verified current as of `verified_at`" from "current right now" - for a request materially later than `verified_at`, it re-checks currency live rather than trusting the stored tag alone, and says so explicitly rather than treating the file's presence as sufficient forever.

**CATEGORY:** temporal / stale internal verification treated as permanent

## TT-04: statute cited without checking for amendment

**INPUT:** "Under the Data Protection Act 1998, what are an individual's rights to access their personal data?"

**TRAP:** The Data Protection Act 1998 was repealed and replaced by the Data Protection Act 2018 (read alongside the UK GDPR) - it is not the current UK data protection statute and hasn't been since 25 May 2018. A system that answers the substantive question (subject access request rights) using 1998 Act framing, because the user named that Act specifically, is answering a repealed regime as if it were live law.

**EXPECTED BEHAVIOUR:** The response flags that the 1998 Act has been repealed and superseded (Data Protection Act 2018 / UK GDPR govern this today), asks whether the user actually means the current regime or is asking a historical question about rights as they stood under the 1998 Act specifically (e.g. for litigation about conduct that occurred while it was in force), and does not silently substitute current law for what was actually asked without flagging the discrepancy either way.

**CATEGORY:** temporal / repealed statute cited as current

---

## Run log

Applied manually against `schemas/matter.schema.json`'s `law_as_of` field, `docs/OPERATING_RULES.md`'s currency requirements, and this repository's own `jurisdictions/us-federal/authority-graph.json` `verified_at` convention during the initial build, 2026-08-22, by reasoning through each trap rather than an automated agent invocation:

| Case | Method step that should catch it | Caught by manual walkthrough? |
|---|---|---|
| TT-01 | No-recall rule for figures requiring live verification | Yes - the trap is designed so no specific number is ever asserted as correct |
| TT-02 | Regime-change awareness (Brexit/retained law) | Yes - well-documented, unambiguous historical transition |
| TT-03 | `verified_at` vs. "current" distinction | Yes - this repository's own schema already separates the two fields, the trap is whether that distinction is actually honoured in practice |
| TT-04 | Repealed-statute check before substantive answer | Yes - DPA 1998's repeal by DPA 2018 is well-established and unambiguous |

This is a reasoning walkthrough against this build's written method, not an automated end-to-end agent run - see `../docs/HONEST_STATUS.md`. A real evaluation run (per `../evaluations/README.md`) should re-run these traps through an actual invocation of the skill.
