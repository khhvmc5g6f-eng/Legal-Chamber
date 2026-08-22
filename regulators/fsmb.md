---
regulator: FSMB (Federation of State Medical Boards) — coordinating body, NOT a licensing or disciplinary authority
jurisdiction: United States (federal-level coordination; actual licensure/discipline is state-based)
verification_status: COMMUNITY_REVIEWED
last_reviewed: 2026-08-22
reviewer: added specifically to avoid a false federal-equivalent structure — the US has no single national physician-licensing regulator, and this profile exists to say so honestly rather than dress FSMB up as one. Includes the Medical Board of California (MBC) as a real, live-verified worked example of where physician discipline actually happens. Sourced via live browser fetches against fsmb.org, mbc.ca.gov, and leginfo.legislature.ca.gov (California's official legislative-text site, the state-level equivalent of law.cornell.edu used elsewhere in this repository), not recalled from training data.
---

# FSMB — and the Medical Board of California as a worked example

**FSMB is not itself a licensing or disciplinary authority.** It has no power to issue, suspend, or revoke a physician's license to practice medicine anywhere. Actual physician licensure and discipline in the United States happens at the **state** medical board level — 50 states, DC, and several territories each run their own board under their own Medical Practice Act. This profile treats FSMB as what it actually is (a national coordinating and model-policy body serving those boards) and then works through **one real state board — the Medical Board of California (MBC)** — to show what physician discipline actually looks like where it happens. This mirrors `ftc.md`'s discipline of covering one regulator's real structure precisely, rather than the CNIL/ICO/FTC comparative sweep, because the sweep here would be across 50+ boards, which is out of scope for one profile.

## What FSMB actually is

Per `fsmb.org/about-fsmb/` (checked 2026-08-22): FSMB's stated mission is "to serve as a national voice for state medical boards, supporting them with services and initiatives that promote patient safety, the integrity of the practice of medicine, access to high-quality health care and regulatory best practices." Founded in 1912. Per `fsmb.org/u.s.-medical-regulatory-trends-and-actions/guide-to-medical-regulation-in-the-united-states/introduction/` (checked 2026-08-22), FSMB's own guide states plainly: "The Federation of State Medical Boards represents the state medical and osteopathic regulatory boards ... within the United States, its territories and the District of Columbia. It assists these boards as they go about their mandate of protecting the public's health, safety and welfare through proper licensing and discipline of physicians" — FSMB *assists*, the state boards *license and discipline*.

The same page grounds this in the US constitutional structure, not merely tradition: "States are authorized under the United States Constitution to establish laws and regulations protecting the health, safety, and general welfare of their citizens," and specifically cites the **10th Amendment** as the basis for state (not federal) authority over medical practice regulation. Each state has enacted its own **Medical Practice Act**, and "the practice of medicine is not an inherent right of an individual, but a privilege granted by the people of a state acting through their elected representatives." Medical licenses are state-issued and, per the same page, "undifferentiated" — a US physician's license is not specialty-specific, and board certification in a specialty is not a legal precondition of licensure.

FSMB's actual functions, verified across the pages above and `fsmb.org/about-fsmb/`:

- **Model policy and standards.** FSMB develops model legislation, policy statements, and a Model Act that individual state legislatures and boards may (but are not compelled to) adopt — this is advisory/coordinating, not binding federal law.
- **USMLE co-sponsorship.** FSMB co-owns and co-administers the United States Medical Licensing Examination together with the National Board of Medical Examiners (NBME); state boards, not FSMB, decide what passing score or exam history they require for licensure.
- **National Practitioner Data Bank (NPDB) facilitation.** FSMB maintains services (e.g. "Practitioner Direct") that help state boards report to, and query, the federally-run NPDB — FSMB is a facilitator of that federal data flow, not the operator of the NPDB itself.
- **Federation Credentials Verification Service (FCVS).** A centralized, physician-initiated credential-verification profile that individual state boards can accept as part of a licensure application, reducing duplicate primary-source verification work — again a shared-service/coordination role, not a licensing decision.
- **Data and reporting.** FSMB is "the primary center for collection, maintenance, and reporting of disciplinary actions taken against physicians by its member boards and other governmental authorities" (per search-engine-summarized secondary characterization of FSMB's own materials — this specific framing was not independently re-rendered from a primary FSMB page this session and should be treated as `COMMUNITY_REVIEWED`, not independently re-verified to the same standard as the `about-fsmb` and `introduction` pages above).

**No FSMB-level appeal route exists** for a physician disciplined by a state board, because FSMB does not make discipline decisions. Any appeal happens entirely within the disciplining state's own administrative and judicial system — which is exactly what the Medical Board of California example below shows.

## Worked example: Medical Board of California (MBC)

MBC was chosen as the worked example because `virtual-hospital`'s own jurisdiction registry already includes a `us-california` pack (see `../../virtual-hospital/jurisdictions/src/registry.ts`), so this profile and that pack can cross-reference each other honestly rather than inventing a second, disconnected state example.

### Investigation stages

Per `mbc.ca.gov/Consumers/File-a-Complaint/complaint-process.aspx` (checked 2026-08-22):

1. **Intake.** Complaints (from patients, family, insurers, other practitioners, mandated reporters, etc.) go to the Board's **Central Complaint Unit (CCU)**, part of the Enforcement Program, which reviews jurisdiction and requests records/licensee response as needed. Business and Professions Code § 800(c) lets the Board share a summary of the complaint with the licensee.
2. **Medical consultant referral.** If CCU finds sufficient basis, the complaint goes to a **medical consultant** for substantive clinical review. Urgent categories (sexual misconduct, physician impairment) can be referred straight to investigation.
3. **Formal investigation.** If a consultant finds a possible violation needing more investigation, the case goes to the **Division of Investigation / Health Quality Investigation Unit (HQIU)**. The Board's own page states this stage is "conducted in an ethical manner to determine whether the Board can prove that a violation occurred by 'clear and convincing evidence'" — a heightened evidentiary standard, notably higher than the ordinary civil "preponderance of the evidence" standard. Under Business and Professions Code § 2220.2(b), a harmed patient/family/representative has up to 60 days after notice to submit a statement about the harm experienced, which becomes part of the record.
4. **Accusation.** If the investigation supports discipline, the case is forwarded to the **California Attorney General's Office (AGO)**, which prepares and files an **accusation** — the formal charging document, served on the licensee.
5. **Hearing or default.** Per `mbc.ca.gov/Enforcement/Disciplinary-Process.aspx` (checked 2026-08-22): the physician has **15 days** after service of the accusation to file a "Notice of Defense" requesting a hearing (Government Code § 11506); failing to do so waives the hearing right and lets the Board act on the accusation unopposed. If a hearing is requested, it is held before an **Administrative Law Judge (ALJ)** of the Medical Quality Hearing Panel (Government Code § 11371) — an administrative proceeding "that closely resembles a court trial," with the physician entitled to (but not required to have) counsel.
6. **Proposed decision and Board review.** The ALJ issues a proposed decision, which goes to a **panel of the Board**, which may adopt, modify, or reject it — the Board panel, not the ALJ, makes the final disciplinary decision, and per Business and Professions Code § 2227 can increase or reduce the proposed penalty.

### Sanction range

Per **Business and Professions Code § 2227** (current text, `leginfo.legislature.ca.gov`, checked 2026-08-22), a licensee found guilty after an ALJ hearing, in default, or under a stipulated agreement may, by Board order:

1. have their license **revoked**;
2. have their right to practice **suspended for a period not to exceed one year**;
3. be placed on **probation**, including a requirement to pay probation-monitoring costs;
4. receive a **public reprimand**, which may include a requirement to complete Board-approved educational courses; or
5. face **any other action taken in relation to discipline as part of an order of probation**, at the Board's or ALJ's discretion.

Except for warning letters, medical review/advisory conferences, professional competency exams, and continuing-education activities completed by agreement, matters under § 2227 are public record (§ 803.1). This profile did not independently re-verify, this session, the specific minimum-wait-before-reinstatement periods (a commonly cited figure of three years for a revoked license, reducible to not less than one at Board discretion, appeared in a secondary-source search summary but was not independently rendered from `leginfo.legislature.ca.gov` this session) — flagged as `UNVERIFIED` at the primary-source-this-session standard rather than asserted.

### Appeal route and forum

Per **Government Code § 11521** (current text, `leginfo.legislature.ca.gov`, checked 2026-08-22): a physician may first petition the **Board itself for reconsideration**, a power that expires 30 days after the decision is delivered/mailed (or on the Board's own stated effective date if earlier), with a possible 10-day extension solely to evaluate the petition.

Beyond reconsideration, per **Code of Civil Procedure § 1094.5** (current text, `leginfo.legislature.ca.gov`, checked 2026-08-22) — the general California statute governing judicial review of any final administrative order made after a required hearing — a disciplined physician may petition the **California Superior Court** for a **writ of administrative mandamus**. The court's inquiry (per § 1094.5(b)) extends to whether the Board proceeded without/in excess of jurisdiction, whether there was a fair trial, and whether there was prejudicial abuse of discretion; § 1094.5(c) distinguishes two review standards depending on the case type: an "independent judgment" standard (where the court itself reweighs the evidence) versus a "substantial evidence" standard (more deferential to the agency). Multiple secondary legal sources checked this session describe physician license discipline specifically as a case where a "vested fundamental right" is at stake, triggering the more searching independent-judgment standard — this specific case-law characterization (tracing to *Bixby v. Pierno*-line California Supreme Court doctrine) was not independently re-verified against a primary court-opinion source this session, and is flagged `UNVERIFIED` at that level of specificity rather than asserted as settled without a primary citation, consistent with `ftc.md`'s own practice of flagging standard-of-review gaps rather than filling them by assumption.

Beyond the Superior Court, ordinary California appellate routes (Court of Appeal, then California Supreme Court by discretionary review) apply as they would to any Superior Court judgment; this profile did not independently re-verify MBC-specific appellate mechanics beyond the general CCP § 1094.5 route.

## What is NOT in this profile

No coverage of the other 49 states' medical boards — MBC was chosen as one verified worked example, consistent with `virtual-hospital`'s own `us-california`/`us-texas`/`us-new-york` sub-national approach, not as a claim that all state boards work identically. No independent verification of MBC's specific reinstatement-period statute. No independent verification of the *Bixby v. Pierno* independent-judgment case-law lineage against a primary court opinion. No coverage of nurse practitioner, physician assistant, or other non-physician licensee discipline at MBC (MBC's own jurisdiction, per its complaint-process page, covers M.D.s, licensed midwives, and polysomnography licensees specifically — D.O.s go to the separate Osteopathic Medical Board of California). No coverage of criminal referral (the AGO's role here is civil/administrative accusation, not criminal prosecution, which is a separate track through county district attorneys or the state DOJ's criminal division).

## Primary sources checked

- `fsmb.org/about-fsmb/` — FSMB mission, vision, founding date, "supports state medical boards" framing
- `fsmb.org/u.s.-medical-regulatory-trends-and-actions/guide-to-medical-regulation-in-the-united-states/introduction/` — FSMB's own statement that it "assists" boards rather than licenses/disciplines, 10th Amendment basis, Medical Practice Act structure, undifferentiated licensure
- `mbc.ca.gov/Consumers/File-a-Complaint/complaint-process.aspx` — CCU intake, medical consultant referral, HQIU investigation, "clear and convincing evidence" standard, § 2220.2(b) impact-statement right, AGO accusation stage
- `mbc.ca.gov/Enforcement/Disciplinary-Process.aspx` — 15-day Notice of Defense window (Government Code § 11506), ALJ hearing before the Medical Quality Hearing Panel, Board panel's adopt/modify/reject power
- `leginfo.legislature.ca.gov` (Business and Professions Code § 2227) — full statutory sanction list: revocation, suspension ≤1 year, probation, public reprimand, other probation terms; public-record rule
- `leginfo.legislature.ca.gov` (Government Code § 11521) — reconsideration procedure and 30-day window
- `leginfo.legislature.ca.gov` (Code of Civil Procedure § 1094.5) — writ of administrative mandamus, scope of judicial inquiry, independent-judgment vs. substantial-evidence standards
