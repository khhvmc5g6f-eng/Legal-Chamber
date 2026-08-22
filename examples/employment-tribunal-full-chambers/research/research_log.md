# Research log, M1-KESTREL

Per `skills/legal-research/SKILL.md` and `skills/legal-authorities/SKILL.md`. Covers (1) verification of the user-supplied seeded authority and (2) bidirectional supporting/disconfirming research on the substantive heads of claim. All searches run 2026-08-22 via WebSearch (open web) and one blocked WebFetch attempt on BAILII (403 - noted per source, not concealed).

## Seeded authority check: "Whitfield v Anglia NHS Foundation Trust [2021] UKEAT 0142_21_0309"

Applying `skills/legal-authorities/SKILL.md` checklist step by step, not accepting the citation because it looks plausible:

| Step | Query | Source | Result |
|---|---|---|---|
| 1. Existence (citation string) | `"UKEAT 0142_21" OR "UKEAT/0142/21"` | web search | No hit for this citation in 2021. Case number 0142 in other years resolves to unrelated real cases: Oliver v The Ultimate Solution Partnership (UKEAT/0142/11), Rawlinson v Brightside Group (UKEAT/0142/17), Spaceman v ISS Mediclean (UKEAT/0142/18), Inchcape Retail v Shelton (UKEAT/0142/19). No 2021 case with this number found on gov.uk, BAILII index, or general search. |
| 1. Existence (party names) | `"Whitfield v Anglia NHS Foundation Trust" EAT` | web search | No hit. Search engine substituted unrelated "North West Anglia NHS Foundation Trust" cases (Gregg v NW Anglia [2019] EWCA Civ 387; Zagorski v NW Anglia [2024] EAT 164; Atton and Harper ET decisions) - none involve a claimant named Whitfield. |
| 1. Existence (party names, variant) | `"Whitfield" v NHS Foundation Trust site:gov.uk employment-appeal-tribunal-decisions` | web search | The only "Whitfield" hit anywhere is **Ms B Whitfield v Guy's and St Thomas' NHS Foundation Trust: 2301668/2022** - a real, differently-numbered, differently-dated **first-instance Employment Tribunal** decision (not EAT), against a **different Trust** entirely. A genuine near-name-collision, not corroboration - exactly the trap `legal-authorities/SKILL.md` step 2 warns about ("case-name collisions... cross-jurisdiction namesakes"). |
| 1. Existence (site-restricted) | `Whitfield NHS whistleblowing site:bailii.org` | web search | No hit - only unrelated BAILII index pages returned. |
| 1. Existence (BAILII direct) | `bailii.org/cgi-bin/find_by_citation.cgi?citation=UKEAT+0142+21` | WebFetch | HTTP 403 - could not confirm or deny via this route this session; existence conclusion below rests on the independent web searches above, not on this blocked attempt, and this gap is disclosed rather than silently dropped. |
| 2. Identity match | n/a - nothing to match against | - | Cannot proceed; no located case to compare court/date/jurisdiction against. |
| 3. Proposition match | n/a | - | Cannot proceed for the same reason. |
| 4/5. Currency/treatment | n/a | - | Cannot proceed for the same reason. |
| Citation-shape sanity check | `python3 scripts/citation_lint.py` on the seeded string | deterministic tool, this repo | Linter matched a truncated `[2021] UKEAT 0142` shape - confirms the string is shape-plausible, which the linter's own documentation (`citation/README.md`) warns is not the same as being real: "a citation can pass the linter and still be fabricated." The full string mixes two incompatible real EAT citation conventions (pre-2020 `UKEAT/NNNN/YY/initials` and post-2020 `[year] EAT number`) and appends what looks like a BAILII file-slug fragment (`0142_21_0309`, matching the `caseNo_year_dayMonth` pattern seen in real BAILII UKEAT URLs) rather than a citation - itself a tell that this was constructed to look like a citation, not transcribed from one. |

**Verdict: NO_VERIFIED_AUTHORITY_LOCATED.** No court, tribunal, party-name match, or citation-number match corroborates this authority existing in any form. It is not merely unverified in the weak sense (not yet checked) - it was actively searched for, independently, by citation and by party name, across the official EAT decisions listing, BAILII, and general web search, and found nowhere except as a coincidental partial name-echo of an unrelated real ET case. Recorded in `authorities/authorities.json` as `AUTH-SEEDED-001`, `rejected_reason: citation error / fabrication`. It is not relied upon for any proposition in this matter, including the whistleblowing-detriment head (ISS-004) it was offered to support - that head instead rests on the real, verified authorities below (AUTH-002, AUTH-004).

