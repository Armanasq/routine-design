# S06 — The agent changes its own training data

**Intersection:** [P010](../attention-learning/P010.md), [P020](../conservative-learning/P020.md), [P021](../counterfactual-learning/P021.md), [P022](../evolving-memory/P022.md).

## Causal problem
A priority policy that always surfaces professional work generates more user clicks on professional work. Using those clicks as preference labels creates feedback bias; professional activities become even more visible. Likewise, time saved by Routin can trigger acceptance of more obligations, creating an overload rebound. This is an architectural threat, not merely a statistical concern.

## Requirements
Log decision context, all eligible candidate actions, suppressed options, selection/exposure probability when randomized, declared constraints and outcome version. Separate `explicit_feedback` from `observed_behavior` and `policy_induced_observation`. Preserve protected user-chosen goals regardless of a click-based ranker.

## Evaluation
Start with deterministic baseline. Use shadow evaluation; deploy counterfactual methods only when valid propensities and support overlap are established. Randomize only low-risk notification/timing policies with consent; never explore external side-effect grants. Compare long-run goal distribution, incorrect preference updates, attention burden and critical misses.

## Failure modes
If all historical policy decisions were deterministic and unlogged, counterfactual estimates may be unidentifiable. Be explicit: we do not know what users would have done with unseen choices. Prioritize direct, minimally burdensome preference corrections rather than fabricate counterfactuals.

## Architecture
[Learning policy](../../docs/algorithms/learning-and-counterfactuals.md), [research evaluation](../../research/evaluation.md).