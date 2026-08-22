# Legal Chambers: Full Original Specification (reference / backlog)

This is the complete specification this repository implements a first, honestly-scoped subset of. It is preserved verbatim as the backlog for future work, see `HONEST_STATUS.md` for what has actually been built so far, and `OPERATING_RULES.md` / `../CLAUDE.md` for what governs this repository's own development in the meantime.

Where this document and the shipped code differ on a point of practice, the shipped code (each skill's own `SKILL.md`, the schemas, the scripts) governs what actually happens. This document is the aspiration; `HONEST_STATUS.md` is the ledger of what has closed the gap so far.

---

## LEGAL CHAMBER 2.0

*Global Legal Intelligence, Research, Drafting, Evidence, Litigation, Transaction, Academic and Adversarial Reasoning System*

### MASTER BUILD INSTRUCTION

Build a production-grade, open, extensible, jurisdiction-aware legal Agent Skill ecosystem named **LEGAL CHAMBER**, with primary router skill `legal-work`.

This must not be built as one enormous prompt. It is a modular legal operating system for Claude Code, Agent Skills and compatible agent environments, coordinating specialised agents, deterministic legal tooling, jurisdiction packs, court-rule packs, document templates, research connectors, evidence systems, academic rubrics, procedural engines and adversarial simulations.

It must support individual users, law students, academics, paralegals, solicitors, barristers, attorneys, in-house legal teams, law firms, regulators, public authorities, corporate legal departments, litigation teams, and compliance teams.

Its governing principle:

```
VERIFIED FACTS → VERIFIED LAW → VERIFIED AUTHORITY → LEGAL TEST →
APPLICATION → EVIDENCE → COUNTERARGUMENT → PROCEDURE → REMEDY →
ADVERSARIAL TESTING → CONCLUSION
```

The system must never reverse-engineer a preferred legal outcome and then search selectively for material supporting it.

### PART I: FUNDAMENTAL OPERATING RULES

Legal Chambers must never fabricate: cases, neutral citations, report citations, statutes, statutory provisions, regulations, court rules, practice directions, tribunal rules, quotations, paragraph numbers, judges, court names, procedural deadlines, legal tests, academic sources, facts, evidence, correspondence, exhibits, expert opinions, or probabilities represented as empirical findings.

If information cannot be established, say `UNKNOWN`, `UNVERIFIED`, `INSUFFICIENT EVIDENCE`, or `NO VERIFIED AUTHORITY LOCATED`. Never substitute plausibility for verification.

### PART II: PRODUCT ARCHITECTURE

```
legal-chambers/
├── README.md, LICENSE, CHANGELOG.md, CONTRIBUTING.md, SECURITY.md,
│   GOVERNANCE.md, AGENTS.md, CLAUDE.md
├── skills/       (legal-work, legal-research, legal-draft, legal-review,
│                  legal-evidence, legal-litigation, legal-contract,
│                  legal-regulatory, legal-transaction, legal-academic,
│                  legal-appeal, legal-negotiation, legal-moot,
│                  legal-authorities, legal-prospects, legal-verify)
├── agents/       (intake, jurisdiction, research, evidence, solicitors,
│                  counsel, opposition, judiciary, academic, transactional,
│                  regulatory, negotiation, quality)
├── jurisdictions/, courts/, regulators/, citation/, rubrics/, templates/,
│   schemas/, workflows/, connectors/, scripts/, benchmarks/, evaluations/,
│   examples/, docs/
```

### PART III: PROGRESSIVE DISCLOSURE

The root `SKILL.md` stays small. Its purpose: identify legal intent, establish jurisdiction, classify task and risk, choose workflow, load appropriate specialist skills/jurisdiction/procedural/document packs, invoke agents, enforce verification gates. Do not load thousands of pages of legal material unnecessarily.

### PART IV: LEGAL MATTER ROUTER

Every request is classified by matter type: Research, Litigation, Administrative and Public Law, Criminal (jurisdiction-pack-gated), Employment, Regulatory, Transactional, Advisory, Negotiation and ADR, Academic. Each routes differently.

### PART V: MATTER COMPLEXITY ENGINE

L1 QUICK · L2 VERIFIED · L3 PROFESSIONAL · L4 ADVERSARIAL · L5 CHAMBERS · L6 COMPLEX MATTER. The orchestrator may escalate automatically.

### PART VI: MATTER WORKSPACE

```
matters/MATTER-ID/
├── intake/ facts/ evidence/ chronology/ issues/ research/ authorities/
│   drafts/ opposition/ moot/ procedure/ costs/ prospects/ final/
```

No unrelated matter information should bleed into another matter.

### PART VII: CONFLICT CHECK ENGINE

Before sensitive professional-style work, record relevant parties, former names, corporate entities, directors, related entities, witnesses, experts, counsel, opposing lawyers. Do not ingest unnecessary confidential information before the conflict position is understood.

### PART VIII: CONFIDENTIALITY CLASSIFICATION

`PUBLIC · PRIVATE · CONFIDENTIAL · LEGALLY PRIVILEGED · LITIGATION PRIVILEGED · WITHOUT PREJUDICE · WITHOUT PREJUDICE SAVE AS TO COSTS · COURT-RESTRICTED · SUPPRESSED · PERSONAL DATA · SPECIAL CATEGORY DATA · SECRET`.

### PART IX: PRIVILEGE ENGINE

Distinguish confidentiality, legal advice privilege, litigation privilege, without-prejudice protection, common interest, joint privilege, waiver, inadvertent disclosure. The applicable jurisdiction controls. Never assume confidential automatically means privileged.

### PART X: DATA GOVERNANCE

Configurable rules on retention, deletion, redaction, access, encryption, model training, external API use, local vs cloud models. Highly sensitive matter material should be capable of being restricted to approved environments.

### PART XI: JURISDICTION FIRST

Before substantive legal reasoning determine: `COUNTRY, LEGAL_SYSTEM, SUB-JURISDICTION, COURT, TRIBUNAL, REGULATOR, GOVERNING_LAW, PROCEDURAL_LAW, APPELLATE_LEVEL, LAW_AS_OF, CITATION_SYSTEM`. Do not treat "UK law" as sufficient where England and Wales, Scotland and Northern Ireland differ.

### PART XII: MULTI-JURISDICTION ENGINE

Build a `JURISDICTION_MATRIX` per issue: potential jurisdiction, applicable law, procedural forum, conflict rule, confidence, authority. Do not collapse a conflict-of-laws issue into one generic answer.

### PART XIII: FORUM ANALYSIS

Where forum is contested: jurisdiction agreements, arbitration clauses, governing-law clauses, domicile, residence, place of performance, place of harm, statutory jurisdiction, service-out rules, forum non conveniens, mandatory jurisdiction, applicable treaty.

### PART XIV: LEGAL CURRENCY

Every matter receives `LAW_AS_OF`; every important authority receives `VERIFIED_AT`. Monitor commencement, amendment, repeal, replacement, appeal, overruling, new Practice Directions, revised court rules, regulator guidance.

### PART XV: BITEMPORAL LAW MODEL

Represent law with Valid Time (when the rule legally applied) and Knowledge Time (when Legal Chambers verified it), so a question about 2022 law isn't accidentally answered with 2026 law.

### PART XVI: AUTHORITY HIERARCHY

Every jurisdiction pack defines binding, persuasive, coordinate, foreign, and secondary authority, machine-readably.

### PART XVII: AUTHORITY GRAPH

Cases exist in relationships: follows / distinguishes / overrules / applies / criticised-by, forming an Authority Treatment Graph.

### PART XVIII: AUTHORITY VERIFICATION

Every cited case needs: case name, court, jurisdiction, date, neutral citation, report citation, judge/panel, relevant paragraph, legal proposition, treatment, primary-source link, verification timestamp. If unavailable, it must not silently become a final authority.

### PART XIX: CITATION EXISTENCE TEST

1. search citation 2. search case name 3. locate primary/authoritative copy 4. check court 5. check date 6. check proposition 7. check treatment. A citation only appearing in another AI-generated document is not verification.

### PART XX: AUTHORITY PROPOSITION TEST

Does this authority actually establish the proposition cited? Detect wrong proposition, dicta-as-ratio, dissent-as-majority, counsel-submission-as-judgment, overturned first-instance decisions, different statutory regime/jurisdiction.

### PART XXI: QUOTATION LOCK

Store QUOTE / SOURCE / PINPOINT / VERIFIED_HASH. If verification fails: remove quotation marks and paraphrase.

### PART XXII: CASE NAME COLLISION

Detect same-name parties, appeals, remittals, consolidated cases, anonymised decisions, different jurisdictions. Require exact authority resolution.

### PART XXIII: PRIMARY SOURCE PREFERENCE

Prefer legislation databases, official judgments, official rules, regulators, official treaty sources. Secondary material for discovery, commentary, synthesis, criticism.

### PART XXIV: RESEARCH PROVIDER ABSTRACTION

Connectors for official court repositories, official legislation, Westlaw/Lexis/vLex/HeinOnline where authorised, CourtListener, CanLII, AustLII, NZLII, BAILII, legislation.gov.uk, Find Case Law, EUR-Lex, HUDOC, Curia, jurisdiction-specific databases. Do not hard-code a commercial database requirement.

### PART XXV: RESEARCH QUERY PLANNER

Generate searches using legal concepts, statutory terms, synonyms, alternative causes of action, adverse propositions, procedural terminology, historical terminology. Do not search only for the desired outcome.

### PART XXVI: BIDIRECTIONAL RESEARCH

Every material proposition requires a SUPPORTING SEARCH and a DISCONFIRMING SEARCH.

### PART XXVII: RESEARCH SATURATION

Continue until: authority hierarchy sufficiently resolves the issue; diminishing returns; user-defined budget; or genuine uncertainty remains. Record why research stopped.

### PART XXVIII: LEGAL PROOF GRAPH

Every significant conclusion traces to Legal Rule → Authorities, Element 1/2 → Facts/Evidence, Opposing Proposition → Authority, and a Confidence rating. No conclusion floats free of its foundations.

### PART XXIX: PROOF GRAPH INTEGRITY

`SUPPORTED` only where required edges exist; otherwise `PARTIALLY SUPPORTED` or `UNSUPPORTED`. Feeds prospects analysis.

### PART XXX: FACT LEDGER

Fact ID, proposition, date, source, status, evidence, contrary evidence, materiality, confidence. Statuses: `ESTABLISHED, ADMITTED, USER-ASSERTED, DISPUTED, INFERRED, ASSUMED, UNKNOWN, CONTRADICTED`.

### PART XXXI: EVIDENCE LEDGER

Evidence ID, type, source, creator, date created, date obtained, authenticity, admissibility, privilege, reliability, issues supported, issues undermined.

### PART XXXII: EVIDENCE PROVENANCE

Preserve filename, original hash, modified hash, metadata, acquisition source, chain-of-custody. Never silently modify original evidence.

### PART XXXIII: DOCUMENT VERSIONING

`ORIGINAL, WORKING COPY, REDACTED COPY, COURT COPY, EXHIBIT COPY`. Never overwrite original evidence.

### PART XXXIV: CHRONOLOGY ENGINE

Date, time, event, actor, source, evidence, disputed, legal significance, confidence. Detect impossible dates, missing periods, retrospective documents, conflicting timestamps, limitation implications.

### PART XXXV: TIMELINE VISUALISATION

Master, procedural, communication, medical, contractual, regulatory chronologies.

### PART XXXVI: CONTRADICTION ENGINE

Compare witness statements, pleadings, contemporaneous documents, emails, records, prior accounts. Classify `MINOR, EXPLAINABLE, MATERIAL, SERIOUS, POTENTIALLY DISPOSITIVE`.

### PART XXXVII: DISCLOSURE AND DISCOVERY ENGINE

Disclosure/discovery/document review/relevance/privilege/responsiveness/confidentiality/issue tagging/production. `DISCLOSURE_INDEX` and `DOCUMENT_REVIEW_MATRIX`.

### PART XXXVIII: MISSING DOCUMENT DETECTOR

Identify documents logically expected but absent. Do not presume what missing evidence contains.

### PART XXXIX: ISSUE TREE

Matter → Jurisdiction → Cause of action → Elements → Defences → Evidence → Procedure → Limitation → Remedy → Costs → Appeal, mapped to the Proof Graph.

### PART XL: ELEMENTS ENGINE

Element, burden, standard, authority, fact required, evidence available, evidence missing, opposition.

### PART XLI: BURDEN AND STANDARD ENGINE

Legal burden, evidential burden, standard of proof, presumptions, reverse burdens.

### PART XLII-XLIV: SOLICITOR / COUNSEL / OPPOSING LEGAL TEAMS

Solicitor Team constructs the strongest sustainable case. Counsel Team independently challenges it. Opposing Legal Team (separate context) advances the strongest reasonable case for the other party, never a manufactured weak opposition.

### PART XLV: FIVE-STAGE ADVERSARIAL SYSTEM

Hearing 1 Justiciability and Pleadability. Hearing 2 Doctrinal and Authority Challenge. Hearing 3 Evidence and Proof. Hearing 4 Procedure, Remedy and Costs. Hearing 5 Full Merits (user's counsel, opposing counsel, reply, neutral judicial panel, reasoned simulated disposition).

### PART XLVI: HEARING MEMORY

Each hearing receives the previous findings and repairs. Five identical arguments is a failure.

### PART XLVII-XLVIII: JUDICIAL ROUTER / DECISION PROTOCOL

Select the correct simulated decision-maker; identify issues, applicable law, burden, findings of fact, application, disposition, remedy, reasons, residual uncertainty. May decide against the user.

### PART XLIX: APPELLATE PANEL

After final merits, ask both directions: how could the opponent appeal if the user wins; what appeal points exist if the user loses.

### PART L-LIII: PRECEDENT DISTINGUISHING / ANALOGICAL REASONING / COUNTERFACTUAL TEST / CASE THEORY ENGINE

Compare by statutory text, material facts, procedural posture, policy, jurisdiction, court level, remedy, never call a case "distinguishable" without naming the material difference. Ask which fact, if changed, would most alter the outcome. Keep LEGAL THEORY, FACT THEORY, EVIDENCE THEORY, REMEDY THEORY, OPPONENT THEORY coherent with each other.

### PART LIV-LIX: WITNESS EVIDENCE / CROSS-EXAMINATION / EXPERT EVIDENCE

Separate what a witness knows from what a lawyer wants to prove, never insert facts a witness hasn't supplied. Build cross-examination themes, propositions, contradiction maps, question sequences. Distinguish expert evidence from advocacy.

### PART LIX-LXI: DAMAGES / REMEDIES / COSTS ENGINES

Deterministic calculators for interest, loss periods, schedules. Analyse damages, declarations, injunctions, specific performance, restitution, rescission, judicial-review remedies, statutory compensation, costs, interest, keep merits and costs risk analytically separate.

### PART LXII-LXVI: PROCEDURAL CALENDAR / DEADLINE VALIDATION / FILING PRE-FLIGHT / COURT RULE OVERRIDE / JUDGE-SPECIFIC RULES

Build deadlines from verified rules, not memory. Excluded days, weekends, holidays, service methods, deemed service, time zones, extensions. Pre-flight-check court, case number, parties, limits, fonts, pagination, certificates, statements of truth, signatures, exhibits, filing method, service. Official rules override house style. Distinguish binding local rules from mere preferences.

### PART LXVII-LXXIV: CONTRACT / DUE DILIGENCE / TRANSACTION / NEGOTIATION / SETTLEMENT / MEDIATION

Extract clauses; map dependencies; build red-flag reports and due-diligence registers; track conditions precedent; model BATNA/WATNA and settlement scenarios; prepare mediation positions, concessions ladders, settlement ranges.

### PART LXXV-LXXVII: REGULATORY WORKFLOW / ALLEGATION MATRIX / MITIGATION ENGINE

Identify regulator, statutory powers, investigation stage, allegations, evidential basis, procedural protections, response deadlines, sanction range, appeal rights. Keep liability and mitigation separate.

### PART LXXVIII-LXXIX: PUBLIC LAW / HUMAN RIGHTS WORKFLOW

Amenability, standing, time, alternative remedy, legality, procedural fairness, rationality, proportionality, legitimate expectation, human rights, relief, discretion, using the actual jurisdiction's framework.

### PART LXXX-LXXXII: COMPARATIVE LAW / LEGISLATIVE HISTORY / STATUTORY INTERPRETATION

Comparative tables (issue / jurisdiction A / jurisdiction B / common principle / material divergence / practical consequence), not parallel summaries. Text, context, purpose, definitions, structure, exceptions, regulations, precedent, interpretative statutes.

### PART LXXXIII-LXXXVIII: ACADEMIC MODE / EXCELLENCE STANDARD / MARKING PANEL / RUBRIC EVIDENCE

Establish university, programme, level, module, assignment, word count, rubric, referencing, learning outcomes before writing. Independent markers per dimension plus an external-examiner check against grade inflation. Never invent institutional rubrics.

### PART LXXXIX-XCIV: PLAIN LANGUAGE / AUDIENCE / DOCUMENT PURPOSE / QUALITY / PROLIXITY / ARGUMENT MAP

Style follows audience. Ask what the document must cause its reader to understand, accept, or do. Maximise precision, relevance, navigability, authority, factual support, procedural compliance, not word count.

### PART XCV-C: STEELMAN / DEVIL'S ADVOCATE / FALSIFICATION / DECISIVE ISSUE / CASE-KILLER / REMEDY-FIRST

Construct the strongest reasonable opposing argument before finalising. Ask what would make the conclusion wrong, then look for it. Rank issues by likely importance. Look specifically for case-killers (limitation, jurisdiction, res judicata, standing, exclusion clause, statutory bar, exhaustion, immunity, mandatory procedural failure). Ask early what remedy actually follows if every liability argument succeeds.

### PART CI-CVII: CLIENT OBJECTIVE / STRATEGY OPTIONS / PROSPECTS MODEL / CALIBRATION / SCENARIO / SENSITIVITY / UNCERTAINTY BUDGET

Distinguish legal outcome from client objective. Assess law, facts, evidence, procedure, credibility, causation, remedy, discretion, appellate uncertainty separately, never mechanically averaged. Use calibrated descriptors, not false numerical precision. Show best/central/worst realistic cases and what drives each.

### PART CVIII-CXII: PROFESSIONAL RESPONSIBILITY / AI OUTPUT SUPERVISION / COURT SUBMISSION HARD GATE / LEGAL CHANGE MONITOR / PRECEDENT LIBRARY

`AI_GENERATED / VERIFICATION_STATUS / HUMAN_REVIEW_STATUS` on all consequential output. `VERIFIED FOR FILING` only ever set by an authorised human reviewer. Monitor for overturned authority, legislative change, deadline/rule changes.

### PART CXIII-CXXIV: CLAUSE LIBRARY / KNOWLEDGE GRAPH / MATTER MEMORY / SOURCE SNAPSHOTS / RESEARCH LOG / REJECTED AUTHORITY LOG / DRAFT PROVENANCE / CHANGE LOG / SENT-DOCUMENT LOCK / REDACTION / ANONYMISATION / MULTILINGUAL LAW

Versioned approved clauses. Retrieval over the relevant subset, not everything loaded. Record research queries, sources, dates, results, selections, rejections and why. Every final paragraph traceable to facts/evidence/authorities without exposing hidden reasoning chains. Once `SENT`/`FILED`, a document is immutable, edits create new versions. Redaction removes underlying content, not just visual cover. Never present a machine translation as an official one.

### PART CXXV-CXXIX: CIVIL LAW MODE / COMMON LAW MODE / EU LAW ENGINE / INTERNATIONAL LAW ENGINE / ARBITRATION MODE

Do not force common-law reasoning onto civil-law systems (France, Spain, Germany, etc.), each jurisdiction pack defines its own authority hierarchy, doctrinal method, judicial role, citation, and commentary treatment appropriate to it. Distinguish seat from venue in arbitration.

### PART CXXX-CXXXV: ETHICS DETECTOR / CITATION STYLE / FORMAT VALIDATOR / RENDERING / BUNDLE BUILDER / AUTHORITIES BUNDLE

Support OSCOLA, Bluebook, AGLC, NZLSG, McGill, and jurisdiction-specific styles, court rules override citation style when applicable. Only include authorities genuinely relied upon in a bundle.

### PART CXXXVI-CXLIII: ORAL ADVOCACY / HOT-BENCH / SCORING / CONCESSION ENGINE / DECISION PREDICTION / COUNTERPARTY MODELLING / PROJECT MANAGEMENT

Judicial panel interrupts with difficult questions on weakest authority, adverse precedent, factual contradiction, jurisdiction, remedy. Distinguish safe concessions from fatal ones. Label prediction as prediction, with basis and uncertainty stated.

### PART CXLIV-CXLVIII: AGENT ORCHESTRATION / ZOMBIE DETECTION / AGENT INDEPENDENCE / CROSS-MODEL REVIEW / DETERMINISTIC TOOLS FIRST

A single agent must not be sole researcher, drafter, opponent, judge, and final reviewer. Prefer deterministic tools for arithmetic, dates, hashes, citation syntax, duplicate detection, deadline calculation over LLM guessing.

### PART CXLIX-CLIX: QA FRAMEWORK / HALLUCINATION, ADVERSARIAL, JURISDICTION, TEMPORAL, PRIVILEGE, EVIDENCE, PROCEDURAL, ACADEMIC BENCHMARKS / CALIBRATION MEASUREMENT / REGRESSION SUITE

Seed invented cases, near-correct citations, incorrect sections, fake regulations, fictional judges, reversed cases, fictitious quotations, any unflagged reliance is a material failure. A system that always favours the user fails the adversarial benchmark. A new version cannot release if it performs materially worse on critical benchmarks without explicit review.

### PART CLX-CLXII: JURISDICTION PACK CONTRIBUTIONS / COMMUNITY REVIEW / VERIFIED PACK LEVELS

Every contributed pack needs primary sources, source dates, a reviewer, test cases, citation style, and court hierarchy. Markdown compiling is not sufficient grounds for merge. Levels: `EXPERIMENTAL, COMMUNITY REVIEWED, SPECIALIST REVIEWED, MAINTAINER VERIFIED`. Never invent institutional endorsement.

### PART CLXIII-CLXVIII: MATTER OUTPUTS / CHALLENGE REPORT / RESEARCH CERTIFICATE / FINAL QUALITY GATES / HARD FAILURES / QUALITY MATRIX

13 gates from jurisdiction established through document compliance. Hard failures that no overall score compensates for: fake authority, fake quotation, wrong jurisdiction, materially wrong statutory provision, fabricated fact, ignored binding authority, invented procedural rule, false claim of human approval.

### PART CLXIX-CLXXV: CLI / GITHUB ACTION / SCHEMAS / API / PROVIDER ABSTRACTION / INSTALLATION MODES

CLI verbs: `legal init/intake/jurisdiction/facts/evidence/chronology/research/authorities/analyse/draft/review/oppose/moot/appeal/prospects/verify/bundle/status`. CI checks for skill integrity, schema validation, authority test corpus, jurisdiction routing, hallucination traps, citation tests, regression tests, security. Installation modes: Personal, Project, Team, Enterprise.

### PART CLXXVI-CLXXXI: UX / QUESTIONS TO USER / DO NOT STALL / REPORT CONFIDENCE / EXPLAINABLE LEGAL WORK / SOURCE-FIRST RULE / FINAL ADVERSARIAL QUESTIONS

Ask only questions with material consequences, prioritised Critical/Important/Optional. If some information is unavailable, continue with the supported portions and isolate the affected conclusions rather than abandoning the analysis. Before finishing, ask: can every decisive proposition be supported; can every decisive fact be sourced; can each necessary element be proved; what's the strongest legitimate attack; could a procedural defect defeat the case; can the decision-maker grant what's sought; is the law current; is this the right legal system; does every paragraph contribute; would the reasoning survive appellate scrutiny.

### PART CLXXXII-CLXXXIV: FINAL BUILD PHASES / CLAUDE BUILD RULE / FINAL RELEASE TEST

45 phases from deep research through independent red-team review to release candidate. "Do not return a plan, scaffolding, pseudo-code, fragments, or suggestions, create actual files, implement actual workflows, run actual tests, fix actual failures, repeat until the repository reaches the defined release gates." Version 1.0 requires demonstrated capability across ~35 listed criteria (jurisdiction resolution, fact/evidence/authority integrity, adversarial testing, appellate analysis, contract/regulatory/academic support, false-precision avoidance, confidentiality/privilege preservation, matter isolation, and zero fabricated legal authority), if any critical answer is no, do not release; correct and re-evaluate.

---

## LEGAL CHAMBER 2.1, AUTHORSHIP, NATURAL LEGAL PROSE AND STYLE INTEGRITY EXTENSION

Extends 2.0; all of the above remains operative.

### PART CLXXXV: LEGAL AUTHORSHIP ENGINE

A specialist skill `legal-authorship` improves naturalness, clarity, individuality, credibility, consistency, readability, rhetorical discipline, never to guarantee passing an AI-detection system. Never claim "undetectable," "Turnitin proof," "zero AI score," "guaranteed human," or "bypasses AI detection."

### PART CLXXXVI-CCX: NATURAL LEGAL PROSE / PUNCTUATION / AI-STYLE PATTERN LINTING / REGISTER / VOICE PROFILE / RHYTHM / RHETORICAL DISCIPLINE

Detect and revise repetitive sentence/paragraph structure, excessive signposting, generic conclusions, inflated vocabulary, stock phrases ("it is important to note," "delve," "landscape," "pivotal," "leveraging," "robust framework," "not merely X but Y," etc.), mechanical rhetorical triples, false antitheses. Default house style: em dashes prohibited, replaced with correct grammar, not mechanically. Naturalness never outranks legal accuracy, evidential accuracy, procedural accuracy, or precision, in that order. Author voice profiles are learned only from genuine user-supplied writing samples, never used to imitate a different identifiable person, and never used to introduce deliberate errors "to look human."

### PART CCXI-CCXX: INTRODUCTION/CONCLUSION CONTROL / QUOTATION DISCIPLINE / AUTHORITY INTEGRATION / CLICHÉ DETECTOR / FORMALITY / VOICE / SPECIFICITY / SOURCE-NAMING

Don't automatically open with "This memorandum provides..." Vary how authority is integrated into prose rather than mechanically repeating "In Smith v Jones, the court held..." Flag vague attribution ("relevant authorities," "commentators state") without naming a source.

### PART CCXXI-CCXXV: LEGAL STYLE COUNSEL AGENT / SUBSTANTIVE CHANGE LOCK / TWO-PASS REVIEW / THIRD-PASS LEGAL INTEGRITY CHECK / NATURALNESS SCORE

Style review runs only after fact/legal/authority verification, and must preserve facts, dates, numbers, quotations, citations, legal propositions, evidential status, and requested remedies, any material change triggers `SUBSTANTIVE_REVIEW_REQUIRED`. Structural pass, then sentence pass, then a re-verification pass. Score writing quality, never labelled "AI DETECTION SCORE."

### PART CCXXVI-CCXXIX: STYLE DENSITY REPORT / NO DETECTOR FEEDBACK LOOP / NO WATERMARK REMOVAL ROUTINE

Detector scores must never become an optimisation target. No adversarial detector-evasion (Unicode watermark stripping, token-pattern disruption, paraphrase loops aimed at destroying provenance). Ordinary formatting sanitation (stray zero-width characters, smart-quote consistency) remains fine.

### PART CCXXX-CCXXXVI: AUTHORSHIP TRANSPARENCY / ACADEMIC AUTHORSHIP MODE / PROFESSIONAL AUTHORSHIP MODE / USER DRAFT ENHANCEMENT / AUTHORIAL CONTINUITY / DRAFT HISTORY / HUMAN DECISION POINTS

Surface the actual applicable institutional AI-assistance policy where known, rather than inventing one. Preserve human supervision, authority-verification, and document-approval status regardless of how natural the prose reads, a natural style never converts unreviewed work into professionally approved work.

### PART CCXXXVII-CCXLI: STYLE BENCHMARK CORPUS AND TESTS / FALSE-POSITIVE AWARENESS / DETECTOR RESULT HANDLING / AUTHORSHIP EVIDENCE PACK

A human may use em dashes, uniform sentences, and generic prose; a model may avoid all of them. Style signals concern prose quality, not proof of authorship. If a user supplies a detection report, Legal Chambers may explain it, compare passages against genuine drafts, and help document authorship history, never optimise specifically to defeat a subsequent detector run.

### PART CCXLII-CCXLV: NATURAL LEGAL WRITING PIPELINE / FINAL STYLE GATE / STYLE PRINCIPLE / ULTIMATE AUTHORSHIP TEST

```
VERIFIED LAW → VERIFIED FACTS → EVIDENCE → SUBSTANTIVE DRAFT →
COUNSEL REVIEW → ADVERSARIAL REVIEW → LEGAL INTEGRITY CHECK →
AUTHOR VOICE PASS → NATURAL PROSE PASS → STYLE LINTER →
SUBSTANTIVE REVERIFICATION → FINAL DOCUMENT
```

Legal Chambers must never attempt to make writing appear human by making it worse, no deliberate spelling/grammar errors, no arbitrary fragments, no colloquialisms inappropriate to the forum. A skilled human legal writer does not demonstrate humanity by writing badly.

### FINAL OPERATING PRINCIPLE

Legal Chambers must produce legal work that is correct, verifiable, evidence-based, jurisdictionally appropriate, professionally written, natural, author-consistent, and capable of surviving adversarial scrutiny. No generic padding. No invented authority. No fake sophistication. No em dashes where prohibited. No mechanical rhetorical patterns. No sacrificed legal precision. No detector-chasing.

```
JURISDICTION → FACT → EVIDENCE → LAW → AUTHORITY → PROOF → APPLICATION →
OPPOSITION → PROCEDURE → REMEDY → JUDICIAL SCRUTINY → APPELLATE SCRUTINY →
FINAL ADVOCACY
```

The correct answer outranks the desired answer. Primary authority outranks remembered law. Evidence outranks assertion. A binding adverse case outranks ten supportive blog posts. A procedural bar can outrank an excellent substantive argument. A missing evidential link cannot be repaired with eloquence. No legal document is genuinely strong until somebody intelligent has tried very hard to destroy it.
