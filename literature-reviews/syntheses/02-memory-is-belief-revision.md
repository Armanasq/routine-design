# S02 — Memory is a controlled belief-revision problem, not chat recall

**Intersection:** [P002](../distributed-cognition/P002.md), [P021](../counterfactual-learning/P021.md), [P022](../evolving-memory/P022.md), [P023](../evolving-memory/P023.md), [P029](../long-memory-evaluation/P029.md).

## Reasoning
A persistent assistant must act on *currently valid* knowledge. Memory benchmarks show that models may retrieve invalidated preferences; recommender-system research shows feedback depends on what the system exposed. Both imply a failure of naive memory consolidation: a user's repeated acceptance of afternoon meetings could be created by the scheduler repeatedly presenting afternoon options.

Thus Routin needs three explicitly disjoint evidence types: `stated_preference`, `observed_pattern`, and `policy-mediated_observation`. Also store `desired_goal`, `temporary_exception` and `authorization` separately. A preference claim is `(proposition, scope, valid-time interval, recorded-time interval, source, confidence, contradictions, supersedes)`. A new observation must not silently overrule a currently valid explicit constraint.

## Policy
Retrieve evidence only after tenant, authorization, valid-time and contradiction filtering. A proposed update passes through (a) source verification, (b) identity/scope check, (c) inconsistency classification, (d) material-decision impact, then (e) silent candidate storage or short explicit clarification. A deletion/revocation must trigger dependency invalidation and cache purge.

## Negative controls
One-off exception after travel; an out-of-date source claiming a prior preference; meetings scheduled by others; user temporarily accepting a disliked arrangement. Test whether feedback-based learners change preference incorrectly after each.

## Empirical test
Memory FAMA/temporal query accuracy plus live decision error: does the revised model pick appropriate suggestions in new contexts? A memory model improving synthetic recall but degrading actual scheduling decisions should not ship.

## Architecture
[Memory](../../docs/architecture/memory-and-learning.md), [learning](../../docs/algorithms/learning-and-counterfactuals.md), [ADR-0002](../../decisions/ADR-0002-bitemporal-evidence-ledger.md).