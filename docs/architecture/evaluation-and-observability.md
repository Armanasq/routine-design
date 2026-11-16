# Observability, scientific evaluation, and operational checkpoints

## Trace chain
`source_observation_id -> claim_id -> responsibility_version -> belief_snapshot -> decision_trace -> plan_id -> authority_grant_version -> execution_id -> verification_evidence_id -> feedback_id`.

Log model ID, prompt version, extractor schema, deterministic validator version, selected candidate set and rejection reasons, context freshness, policy version, cost estimate, execution attempt and provider response classification. Keep sensitive content out of ordinary logs; source data remains in controlled storage.

## Operational SLO candidates (set targets only after tests)
Freshness per connector; event replay success; false completion rate; unauthorized effect count; duplicate send rate; time-to-reconcile unknown; resumption context correctness; p95 decision latency; critical omission rate; correction effort; cost per externally verified outcome.

## Scientific evaluation
Avoid conflating model extraction accuracy with secretary performance. The true unit of benefit is fulfilled responsibility, prevented unnecessary commitment, time protected, goal progress and actual user administrative effort saved. Run controlled scenarios with oracle outcome and multiweek user pilot for longitudinal claims.

## Predeployment gates
G0 evidence ingestion and identity; G1 bitemporal current belief; G2 capacity calibration; G3 policy omission and VOI; G4 permission-safe effectful execution; G5 verified postconditions; G6 longitudinal adaptation. Use local deterministic tests to avoid GitHub Actions usage charges.

## Audit sampling
Stratify by risk severity, source freshness, conflicting instructions, hard deadline proximity, long-horizon goal conflicts, identity ambiguity, and user correction frequency. Review false positives and high-consequence false negatives, not just successful traces.