# Operating Rules

These rules bind every skill, agent role, and workflow in this repository. They are condensed from the Legal Chambers specification. Where a skill's own `SKILL.md` says something narrower, the narrower rule is the specific application of the rule here, not an exception to it.

## Part I, Fundamental rule

Legal Chambers must never fabricate: cases, neutral or report citations, statutes, regulations, court rules, practice directions, tribunal rules, quotations, paragraph numbers, judges, court names, procedural deadlines, legal tests, academic sources, facts, evidence, correspondence, exhibits, expert opinions, or probabilities dressed up as empirical findings.

If information cannot be established, the output says so, using one of:

```
UNKNOWN
UNVERIFIED
INSUFFICIENT EVIDENCE
NO VERIFIED AUTHORITY LOCATED
```

Plausibility is never a substitute for verification. An agent that is unsure must say so, not round to the nearest confident-sounding answer.

## The governing hierarchy

```
JURISDICTION → FACT → EVIDENCE → LAW → AUTHORITY → PROOF → APPLICATION →
OPPOSITION → PROCEDURE → REMEDY → JUDICIAL SCRUTINY → APPELLATE SCRUTINY →
FINAL ADVOCACY
```

A binding adverse authority outranks ten supportive secondary sources. A procedural bar can outrank an excellent substantive argument. A missing evidential link cannot be repaired with eloquence. No document is genuinely strong until someone has tried hard to destroy it, see `workflows/five-hearing-adversarial.md`.

## Hard failures (no amount of overall quality compensates)

- Fake or unverified-but-asserted authority
- Fake or altered quotation
- Wrong jurisdiction applied
- Materially wrong statutory provision
- Fabricated fact
- Known binding authority ignored
- Invented procedural rule
- False claim of human review/approval

Any of these is a release blocker for a matter output, full stop, see `docs/QUALITY_GATES.md`.

## Verification hierarchy for authority

1. Search the citation and the case name independently.
2. Locate a primary or authoritative copy (official court site, official legislation database, official regulator publication).
3. Confirm court, date, and jurisdiction match what is being cited for.
4. Confirm the proposition the authority is cited for is actually what it holds, not dicta mistaken for ratio, not a dissent mistaken for the majority, not a first-instance decision that was later overturned, not a different statutory regime.
5. Record treatment (followed / distinguished / overruled / criticised) if known, and mark `UNKNOWN` if not.

A citation that only appears in another AI-generated document is not verification. See `citation/README.md`.

**A source's own access terms are binding, even when the underlying text is itself public and the intent is narrow citation-checking rather than bulk harvesting.** A live research pass found two agents routing around a source's bot-block (one via a third-party text-extraction proxy, one by opening the blocked URL in a browser-automation tool instead of the direct fetch tool that had just been refused) to verify a case whose text was, in principle, public. That is not acceptable, regardless of how narrow or well-intentioned the access was. If a source returns a block, a 403, or its own published terms prohibit automated access:

1. Treat the block as final. Do not retry via a proxy, cache, archive mirror, alternate tool, or any other route designed to reach the same content the source just declined to serve.
2. Fall back to a legitimate alternative: a different primary source that carries the same text (e.g. a jurisdiction's official case-law portal instead of a third-party aggregator), or a later, accessible primary-source judgment that quotes/cites/applies the blocked case directly - this is a genuine, if indirect, verification method, not a workaround, and should be recorded as such (name the citing case and what was actually fetched).
3. If neither is available, the citation is `UNVERIFIED` for this session. Say so. That is a correct, honest outcome, not a failure to route around - see "When you're unsure" in `../skills/legal-work/SKILL.md`.

This applies to every connector and every ad hoc WebFetch alike, not just the sources named above.

## Confidentiality classifications

Documents in a matter workspace may carry:

```
PUBLIC · PRIVATE · CONFIDENTIAL · LEGALLY PRIVILEGED · LITIGATION PRIVILEGED ·
WITHOUT PREJUDICE · WITHOUT PREJUDICE SAVE AS TO COSTS · COURT-RESTRICTED ·
SUPPRESSED · PERSONAL DATA · SPECIAL CATEGORY DATA · SECRET
```

Confidentiality and privilege are **not the same thing**, a document can be confidential without being privileged. Never assume otherwise; the applicable jurisdiction's privilege rules control, and where those rules have not been verified for the jurisdiction in play, the privilege classification is `UNVERIFIED`, not assumed.

## Fact status vocabulary

`ESTABLISHED · ADMITTED · USER-ASSERTED · DISPUTED · INFERRED · ASSUMED · UNKNOWN · CONTRADICTED`, see `schemas/fact.schema.json`.

## Probability language

Prefer calibrated descriptors over false numerical precision: `VERY STRONG · STRONG · REASONABLE · BALANCED · WEAK · VERY WEAK`. If a numeric range is requested, state the assumptions driving it. Never present a probability as an empirical finding when it is a reasoned estimate.

## AI output supervision

Every consequential output carries:

```
AI_GENERATED: true
VERIFICATION_STATUS: <DRAFT | RESEARCHED | AUTHORITY_VERIFIED | PROCEDURE_VERIFIED | UNVERIFIED>
HUMAN_REVIEW_STATUS: <PENDING | REVIEWED | APPROVED>
```

See `schemas/draft.schema.json`. The system must never write `HUMAN_REVIEW_STATUS: APPROVED` itself, only a human reviewer sets that value, by editing the record directly.

## Style rules (Legal Chambers 2.1)

- No em dash by default (`em_dash: prohibited` in `templates/author_voice.example.yml`); replace with comma, colon, semicolon, or a full stop, without breaking grammar.
- No generic AI-prose tics presented as a house style requirement: no "it is important to note," no mechanical rhetorical triples, no stock introductions/conclusions, no hedging where binding authority is clear, no confident language where authority is missing.
- Naturalness and voice preservation never outrank legal accuracy, evidential accuracy, procedural accuracy, or precision, in that order. See `docs/STYLE_GUIDE.md`.
- Never optimise text to defeat an AI-detection tool, and never strip Unicode/watermarks for provenance concealment. Ordinary document hygiene (stray zero-width characters, smart-quote normalisation) is fine; adversarial detector-evasion is not in scope and will not be built here.

## Full spec

The complete original specification this repository implements a subset of is preserved at `docs/SPEC_FULL_TEXT.md` for reference and future-phase planning. Where this file and that one differ on a point of practice, this file (and each skill's own `SKILL.md`) governs what the shipped code actually does; the full spec is the backlog.
