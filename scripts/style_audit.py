#!/usr/bin/env python3
"""Explainable legal-writing audit and substantive-change lock.

The audit reports editorial signals. It is not an AI detector. Comparison
mode fails closed when quotations, citations, dates, numbers, measurements,
URLs, or email addresses differ between the pre-edit and post-edit versions.

Usage:
    python3 scripts/style_audit.py draft.md
    python3 scripts/style_audit.py --json draft.md
    python3 scripts/style_audit.py --compare before.md after.md
    python3 scripts/style_audit.py --selftest
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from citation_lint import STOCK_PHRASES  # noqa: E402
from style_fix import _protected_spans  # noqa: E402

_SENTENCE = re.compile(r"(?<=[.!?])\s+")
_WORD = re.compile(r"\b[\w'-]+\b")
_ANCHOR_PATTERNS = (
    ("url", re.compile(r"https?://[^\s<>()\]\[{}]+", re.I)),
    ("email", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)),
    ("neutral_citation", re.compile(r"\[\d{4}\]\s*(?:\d+\s*)?[A-Z]{2,}(?:\s+[A-Za-z]+)*\s+\d+")),
    ("ecli", re.compile(r"\bECLI:[A-Z]{2}:[A-Z0-9.]+:\d{4}:[A-Z0-9.]+\b", re.I)),
    ("case_number", re.compile(r"\b(?:Case|Claim|Appeal)\s+(?:No\.?\s*)?[A-Z0-9][A-Z0-9/.-]+\b", re.I)),
    ("date", re.compile(r"\b(?:\d{1,2}\s+)?(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b", re.I)),
    ("number", re.compile(r"(?<!\w)(?:£|\$|€)?\d+(?:[,.]\d+)*(?:\s?(?:%|mg|g|kg|ml|l|cm|mm|km|m|hours?|days?|weeks?|months?|years?))?(?!\w)", re.I)),
)


def _unprotected_text(text):
    chars = list(text)
    for start, end in _protected_spans(text):
        chars[start:end] = " " * (end - start)
    return "".join(chars)


def extract_anchors(text):
    """Return typed exact-value anchors, preserving duplicate counts."""
    anchors = []
    for start, end in _protected_spans(text):
        value = text[start:end]
        if value.lstrip().startswith("```"):
            continue
        anchors.append(("quotation", value))
    for kind, pattern in _ANCHOR_PATTERNS:
        anchors.extend((kind, match.group(0).rstrip(".,;:")) for match in pattern.finditer(text))
    return anchors


def compare_texts(before, after):
    """Compare substantive anchors and return a fail-closed integrity report."""
    before_counts = Counter(extract_anchors(before))
    after_counts = Counter(extract_anchors(after))
    missing = list((before_counts - after_counts).elements())
    added = list((after_counts - before_counts).elements())
    return {
        "passed": not missing and not added,
        "status": "PASSED" if not missing and not added else "SUBSTANTIVE_REVIEW_REQUIRED",
        "missing": [{"kind": kind, "value": value} for kind, value in sorted(missing)],
        "added": [{"kind": kind, "value": value} for kind, value in sorted(added)],
        "before_anchor_count": sum(before_counts.values()),
        "after_anchor_count": sum(after_counts.values()),
        "scope": "Exact-value comparison only; legal propositions still require human substantive review.",
    }


def audit_text(text):
    """Report deterministic editorial signals without judging authorship."""
    prose = _unprotected_text(text)
    sentences = [part.strip() for part in _SENTENCE.split(prose.strip()) if part.strip()]
    sentence_lengths = [len(_WORD.findall(sentence)) for sentence in sentences]
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", prose) if p.strip()]
    paragraph_lengths = [len(_WORD.findall(p)) for p in paragraphs]
    signals = []

    stock = sorted({phrase for phrase in STOCK_PHRASES if re.search(rf"\b{re.escape(phrase)}\b", prose, re.I)})
    if stock:
        signals.append({"code": "stock_phrasing", "severity": "warning", "examples": stock})

    long_sentences = sum(length > 38 for length in sentence_lengths)
    if long_sentences:
        signals.append({"code": "long_sentences", "severity": "review", "count": long_sentences})

    openings = []
    for sentence in sentences:
        words = _WORD.findall(sentence.lower())[:3]
        if words:
            openings.append(" ".join(words))
    repeated = sorted(opening for opening, count in Counter(openings).items() if count >= 3)
    if repeated:
        signals.append({"code": "repeated_openings", "severity": "review", "examples": repeated})

    if len(sentence_lengths) >= 5 and max(sentence_lengths) - min(sentence_lengths) <= 6:
        signals.append({"code": "uniform_sentence_rhythm", "severity": "review"})

    if len(paragraph_lengths) >= 4:
        average = sum(paragraph_lengths) / len(paragraph_lengths)
        if average and max(abs(length - average) for length in paragraph_lengths) / average <= 0.12:
            signals.append({"code": "uniform_paragraph_shape", "severity": "review"})

    passive_candidates = re.findall(r"\b(?:is|are|was|were|be|been)\s+[a-z]+(?:ed|en)\b", prose, re.I)
    if len(passive_candidates) >= 3:
        signals.append({
            "code": "passive_voice_candidates",
            "severity": "review",
            "count": len(passive_candidates),
            "note": "Pattern match only; passive voice may be correct in legal drafting.",
        })

    penalty = sum(18 if s["code"] == "stock_phrasing" else 10 for s in signals)
    return {
        "editorial_quality_score": max(0, 100 - penalty),
        "signals": signals,
        "sentence_count": len(sentences),
        "average_sentence_words": round(sum(sentence_lengths) / len(sentence_lengths), 1) if sentence_lengths else 0,
        "disclaimer": "Editorial diagnostic only. It is not an AI detector or a legal-accuracy check.",
    }


def selftest():
    failures = []
    before = 'On 12 June 2026 the claimant paid £1,250. She said, "I paid it in full." See [2024] EWCA Civ 123.'
    if not compare_texts(before, before)["passed"]:
        failures.append("identical text failed comparison")
    changed = before.replace("£1,250", "£1,500")
    report = compare_texts(before, changed)
    if report["passed"] or report["status"] != "SUBSTANTIVE_REVIEW_REQUIRED":
        failures.append("changed amount did not fail closed")
    changed_quote = before.replace("I paid it in full", "I paid most of it")
    if compare_texts(before, changed_quote)["passed"]:
        failures.append("changed quotation was not detected")
    audit = audit_text("It is important to note that the point matters.")
    if not any(item["code"] == "stock_phrasing" for item in audit["signals"]):
        failures.append("stock phrase was not reported")
    if "not an AI detector" not in audit["disclaimer"]:
        failures.append("authorship disclaimer missing")

    if failures:
        print("SELFTEST FAILED:")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("SELFTEST OK (all checks passed)")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("file", nargs="?", help="document to audit")
    parser.add_argument("--compare", nargs=2, metavar=("BEFORE", "AFTER"), help="compare pre-edit and post-edit documents")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()

    if args.selftest:
        sys.exit(selftest())
    if args.compare:
        before_path, after_path = map(Path, args.compare)
        result = compare_texts(before_path.read_text(encoding="utf-8"), after_path.read_text(encoding="utf-8"))
        result.update({"before": str(before_path), "after": str(after_path)})
        print(json.dumps(result, indent=2) if args.json else _format_comparison(result))
        sys.exit(0 if result["passed"] else 1)
    if not args.file:
        parser.error("supply a file, --compare BEFORE AFTER, or --selftest")
    path = Path(args.file)
    result = audit_text(path.read_text(encoding="utf-8"))
    result["file"] = str(path)
    print(json.dumps(result, indent=2) if args.json else _format_audit(result))


def _format_comparison(result):
    lines = [f"Substantive change lock: {result['status']}"]
    for label in ("missing", "added"):
        for item in result[label]:
            lines.append(f"  {label[:-1]} {item['kind']}: {item['value']}")
    lines.append("  " + result["scope"])
    return "\n".join(lines)


def _format_audit(result):
    lines = [f"Editorial quality: {result['editorial_quality_score']}/100"]
    if result["signals"]:
        lines.extend(f"  {item['severity'].upper()}: {item['code']}" for item in result["signals"])
    else:
        lines.append("  no deterministic style findings")
    lines.append("  " + result["disclaimer"])
    return "\n".join(lines)


if __name__ == "__main__":
    main()
