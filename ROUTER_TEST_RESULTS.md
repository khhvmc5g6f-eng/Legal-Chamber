# Router Test Results

Method: traced 10 natural-language requests against the actual routing table in `skills/legal-work/SKILL.md` Steps 1 and 4 as written, checking whether each would resolve to the correct matter type, specialist skill, and complexity tier **without the user needing to know any internal command or tier name**.

| # | Request (as a user would actually phrase it) | Expected route | Traced result | Pass? |
|---|---|---|---|---|
| 1 | "Can you check whether this case I found is real?" | `legal-authorities` | Matches "Just verifying a specific citation/authority" row directly | PASS |
| 2 | "I need help fighting my unfair dismissal case at tribunal" | `legal-litigation`, employment matter type | Matches "A claim, defence, application, trial, or appeal in a court/tribunal" | PASS |
| 3 | "Review my employment tribunal case using Full Chambers" (the README's own quick-start example) | `legal-litigation` at `L5 CHAMBERS` | **Originally FAILED before this test**: Step 1's tier list only stated the internal label `L5 CHAMBERS` with no natural-language trigger phrase - "Full Chambers" was not explicitly mapped to it anywhere, meaning the router's own worked example in `README.md` was not actually wired to Step 1's tier logic. Fixed during this test - see below | PASS (after fix) |
| 4 | "Can you calculate when my response is due?" | Ambiguous - no explicit row for a bare deadline-calculation request | Falls through to the closest row, "A claim, defence, application, trial, or appeal in a court/tribunal" (`legal-litigation`), which does cover procedure/deadlines in its step 4, but only if the request has litigation context. A bare "calculate my deadline" with zero other case context has no direct row match | PARTIAL - see finding below |
| 5 | "I want to negotiate a settlement in my dispute" | `legal-negotiation` | Matches "Negotiation, mediation, or settlement strategy" directly | PASS |
| 6 | "Write me a research memo on whether X applies" | Ambiguous between `legal-research` (research) and `legal-draft` (producing a document) | Both rows match; resolved by the router's own note ("more than one may apply in sequence... route to the first one needed") - research necessarily precedes drafting substantively, so this resolves correctly in practice even though the table has no explicit precedence rule | PASS (with a soft ambiguity noted, not a failure) |
| 7 | "I got a letter from the regulator about a complaint" | `legal-regulatory` | Matches "A regulator, disciplinary process, or investigation" | PASS |
| 8 | "My professional registration got refused, can I appeal?" | `legal-appeal` | Matches "An appeal (existing or anticipated)" directly | PASS |
| 9 | "Write my law essay on separation of powers" | `legal-academic` | Matches "A university assignment, essay, problem question, or dissertation" | PASS |
| 10 | "I'm buying a SaaS company, need the deal handled" | `legal-transaction` | Matches "An acquisition, financing, property, or other transaction" | PASS |

## Finding and fix made during this test

**Finding:** `skills/legal-work/SKILL.md` Step 1 listed complexity tiers only by their internal label (`L1 QUICK` through `L6 COMPLEX MATTER`), with no natural-language phrase mapped to any of them. This directly contradicts the requirement that "the router must not require the user to know internal command names" - the README's own quick-start example ("...using Full Chambers") used a phrase the router had no explicit mapping for.

**Fix applied:** Step 1 now lists the natural-language signals that indicate each tier (e.g. "full chambers," "the full process," "moot this," or a request for opposing counsel *and* a simulated judicial outcome together, all now explicitly mapped to `L5 CHAMBERS`) rather than only the internal label. See `skills/legal-work/SKILL.md` Step 1, and `CHANGELOG.md` for the record of this fix.

## Open finding, not fixed (flagged rather than silently left)

**Test 4** shows a real, narrower gap: a bare request with no litigation/matter context at all ("calculate my deadline") has no direct routing-table row. In practice this is a minor gap - almost every real deadline question arrives with at least some case context that routes correctly - but a purely isolated deadline question would currently fall through to the closest-but-imperfect litigation row rather than a dedicated one. Not fixed in this pass because adding a dedicated row for a single narrow utility request risks cluttering the table for a case that's rare in practice; recorded here rather than silently ignored. Tracked as a low-priority open item in `docs/HONEST_STATUS.md`.
