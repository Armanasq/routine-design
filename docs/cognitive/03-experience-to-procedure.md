# Verified Experience and Procedural Learning

**Sources:** Reflexion (NeurIPS 2023), ExpeL (AAAI 2024), Voyager (TMLR 2024), AdaMEM (2026), Memory-R1 (ACL 2026), MAGE (EMNLP 2026).

## Central challenge: a success is not a reusable skill

An episode can succeed for incidental reasons. One user corrections may not imply a general preference. An unsuccessful operation can be caused by an expired permission, stale source, ambiguous request, provider failure or a flawed plan; blindly generalizing failures creates brittle rules. AdaMEM explicitly notes that it stores successful trajectories and observes both hallucinated strategies and strategy inertia.

The candidate contribution is **evidence-gated experience compilation**: transform raw experiences into context-bounded reusable procedures with clear preconditions, postconditions, side effects, provenance, safety and validation status. The idea of memory-based skill reuse is established prior art; applying verified, permission-sensitive procedure promotion to personal coordination remains a testable integration.

## Experience record

An episode captures objective, initial state version, authorization and constraints, source freshness, candidate actions, selected action, provider calls, tool results, verification evidence, user correction, final outcome, observed cost, counterparty state and validity context.

Do not label a step as beneficial merely because the entire trajectory succeeded. Require causal skepticism: record what would have happened under the baseline if observable, otherwise mark contribution attribution unknown.

## Procedure synthesis pipeline

1. **Candidate discovery:** group episodes by task pattern and situation, not just lexical similarity.
2. **Contrast:** examine representative success and failure episodes; identify necessary preconditions and known failure triggers. Failed episodes remain in a restricted diagnostic store.
3. **Extract:** propose a typed procedure with reversible and irreversible steps, permission gates, expected postconditions, cleanup, compensation and timeouts.
4. **Static verification:** schema check, forbidden effects, identity, target scope, wrong-recipient and source-trust tests.
5. **Replay:** execute in sandbox/synthetic or authorized test environment with injected failures; require repair path and no duplicate external effects.
6. **Shadow mode:** advise or prepare without dispatch; measure how often its suggested decisions would diverge from accepted baselines and whether resulting corrections decline.
7. **Certification:** promote only after sufficient diverse representative evidence and declared thresholds; store policy/model/tool versions.
8. **Runtime gating:** check current scope, consent, source health, expiry, identity and procedure preconditions before running.
9. **Continuous monitoring:** compare expected vs actual effects, quarantine failing procedures, roll back to validated alternative.
10. **Retirement:** invalidate a procedure after upstream API changes, policy revision, repeated faults or revoked source rights.

## Procedure schema

ProcedureID, version, description, applicability predicate, negative applicability predicate, goals supported, required observation types, permission class, reversible steps, irreversible steps, effect idempotency keys, postcondition query, retry protocol, user choice required, evidence episode IDs, test suite, failure rate estimate with denominator, owner, approved status and expiration/review condition.

**Do not store a free-text "learned trick" as an executable instruction without the typed plan and policy validator.**

## Example: reliable meeting negotiation

After repeated verified episodes, Routin may propose a playbook that checks capacity, suggests acceptable alternatives, sends within authorized scope, and awaits counterparty agreement. The learned playbook must never automatically accept an incoming request, even if the user historically accepted similar ones, unless the specific grant permits it.

## What counts as transfer

A procedure trained on scheduling one colleague must not be generalized to all contacts without checking relationship, timezone, meeting type, user constraints and communication norms. Novelty is not adding a "skill library"; Voyager already does that. The contribution to test is transfer **under provable authority, uncertainty and interaction cost constraints**.

## Tests and ablations

Episode retrieval only; unverified reflection; verified procedure without counterexamples; verified procedure with counterexamples; full Routin controller. Outcomes: reliable real-world completion, duplicate effects, invalid actions, procedural transfer precision, prompts/corrections, cost per verified outcome and regression under changing APIs.

## Learning limitation

Avoid online model fine-tuning at first. Maintain a transparent, versioned external procedure library. Consider parameter training only after a sufficiently large, consented corpus and offline superiority with drift, negative-transfer and privacy tests.