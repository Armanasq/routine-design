# Deterministic reference decision kernel

**Purpose:** research and specification by executable example. NOT a production assistant, optimizer, scheduler, voice runtime, verified evidence store, permission service or agent.

Python >= 3.11; zero third-party runtime dependencies.

## Which invariants it illustrates
- A proposed or conditional obligation must not be silently accepted.
- Explicit scoped preferences override inferred behavioral evidence; temporary exceptions expire.
- Absence of reply is unknown if the connector is stale, incomplete, or revoked.
- Protected user-chosen intervals and insufficient budget block naive admission.
- External operations require a current, exact operation-and-target grant.
- A provider send acknowledgment is not independently sufficient to verify real-world outcome.
- A focus interruption is deferred to a safe breakpoint unless the last intervention opportunity has arrived.
- Click-based behavior is not promoted to an authoritative preference.

## Honest limitations
No persistent event store, probabilistic forecasting, causal identification, conflict solving, true source-identity verification, provider integrations, retry engine, hard ACL enforcement, formal temporal logic, or calibrated attention cost model. Admission uses point estimates as an intentionally visible lower-quality baseline; a future stochastic planner must replace it. A nonempty outcome evidence identifier is not evidence integrity; real implementation needs signed/provider-resolved verification with provenance and state version. This kernel returns an *advisory dispatch eligibility*; the actual workflow MUST recheck authority and state at effect time.

## Verification
From repository root:
    python -m unittest discover -s tests -p 'test_reference_kernel.py' -v

Do not deploy this demonstrator for real user accounts. Its role is to make assumptions and counterexamples inspectable and to establish regression cases for the architecture.
