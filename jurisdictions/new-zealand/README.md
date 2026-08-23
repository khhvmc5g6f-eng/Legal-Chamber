---
jurisdiction: New Zealand
legal_system: common-law
verification_status: STRUCTURAL_DRAFT
last_reviewed: 2026-08-22
reviewer: initial repository build (not independently re-checked by a second reviewer); a populated Authority Graph was added the same day via four parallel-agent research passes, each independently re-verified where reachable against a live primary source by the orchestrating session before being written - see "Populated Authority Graph" below
---

# New Zealand

See `docs/HONEST_STATUS.md`. New Zealand is a single unitary jurisdiction (unlike Australia/Canada/US), which simplifies court structure but does not reduce the need to verify current law - New Zealand has no entrenched constitution restricting Parliament, so statute can change quickly relative to some other common-law systems.

## Court hierarchy

```
Supreme Court of New Zealand (final appellate court, since 2004; replaced appeals to the UK Privy Council)
  └── Court of Appeal of New Zealand
        └── High Court of New Zealand (general/inherent jurisdiction, trial + some appellate)
              └── District Court (most civil and criminal first instance business)
Employment Court (specialist, separate track from the general courts for employment matters)
```

## Authority hierarchy

The Supreme Court binds all New Zealand courts. Pre-2004 Privy Council decisions remain persuasive/historically binding depending on when a matter arose - this pack does not resolve that transitional question for any specific case; check it live if relevant.

## Citation style

New Zealand uses a style close to OSCOLA/Bluebook conventions with local variants; neutral citation shape e.g. `Party v Party [2023] NZSC 12`. Statute citation: `Short Title Year, s X`.

## Governing statutes/codes (named, not summarised)

No single code; Acts of Parliament plus common law. Key procedural instruments by name only: the High Court Rules, the District Court Rules.

## Primary sources to check against

- `nzlii.org` (NZLII) - legislation and case law
- `legislation.govt.nz` - official New Zealand legislation
- `courtsofnz.govt.nz` - judgments and practice notes

## Populated Authority Graph

`authorities/` holds four doctrinal files across four subjects - New Zealand's first Authority Graph content in this repository.

| File | Subject | Lead case |
|---|---|---|
| `authorities/contract-cancellation-misrepresentation-substantiality.json` | Contract Law - the statutory cancellation right for misrepresentation and its substantiality gate | *Anderson v De Marco* [2020] NZHC 2979 |
| `authorities/tort-acc-bar-exemplary-damages-exception.json` | Tort Law - the ACC no-fault bar's exemplary-damages exception (a structurally distinctive feature of NZ tort law) | *Couch v Attorney-General (No 2)* [2010] NZSC 27 |
| `authorities/criminal-self-defence-excessive-force-no-partial-defence.json` | Criminal Law - excessive self-defence's exclusion from partial-defence status | *Murray v R* [2018] NZSC 15 |
| `authorities/treaty-waitangi-principles-paramount-clause.json` | Treaty of Waitangi jurisprudence - the paramount status of a "principles of the Treaty" clause | *New Zealand Maori Council v Attorney-General* [2013] NZSC 6 |

Deliberately narrow, matching the same one-or-two-doctrinal-points-per-file discipline used throughout this repository's other jurisdictions. The dominant access-pattern finding this session: **legislation.govt.nz and courtsofnz.govt.nz both presented an active bot-check gate** (an AWS WAF JavaScript challenge for legislation.govt.nz, a "Human Verification" gate for courtsofnz.govt.nz) to every direct fetch attempted across all four research passes - not a simple 403, but an interactive challenge. Per this repository's rules, no pass attempted to solve or bypass these gates. Each instead used NZLII (`nzlii.org`), a free-access, non-proxy legal information institute with the same institutional model as AustLII/CanLII, as the working primary source where NZLII itself was reachable; where NZLII also blocked a specific fetch, the citing-judgment method or independent secondary-source corroboration was used instead, stated honestly in each file. Two files (Contract, Tort) rest on the fully-verified two-tier chain (researching agent's genuine NZLII fetch, this session's own independent WebSearch corroboration since NZLII itself became intermittently blocked on re-fetch); the Criminal Law entry could not reach a reliable primary statute text at all and rests on corroborated secondary sourcing throughout.

## What is NOT in this pack

No verified procedural deadline beyond what the four Authority Graph entries above touch on incidentally.
