# Dead Component Report

Method: programmatic checks run against the repository on 2026-08-22 (not a manual skim). See commands below each finding - reproducible by rerunning them.

**Update (later same session, 2026-08-22)**: the "Genuine gaps found" section below is now stale. A real CLI and programmatic API were built and selftested (`scripts/legal_cli.py`, `scripts/legal_api.py`) - "No CLI and no programmatic API exist" no longer holds. `regulators/` now has three real profiles (`ico.md`, `cnil.md`, `ftc.md`) plus a `README.md`, `rubrics/` has one real sourced rubric (`level7-distinction-standard.md`), and `templates/` has five real files - these are no longer "intentionally-empty stubs." Counts in section 1 and section 6 are also stale: there are now 10 jurisdiction entries (not 9) and every one of the 8 scripts in `scripts/` (not 2) carries a passing `--selftest`. Kept here rather than rewritten so the version history stays legible, per `docs/HONEST_STATUS.md`'s convention.

## 1. Reference check - every skill/agent/jurisdiction/schema/template/workflow file

```python
# for each file in skills/*/SKILL.md, agents/*/ROLE.md, jurisdictions/*/README.md,
# schemas/*.schema.json, templates/*, workflows/*.md: search all other .md files
# for the file's basename or parent-directory name
```

**Result: zero orphans.** All 16 skills, 13 agents, 9 jurisdiction entries (8 + template), 11 schemas, 3 templates, and 4 workflow files are referenced by at least one other file (range: 6 to 54 mentions each - see raw output in session transcript). No agent file, skill, template, or schema exists that nothing else points to.

## 2. Broken relative path check

```python
# regex over both markdown-link syntax [text](path) and backtick-quoted paths
# `../relative/path.ext`, resolved against each referencing file's own directory
```

**Result: zero genuinely broken links.** 8 markdown-link-syntax references and 219 backtick-quoted relative paths (196 unique) were checked. 11 backtick-quoted paths resolved to a nonexistent file, but every one of them uses an intentional placeholder segment (`<slug>` or `*`), e.g. `` `../../jurisdictions/<slug>/README.md` `` in `skills/legal-work/SKILL.md` - these are meant to be substituted with an actual jurisdiction slug at the point of use, not literal paths. Confirmed by inspection: this is the correct, intended pattern for referring to "whichever jurisdiction pack applies," not a dead link.

## 3. Duplicate workflow / obsolete file check

Reviewed `workflows/` (4 files: `matter-lifecycle.md`, `five-hearing-adversarial.md`, `research-log.md`, `disclosure-register.md`) and `skills/` (16 files) for overlapping scope.

**Result: no duplication found.** Each workflow file covers a distinct concern (matter status progression, the specific five-hearing adversarial process, a research-log template, a disclosure-tracking template) with no two files describing the same process. Skills overlap in the sense that several hand off to each other (e.g. `legal-litigation` hands off to `legal-draft`), but this is designed composition, not duplication - confirmed by reading each skill's "Hand off" section, which names a different next step in every case rather than repeating another skill's content.

## 4. Unused schema fields check

Spot-checked whether every schema's declared `enum` values actually appear somewhere in the workflow/gate documentation that's supposed to use them (a form of "does this field have a consumer").

**Result: consistent.** `matter.schema.json`'s `status` enum matches `workflows/matter-lifecycle.md`'s stated lifecycle exactly (`INTAKE → RESEARCHING → DRAFTING → REVIEWING → ADVERSARIAL_REVIEW → HUMAN_REVIEW_PENDING → VERIFIED_FOR_FILING → CLOSED`). `draft.schema.json`'s `filing_state` enum matches `docs/QUALITY_GATES.md`'s filing states exactly. No orphaned enum value found in this pass (this was also checked by the independent technical review before the previous commit - see `docs/HONEST_STATUS.md`).

## 5. Tests that don't execute meaningful behaviour

The only genuinely executable tests in this repository are `scripts/deadline_calculator.py --selftest` (10 cases) and `scripts/citation_lint.py --selftest`. Both were re-run today and pass. Neither is a "test that doesn't execute meaningful behaviour" - both selftest suites assert specific input/output pairs and fail loudly on regression (verified: the 2026-08-22 review pass caught and fixed three real regex bugs and one real deadline-arithmetic gap this way).

**What is NOT covered by any executable test, and should not be assumed to be:** every skill's and agent role's actual behaviour when invoked live by an LLM. These are prompt specifications, not code - there is no unit-test framework in this repository capable of asserting "given this input, `legal-litigation/SKILL.md` produces this output," because that would require actually invoking an agent, which is precisely what the seven-matter stress test (this same session, following this report) is for.

## 6. Jurisdiction packs with no router connection

**Result: none found.** All 8 real jurisdiction packs plus `_template/` are named explicitly in `README.md`'s jurisdiction table and reachable via `skills/legal-work/SKILL.md` Step 2's generic `../../jurisdictions/<slug>/README.md` lookup - confirmed the lookup pattern works for every one of the 8 real slugs (`england-wales`, `scotland`, `us-federal`, `australia`, `canada`, `new-zealand`, `spain`, `france`) by checking each directory exists at that exact slug.

## Genuine gaps found (not "dead," but real absences - carried into the capability map)

- No CLI and no programmatic API exist (`docs/SPEC_FULL_TEXT.md` describes both; neither was built - see `REPOSITORY_CAPABILITY_MAP.md`).
- `regulators/`, `rubrics/`, and most of `templates/`/`examples/`/`evaluations/` are intentionally-empty stubs, not dead code - they were never wired up because there is nothing real inside them yet, which is different from a broken wire to something that does exist.

## Fixes applied as part of this pass

None required - no dead wiring, broken paths, or orphaned files were found. This is a genuinely different outcome from finding problems and not fixing them: the checks above were run, and came back clean.
