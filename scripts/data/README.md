# Vendored data

- `reporters.json`: US court-reporter abbreviation table, vendored from [Free Law Project's reporters-db](https://github.com/freelawproject/reporters-db) (`reporters_db/data/reporters.json`, fetched 2026-08-22). BSD-2-Clause, see `REPORTERS_DB_LICENSE.txt`. Used only by `../citation_lint.py`'s reporter-name recognition check: it validates that a shape-matched US reporter abbreviation is a real, known one, not whether the underlying case exists (that still requires CourtListener or an equivalent primary source, per `../../docs/OPERATING_RULES.md`).
- `REPORTERS_DB_LICENSE.txt`: the exact upstream license text for reporters.json, vendored alongside it per the BSD-2-Clause redistribution terms.
- `courts.json`: US court name/abbreviation table (2,809 records), vendored from [Free Law Project's courts-db](https://github.com/freelawproject/courts-db) (`courts_db/data/courts.json`, fetched 2026-08-22). BSD-2-Clause, see `COURTS_DB_LICENSE.txt`. Used by `../verify_court_name.py`, same publisher and licensing model as reporters-db, same non-claim: it validates the court *name* is real, not that a specific case was actually decided there.
- `COURTS_DB_LICENSE.txt`: the exact upstream license text for courts.json, vendored alongside it per the BSD-2-Clause redistribution terms.

Not re-fetched automatically. If either upstream project publishes a new release, re-download its data file from the `main` branch and replace the corresponding file here. There's no build step or dependency pin to update; it's plain JSON read directly by the Python scripts that use it.
