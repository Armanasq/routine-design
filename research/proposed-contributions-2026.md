# Routin Research Contributions — Candidate Problems, not Novelty Claims

## Candidate A: Decision-adequate memory selection under permissions and bounded attention

**Proposed problem:** choose the smallest evidence set supporting a correct, authorized decision while minimizing model latency and human attention and avoiding hidden critical constraints.

**Prior art:** MemGPT virtual context; LongMemEval; MAGE execution state; MemPABench interaction preferences; human mixed initiative. A mere multi-layer hierarchy is not original.

**Candidate methodological distinction:** first enforce evidence/current state/permission invariants and uncertainty coverage; then optimize optional context by expected marginal decision usefulness; independently verify generated behavior against selected preference and policy.

**Falsification:** does it reduce false decisions, source omissions and manual corrections versus typed-state-only and retrieval baselines at equal token budget? If not, remove the context-utility model and retain simpler deterministic state.

## Candidate B: Verified experience-to-procedure with conservative negative transfer

**Problem:** an agent with history repeatedly encounters similar administrative processes but cannot safely transform observations into autonomous executable skills.

**Prior art:** Reflexion language feedback; ExpeL trajectory knowledge; Voyager skills; AdaMEM dynamic strategy; MAGE state revision; saga transactions. Reuse by itself is fully established.

**Candidate distinction:** promote only evidence-backed procedures with applicability/negative applicability predicates, action authority, permission scope, external postcondition verifier, failure-injection replay and valid-time expiry. Failed episodes inform warnings but do not become universal instructions.

**Falsification:** compare repeated workflow success, duplicate effects, silent wrong-recipient actions, and corrections versus static scripts and prompted trajectory reuse. Procedures must not expand permissions.

## Candidate C: Goal-preserving attention policy conditioned on learned memory reliability

**Problem:** an assistant can accurately remember a user but still interrupt at the wrong time or sacrifice personal goals, producing zero net benefit.

**Prior art:** mixed initiative, interruptibility systems, personal goals, stochastic scheduling and proactive agents.

**Candidate distinction:** jointly select subject, timing, information depth, delegation actor, and memory/strategy refresh under capacity constraints, normative user goals, and calibrated evidence reliability. Account for presentation-policy feedback and overcommitment rebound.

**Falsification:** real user-and-counterparty effort, missed important obligations, protection of chosen development goals, and errors from preference drift versus independent subsystem optimization.

## Candidate D: Cross-timescale reconciliation and metacognitive repair

**Problem:** asynchronous information changes plans; agent memory contains previously successful but now-invalid instructions; tool effects have unknown state.

**Prior art:** MAGE's hierarchical revision; AdaMEM dynamic refresh; AGM belief revision; temporal databases, sagas.

**Candidate distinction:** one consistent revision protocol that propagates invalidations across evidence, beliefs, strategies, active executions, derived personal routines and external reconciliation. Selectively correct affected branches without erasing valid progress or pretending irreversible actions can be undone.

**Falsification:** cascade size and recovery time after injected changes, false terminal states, repeat side effects, and stale strategy use.

## Proposed scientific path

1. Define a formal environment with actor, action, information access, goal, time, permissions, social counterpart and delayed outcome.
2. Implement strong baselines and a decision trace with source-level ground truth.
3. Run ablations by memory tier and policy stage, measuring correctness, token costs and intervention burden.
4. Evaluate transfer to realistic tool workflows and changing user preferences.
5. Collect a consented, carefully governed longitudinal study to validate actual usefulness.
6. Publish negative findings as well as positive ones.

No novelty score, scientific effect size, or productivity improvement is asserted before these steps.