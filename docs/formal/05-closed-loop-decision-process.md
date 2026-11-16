# Closed-loop Practical Reasoning and Adaptive Coordination

**Status:** proposed mathematical and system specification; not empirically calibrated.

## A formal boundary

The system's actual world state is only partially observed. Connected sources are incomplete, delayed, permission-scoped and sometimes contradictory. Routin's control loop must therefore distinguish the *external world* from the *model's current beliefs about that world*.

Define:
- S(t): latent user/environment state including commitments, relationships and actual outcomes.
- O(t): source observations and coverage evidence.
- B(t): posterior or set-valued belief state supported by O(0:t) and earlier actions.
- I(t): user-chosen intentions, interpersonal commitments and valued boundaries.
- G(t): explicit grants that restrict effectful actions.
- A(t): candidate assistant actions, including wait, observe, compute, ask, prepare, surface, interrupt, negotiate and execute.
- Y(t+1): externally verified outcomes with provenance, which may remain unknown.

State evolution is influenced by the assistant itself: external actions can change workload, collaborators' reactions and the evidence available for learning. The system is a controller inside the environment, not an outside narrator of it.

## Do not learn a value function from observational behavior

B(t) contains *descriptive* hypotheses. I(t) contains *normative* choices. G(t) contains *legal/operational authority*. None can be safely inferred from the other simply because they correlate.

A crowded late calendar is evidence of a work pattern but not a value judgment that late work is preferred. High interaction with professional tasks may have been caused by the assistant showing only those tasks. A rapid approval is not proof of informed consent to future, broader actions.

## Lexicographic decision boundaries

Stage 0 — evidence admissibility: source valid and fresh enough for this action class; identity and actor known; modal status typed correctly.
Stage 1 — authorization admissibility: current grants and explicit user constraints; no forbidden external effects.
Stage 2 — feasibility: time, resources, deadlines, dependencies and accepted social commitments; if unknown, consider safe information-gathering.
Stage 3 — attention ownership: decide whether human intervention is necessary and its latest useful moment.
Stage 4 — multiobjective outcome comparison: evaluate delay, attention, correction, external coordination costs, protected goals, churn and computation.
Stage 5 — execute or abstain: only within grants and with an outcome verifier.
Stage 6 — feedback update: compare predicted and realized outcomes; log alternatives and whether the assistant's own selection policy influenced feedback.

Do not collapse Stage 1 into a weighted loss. Permissions and some hard personal constraints cannot be traded away for estimated productivity.

## Multiobjective decision, not one unsupported score

For feasible permissible actions, compare the *vector*:
- risk of missing confirmed critical commitments;
- delay and last-safe-intervention margin;
- human administrative/correction burden;
- counterparty coordination burden where measurable;
- loss of user-chosen protected time;
- rescheduling displacement and interruption recovery;
- model/tool cost and latency;
- uncertainty about the actual external outcome.

When one action dominates another across all relevant measured dimensions, reject the dominated action. When there is a genuine trade-off between user values, ask or defer according to the user-established rule; do not invent universal trade-off weights.

Use conservative interval estimates and scenario analysis before deploying probability-based objectives; until calibration exists, report an uncertainty class and enforce deterministic exceptions.

## Decision proof object

Every high-impact decision must retain:
- observed source IDs and coverage windows;
- current belief and intention versions;
- recognized unknowns and disagreements;
- constraint checks, permission checks and counterparty state;
- alternatives considered and reasons rejected;
- predicted consequences with model/calibration version;
- selected action and last-safe time;
- postconditions, recovery plan and actual outcome evidence.

This object can be small in memory but must be reproducible. A language model explanation may be generated from the proof object; it must not serve as the proof.

## Counterexample: scheduling a request

Incoming mail: a client proposes a Thursday evening discussion. Existing calendar contains some late meetings. User has explicitly protected evenings. A naive scheduling agent sees a free slot and auto-accepts. A better LLM might detect conflict but invent a preference update. Routin must:
1. Preserve proposal status until user or authorized agreement.
2. Reject treating past late meetings as current permission.
3. Compute feasible daytime alternatives and costs of renegotiation.
4. Decide if contacting the client is allowed for that exact operation.
5. Record sent offer separately from acceptance, and acceptance separately from meeting completion.
6. Update preference only if the user explicitly changes it or enough context-specific evidence supports asking.

## Research/implementation sequence

Start with deterministic typed state and authorization invariants. Introduce uncertainty-aware time estimates next, then attention timing and preference selection, then bounded safe policy learning. Keep comparisons to static rules and pure LLM recommendations. Validate each brick before proceeding.

**Prior art:** Horvitz (1999) mixed initiative, Bratman (1987) planning intentions, Schmidt/Bannon (1992) articulation work, MemPABench (2026) and Memora (2026) memory failure, Garcia-Molina/Salem (1987) saga recovery. This integration is a hypothesis, not established novelty.