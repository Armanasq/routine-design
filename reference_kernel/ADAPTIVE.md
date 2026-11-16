# Adaptive planner reference module

The standalone Python file reference_kernel/adaptive_planner.py is **not an LLM agent, production planner, safety engine or working provider integration**. It is a deliberately narrow executable demonstration that *the same search algorithm can compose arbitrary named capabilities supplied in a runtime registry*. No input is dispatched to an actual provider.

## Supported

- Immutable versioned capability registry with unique names, preconditions, predicted effects, deletions, cost and trusted/not-trusted marker.
- Uniform-cost search under maximum step/state budgets.
- Goal satisfaction with multiple desired facts and shared prerequisite effects.
- Distinction between already satisfied, feasible proposal, requires named grant, genuinely unreachable within fully explored model, and search budget exhausted.
- Advisory dispatch eligibility guard for changed registry, stale observation, unverified prerequisite and missing grant.
- Outcome check against independently supplied facts, not plan-predicted state.

## Example

Register any two operations: source_lookup produces source_known; draft_report requires source_known and produces report_draft. The desired predicate report_draft produces a two-step proposal, whatever the subject of the report. Introduce a new validated operation while the process is running and the next proposed plan can use it without modifying planner code.

## Reproducible testing

In repository root: python -m unittest discover -s tests -p test_adaptive_planner.py -v

Local 2026-11-16 run: 19 tests passed under Python 3.x, standard library only. The locally tested module and test file were confirmed to have exactly the same Git blob hashes as the remote main copies:
- adaptive_planner.py: 323ad33d8a7f238a4bf6565054da61de61a427b5
- test_adaptive_planner.py: 8ad32584a568b9ec97d8279a73314640d7694464

## Important limitations

The registry is manually populated test data. Actual MCP/tool discovery is NOT implemented. Trust markers are not independently verified. Raw string predicates do not carry event time, account identity, user consent, sensitive data, source coverage or authority semantics. An operator's predicted effect is NOT proof of a real effect; an incorrect operator declaration can produce an unsafe plan. The cost model is synthetic; the state space can grow exponentially, and concurrency and negative/conditional effects are not fully modeled. The dispatch guard is advisory, with no provider access or atomic authorization logic.

Most importantly: even a perfectly valid symbolic plan is only a candidate. A production coordinator must enforce policy and current source state independently, and verify real postconditions through authorized provider records.

## Next engineering increments

Typed evidence and effect algebra -> capability-registry discovery and signature verification -> authorization and exact recipient binding -> outcome-verifier binding -> temporal/resource uncertainty -> durable workflow simulator -> learning and cost evaluation against baseline. Avoid deploying this prototype for health, finance or personal-data actions.