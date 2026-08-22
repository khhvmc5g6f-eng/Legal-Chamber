---
regulator: HIS (Healthcare Improvement Scotland)
jurisdiction: Scotland only - Scotland's equivalent of England's CQC, but NOT a like-for-like equivalent; see the statutory-model note below before assuming parity
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added alongside cqc.md to build out the UK healthcare-regulator set, sourced via live WebSearch against healthcareimprovementscotland.scot and legislation.gov.uk, not recalled from training data
---

# HIS

The eleventh regulator profile in this repository - see `README.md`. Like CQC and HIW, HIS is a **provider/service quality regulator**, not an individual-practitioner fitness-to-practise body.

## Statutory basis - and a materially different model from CQC, confirmed this session

HIS was established under the **Public Services Reform (Scotland) Act 2010**, taking over the functions of NHS Quality Improvement Scotland and the Care Commission's independent-healthcare regulatory role. Sections 10A-10Z19 of the **National Health Service (Scotland) Act 1978** (inserted by section 108 of the 2010 Act) set out its scrutiny functions. **This is not a single unified registration regime the way CQC's is.** Per the sources checked (checked 2026-08-22): HIS **regulates and registers** independent healthcare services (under the Healthcare Improvement Scotland (Requirements as to Independent Health Care Services) Regulations 2011), but for **NHS Scotland** bodies it performs **inspection and scrutiny** without an equivalent registration-and-cancellation power - there is no "deregistering an NHS Scotland hospital" mechanism analogous to what CQC can do to an NHS trust in England. Do not assume the CQC model transfers across; it doesn't, on the sources checked.

## Enforcement stages (independent healthcare registration track)

Per `healthcareimprovementscotland.scot` and `legislation.gov.uk`'s text of the Public Services Reform (Scotland) Act 2010 (checked 2026-08-22), for the independent-healthcare registration function specifically:

- **Registration** - an independent healthcare service must register with HIS before operating; operating a scoped-in service without registration is itself an offence.
- **Condition Notice** / **Improvement Notice** - HIS can require specific action or standards be met.
- **Cancellation of registration** - if, having been issued an Improvement Notice, a service is still non-compliant, HIS can act to cancel registration.
- **Emergency cancellation** - HIS can apply to the **sheriff** for an order immediately cancelling registration where the sheriff considers there is a serious risk to the life, health, or wellbeing of service users absent that order.

For NHS Scotland bodies, HIS instead runs a programme of proactive inspections and responds to incident notifications, with enforceable "requirements" where standards aren't met, but (per the sources checked) without the registration-cancellation lever described above.

## Sanction range

For the independent-healthcare track: **condition notices**, **improvement notices**, **cancellation of registration** (routine, following an unremedied Improvement Notice), and **emergency cancellation** (via sheriff order, for immediate serious risk). No fixed monetary-fine figure was identified in the sources checked this session for civil enforcement; separately, operating without required registration is a criminal offence under the 2010 Act, but a maximum penalty figure was not independently confirmed this session - flagged `UNVERIFIED` below.

## Appeal route and forum

Per `legislation.gov.uk`'s text of the Public Services Reform (Scotland) Act 2010 (checked 2026-08-22): a person given notice of a decision to implement a registration proposal (e.g. to cancel or vary conditions) may appeal to the **sheriff**, within **14 days** of that notice - notably a shorter window and a different forum (the sheriff court, not a specialist tribunal) than the 28-day First-tier Tribunal route used by CQC in England and HIW in Wales. On appeal, the sheriff can confirm the decision, direct that it not have effect, and where registration is not cancelled, vary, remove, or add conditions.

## Primary sources checked

- `healthcareimprovementscotland.scot/inspections-reviews-and-regulation/regulation-of-independent-healthcare/background-and-legislation/` and its sibling pages on how HIS inspects independent services (indexed via WebSearch)
- `legislation.gov.uk/asp/2010/8/section/108` (Public Services Reform (Scotland) Act 2010, section 108, indexed via WebSearch)
- `legislation.gov.uk/ssi/2011/182` (Healthcare Improvement Scotland (Requirements as to Independent Health Care Services) Regulations 2011, indexed via WebSearch)
- `gov.scot` "Annex 2: Key legislation relating to the functions and powers of Healthcare Improvement Scotland" (operating-framework document, indexed via WebSearch)

## What is NOT in this profile

No confirmed maximum penalty figure for the criminal offence of operating an unregistered independent healthcare service in Scotland - flagged `UNVERIFIED`, not checked against the Act's own penalty provision this session. No verified detail on HIS's separate quality-improvement/guideline-setting function (distinct from its scrutiny/regulatory role, and a much larger part of what "Healthcare Improvement Scotland" does day-to-day) - not researched here, this profile covers only the regulatory/enforcement function per this repository's regulator-profile template. No case-by-case HIS enforcement-action database - this is a procedural/structural profile only.
