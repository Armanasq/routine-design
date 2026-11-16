# Reference kernel verification snapshot

**Run date:** 2026-11-16.
**Environment:** isolated container, Python 3.13.5.
**Command:** python -m unittest discover -s tests -v
**Result:** 23 tests, all passed. Python compileall also passed.

The tests were run on a local working copy of the kernel and matching test content, then the same source was committed to GitHub on main. A remote Python execution environment was not invoked: GitHub-side execution has not been verified. GitHub Actions were not added, to avoid spending usage unnecessarily.

Covered cases: conditional intent, proposal admission without automatic acceptance, protected user time, insufficient point-estimate capacity, expired grants, scoped/expired preferences, exposure-aware learning, stale connector and expected non-events, explicit provider vs outcome evidence, deferrable focus and last-safe intervention.

**Explicit limitations:** not a calibrated policy, real scheduling solver, database, durable workflow, secure identity resolver or provider integration. Boolean validation of a supplied evidence identifier cannot establish its authenticity. Production must verify against authorized source records and current grant versions. No network or API side effects occur.
