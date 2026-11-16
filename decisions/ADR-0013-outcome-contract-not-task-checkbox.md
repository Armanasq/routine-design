# ADR-0013 — Every domain declares evidence of progress and completion

**Status:** proposed.

## Context

Completion of one agent action is not synonymous with the user's substantive objective. Learning, fitness, wellbeing, application and interpersonal commitments differ in what can be observed and when outcomes are determined.

## Decision

Use outcome contracts with explicit success predicate, partial state, observation/proxy validity, trusted verifier, temporal window, uncertainty and domain-risk boundary. Shared responsibility lifecycle accepts domain verifier result but not generated assertions. Measurements support heterogeneous goal trajectories; no universal "productivity score."

## Alternatives

Task checkbox (false positives), one global LLM judge (overconfident), always ask user (burdensome, not verifiable).

## Gate

In test cases, study session != mastery, reminder != wellness improvement, submission draft != application, sent email != agreement, booked health appointment != completed care. Compare false complete rate and correction burden.

## Evidence

P063, P064, P067, P068, P070, P037.