## Substantive supporting/disconfirming research (bidirectional, per legal-research SKILL.md step 1)

| Query | Source | Date | Supporting/disconfirming | Considered | Selected | Rejected | Rejection reason |
|---|---|---|---|---|---|---|---|
| Fecitt v NHS Manchester causation "materially influenced" | web search (BAILII URL identified, direct fetch 403; corroborated via Employment Cases Update, Croner-i, CMS, Reed Smith) | 2026-08-22 | Supporting (ISS-004 causation element) | Fecitt; also checked for later Supreme Court reversal | AUTH-002 | - | - |
| Fecitt v NHS Manchester overruled/distinguished check | web search | 2026-08-22 | Disconfirming attempt (currency check) | No overruling or SC reversal found in available sources | - | - | Not rejected; currency remains as found, `LAW_AS_OF 2026-08-22` per this search only, not an independent Westlaw/Lexis citator check |
| Kuzel v Roche Products burden of proof s.103A | web search (BAILII URL identified, not fetched; Croner, Practical Law, swarb.co.uk) | 2026-08-22 | Supporting (ISS-003 burden element) | Kuzel | AUTH-003 | - | - |
| Beatt v Croydon Health Services whistleblowing reasonable belief | web search (BAILII URL identified; 12 KBW, Bird & Bird, Employment Cases Update) | 2026-08-22 | Supporting (ISS-003/004 - and itself a real, correctly-named NHS whistleblowing EAT/CA authority, a useful contrast to the seeded fabrication) | Beatt | AUTH-004 | - | - |
| Gallop v Newport City Council OH knowledge "rubber stamp" | web search (BAILII URL identified; Croner, Legal Island, Brightmine) | 2026-08-22 | Supporting (ISS-005/006/007 employer-knowledge elements) | Gallop | AUTH-005 | - | - |
| Environment Agency v Rowan PCP identification | web search (casemine secondary report of [2008] ICR 218) | 2026-08-22 | Supporting (ISS-007 - explains why F-024 gap is dispositive) | Rowan | AUTH-006 | - | - |
| ACAS EC Day A/Day B "reasonably practicable" case law | web search (Lexology/Stevens & Bolton reporting Raison v DF Capital Bank Ltd) | 2026-08-22 | Disconfirming/limiting (checks whether EC start date could rescue a late claim) | Raison | AUTH-007 (UNVERIFIED tier - see rejection reason in authorities.json) | - | Logged as a lead, not relied upon, pending primary-source confirmation |
| Employment Rights Act 2025 s.152 time-limit extension to 6 months, in-force date | web search (multiple independent employment-law-firm summaries: Impact Employment Law, Thompsons, Make UK, Didlaw, GA Solicitors, Brightmine) | 2026-08-22 | Disconfirming/currency (checks whether the statutory 3-month period this matter's limitation.md relies on is about to change) | Multiple consistent secondary reports | Noted in `procedure/limitation.md` addendum below | - | Not independently confirmed against legislation.gov.uk's Employment Rights Act 2025 text this session - flagged `VERIFIED_SECONDARY_SOURCE` only, high consistency across independent commentators |

## Rejected authority log

| Authority | Why not relied upon |
|---|---|
| "Whitfield v Anglia NHS Foundation Trust [2021] UKEAT 0142_21_0309" | citation error / fabrication - no verified authority located, see full trail above and `authorities/authorities.json` AUTH-SEEDED-001 |
| Ms B Whitfield v Guy's and St Thomas' NHS Foundation Trust (2301668/2022) | Not the seeded case (different Trust, different court level, different year, different number) and not otherwise relied upon in this matter - noted only to show what the name-collision actually was |
| Raison v DF Capital Bank Ltd | Full citation not independently confirmed this session; kept as a research lead only, not relied upon for any proposition (see AUTH-007) |

## Stopping point

Per `legal-research/SKILL.md` step 4: research on the seeded authority is saturated (it was searched by citation, by party name in two variants, by site-restriction, and by the shape-linter, with a consistent negative result across all of them - further searching without new terms would not change this). Research on the substantive heads is NOT saturated - this pass verified enough authority to confirm the *shape* of each head's legal test and to show why several evidentiary gaps already logged in `issues/issues.json` (F-010, F-016, F-020, F-022, F-024) are dispositive rather than cosmetic, but it did not attempt full case-law coverage of every element (e.g. no search was run yet on the disability-status "long-term effect" test itself, or on ACAS Code uplift case law). Flagged as further work, not silently left incomplete.
