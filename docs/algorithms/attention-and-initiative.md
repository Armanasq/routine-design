# Attention, initiative and information allocation

## Decisions, not scores
The policy jointly chooses `subject, action, timing, detail_level, actor`. Candidate actions: monitor; prepare; schedule privately; batch; surface; interrupt; ask; request approval; execute with an explicit grant. Importance and interruptibility are different estimates.

## Policy specification (research hypothesis)
At decision epoch t, belief b_t includes current obligations, deadlines, user goals and constraints, source freshness, predicted future capacity, current focus, memory uncertainty and valid permissions.

Hard filter: permissions, external side-effect class, protected user constraints, evidence requirements and critical deadlines. Generate candidate actions. Estimate consequences using calibrated forecasts. Choose policy minimizing risk-sensitive expected loss:
`min_a E[L_critical + L_delay + L_interrupt + L_manual_effort + L_goal_displacement + L_plan_churn + L_tool_error] + uncertainty_penalty`.
Do not silently trade away rights/permissions or unsupported user values through weights.

## Value of clarification
`VOI(q) = risk(recommended_without_q) - E[risk(recommended_after_answer)] - user_question_cost(q) - delay_cost(q)`.
Ask only if positive and a consequential decision changes. One-time exceptions and inaccessible data should not become broad preferences.

## Value of computing
`VOC(c) = E[improved_decision_value_from_c] - latency_cost(c) - compute_cost(c)`.
Deterministic no-LLM path first; expensive reasoning for genuinely uncertain, consequential situations.

## Attention stability
Hysteresis to prevent thrashing of focus; batched low-impact updates; critical exceptions; exposure/selection logging for counterfactual evaluation; no guaranteed 'optimal' learned policy before field calibration.

## Information contract (not UI)
L0: subject and one required next action. L1: key constraint / consequence. L2: supporting evidence, alternatives, authority. L3: full decision audit. Which level to expose is a risk/decision-need question, not a graphic design choice.

## Baselines
Chronological list, EDF, static weighted rank, LLM-only triage, rules-based breakpoint notification, ablation of capacity and preferences. Measure net manual minutes, missed critical events, attention intrusions, decision quality and trust calibration.