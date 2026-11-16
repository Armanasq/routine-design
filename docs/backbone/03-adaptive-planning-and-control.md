# Open-World Planning and Adaptive Control

## Core decision problem

Given a current, partially observed world state; a person-adopted goal; a versioned capability registry; authorization grants; resource/time constraints; a cost/attention budget; and uncertainty, generate a plan that can be verified. If the user modifies the goal or the environment invalidates a premise, revise the dependent steps without pretending old external effects were undone.

## Proven planning concepts

SHOP2 (Nau et al., JAIR 2003) formalizes hierarchical task decomposition into primitive operators; this is strong prior art for separating goals from available actions. ReAct (ICLR 2023) interleaves reasoning, actions, and new observations, but its model-driven trace cannot independently establish consent or external outcome truth.

The Agent Planning Benchmark (EMNLP 2026) provides 4,209 cases across 22 domains, demonstrating weaknesses with irrelevant/broken tools, long horizon, and infeasible tasks. This argues for a distinct planning diagnosis rather than scoring only final text.

## Planning state

IntentGraph: user ends, accepted obligations, resource constraints, deadlines, human participants and dependencies.

WorldBelief: provenance, validity, uncertainty, source coverage, observation permissions.

OperatorGraph: currently trusted capabilities with preconditions, predicted/possible effects, external verifier, cost, time, grants and failures.

ExecutionGraph: completed/verified subgoals, pending/in-flight operations, irreversible effects and current strategy validity.

## Dynamic planning sequence

A. Build the current typed world snapshot; mark unknowns without inventing them.

B. Generate candidate subgoals needed for the verified outcome. Some subgoals are informational or clarification tasks; others are coordination or real-world effects.

C. Resolve abstract capabilities against the changing tool registry. Avoid compiling all tools into the prompt.

D. Generate several candidate dependency graphs, informed by validated procedural memory and current constraints, not merely a memorized workflow.

E. Run static admissibility: correct identities, permission coverage, precondition observability, source freshness, domain competence, time/resource feasibility and prohibited effects.

F. Compare admissible candidates for critical omission, constraint violations, net user effort, counterpart burden, reversibility, timing, risk and model/tool cost. Treat hard user values/authority as constraints, not weighted preferences that can be overridden by a guessed utility number.

G. Select proceed, ask, prepare, batch, observe, seek data, request capability, or abstain. The most intelligent action is sometimes NOOP.

H. Before each real operation, re-read current registry and source state. A plan is a proposal, not a transaction.

I. Verify provider postconditions, update the world state, and replan only if necessary.

J. Record outcome and which evidence/previous experience actually affected the decision.

## Formal objective (research hypothesis)

For permitted candidate plans pi, select a Pareto-efficient plan over (missed-confirmed-obligation risk, action error, user and collaborator coordination burden, delayed user-goal progress, scheduling churn, execution/tool cost, uncertainty).

Where user trade-off weights are unknown, preserve multiple alternatives and ask at the smallest consequential decision. Never reduce all human values to a global score learned from click behavior.

## Search completeness

A bounded search failing to find a solution is not proof the objective is impossible. Distinguish:
- impossible under complete formal model and permitted operations;
- search exhausted by time/step/state budget;
- lacking a currently available capability;
- preconditions unknown because sources are incomplete;
- capable but approval missing;
- human or specialist value choice unresolved.

The current Python reference planner distinguishes approval, impossibility and search exhaustion; it is propositional, not a production temporal/POMDP planner.

## Replanning and real-world consistency

Local revision must preserve verified unaffected progress and exact external effects. If a calendar cancellation succeeded, merely reverting the agent's internal plan cannot reinstate the meeting. After timeout on a side-effectful operation, query provider state before retrying. Record partial/unknown and select repair-forward or compensation only where provider actually supports it.

## What is NOT novel

Hierarchical decomposition, tool planning, ReAct loops, backtracking, memory-conditioned planning and task-graph execution are established ideas. Routin's research opportunity is to evaluate a **joint, consent-aware controller** for dynamically assembled cross-domain obligations, current tool capability, evolving user goals, and measured real-world outcomes.

## Tests

Leave-domain-out, tool-renaming, tool-removal, permission revocation, missing preconditions, multiple simultaneous goals, resource conflicts, stale source, uncertain external effect, user changes objective, identical historical actions with different current values, latency/cost-limited search. Compare static and adaptive policies at matched budgets.