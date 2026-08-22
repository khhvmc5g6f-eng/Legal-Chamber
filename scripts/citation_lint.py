#!/usr/bin/env python3
"""Deterministic citation-shape and house-style linter.

This is pattern matching, not legal judgement. It cannot tell you whether a
citation is real - only whether its shape matches a recognised pattern, and
whether the surrounding prose violates this project's house style (see
docs/STYLE_GUIDE.md). A citation that passes this linter still requires the
verification steps in docs/OPERATING_RULES.md before it can be relied upon.

Citation shapes covered: UK neutral citations (with an optional trailing
parenthetical, e.g. "(Ch)", "(GRC)" - captured whole because it's usually a
real division/chamber code, but this pattern doesn't verify that; a short
non-code parenthetical like "(unreported)" immediately after a citation
gets swept in too, so treat the captured suffix as "here's what followed
the citation," not as a confirmed chamber code), UK OSCOLA law-report
citations ("[2023] 2 WLR 456"), UK OSCOLA statute citations ("Theft Act
1968, s 1"), EU case numbers ("C-45/21"), ECLI identifiers (EU/France/Spain
case law, "ECLI:NL:HR:2009:384425"), Canadian McGill Guide neutral
citations ("2023 SCC 12"), and US reporter citations - the last of these
is additionally checked against a real, vendored table of ~3,590
known US reporter abbreviations and variant spellings (Free Law Project's
reporters-db, BSD-2-Clause, see data/REPORTERS_DB_LICENSE.txt) rather than
shape alone, so a citation whose reporter name doesn't exist gets flagged
even though its punctuation looks right - including a citation with a page
pincite (e.g. "410 U.S. 113, 115 (1973)").

Usage:
    python3 citation_lint.py path/to/file.md [path/to/other.md ...]
    python3 citation_lint.py --selftest
"""

import argparse
import json
import re
import sys
from pathlib import Path

EM_DASH = "—"

# Real US reporter-abbreviation table, vendored from Free Law Project's
# reporters-db (BSD-2-Clause, see data/REPORTERS_DB_LICENSE.txt), not
# hand-guessed. Used only to check whether a shape-matched US reporter
# citation's abbreviation is a real, known one - it says nothing about
# whether the underlying case exists or holds what it's cited for, that
# still requires CourtListener (or an equivalent primary source) per
# docs/OPERATING_RULES.md.
_REPORTERS_DATA_PATH = Path(__file__).resolve().parent / "data" / "reporters.json"
_reporter_abbreviations_cache = None


def _normalize_reporter(raw):
    """Whitespace-collapse and lowercase. Lowercasing means a miscased
    citation ("593 u.s. 374") is still recognised as the same real reporter
    as the properly-cased form, rather than being invisible to the shape
    pattern entirely (an earlier version required an uppercase first
    letter, so a lowercase reporter wasn't merely unrecognised - it wasn't
    even detected) or falsely flagged as fabricated purely for casing.
    Casing correctness is a separate, cosmetic concern this check
    deliberately doesn't conflate with "is this a real reporter name."""
    return re.sub(r"\s+", " ", raw.strip()).lower()


def known_us_reporter_abbreviations():
    """Lazily load and cache the set of every recognised US reporter
    abbreviation (canonical editions and known variant spellings) from the
    vendored reporters-db data. Returns an empty set (rather than raising)
    if the data file is missing, so a stale checkout degrades to
    shape-only linting instead of crashing."""
    global _reporter_abbreviations_cache
    if _reporter_abbreviations_cache is not None:
        return _reporter_abbreviations_cache
    abbreviations = set()
    try:
        with open(_REPORTERS_DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        for entries in data.values():
            for entry in entries:
                abbreviations.update(_normalize_reporter(k) for k in entry.get("editions", {}))
                abbreviations.update(_normalize_reporter(k) for k in entry.get("variations", {}))
    except (OSError, json.JSONDecodeError):
        pass
    _reporter_abbreviations_cache = abbreviations
    return abbreviations

# Fixed phrases matched literally (word-boundary, case-insensitive). Kept as
# ONE list so a phrase added here is always enforced - a previous version had
# a second, separately-maintained regex list that silently drifted out of
# sync with this one.
STOCK_PHRASES = [
    "it is important to note",
    "it is worth noting",
    "it is crucial to",
    "in today's",
    "delve into",
    "delve deeper",
    "a nuanced approach",
    "a multifaceted",
    "robust framework",
    "plays a crucial role in",
    "stands as a testament to",
    "cannot be overstated",
    "in the realm of",
    "navigate the complexities of",
    "paradigm shift",
    "underscore the importance of",
]
# (readable label, compiled regex) pairs - the label is what gets reported in
# findings, since re.escape()'d patterns are unreadable (it backslash-escapes
# spaces too) and shouldn't leak into user-facing output.
STOCK_REGEXES = [(phrase, re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)) for phrase in STOCK_PHRASES]
# Structural patterns that need their own regex rather than a literal phrase:
STOCK_REGEXES += [
    ("not merely...but", re.compile(r"\bnot merely\b.{0,40}\bbut\b", re.IGNORECASE)),
    ("not only...but also", re.compile(r"\bnot only\b.{0,40}\bbut also\b", re.IGNORECASE)),
]

