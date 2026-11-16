# Formalizing decisions, priorities and hierarchical attention

## Priority is not a single scalar
Define `consequence_if_missed`, `latest_safe_intervention`, `actionability`, `goal_alignment`, `dependency_blocking`, `source_confidence`, `interruptibility`, `authority`, and `user_action_time` separately. Do not assign one universally meaningful importance weight.

## Feasible action classes
`monitor`, `prepare`, `reschedule_internal`, `batch`, `surface`, `interrupt`, `ask`, `request_approval`, `execute_with_grant`, `verify`.

## Decision cascade
1. Validate source trust and recency (reconcile when insufficient).
2. Evaluate hard risk and critical-response windows.
3. Check authorization and protected commitments.
4. Forecast consequence/feasibility under alternatives.
5. Evaluate user intervention cost versus risk of delay.
6. Choose who should act, when and whether further computation/questions are warranted.
7. Select information depth: actionable conclusion -> brief causal reason -> alternatives/evidence -> complete audit.
8. Persist suppressed alternatives and state/version for learning.

## Human decision boundary
Only the user may legitimately choose personal values, accept meaningful boundary exceptions, and authorize consequential side effects. Never optimize personal-life priorities by inferred engagement patterns. If a decision's value trade-off is genuinely unresolved, present that conflict explicitly, not a fabricated optimized score.

## Acceptance criteria
More accurate urgent exceptions without noise, fewer harmful interruptions, lower time-to-decision with no quality loss, stable focus ordering, current preference validity and preserved auditability.