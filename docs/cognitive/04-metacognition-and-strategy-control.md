# Metacognition, Strategy Validity and Selective Deliberation

## Background

AdaMEM creates strategies at inference time from retrieved trajectory evidence. Its low-refresh variant can display strategy inertia: a failing plan is wrongly judged still suitable. MAGE shows how revision at subgoal boundaries can preserve unaffected work. Rational metareasoning and mixed-initiative HCI motivate deciding whether more computation, a question or an intervention is worthwhile.

Routin therefore needs a **strategy validity monitor independent from the model that wrote the strategy**. It should use typed environmental evidence and explicit progress signals to decide when a planned action sequence has become invalid.

## Three levels of self-monitoring

**Execution monitor:** did the provider execute the expected effect? Did the response contain a rejection or ambiguity? Is the state stale or unknown?

**Plan monitor:** are the original preconditions still true? Is a dependency blocking progress? Is the last safe action time approaching? Has a lower-level goal been met or abandoned?

**Learning monitor:** are repeated failure patterns explained by tool errors, bad plans, wrong personalization or unavailable evidence? Did Routin's own exposure policy bias the feedback?

## Strategy refresh gate

Recompute strategy if any hard invalidation condition is true:
- precondition violation, revoked grant, changed deadline, changed actor identity;
- verified postcondition failure;
- unexpected tool response or contradiction with active state;
- repeated no-progress episodes exceeding a defensible bound;
- user correction of the strategy's target or scope.

Otherwise estimate whether refinement reduces expected decision loss more than latency/compute/interruption cost. At cold start use cheap, conservative rules. Do not ask the same LLM "are you still correct?" and treat its answer as an independent verifier.

## Hierarchical selective revision

Maintain a task execution tree. Every subgoal boundary has source-state snapshot, verified postconditions and child dependencies. When an error occurs:
1. identify the earliest boundary with a violated premise;
2. keep verified unaffected subgoals;
3. mark downstream dependent states untrusted, not falsely "undone";
4. for reversible effects, execute authorized compensation; for irreversible effects, escalate repair-forward;
5. branch to a revised feasible plan with updated evidence;
6. preserve failed trace for diagnosis but do not use it as a proven procedure.

The tree is a *planning and memory abstraction*, not a substitute for real event sourcing or external side-effect reconciliation.

## Learning from failure without self-blame loops

Associate each failure with a causal uncertainty class: extraction error, memory misapplication, bad scheduling model, stale source, authorization mismatch, provider failure, counterpart nonresponse, or unknown. Multiple causes may be plausible. The system cannot automatically assign fault to the user or counterpart.

Only when a failure cause is sufficiently evidenced should it become a procedural negative rule. A guessed cause can be quarantined as a diagnostic hypothesis; it must not contaminate all future runs.

## Computational architecture

Deterministic fast checks run on every meaningful event. LLM strategy revision only when it could change a decision. Independent validators check facts, permissions and tool schemas. High-impact ambiguous outcomes require user input rather than unbounded agent debate.

## Tests

Stale strategy continues despite expired grant; failed action erroneously causes new "put" tool verb; user changes goal after two substeps; backtrack mistakenly resends an external email; repeated no-progress not detected; model rationalizes a failed plan; strategic recompute overuses tokens without improving outcomes. Compare adaptive gating against always-refresh, never-refresh and direct model self-assessment.

No claim of proven self-awareness or metacognitive consciousness.