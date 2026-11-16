# Commitment admission and stochastic time budget

## Fundamental decision
Before accepting a new obligation, estimate whether it is feasible and whether it displaces work or goals. 'Calendar free' is not 'human capacity free'. No automatic admission of third-party requests.

## Estimation
Fit conditional duration distributions by task category, user history and context. At cold start use explicit user estimate and shrinkage prior with uncertainty. Account for preparation, travel, switching cost, rest, accessibility, fixed commitments, soft constraints, dependencies and source reliability. Do not infer sleep/health needs from calendar emptiness.

## Optimizer
Use rolling-horizon constraint programming (e.g. CP-SAT intervals for precedence/no-overlap), followed by scenario simulation for uncertain durations. Hard constraints: current authorization and confirmed fixed/protected commitments. Soft objectives: lateness, deadline risk, weighted schedule displacement, overcommitment, personal goal displacement and excess fragmentation.

## Accept / negotiate / defer / decline
Plan hypothetical state with new request vs without. Compare feasibility and affected responsibilities; produce alternative timing or scope if infeasible. Ask permission before external negotiations. Protect recovered time from unconsented automatic refill.

## Work in progress
Queueing theory motivates measuring active concurrency and cycle time; Little's Law requires stationarity and consistent flow definitions. Do not impose universal WIP limits without actual measurement.

## Fallback
If uncertainty poorly calibrated, report feasible alternatives and unknowns, without mathematical success guarantees. No automatic changes to commitments on weak evidence.

## Evaluation
On-time confirmed completion, forecast coverage, actual task-duration calibration, schedule-churn cost, protected-goal preservation, accepted-obligation overload rate, user correction burden. Separate gains from easier incoming workload and baseline effects.