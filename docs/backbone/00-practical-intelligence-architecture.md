# Routin Adaptive Backbone — Practical Intelligence, Not Case Routing

**State:** research-backed system design, 2026-11-16. The bounded reference planner is implemented; the full agent runtime is NOT implemented.

## North star

Routin does not have a list of tasks it knows how to solve. It maintains a model of a person's evolving purposes and responsibilities, discovers what knowledge and operations each unfamiliar purpose requires, selects a feasible and authorized strategy, verifies actual outcomes, and learns from the resulting experience.

The generalization target is not "handle every domain"; it is to use the same reasoning machinery when the field, language, available tools, workflows, user context, and failure modes differ from those seen during development.

## One irreducible separation

1. **Normative state:** What the person wants, what they agreed to, what they forbid, and what they authorize. This is not inferred from productivity traces.
2. **Epistemic state:** What observations support, contradict, or leave uncertain. Source freshness and visibility matter.
3. **Operational state:** What operations are available now, with which preconditions, effects, targets, permissions, and version.
4. **Control state:** What to reason about, ask, prepare, execute, monitor, verify or revise now.
5. **Outcome state:** What genuinely changed in the world, and whose evidence establishes it.

A language model is used for semantic interpretation, abstraction, hypothesis generation, alternative planning and communication. It is not the sole authority over permissions, acceptance, verified outcomes or provider-side effects.

## Backbone components

- **Observation/evidence intake:** source health, dedupe, records and user corrections.
- **Goal interpreter:** extracts desired outcomes, support mode, unresolved ambiguity, and normative versus descriptive claims.
- **World and personal belief model:** temporal facts, source confidence, relationships, constraints, goals, and current commitments.
- **Working context compiler:** selects mandatory evidence and optionally relevant episodes, without context-window truncation of hard constraints.
- **Meta-controller:** chooses cheap direct response, missing-information research, planning, limited clarification, safe preparation, or abstention.
- **Abstract capability generator:** describes required operations by needed effects and preconditions, never invents an executable tool identifier.
- **Live capability registry:** discovers approved connectors, available operators, versions and tool health; updates without model retraining.
- **Compositional planner:** assembles alternative dependency-aware, bounded plans across currently available, validated operators.
- **Constraint and authority engine:** independent typed approval, consent, cross-domain data and risk policies.
- **Durable executor/verifier:** executes permitted effects with remote reconciliation and real postcondition observation.
- **Experience learner:** records failures, user corrections and verified outcomes; produces scoped strategy/procedure candidates rather than unrestricted self-modification.
- **Selective revision controller:** invalidates only the plan portions whose premises changed while preserving verified side effects and human commitments.

One human/user model and one responsibility graph underlie these components. Specialist competence is supplied when needed, but domain names are NOT routing keys to scripted workflows.

## What can change at runtime

The user can introduce an unseen objective. A provider can add/remove/rename an operation. New evidence can invalidate a strategy. The user may change a standing preference or an individual exception. A tested procedural skill may become available after certification. The optimizer may change a proposed plan while keeping the user's accepted end fixed.

No step requires adding a hardcoded if/else for "gym", "beekeeping", "PhD" or "house repair". A capability can only become executable if it has a trusted schema, adequate domain competence, current permissions and an independent outcome verifier.

## Semantic generalization has a boundary

Novel wording and new task composition are often tractable. Entirely novel physical, clinical, legal or financial capabilities require validated knowledge and/or real tools. If the required effect is not representable or authorized, the legitimate product outcome is bounded assistance: research, prepare, ask, route to a professional, or abstain. Do not claim the AI can execute every possible task.

## Required comparison

Compare against (A) task-specific scripts, (B) general LLM + many fixed tools, (C) retrieval-first tool selection, (D) plan-first tool selection, (E) shared state without procedural learning, and (F) full adaptive controller. Hold models, tool access, permissions and cost fixed. Test held-out domains, changed tools, temporal shifts, irreversible operations and real-world outcome verification.

Read: [intention representation](01-intention-and-capability-model.md), [tool discovery](02-dynamic-tool-discovery.md), [planning](03-adaptive-planning-and-control.md), [learning](04-experience-and-continual-learning.md), [execution](05-durable-execution-and-unknown-outcomes.md).