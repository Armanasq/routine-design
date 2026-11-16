# S22 — Planning Proofs, Tool State, and External Outcomes

**Linked research:** P081 (HTN planning), P080 (ReAct), P073 (APB), P078 (ToolSandbox), P077 (tau-bench), P027 (sagas).

## Synthesis

SHOP2 supplies hierarchical planning decomposition; ReAct supplies feedback between reasoning and observation. APB demonstrates why planning errors need separate diagnosis. ToolSandbox evaluates dynamic intermediate milestones and state dependencies. Tau-bench shows policy adherence and final database correctness are not reliably obtained from a plausible conversation. Sagas provide recovery patterns for long-running operations.

Routin should model *three distinct artifacts*: a planning proposal with predicted effects; a durable execution trace with provider acknowledgments; and externally verified responsibility outcomes. Each stage has different invariants and access rights.

## Consequential counterexample

An email-send operation can be correctly planned, authorized and acknowledged, yet the recipient may never agree. The planner should never mark the agreed meeting as complete from a tool result. After a timeout, a blind send retry could harm the relationship; a proper system must reconcile real provider state before retry.

## Model limitation

A propositional planner assumes operator effects are meaningful and observable, which is rarely fully true in social coordination. A user task might be impossible because a crucial tool is unavailable, or it may be unresolved because the search horizon was exhausted. These states must not be conflated.

## Test

Cross tool versions, stale webhooks, interrupted approvals, unseen domains, wrong recipient, ambiguous user instruction and delayed third-party outcome. Measure completeness of valid plan, actual milestone transitions, false terminal claims and duplicate irreversible effects.

**Current reference:** reference_kernel/adaptive_planner.py is a bounded symbolic illustration, not a verified provider executor.