# Real OSCOLA UK law-report series abbreviations, single-token only (the
# uk_law_report pattern's abbreviation slot has no internal whitespace, so
# a genuinely real but multi-word series like "All ER" can't be matched by
# it yet - a separate, pre-existing limitation, not fixed here). This is an
# allowlist, not "any capitalised word" - an earlier version accepted any
# capitalised word in that slot and matched an ordinary date's month name
# ("[2023] 12 May 2024") as if it were a law-report citation. Not
# exhaustive; a real series missing from this list won't be matched
# (false negative), which is the safer failure direction than matching an
# arbitrary word (false positive).
_UK_LAW_REPORT_SERIES = [
    "AC", "WLR", "QB", "KB", "Ch", "Fam", "FLR", "ICR", "IRLR", "EMLR",
    "BCLC", "BCC", "RTR", "RVR", "EGLR", "PIQR", "FSR", "RPC", "BHRC",
    "HRLR", "UKHRR", "Ex", "Beav",
]
_UK_LAW_REPORT_SERIES_RE = "|".join(sorted(_UK_LAW_REPORT_SERIES, key=len, reverse=True))

# Real Canadian (McGill Guide) court/tribunal codes used in neutral
# citation since ~2000 - federal plus provincial/territorial appellate and
# superior courts. An allowlist for the same reason as the law-report list
# above: an earlier version accepted any 2-6 capital letters and matched
# ordinary business acronyms ("2023 USD 500", "2024 YOY 12") as if they
# were Canadian case citations. Alberta and Saskatchewan each list both
# their pre- and post-2023 Queen's/King's Bench abbreviations (the rename
# happened mid-citation-history, both forms appear in real use depending
# on date). Not exhaustive - missing a real but rare tribunal code is the
# safer failure direction than matching an arbitrary acronym.
_CANADA_COURT_CODES = [
    "SCC", "FC", "FCA", "TCC", "CMAC", "CHRT",
    "ONCA", "ONSC", "ONCJ", "BCCA", "BCSC", "BCPC",
    "ABCA", "ABQB", "ABKB", "ABPC", "QCCA", "QCCS", "QCCQ",
    "MBCA", "MBQB", "MBPC", "SKCA", "SKQB", "SKKB", "SKPC",
    "NSCA", "NSSC", "NBCA", "NBQB", "NBKB", "NLCA", "NLSC",
    "PECA", "PESC", "YKCA", "YKSC", "NWTCA", "NWTSC", "NUCA", "NUCJ",
]
_CANADA_COURT_CODES_RE = "|".join(sorted(_CANADA_COURT_CODES, key=len, reverse=True))

