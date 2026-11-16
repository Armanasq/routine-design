# S05 — Personal growth requires preserving the right to pursue an activity

**Intersection:** [P011](../goal-systems/P011.md), [P012](../goal-systems/P012.md), [P013](../goal-adaptation/P013.md), [P014](../behavior-change/P014.md), [P024](../human-agency/P024.md), [P025](../motivation/P025.md), [P026](../personal-informatics/P026.md).

## Derivation
Goal-systems theory differentiates ends from means; implementation intentions connect explicit cues to plans; adaptive disengagement shows revising unattainable means can be healthy; self-determination emphasizes choice; lived-informatics work normalizes lapses. AI skill-retention research raises a countervailing risk: optimizing short-term convenience can remove the very practice that enables long-term competence.

Routin must distinguish user commands: *do it for me* vs *help me learn to do it*. The first prioritizes verified efficiency, the second preserves user participation and chosen learning opportunities.

## Proposed domain model
`Goal {desired_outcome, explicit_user_choice, reasons_optional, alternative_means, protected_capacity, constraints, change_policy, outcome_signals}`. `Routine` is a means linked to a goal, not a proxy for one. `Lapse` is classified as conflict, temporary suspension, infeasible plan, changed preference or unknown—not automatic failure.

## Conflict
Overprotection of a declared goal can be as paternalistic as automatic displacement. Allow explicit pausing/retirement; never infer personal values from tracking logs. Learning workflows are optional and must not impose training exercises on someone requesting simple administrative delegation.

## Tests
Compare rigid routine rules, unconstrained optimizer and goal-aware adaptive planning; measure long-term goal progress, incorrect abandonment, perceived agency, overcommitment, skill maintenance and user effort.

## Architecture
[Memory](../../docs/architecture/memory-and-learning.md), [capacity](../../docs/algorithms/capacity-and-admission.md).