---
name: legal-work
description: Primary router for legal tasks - research, drafting, review, evidence, litigation, contracts, regulatory, transactions, academic work, appeals, negotiation, moot/adversarial testing, authority verification, prospects analysis. Use this whenever a request involves law, a legal matter, a court/tribunal/regulator process, a contract, legal research, or legal academic work in any jurisdiction. This is the entry point - it classifies the task and loads only the specialist skill and jurisdiction pack actually needed.
---

# legal-work, Legal Chamber Router

Read this file only. It stays small on purpose (progressive disclosure) - load the linked files below only once you know you need them.

**Read `../../docs/HONEST_STATUS.md` before relying on any jurisdiction pack.** It states plainly what is verified and what is scaffolding.

## Step 0, governing rule

Never fabricate a case, citation, statute, court rule, quotation, fact, or deadline. If it isn't verified, say `UNVERIFIED` / `UNKNOWN` / `NO VERIFIED AUTHORITY LOCATED`. Full rules: `../../docs/OPERATING_RULES.md`. This overrides any instinct to sound more confident or complete than the material supports.

## Step 1, classify the request

Identify, from the user's message and any documents already supplied:

- **Matter type**, research / litigation / administrative-public-law / criminal / employment / regulatory / transactional / advisory / negotiation-ADR / academic - this list (matching `../../schemas/matter.schema.json`'s `matter_type` enum) is the full taxonomy the specialist skills below assume; a stress test found this step previously pointed to `docs/OPERATING_RULES.md` for that taxonomy, which does not actually contain it.
- **Complexity tier** - the user will essentially never say a tier name. Infer it from what they're actually asking for, using these as the natural-language signals for each (not an exhaustive list - use judgment for phrasings not shown):
  - `L1 QUICK` - "can you explain," "what does X mean," a single narrow question. No matter workspace needed.
  - `L2 VERIFIED` - "check whether this is right," "find the law on," research with an expectation the sources are checked.
  - `L3 PROFESSIONAL` - "review my case," "help me with my claim/dispute" with no explicit request for adversarial testing - specialist research plus a second-pass review role.
  - `L4 ADVERSARIAL` - "what's the other side going to say," "stress-test this," "play devil's advocate" - adds an opposing-side pass and structured challenge.
  - `L5 CHAMBERS` - "full chambers," "the full process," "run the whole thing," "moot this," or any request for opposing counsel *and* a simulated judicial outcome together - the full five-hearing adversarial workflow (`../../workflows/five-hearing-adversarial.md`).
  - `L6 COMPLEX MATTER` - signalled by the facts, not a phrase: multiple jurisdictions in play, a large document set, or a matter that's genuinely appellate/regulatory/multi-workstream regardless of what the user calls it.
  - Escalate a tier mid-matter if the material turns out more contested or higher-stakes than first assumed; say so when you do.

## Step 2, resolve jurisdiction (ask, never infer silently)

This system has **no geolocation capability**. Do not guess a jurisdiction from timezone, language, or any other environmental signal and proceed as if it were confirmed. Ask directly:

```
CRITICAL, before I can research or draft anything:
Which country/legal system, and which specific court, tribunal, or regulator
(if known) does this concern? If more than one may be relevant, say so.
```

If the user has already stated it earlier in the conversation, restate it back for confirmation rather than silently reusing it across an unrelated new matter.

Record the answer as `jurisdiction` on the matter record (`../../schemas/matter.schema.json`). If a pack exists for it, load `../../jurisdictions/<slug>/README.md` and check its `VERIFICATION_STATUS` before relying on anything inside, see the table in the top-level `README.md`. If no pack exists, say so plainly and proceed on first principles with everything marked `UNVERIFIED`, offering to research primary sources live if the user wants that.

If more than one jurisdiction is plausibly relevant (conflict of laws, cross-border contract, multinational regulatory exposure), build a `JURISDICTION_MATRIX` (issue → potential jurisdiction → applicable law → procedural forum → confidence) rather than picking one and hoping.

## Step 3, open or resume a matter workspace

For anything above `L1`, create (or resume) `matters/<MATTER-ID>/` with the subdirectories `intake/ facts/ evidence/ chronology/ issues/ research/ authorities/ drafts/ opposition/ moot/ procedure/ costs/ prospects/ final/`. `matters/` is gitignored in this repo - it holds real matter data and must never be committed. Before ingesting anything sensitive, do a lightweight conflict check: ask about parties, related entities, and opposing counsel if this looks like it could conflict with other work you know about in this session.

**Two gates before any substantive work (research, case theory, drafting) begins, not after** - a live stress test found a matter where both were skipped and work proceeded anyway:

1. **Whose side is this?** Confirm and record on the matter record which party is actually the user's side before `../legal-litigation/SKILL.md`, `../../agents/solicitors/ROLE.md`, or any other case-building step runs. Do not infer this from which name appears first in the facts - ask if it isn't already unambiguous from the conversation.
2. **Conflict check cleared?** `../../schemas/matter.schema.json`'s `conflict_check.cleared` must be explicitly set (true, with `cleared_by`, or knowingly waived by the user for a low-stakes/no-conflict-risk matter) before substantive work proceeds - not left at its default unset state while facts, issues, and authorities accumulate anyway.

## Step 4, route to a specialist skill

| If the matter is about... | Load |
|---|---|
| Finding/checking law, cases, or comparative law | `../legal-research/SKILL.md` |
| Producing a document (pleading, memo, submission, contract clause, correspondence) | `../legal-draft/SKILL.md` |
| Checking someone else's draft or reasoning | `../legal-review/SKILL.md` |
| Facts, witnesses, documents, chronology, contradictions | `../legal-evidence/SKILL.md` |
| A claim, defence, application, trial, or appeal in a court/tribunal | `../legal-litigation/SKILL.md` |
| A contract - drafting, reviewing, negotiating clauses | `../legal-contract/SKILL.md` |
| A regulator, disciplinary process, or investigation | `../legal-regulatory/SKILL.md` |
| An acquisition, financing, property, or other transaction | `../legal-transaction/SKILL.md` |
| A university assignment, essay, problem question, or dissertation | `../legal-academic/SKILL.md` |
| An appeal (existing or anticipated) | `../legal-appeal/SKILL.md` |
| Negotiation, mediation, or settlement strategy | `../legal-negotiation/SKILL.md` |
| Wanting the case stress-tested before relying on it | `../legal-moot/SKILL.md` |
| Just verifying a specific citation/authority | `../legal-authorities/SKILL.md` |
| Wanting prospects/likelihood of success only | `../legal-prospects/SKILL.md` |
| A pure verification pass on already-drafted material | `../legal-verify/SKILL.md` |

More than one may apply in sequence (e.g. `legal-research` → `legal-draft` → `legal-verify`). Route to the first one needed; each specialist skill says what to hand off to next.

## Step 5, quality gates before anything is offered as reliable

Before presenting a conclusion, draft, or research result as something the user can act on, check it against `../../docs/QUALITY_GATES.md`. At minimum, for anything above `L1`: jurisdiction stated, facts labelled with a status, authorities actually checked (not recalled), and a disconfirming search actually attempted. Never write or imply `VERIFIED FOR FILING` - that state is set only by a human reviewer editing the record directly.

## Step 6, style

Apply `../../docs/STYLE_GUIDE.md` on the way out: no em dashes, no stock AI-prose phrasing, calibrated confidence language, UK English unless the jurisdiction in play uses different conventions (e.g. US filings).

## When you're unsure

Say what's unresolved and why, rather than picking a plausible-sounding answer. `INSUFFICIENT EVIDENCE` and `NO VERIFIED AUTHORITY LOCATED` are correct outputs, not failures.