CITATION_PATTERNS = {
    # UK neutral citation - court code may be one word (UKSC, EWHC, UKUT) or
    # two (EWCA Civ, EWCA Crim, EWHC Comm), e.g. [2023] UKSC 12 / [2023] EWCA Civ 456.
    # Trailing division/chamber parenthetical is optional and, when present,
    # is now captured as part of the match (e.g. "[2023] EWHC 123 (Ch)",
    # "[2026] UKFTT 1219 (GRC)") - confirmed against real live examples from
    # Find Case Law/judiciary.uk; the un-suffixed base shape still matches
    # citations that don't carry one (e.g. plain UKSC citations).
    "uk_neutral": re.compile(r"\[\d{4}\]\s+[A-Z]{2,10}(?:\s+[A-Za-z]{2,10})?\s+\d+(?:\s*\([A-Za-z]{2,10}\))?"),
    # OSCOLA law-report citation - distinct shape from a neutral citation:
    # a volume number comes immediately after the year, before the report
    # abbreviation, e.g. "[2023] 2 WLR 456", "[2023] 1 AC 45". Neutral
    # citations never have a bare digit there (letters follow the year
    # directly), so the two patterns cannot both match the same span. The
    # abbreviation itself is restricted to _UK_LAW_REPORT_SERIES above, not
    # any capitalised word - see that list's own comment for why.
    "uk_law_report": re.compile(rf"\[\d{{4}}\]\s+\d{{1,2}}\s+(?:{_UK_LAW_REPORT_SERIES_RE})\b\s+\d+"),
    # OSCOLA statute citation, e.g. "Theft Act 1968, s 1", "Human Rights Act
    # 1998, sch 1". Shape-only, like every other pattern here - it cannot
    # confirm the Act or section actually exists, only that the text has
    # the right grammatical shape for one. The word/connector classes allow
    # a hyphen and a few more connectors ("&", "at", "for", "to", "in",
    # "on") beyond the original of/and/the set - a real Act name containing
    # one of these ("Anti-social Behaviour Act 2003", "Health & Safety at
    # Work Act 1974") previously couldn't be matched from its own first
    # word: the regex engine, unable to consume the disallowed word, still
    # found a match starting from a LATER word in the same name instead of
    # failing outright, silently truncating the captured citation rather
    # than matching it in full or not at all. This widens the classes but
    # doesn't eliminate the risk for a connector still not covered - a
    # matched span that looks like it starts mid-name is a signal to check
    # by hand, not a guarantee the full name was captured.
    "uk_statute": re.compile(
        r"\b[A-Z][A-Za-z'-]+(?:\s+(?:of|and|the|&|at|for|to|in|on|[A-Z][A-Za-z'-]+))*\s+Act\s+\d{4}"
        r"(?:,\s*s(?:ch)?\.?\s*\d+[A-Za-z]?(?:\(\d+\))?)?\b"
    ),
    # EU case number, e.g. "C-45/21". Known, disclosed limitation: this
    # exact shape (letter-hyphen-digits-slash-digits) is also a plausible
    # bundle/exhibit page-reference convention in litigation documents
    # ("see page C-45/21 of the trial bundle") - genuinely ambiguous from
    # shape alone, not fixed here. Treat a match found in evidence/bundle
    # context with more suspicion than one found in a citations/authorities
    # section.
    "eu_case": re.compile(r"[Cc]-\d+/\d{2,4}"),
    # Canadian (McGill Guide) neutral citation - a distinct shape from the UK
    # form: bare year with no brackets, e.g. "2023 SCC 12", "2021 ONCA 456".
    # Requires the year to be followed immediately by whitespace then the
    # court-code letters (no bracket in between), so it cannot double-match
    # a UK citation's "[2023] UKSC 12" (there the year is followed by "]",
    # not whitespace, before the court code). The court code is restricted
    # to _CANADA_COURT_CODES above, not any 2-6 capital letters - see that
    # list's own comment for why.
    "canada_neutral": re.compile(rf"\b\d{{4}}\s+(?:{_CANADA_COURT_CODES_RE})\b\s+\d+\b"),
    # European Case Law Identifier - EU-wide standard, five colon-separated
    # elements, e.g. "ECLI:NL:HR:2009:384425". Covers case-law citations
    # across the EU, France, and Spain jurisdiction packs at once; confirmed
    # live and current against EUR-Lex's own documentation, not deprecated.
    "ecli": re.compile(r"\bECLI:[A-Z]{2}:[A-Z0-9.]+:\d{4}:[A-Za-z0-9.]{1,25}\b"),
    # US reporter citation - the reporter abbreviation itself often contains
    # digits (F.2d, F.3d, F.4th, F. Supp. 2d), so the character class must
    # allow them; volume/page stay digit-only either side of it. An optional
    # pincite ("410 U.S. 113, 115 (1973)", "550 U.S. 544, 555-56 (2007)") may
    # follow the page number - without this, a pincited citation (extremely
    # common in real legal writing) matched nothing at all, silently
    # skipping the reporter-recognition check below for exactly the
    # citations most likely to appear in real drafting. The trailing
    # parenthetical is "(Court Year)" for circuit/district citations (e.g.
    # "(9th Cir. 1969)") but just "(Year)" for the US Reports - allow any
    # non-paren text before the 4-digit year rather than requiring the year alone.
    # Case-insensitive: a miscased or OCR'd citation ("593 u.s. 374") is
    # still detected and run through the reporter-recognition check below
    # (which is itself case-insensitive, see _normalize_reporter) - an
    # earlier version required an uppercase first letter and so was blind
    # to a lowercase reporter entirely, not merely unrecognised.
    "us_reporter": re.compile(r"\d+\s+[A-Za-z][A-Za-z0-9.'\s]{1,20}\d+(?:,\s*\d+(?:[-–]\d+)?)?\s*\([^()]*\d{4}\)", re.IGNORECASE),
}

