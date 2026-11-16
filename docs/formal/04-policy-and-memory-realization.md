# Retrieval, Preference Selection, Behavioral Realization

**Sources:** MemPABench (Li et al., 2026, arXiv:2610.30485), Memora (Uddin et al., 2026), HorizonBench (Li et al., 2026), Agent Memory (Omri et al., 2026).

## A new failure class

Long-term memory is not equivalent to correct user treatment. The October 2026 MemPABench study separates which interaction preference is selected from whether it is actually implemented in behavior. Under its simulated evaluation, several retrieval-based memory conditions are close to a no-memory baseline; file memory shows a selection advantage but suffers contextual overspill. These are benchmark-specific results, not product efficacy estimates.

## Required three-gate architecture

### Gate A: Current-belief retrieval
Input: user, action, context, time and granted scope. Output: candidate scoped preferences with evidence and competing hypotheses. Filtering by current validity and authorization occurs before semantic similarity. A retrieved obsolete preference must not override a current one.

### Gate B: Preference selection
Select the applicable preference for the *current context*, not merely the highest similarity. Explicit preference overrides inferred preference within compatible scope; temporary exceptions are never generalized automatically. Conflicting explicit preferences require reconciliation. No selected preference may expand an authority grant.

### Gate C: Behavior enforcement
The response and tool plan are checked *after* model generation and *before* effectful execution. If selected brevity is not realized, the agent failed even if it retrieved the preference. If a model proposes unauthorized external contact, the authority gate blocks it regardless of a learned autonomy preference.

## Memory write/read cost

The Agent Memory systems characterization motivates profiling memory construction, retrieval and generation separately. Routin should keep fast typed operational state and versioned source evidence, with asynchronous consolidation. Bad or stale belief invalidation takes precedence over adding another summary.

## Learning from the agent's own actions

The system's own presentation policy influences feedback: shown items receive clicks; hidden goals receive none. Treat observed feedback as policy-mediated evidence. Store candidate set, exposure probabilities when applicable, explicit corrections, and subsequent outcomes. Do not learn implicit high-stakes authorization from engagement.

## Evaluation matrix

Measure independently: current-preference retrieval accuracy, scope/context correctness, preference evolution tracking, realization adherence, user correction burden, latency, memory-construction cost, false autonomous effects and data deletion recovery. Apply MemPABench and locally curated adversarial cases, using exact benchmark version and no ungrounded generalization.