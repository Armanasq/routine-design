# Reference Kernel Validation

**Test date:** 2026-11-16.  
**Environment:** isolated container, Python 3.13.5.  
**Executed command:** python -m unittest discover -s tests -v  
**Observed result:** 26 tests passed, including 23 pure decision cases and 3 integrated scenarios.

The same Python source and test contents were committed to GitHub main and compared by their Git blob SHA against the locally tested files. No GitHub-hosted test run was executed and no paid GitHub Actions workflow was created.

## Confirmed only for the reference model

- Conditional proposals are not silently converted into commitments.
- Feasible proposed commitments still require acceptance.
- Protected explicit goals and stated preferences outrank observations.
- Unknown/partial source coverage cannot prove a missing reply.
- External effects require operation- and recipient-matched current grants.
- Provider acknowledgments are not goal completion; distinct outcome evidence is required.
- Deferrable interventions can wait until a safe breakpoint.
- Click behavior is not promoted into authoritative preference without explicit confirmation.

## Not implemented or validated

No persistent source ledger; no integration with real Gmail/Calendar; no recipient identity proof; no cryptographic outcome-verification check; no stochastic duration distributions or OR solver; no real attention-cost calibration; no workflow retries or cross-provider state reconciliation; no longitudinal preference learner. The verifier accepts a string identifier as evidence in this intentionally small model; the real system must resolve the identifier against authenticated evidence before trusting it.

**Correct interpretation:** deterministic specification regression tests, not a measured productivity benefit or complete production validation.
