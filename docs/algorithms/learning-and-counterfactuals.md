# Learning without self-reinforcing errors

## Exposure confounding
The user can only click or dismiss what the algorithm chose to show. Observations are endogenous to Routin's exposure policy. Treat clicks as ambiguous feedback, not ground-truth priorities.

## Decision log
Store decision ID, candidate set, selected content, presentation timing, propensity when randomized, user choice availability, policy version, risk constraints, earlier explicit preferences, relevant outcome and delayed evidence.

## Promotion gates
Source observation -> repeated context-matched hypothesis -> explicit confirmation when consequential -> scoped preference. Keep temporary exception separate. Track contradictory episodes and reversal.

## Offline learning
Initially supervised calibration and deterministic decision thresholds. Counterfactual evaluation only if treatment propensities were logged, support overlaps and outcome labels are observable. If overlap fails, mark estimates uninterpretable.

## Online deployment
Shadow evaluate -> consented low-risk A/B where warranted -> guardrail monitoring -> gradual rollout -> rollback. Never explore authorization boundaries, reveal private information for learning or experiment on irreversible actions.

## Causal checks
Time saved could invite more commitments; algorithm ranking could create false preference evidence; model-driven schedule churn could undermine scheduling. Quantify these loops and include negative controls.

Research basis: Schnabel et al. ICML 2016; Kazerouni et al. NeurIPS 2017; Kapoor & Horvitz CHI 2008; Memora ACL 2026.