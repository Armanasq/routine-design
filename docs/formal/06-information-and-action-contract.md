# Minimal Information Contract (Backend, Not UI)

The future interface should be extremely small, but the amount of information to expose is a decision outcome, not a fixed design rule. The policy must answer four questions for each situation: *which responsibility, when, how much context, and whose action?*

## Information levels

L0 — one decision/action headline: user can understand the immediate required step.
L1 — why-now causal reason: one source-backed constraint or consequence.
L2 — relevant alternatives, evidence, permission and uncertainty sufficient for a responsible decision.
L3 — complete audit: source coverage, revisions, candidate options, policy version and execution history.

Routin must not default to L0 when a user is asked to approve a consequential, difficult-to-reverse operation. The policy chooses the minimum level that supports an informed decision under the current risk class.

## AttentionDirective contract

Fields:
- responsibility_id and current evidence snapshot;
- action_kind: silence / prepare / batch / surface / interrupt / ask / request_approval / execute;
- target_actor: agent / principal / counterparty;
- earliest and last-safe intervention timestamps;
- required decision and mutually exclusive alternatives;
- level_of_detail and required disclosure flags;
- authority reference, missing input and verification plan;
- why-now explanation grounded in documented consequences;
- suppression cause if other work was not shown;
- policy version, uncertainty and explicit user override opportunity.

## Selection constraints

Do not infer importance from click frequency alone. A critical item may need immediate attention even while focus is active. A major but nonactionable item may be monitored silently. A minor operation with a valid grant may be completed without user interruption. An item with stale evidence may require resynchronization, not a prompt.

Prevent thrash through hysteresis and bounded re-evaluation. Ensure all confirmed obligations remain findable; non-displayed does not mean forgotten.

## Grounding and user effort

Ask one question when it would change the permissible decision materially. Avoid repeated confirmations in contexts where an exact standing grant applies. However, a learned "do not ask" preference never supersedes legal, safety or authorization rules.

## Evaluation

Do not optimize screen emptiness. Measure time to correct decision, critical omission rate, unnecessary intervention burden, comprehension accuracy, correction time and actual postconditions. Use MemPABench to test preference selection vs behavior realization; use task-level user studies to test human outcome and trust.