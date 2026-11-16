# S03 — Attention allocation must include the cost of returning to interrupted work

**Intersection:** [P004](../prospective-memory/P004.md), [P005](../interruptions/P005.md), [P006](../interruptions/P006.md), [P008](../active-elicitation/P008.md), [P010](../attention-learning/P010.md).

## Derivation
Prospective memory motivates externalizing intentions; interruption studies show timing changes cognitive cost; ready-to-resume work suggests a mitigation when an interruption must occur; value-of-information methods explain when to ask. Combining these yields two coupled decisions: (1) should Routin intervene at all? (2) if yes, how can it minimize both interruption and subsequent resumption cost?

Do not reduce this to `rank by urgency`: an item can be highly important but safely deferrable, or urgent yet impossible for the user to act on now.

## Policy
Estimate `last_safe_intervention` from hard deadlines and intervention lead time; estimate focus disruption using cautious observable context, not psychological mind reading. Choose `silence / prepare / batch / clarify / surface / interrupt`. If interruption is unavoidable and work state is recoverable, offer a one-line resumption capsule including artifact, outstanding choice and next actionable step, plus conservative return time. No automatic summary if evidence is unreliable.

## Conflict and constraints
An optional capsule can itself interrupt. Safety-critical situations override ordinary batching. The user may prefer direct notification regardless of inferred focus. Never infer emotional state or mental health from app usage.

## Research tests
A/B compare timestamp-only alerts, context/breakpoint alerts and context+optional resumption. Measure missed useful windows, inappropriate interruptions, correction burden, return latency and work quality. Predefine critical omission ceilings.

## Architecture
[Attention policy](../../docs/algorithms/attention-and-initiative.md), [workflow C](../../docs/workflows/end-to-end.md).