# Same shape as CITATION_PATTERNS["us_reporter"], but with the reporter
# abbreviation itself in its own capture group, ending on an alphanumeric-or-
# period character followed by an explicit \s+ before the page number - not
# just "grow until \d+ happens to fit," so a reporter abbreviation that
# itself contains a digit (F.2d, F.3d) or an internal space (F. Supp. 2d)
# is captured whole rather than depending on regex backtracking to land in
# the right place. Kept as a second, separate regex rather than adding a
# group to the one above, so every entry in CITATION_PATTERNS keeps
# returning plain match strings from findall() (the uniform shape
# lint_text()'s citation-collection loop and main() both rely on). Used
# only by the reporter-name recognition check below.
_US_REPORTER_WITH_GROUP = re.compile(
    r"\d+\s+([A-Za-z][A-Za-z0-9.'\s]*?[A-Za-z0-9.])\s+\d+(?:,\s*\d+(?:[-–]\d+)?)?\s*\([^()]*\d{4}\)",
    re.IGNORECASE,
)


# Matches a fence of 3+ backticks and its closing fence of the SAME length,
# per CommonMark (a longer inner fence, e.g. 4 backticks wrapping a 3-backtick
# example, is not closed by the first 3-backtick run it contains).
FENCED_CODE_BLOCK = re.compile(r"(`{3,})[^\n]*\n.*?\n\1`*", re.DOTALL)


def _strip_fenced_code_blocks(text):
    """Remove fenced code blocks entirely for the prose-only checks (double
    space, stock phrasing, quotation-mark mixing) - ASCII diagrams and JSON
    examples legitimately use multi-space alignment that isn't a house-style
    violation, and counts here don't need to preserve position. Citation-shape
    detection and em-dash detection still run against the original,
    unstripped text."""
    return FENCED_CODE_BLOCK.sub(" ", text)


def lint_text(text):
    findings = []
    prose = _strip_fenced_code_blocks(text)

    em_dash_count = text.count(EM_DASH)
    if em_dash_count:
        findings.append(f"em_dash: {em_dash_count} occurrence(s) - house style prohibits em dashes (docs/STYLE_GUIDE.md)")

    # Mid-line only - leading indentation for nested markdown lists is not a
    # house-style violation, only an accidental double space within a sentence.
    double_space_count = len(re.findall(r"(?<=\S)[^\S\n]{2,}", prose))
    if double_space_count:
        findings.append(f"double_space: {double_space_count} occurrence(s)")

    straight_quotes = prose.count('"')
    curly_quotes = prose.count("“") + prose.count("”")
    if straight_quotes and curly_quotes:
        findings.append(f"mixed_quotation_marks: {straight_quotes} straight + {curly_quotes} curly - pick one convention")

    for label, rx in STOCK_REGEXES:
        matches = rx.findall(prose)
        if matches:
            findings.append(f"stock_phrase '{label}': {len(matches)} occurrence(s)")

    citations_found = {}
    for name, rx in CITATION_PATTERNS.items():
        matches = rx.findall(text)
        if matches:
            citations_found[name] = matches

    known_reporters = known_us_reporter_abbreviations()
    if known_reporters:
        unrecognized = []
        for m in _US_REPORTER_WITH_GROUP.finditer(text):
            candidate = _normalize_reporter(m.group(1))
            if candidate not in known_reporters:
                unrecognized.append(candidate)
        if unrecognized:
            shown = ", ".join(repr(r) for r in unrecognized)
            findings.append(
                f"unrecognized_us_reporter: {shown} - citation shape is plausible but this abbreviation "
                "isn't in reporters-db's known table (Free Law Project, BSD-2-Clause, scripts/data/reporters.json). "
                "Doesn't mean the citation is wrong, only that the reporter name needs a human/live check "
                "before relying on it - reporters-db's own coverage isn't guaranteed exhaustive either."
            )

    return findings, citations_found


