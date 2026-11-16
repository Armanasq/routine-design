# S04 — Prevent overload before optimizing schedules

**Intersection:** [P015](../time-planning/P015.md), [P016](../queueing/P016.md), [P017](../robust-scheduling/P017.md), [P018](../robust-scheduling/P018.md), [P032](../time-management/P032.md).

## Derivation
Planning-fallacy research highlights duration uncertainty; operations research describes stable schedules under disruption; queueing connects work inventory and lead time under defined stationarity assumptions. The cross-paper insight is that scheduling after acceptance is too late if the accepted demand already exceeds capacity. Therefore **admission and negotiation** precede scheduling, and calendar gaps are not treated as capacity.

## Decision system
When a new proposed responsibility arrives:
1. Resolve whether it is an offer/request or already a user-confirmed obligation.
2. Predict required preparation, duration interval, dependencies and uncertainty (task-class prior adjusted to user history).
3. Compare two rolling-horizon worlds: baseline vs accepted request. Respect confirmed commitments, hard limits and protected goals.
4. Estimate deadline risk and stability cost, including the required contingency.
5. Output feasible accept, counterproposal, scope reduction, defer or decline.
6. Route any third-party communication through explicit authority.
7. Reforecast only after a material change, to avoid replan thrash.

## Critical caveat
Little's Law does not prove a universal cap on heterogeneous personal work. Duration distributions may be miscalibrated. Schedule stability may conflict with urgent priorities; hard new obligations sometimes require movement. Record uncertainty honestly.

## Tests
Accepted infeasible commitments, completion reliability, goal displacement, calendar churn, expected vs actual duration and false declines. Compare greedy earliest-empty-slot and EDF planners.

## Architecture
[Capacity admission](../../docs/algorithms/capacity-and-admission.md), [ADR-0003](../../decisions/ADR-0003-admission-before-scheduling.md).