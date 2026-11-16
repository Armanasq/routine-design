# Adaptive Backbone Experiments — Pre-registered Proposal

**Status:** design only. No performance claim, novelty score or benchmark run is implied.

## Hypothesis H-G1: capability composition over case scripts

Fixed goal, agent and tools. Novel case domains and randomized tool names. Compare literal case router, generic LLM and capability operator search. Test if the latter plans available solutions without adding code for each domain. Primary: verified task success and unsafe action count. Secondary: answer quality and execution cost.

## H-G2: adaptive tool discovery

On simple vs multi-effect tasks, compare direct retrieve-first, plan-first abstract stubs and complexity-gated hybrid at equal tool registry and inference budget. Primary: every necessary tool found and correctly mapped. Protect against fabricated stubs and tools removed midtask.

## H-G3: later-task learning rather than memory recall

Sequential tasks with shared latent structure but different surface text. Compare reset, full history, BM25/semantic memory, typed episodic state and verified procedural learning. Primary: increment in outcome accuracy on later tasks over identical no-memory baseline. Stratify negative transfer and feedback misattribution.

## H-G4: outcome and authority integrity

Adversarial action sequence with provider timeout after possible side effect, changed grant and third-party nonresponse. Compare direct tool-calling agent, workflow-only agent and Routin with separate effect and human outcome verifier. Primary: duplicate effects, false completion and ungranted external actions. Release gate: zero unauthorized effect.

## H-G5: intelligence spends thinking budget only where useful

Evaluate easy exact tasks and difficult uncertain tasks. Always-plan vs direct-lookup vs value-gated strategy selection under equal total compute budget. Primary: error-adjusted cost per verified outcome, p95 latency, unnecessary user questions, deadline misses.

## H-G6: user goals survive cross-domain dynamic planning

Conflicting job/application, learning, family and wellbeing commitments with explicit protected goals and many historical late-work observations. Compare calendar-gap optimizer, engaged-item ranker, constrained portfolio and human-directed tradeoff selection. Primary: critical obligations fulfilled, protected time lost, user correction burden and nonconsensual changes.

## H-G7: unexpected tool skills under dynamic registry

At runtime introduce one authorized tool that produces a formerly unavailable effect; separately remove a needed tool. Same goal and memory state. A generalist should re-plan without application code modification, but not infer permissions. Failure states include absent capability, needed approval, insufficient evidence and search exhaustion.

## Experimental hygiene

Scenario seeds: research/scenarios/universal-100.json (100 examples, 16 classes). These must be transformed into independently generated worlds; do not train to exact literal text. Seed and outcome-oracle provenance retained. Measure LLM backbone/version, all granted tools, trusted registry state and accumulated cost. Report real-world risks and counterexamples, not one composite "intelligence score".

## Readiness

R0 case dataset: committed.
R1 bounded propositional planner: committed and 19 local tests passed.
R2 typed, source-backed tool binding: planned.
R3 dynamic authorized provider discovery: planned.
R4 durable fault-injected simulation: planned.
R5 learning gain and personal longitudinal outcomes: planned.
Only R0 and a limited R1 demonstrator are verified as implemented.