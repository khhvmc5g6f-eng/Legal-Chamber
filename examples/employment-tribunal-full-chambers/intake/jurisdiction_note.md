# Jurisdiction resolution, M1-KESTREL

## What the user stated

"Jurisdiction: England & Wales, Employment Tribunal" - given explicitly and unambiguously in the instruction that opened this matter, not inferred from any environmental signal (no geolocation capability exists in this system per `agents/jurisdiction/ROLE.md` and `skills/legal-work/SKILL.md` Step 2). Per `agents/jurisdiction/ROLE.md`, "the UK" is not treated as one jurisdiction: England & Wales, Scotland, and Northern Ireland are distinct legal systems, and the user specified the correct one directly rather than leaving it for inference.

Because this is the message that opens the matter (not a reuse of a jurisdiction stated earlier for a different, unrelated matter), Step 2's instruction to "restate it back for confirmation rather than silently reusing it" is satisfied by recording it here for the file and flagging it in the report back to the requester, rather than by asking a redundant question when the user has already answered it in the same breath as the instruction.

## Pack check

`jurisdictions/england-wales/README.md` exists. Its front matter was read before anything in it was relied upon:

```
verification_status: STRUCTURAL_DRAFT
last_reviewed: 2026-08-22
reviewer: initial repository build (not independently re-checked by a second reviewer)
```

Per `docs/HONEST_STATUS.md`, `STRUCTURAL_DRAFT` means: court hierarchy and citation-style structure is believed accurate as general legal knowledge, but no specific case, statutory pinpoint, or procedural deadline in that file has been checked against a primary source. The pack itself says so at line 11 and again at line 55 ("What is NOT in this pack").

Consequence for this matter: the pack's own hierarchy diagram (Employment Tribunal, sitting below the Employment Appeal Tribunal) was used as structural confirmation of forum, but no substantive rule (limitation period, ACAS EC mechanics, discrimination time limit) was taken from the pack as verified. Those were independently checked live this session against `legislation.gov.uk` (see `procedure/limitation.md`), which is one of the pack's own listed "Primary sources to check against."

## Single-jurisdiction matter, no matrix needed

Facts disclose no cross-border element, no competing governing-law clause, and no second forum in play. A `JURISDICTION_MATRIX` (issue -> jurisdiction -> governing law -> forum -> confidence) is not required under Step 2's trigger condition ("more than one jurisdiction is plausibly relevant"). Recorded here as a deliberate no rather than an omission.

## Confidence

`confidence: asserted-by-user` in `intake/matter.json`, not `confirmed` - the user's statement is unambiguous but has not been independently corroborated against any document (e.g. an ET1/ET3, contract of employment) naming the employer or confirming no separate devolved-administration or overseas element applies. If evidence later surfaces suggesting the employer sits partly under a different NHS jurisdiction (e.g. an NHS Scotland or NHS Wales cross-border secondment - Wales is still England & Wales for ET purposes, but Scotland is not), this should be revisited rather than assumed closed.
