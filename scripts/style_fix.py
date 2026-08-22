#!/usr/bin/env python3
"""Deterministic plain-language style fixer for house-style stock phrases and
em dashes (see docs/STYLE_GUIDE.md).

This is a companion to citation_lint.py: that script *detects* house-style
violations, this one *fixes* the subset that can be fixed safely without
touching legal meaning. It shares citation_lint.py's STOCK_PHRASES list
rather than keeping a second one, for the exact reason documented in that
file - two independently maintained phrase lists drift out of sync.

Scope, deliberately narrow (docs/STYLE_GUIDE.md, "What this repo will not
build"):
  - Every replacement swaps a phrase for another phrase in the SAME
    grammatical slot (adverb for adverb, verb phrase for verb phrase, noun
    phrase for noun phrase), so a blind substitution cannot break grammar.
  - Nothing inside a quotation (straight or curly) is ever touched. A
    direct quotation must stay verbatim - altering one, even for house
    style, is a legal-accuracy problem, not a style one.
  - Nothing inside a fenced code block is touched.
  - No number, date, or citation-shaped span is a target of any rule here
    (none of the current rules can match one, and this stays true if rules
    are added later - keep replacements to prose connectives and clichés).
  - This tool does not soften hedged or absolute legal claims ("always",
    "guarantees") - the source repo Legal Chamber's local-humanizer.ts did
    that for general prose, but STYLE_GUIDE.md ranks legal accuracy above
    naturalness, and a proposition binding authority states as absolute
    must not be quietly hedged by a style pass.
  - This tool does not restructure sentences, vary sentence openings, or
    split long sentences. Those change rhythm by inserting or rearranging
    words a human didn't choose, which STYLE_GUIDE.md's "author voice"
    section specifically warns against ("never introduce deliberate errors
    or artificial variance 'to look human'").
  - This tool makes NO claim about, and has NO effect on, whether output
    is flagged by an AI-content detector. See docs/STYLE_GUIDE.md, "What
    this repo will not build": detector-feedback loops and adversarial
    detector-evasion are explicitly out of scope for this repository.
  - Em dashes are counted and reported, never auto-fixed. The correct
    replacement (comma, colon, semicolon, full stop) depends on whether
    the clause on either side is independent, which a regex cannot
    reliably judge - a comma is only safe when the second side is NOT an
    independent clause, and guessing wrong produces a comma splice, a
    real grammar error the house style rule was never meant to introduce.
    That decision is left to whoever is doing the style pass.

Usage:
    python3 style_fix.py path/to/file.md [path/to/other.md ...]   # dry run
    python3 style_fix.py --apply path/to/file.md                   # write changes
    python3 style_fix.py --selftest
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from citation_lint import STOCK_PHRASES, _strip_fenced_code_blocks  # noqa: E402

EM_DASH = "—"

# Same-slot replacements only - see module docstring. Two ladder entries
# ("...that" variant tried before the bare phrase) exist where the stock
# phrase is naturally followed by a redundant "that" that the replacement
# no longer needs.
_PHRASE_FIXES = [
    (r"\bit is important to note that\b", "notably,"),
    (r"\bit is important to note\b", "notably,"),
    (r"\bit is worth noting that\b", "notably,"),
    (r"\bit is worth noting\b", "notably,"),
    (r"\bit is crucial to\b", "it matters to"),
    (r"\bin today's\b", "in the current"),
    (r"\bdelve deeper into\b", "look more closely at"),
    (r"\bdelve into\b", "examine"),
    (r"\ba nuanced approach\b", "a careful approach"),
    (r"\ba multifaceted\b", "a complex"),
    (r"\brobust framework\b", "solid framework"),
    (r"\bplays a crucial role in\b", "is central to"),
    (r"\bstands as a testament to\b", "shows"),
    (r"\bcannot be overstated\b", "matters a great deal"),
    (r"\bin the realm of\b", "in the area of"),
    (r"\bnavigate the complexities of\b", "work through the complexities of"),
    (r"\bparadigm shift\b", "major change"),
    (r"\bunderscore the importance of\b", "highlight the importance of"),
]
PHRASE_FIXES = [(re.compile(pattern, re.IGNORECASE), replacement) for pattern, replacement in _PHRASE_FIXES]

# Sanity check at import time: every literal phrase citation_lint.py flags
# has a same-slot fix here, so the two files can't silently drift apart -
# the exact failure mode the "one list" comment in citation_lint.py warns
# about, just one level up (detect vs. fix instead of two detect lists).
for _stock in STOCK_PHRASES:
    if not any(_stock in pattern for pattern, _ in _PHRASE_FIXES):
        raise AssertionError(
            f"style_fix.py has no fix rule for citation_lint.py STOCK_PHRASES entry {_stock!r} "
            "- add one to _PHRASE_FIXES or explicitly document it as report-only below."
        )

# Structural patterns citation_lint.py flags but this tool deliberately does
# NOT auto-fix: rewriting a "not merely X but Y" construction requires
# understanding what X and Y are, which is a judgement call, not a
# same-slot swap. Left for the human/agent doing the style pass.
REPORT_ONLY_STRUCTURAL = ["not merely...but", "not only...but also"]

# Quoted spans (straight or curly, double or single) are never touched.
# Non-greedy so a document with several short quotations doesn't have one
# match swallow everything between the first opening and last closing mark -
# bounded from crossing a paragraph break (blank line) for the same reason,
# since an unclosed quote mark earlier in a long document would otherwise
# make the match run away across many paragraphs. A real quotation CAN wrap
# a single line break within one paragraph (a witness statement quoted
# across a markdown line wrap, for instance) - an earlier version of this
# pattern excluded '\n' entirely and so treated a line-wrapped quotation as
# unprotected, editing wording inside it. Fixed to allow a single line
# break, not just same-line matches.
#
# Single quotes are matched only when NOT adjacent to a letter/digit on
# either side (a lookaround, not a character-class exclusion) - this is a
# heuristic, not a guarantee: the same apostrophe character opens a
# quotation ("he said, 'stop'") and marks a contraction/possessive
# ("don't", "the witness's car"), and telling those apart in general needs
# understanding the sentence, not just the character. The boundary check
# correctly excludes the common contraction case (letters on both sides of
# the mark) but is not proof against every edge case - if in doubt, this
# errs toward treating MORE text as quoted (skipping a fix) rather than
# less, which is the safe failure direction for a tool whose whole promise
# is never editing a quotation.
_NO_PARA_BREAK = r"(?:(?!\n\s*\n)[^{}])*?"
QUOTED_SPAN = re.compile(
    r'"' + _NO_PARA_BREAK.format('"') + r'"'
    r'|“' + _NO_PARA_BREAK.format('”') + r'”'
    r"|(?<![A-Za-z0-9])'" + _NO_PARA_BREAK.format("'") + r"'(?![A-Za-z0-9])"
    r"|(?<![A-Za-z0-9])'" + _NO_PARA_BREAK.format("’") + r"’(?![A-Za-z0-9])"
)

# Fenced code blocks, same definition as citation_lint.py.
FENCED_CODE_BLOCK = re.compile(r"(`{3,})[^\n]*\n.*?\n\1`*", re.DOTALL)


def _protected_spans(text):
    """Return a sorted list of (start, end) character ranges that must not
    be modified: fenced code blocks and quoted spans."""
    spans = [m.span() for m in FENCED_CODE_BLOCK.finditer(text)]
    spans += [m.span() for m in QUOTED_SPAN.finditer(text)]
    spans.sort()
    return spans


def _is_protected(start, end, spans):
    return any(s <= start and end <= e for s, e in spans)


def _apply_fixes_outside_protected(text, spans):
    """Apply PHRASE_FIXES and the em-dash fix, skipping any match that
    falls inside a protected span. Runs each fix pattern across the whole
    string (not per-segment) so match positions stay stable against the
    original protected-span offsets."""
    fixes_applied = {}

    def make_sub(compiled, replacement, counter_key):
        def _sub(m):
            if _is_protected(m.start(), m.end(), spans):
                return m.group(0)
            fixes_applied[counter_key] = fixes_applied.get(counter_key, 0) + 1
            out = replacement
            # Preserve sentence-initial capitalization: if the matched
            # phrase opened a sentence (start of text, or preceded only by
            # whitespace after a sentence-ending mark or paragraph break),
            # capitalize the replacement's first letter too. `text` here is
            # the enclosing function's current string (the one this .sub()
            # call is scanning), looked up at call time.
            before = text[: m.start()]
            if re.search(r"(^\s*|[.!?]\s+|\n\s*\n\s*)$", before):
                out = out[:1].upper() + out[1:]
            return out

        return _sub

    for compiled, replacement in PHRASE_FIXES:
        text = compiled.sub(make_sub(compiled, replacement, compiled.pattern), text)
        # Recompute spans after each substitution since positions shift.
        spans = _protected_spans(text)

    return text, fixes_applied


def _count_em_dashes_needing_review(text, spans):
    """Em dashes outside quoted spans / code blocks - these are never
    auto-fixed (see module docstring), only counted for the human/agent
    doing the style pass to resolve by hand."""
    return sum(1 for m in re.finditer(EM_DASH, text) if not _is_protected(m.start(), m.end(), spans))


def fix_text(text):
    """Return (fixed_text, report). report has 'fixes' (dict of rule ->
    count actually applied) and 'em_dash_review' (count of em dashes
    outside quotes/code, left for manual review)."""
    spans = _protected_spans(text)
    fixed, fixes_applied = _apply_fixes_outside_protected(text, spans)

    review_count = _count_em_dashes_needing_review(fixed, _protected_spans(fixed))
    report = {"fixes": fixes_applied, "em_dash_review": review_count}
    return fixed, report


def fix_file(path, apply):
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()
    fixed, report = fix_text(original)
    changed = fixed != original
    if apply and changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(fixed)
    return changed, report


def selftest():
    failures = []

    # Same-slot phrase fix, the redundant trailing "that" is consumed by
    # the ladder's "...that" variant rather than left dangling, and
    # sentence-initial capitalization is preserved (not lower-cased).
    text = "It is important to note that the deadline applies."
    fixed, report = fix_text(text)
    if fixed != "Notably, the deadline applies.":
        failures.append(f"unexpected phrase fix output: {fixed!r}")

    # Same fix mid-sentence (no preceding sentence boundary) must NOT be
    # capitalized.
    mid = "This matters and it is important to note that the deadline applies."
    fixed, _ = fix_text(mid)
    if "it is important to note that" in fixed:
        failures.append("mid-sentence phrase fix did not fire")
    if "and notably, the deadline applies." not in fixed:
        failures.append(f"mid-sentence fix should stay lower-case: {fixed!r}")

    # Quotation is never touched, even though it contains a stock phrase.
    quoted = 'The witness said, "it is important to note that I was not there."'
    fixed, _ = fix_text(quoted)
    if "it is important to note that I was not there" not in fixed:
        failures.append(f"quotation was altered: {fixed!r}")

    # A quotation that wraps a single line break is still a quotation - an
    # earlier version of QUOTED_SPAN excluded '\n' entirely and edited
    # wording inside a line-wrapped quote, exactly the failure the module's
    # own promise exists to prevent.
    multiline_quoted = 'The witness said, "it is important to note\nthat I was not there."'
    fixed, _ = fix_text(multiline_quoted)
    if fixed != multiline_quoted:
        failures.append(f"a quotation spanning a line break was altered: {fixed!r}")

    # Single-quoted text (UK primary-quote convention) must be recognised as
    # a quotation too - an earlier version only matched double quotes.
    single_quoted = "The witness said, 'it is important to note that I was not there.'"
    fixed, _ = fix_text(single_quoted)
    if fixed != single_quoted:
        failures.append(f"a single-quoted quotation was altered: {fixed!r}")

    # A contraction's apostrophe must not be mistaken for an opening single
    # quote and swallow real, fixable content that follows it.
    contraction_nearby = "The claimant didn't attend. It is important to note that this matters."
    fixed, report = fix_text(contraction_nearby)
    if "notably, this matters" not in fixed.lower():
        failures.append(f"a nearby contraction incorrectly suppressed a real fix: {fixed!r}")
    if "didn't" not in fixed:
        failures.append(f"a nearby contraction was itself altered: {fixed!r}")

    # Fenced code block is never touched.
    coded = "Explanation.\n\n```\nit is important to note that this is code\n```\n"
    fixed, _ = fix_text(coded)
    if "it is important to note that this is code" not in fixed:
        failures.append(f"code block was altered: {fixed!r}")

    # Em dashes are never auto-fixed (comma-splice risk, see module
    # docstring) - both occurrences here are left untouched and counted for
    # manual review, one inside a quotation and so not double-counted there.
    dashed = 'The claim succeeds — the evidence supports it. The witness said "I saw it — clearly."'
    fixed, report = fix_text(dashed)
    if fixed != dashed:
        failures.append(f"em dash should never be auto-fixed: {fixed!r}")
    if report["em_dash_review"] != 1:
        failures.append(
            f"expected 1 em dash flagged for review (the one outside the quotation), got {report['em_dash_review']}"
        )

    # Idempotency: running the fixer on its own output changes nothing further.
    twice, _ = fix_text(fixed)
    if twice != fixed:
        failures.append("fixer is not idempotent")

    # A clean sentence is left alone.
    clean = "The tribunal has jurisdiction over this claim."
    fixed, report = fix_text(clean)
    if fixed != clean or report["fixes"]:
        failures.append(f"false positive on clean text: {fixed!r}")

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
    p.add_argument("--apply", action="store_true", help="write fixes back to each file (default: dry run, report only)")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()

    if args.selftest:
        sys.exit(selftest())

    if not args.files:
        p.error("supply at least one file, or --selftest")

    exit_code = 0
    for path in args.files:
        changed, report = fix_file(path, args.apply)
        print(f"--- {path} ---")
        if not report["fixes"] and not report["em_dash_review"]:
            print("  no findings")
            continue
        for rule, count in report["fixes"].items():
            label = rule.replace("\\b", "").strip()
            verb = "fixed" if args.apply else "would fix"
            print(f"  {verb}: {label!r} x{count}")
            exit_code = 1
        if report["em_dash_review"]:
            print(f"  MANUAL REVIEW: {report['em_dash_review']} em dash(es), not auto-fixed (see module docstring)")
            exit_code = 1
        if changed and not args.apply:
            print("  (dry run - rerun with --apply to write these changes)")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
