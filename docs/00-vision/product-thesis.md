# Routin — Product Thesis

## Mission
A delegated personal coordination system that protects the user's scarce time, attention, commitments and chosen growth, while requiring minimal administration. Routin is not an engagement-maximizing product, a generic chatbot, a task list, or an automatic calendar filler.

## Outcome contract
The user should not need to reconcile multiple inboxes, maintain another task board, repeatedly restate preferences, or monitor agents manually. Routin observes authorized sources, constructs evidence-backed responsibilities, understands who owes what to whom, forecasts feasibility, recommends or safely performs the smallest useful next action, verifies results, and corrects its understanding over time.

## Design invariants
1. The source of truth is typed, time-versioned evidence and responsibility state—not an LLM response.
2. Observed behavior is not a stated preference; inferred preference is not permission; a routine is not automatically a goal.
3. A task being done by Routin is not identical to an externally achieved outcome.
4. Preventing bad commitments can be more valuable than scheduling them.
5. Decisions about what to show consider consequence, timeliness, user context and interruption cost; they are not equivalent to priority sorting.
6. Rescued time must not silently become availability for additional commitments.
7. Important personal goals and chosen skills remain legitimate objectives, not spare capacity.
8. Human-initiated overrides are honored, inspectable and revocable; indirect third-party content never grants authority.
9. The assistant must know when NOT to infer, interrupt, ask, execute, or learn.
10. Minimality is reduction in user effort with preserved decision quality, not visual emptiness.

## Research status
These are product and architecture requirements, not experimentally demonstrated benefits. Compare to actual competitors and baselines; do not assert novelty on aggregation alone.

See [research agenda](../../research/hypotheses.md), [architecture](../architecture/system-context.md), [ADRs](../../decisions/).