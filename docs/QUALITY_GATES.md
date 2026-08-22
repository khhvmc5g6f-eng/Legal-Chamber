# Quality Gates

A matter output cannot be represented as ready for reliance, filing, sending, or advising a client, until it has passed these gates. Gates are cumulative; a later gate does not waive an earlier one.

| # | Gate | Passes when |
|---|------|-------------|
| 1 | Jurisdiction established | `matter.jurisdiction` is set from an explicit user answer or explicit config, not inferred silently. See `schemas/matter.schema.json`. |
| 2 | Material facts classified | Every fact the conclusion depends on has a status from the Fact Ledger vocabulary, not left implicit in prose. |
| 3 | Issues identified | `schemas/issue.schema.json` records elements, burden, and standard for each cause of action / defence in play. |
| 4 | Primary legal research completed | Each material proposition has a `research log` entry (`workflows/research-log.md` template) showing what was searched and where. |
| 5 | Authority integrity verified | Every cited authority has been checked per `docs/OPERATING_RULES.md` § verification hierarchy, not merely recalled. |
| 6 | Adverse authority searched | A disconfirming search was actually run for each material proposition, not only a supporting one. |
| 7 | Evidence mapped | Each element has its supporting/undermining evidence recorded in `schemas/evidence.schema.json`, including gaps. |
| 8 | Procedure checked | Deadlines and filing requirements were checked against `scripts/deadline_calculator.py` and the jurisdiction's procedural pack, not recalled from memory. |
| 9 | Remedy checked | The relief sought is one the relevant decision-maker can actually grant, checked before, not after, the main drafting effort. |
| 10 | Adversarial review complete | At minimum a steelman of the opposing case was constructed and answered; see `workflows/five-hearing-adversarial.md` for the full version. |
| 11 | Citation audit complete | `scripts/citation_lint.py` run, and every flagged citation individually resolved (not just formatted). |
| 12 | Fact audit complete | No fact in the final draft traces to a source weaker than what its Fact Ledger status claims. |
| 13 | Document compliance complete | Court/format/word-count/statement-of-truth requirements checked against the jurisdiction's procedural pack, see `courts/`. |

## Hard failures

These cannot be offset by a high score elsewhere and block release regardless of how many gates otherwise passed:

- fabricated or unverified-but-asserted authority
- fabricated or altered quotation
- wrong jurisdiction applied
- materially wrong statutory provision
- fabricated fact
- known binding authority ignored
- invented procedural rule
- a false claim of human approval

## Filing/output states

```
DRAFT → RESEARCHED → AUTHORITY VERIFIED → PROCEDURE VERIFIED →
HUMAN REVIEW PENDING → VERIFIED FOR FILING
```

`VERIFIED FOR FILING` is set only by a named human reviewer editing the matter record directly. No skill, agent, or workflow in this repository sets that value itself. See `schemas/draft.schema.json`.

## Final legal quality matrix

Score `/10` per dimension, weighted by task type (a contract review weights "Procedure" lower and "Contract dependency mapping", tracked separately, higher; a skeleton argument weights "Procedure" and "Citation" higher):

```
Jurisdiction        Legal accuracy     Authority           Research currency
Issue identification  Fact integrity   Evidence            Application
Counterargument     Procedure          Remedy              Strategy
Drafting            Citation           Presentation
```

This matrix is a review aid, not a pass/fail gate by itself, the gates and hard failures above are what actually blocks release.