def lint_file(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    findings, citations = lint_text(text)
    return findings, citations


def selftest():
    failures = []

    bad_text = "This is bad — it has an em dash. It is important to note that this is not merely wrong but also flagged."
    findings, _ = lint_text(bad_text)
    joined = " ".join(findings)
    if "em_dash" not in joined:
        failures.append("did not flag em dash in bad_text")
    if "it is important to note" not in joined.lower():
        failures.append("did not flag stock phrase in bad_text")
    if "not merely" not in joined.lower():
        failures.append("did not flag 'not merely...but' construction")

    good_text = "This is a clean sentence with no house-style violations at all."
    findings, _ = lint_text(good_text)
    if findings:
        failures.append(f"false positive(s) on clean text: {findings}")

    citation_text = "See Smith v Jones [2023] UKSC 12 and Case C-45/21."
    _, citations = lint_text(citation_text)
    if "uk_neutral" not in citations:
        failures.append("did not detect UK neutral citation shape")
    if "eu_case" not in citations:
        failures.append("did not detect EU case citation shape")

    # UK neutral citation with a division/chamber suffix - previously
    # matched only up to the bare citation, dropping "(Comm)".
    division_text = "See Smith v Jones [2023] EWHC 123 (Comm) for the point."
    _, citations = lint_text(division_text)
    if not any("(Comm)" in c for c in citations.get("uk_neutral", [])):
        failures.append(f"did not capture the division suffix on a UK neutral citation: {citations.get('uk_neutral')}")

    # OSCOLA law-report and statute citations - previously zero coverage.
    oscola_text = "The rule in [2023] 2 WLR 456 turns on the Theft Act 1968, s 1."
    _, citations = lint_text(oscola_text)
    if "uk_law_report" not in citations:
        failures.append("did not detect UK OSCOLA law-report citation shape")
    if "uk_statute" not in citations:
        failures.append("did not detect UK OSCOLA statute citation shape")

    # uk_law_report must not match an ordinary date's month name as if it
    # were a report-series abbreviation - a real earlier false positive.
    _, citations = lint_text("The hearing on [2023] 12 May 2024 proceeded as scheduled.")
    if "uk_law_report" in citations:
        failures.append(f"uk_law_report false-matched a date's month name: {citations['uk_law_report']}")

    # uk_statute must capture a hyphenated or ampersand/preposition-joined
    # Act name in full, not silently truncate to a later word - a real
    # earlier bug (both examples mid-sentence, not sentence-initial, to
    # isolate the connector-widening fix from the separate, pre-existing,
    # undocumented quirk that a sentence-initial capitalised lead-in word
    # like "Under"/"The" can itself get swept into the match).
    _, citations = lint_text("The order was made under the Anti-social Behaviour Act 2003.")
    if citations.get("uk_statute") != ["Anti-social Behaviour Act 2003"]:
        failures.append(f"uk_statute truncated a hyphenated Act name: {citations.get('uk_statute')}")
    _, citations = lint_text("The claim proceeds under the Health & Safety at Work Act 1974, s 2.")
    if citations.get("uk_statute") != ["Health & Safety at Work Act 1974, s 2"]:
        failures.append(f"uk_statute truncated an ampersand-joined Act name: {citations.get('uk_statute')}")

    # ECLI - one pattern covering EU/France/Spain case-law citations.
    ecli_text = "See ECLI:NL:HR:2009:384425 on this point."
    _, citations = lint_text(ecli_text)
    if "ecli" not in citations:
        failures.append("did not detect ECLI citation shape")

    # Canadian neutral citation - bare year, no brackets - and confirm it
    # does NOT double-match inside a UK bracketed citation's year+court-code
    # run.
    canada_text = "See R v Smith, 2023 SCC 12, and Doe v Roe, 2021 ONCA 456."
    _, citations = lint_text(canada_text)
    if len(citations.get("canada_neutral", [])) != 2:
        failures.append(f"did not detect both Canadian neutral citations: {citations.get('canada_neutral')}")
    uk_only_text = "See Smith v Jones [2023] UKSC 12."
    _, citations = lint_text(uk_only_text)
    if "canada_neutral" in citations:
        failures.append(f"canada_neutral false-matched inside a UK bracketed citation: {citations['canada_neutral']}")

    # canada_neutral must not match an ordinary business/currency acronym -
    # real earlier false positives, since any 2-6 capital letters used to
    # qualify.
    _, citations = lint_text("In 2023 USD 500 million was invested in the fund.")
    if "canada_neutral" in citations:
        failures.append(f"canada_neutral false-matched a currency code: {citations['canada_neutral']}")
    _, citations = lint_text("Revenue grew 2024 YOY 12 percent across the group.")
    if "canada_neutral" in citations:
        failures.append(f"canada_neutral false-matched a business acronym: {citations['canada_neutral']}")

    # US reporter recognition: a real reporter abbreviation (including one
    # with an embedded digit, testing the extraction regex specifically)
    # should not be flagged; a fabricated one should be.
    real_reporter_text = "See Van Buren v. United States, 593 U.S. 374 (2021) and 676 F.3d 854 (9th Cir. 2012)."
    findings, _ = lint_text(real_reporter_text)
    if any("unrecognized_us_reporter" in f for f in findings):
        failures.append(f"false positive flagging a real US reporter: {findings}")

    fake_reporter_text = "See Example v. Test, 123 Q.Z. Rptr. 456 (2020)."
    findings, _ = lint_text(fake_reporter_text)
    if not any("unrecognized_us_reporter" in f for f in findings):
        failures.append("did not flag a fabricated US reporter abbreviation")

    # A miscased reporter must still be detected and recognised as the
    # same real reporter - an earlier version required an uppercase first
    # letter and so was blind to a lowercase citation entirely (not
    # merely unrecognised, invisible to detection at all).
    lowercase_reporter_text = "See Van Buren v. United States, 593 u.s. 374 (2021)."
    findings, citations = lint_text(lowercase_reporter_text)
    if "us_reporter" not in citations:
        failures.append("lowercase US reporter citation not detected at all")
    if any("unrecognized_us_reporter" in f for f in findings):
        failures.append(f"lowercase-but-real reporter incorrectly flagged as unrecognized: {findings}")

    if not known_us_reporter_abbreviations():
        failures.append("reporters-db data file failed to load (scripts/data/reporters.json) - reporter validation is silently disabled")

    # Pincited citations (extremely common in real legal writing) must not
    # silently bypass detection/recognition entirely - a real fix, not just
    # a documented limitation, after an audit found the original pattern
    # matched zero pincited citations of any kind.
    real_pincite_text = "See Roe v. Wade, 410 U.S. 113, 115 (1973) and Twombly, 550 U.S. 544, 555-56 (2007)."
    findings, citations = lint_text(real_pincite_text)
    if len(citations.get("us_reporter", [])) != 2:
        failures.append(f"pincited real reporters not both matched: {citations.get('us_reporter')}")
    if any("unrecognized_us_reporter" in f for f in findings):
        failures.append(f"false positive flagging a real pincited US reporter: {findings}")

    fake_pincite_text = "See Fake v. Case, 123 Q.Z. Rptr. 456, 460 (2020)."
    findings, citations = lint_text(fake_pincite_text)
    if "us_reporter" not in citations:
        failures.append("pincited citation shape not detected at all")
    if not any("unrecognized_us_reporter" in f for f in findings):
        failures.append("did not flag a fabricated US reporter abbreviation carrying a pincite")

    if failures:
        print("SELFTEST FAILED:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("SELFTEST OK (all checks passed)")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("files", nargs="*")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()

    if args.selftest:
        sys.exit(selftest())

    if not args.files:
        p.error("supply at least one file, or --selftest")

    exit_code = 0
    for path in args.files:
        findings, citations = lint_file(path)
        print(f"--- {path} ---")
        if citations:
            for name, matches in citations.items():
                print(f"  citation shapes ({name}): {matches}")
        if findings:
            exit_code = 1
            for f in findings:
                print(f"  FLAG: {f}")
        if not findings and not citations:
            print("  no findings")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
