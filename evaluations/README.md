# Evaluations

How to actually run the benchmarks in `../benchmarks/`.

## Status

**Manual only, in this build.** There is no automated harness yet that feeds `../benchmarks/hallucination-traps.md` cases into a live Claude Code session running the `legal-work` skill and scores the output. See `../docs/HONEST_STATUS.md`.

## How to run the current starter set by hand

1. Open a Claude Code session with this plugin installed (`../docs/INSTALL.md`).
2. For each case in `../benchmarks/hallucination-traps.md`, give the `INPUT` text to `legal-verify` or `legal-authorities` as if it were a passage to check.
3. Compare the actual output against `EXPECTED_BEHAVIOUR`.
4. Record pass/fail per case, and update `../benchmarks/README.md`'s status table and `../CHANGELOG.md` if the result changes what's claimed as working.

## Building a real harness (future work)

A real evaluation harness would need: a way to script many such cases through the skill non-interactively, a scoring rubric per category (see `../benchmarks/README.md`'s categories), and a regression gate comparing a new build's pass rate against the previous one before it's considered a valid release, per `../docs/OPERATING_RULES.md`'s "regression suite" principle. Not built in this version.
