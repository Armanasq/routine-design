# S01 — A secretary is a distributed coordination system

**Research intersection:** [P001](../secretarial/P001.md) + [P002](../distributed-cognition/P002.md) + [P003](../team-coordination/P003.md) + [P027](../distributed-workflows/P027.md).

## Derivation
Secretarial ethnography identifies anticipation, situational monitoring and delegation. Distributed cognition tells us the relevant state is spread across people and artifacts, not stored in one individual's head. Implicit coordination theory explains why shared expectations permit work without repeated explicit requests. Distributed transaction theory adds the missing execution semantics: a handoff is not a completed transaction, and external parties may never acknowledge it.

Consequently, the central object is neither a task nor a message. It is a **responsibility relation** involving a principal, counterparty, deliverable/outcome, source evidence, expected next event, authority and an explicit verification state. The system should detect expected *non-events* (missing reply, unprepared document, failed handoff), but only when its source coverage is recent enough that the absence is interpretable.

## Derived mechanism
For a relationship edge `user -> delegatee: outcome`, record `expected_signal`, confidence that a signal should exist, latest useful check, evidence freshness and an escalation policy. A missing event is evaluated as `unknown_source_state` if sync freshness is inadequate; otherwise `waiting_external` becomes `follow_up_candidate` after its expected window. The final action is chosen by the attention policy and permission gate, not automatically sent.

## Conflict / counterexample
A manager's email is suggestive, not a binding delegated commitment; a third party's intention cannot be assumed; team-specific shared knowledge might be unavailable. A fresh inbox with no reply does not show that a person has not worked on an offline deliverable.

## Falsification
Compare graph-based handoff tracking vs email-task extraction in paired scenarios. Score precision of awaited events, premature follow-ups, false commitments and downstream verified resolutions; audit wrong-person matches independently.

## Architectural outputs
[Ontology](../../docs/architecture/domain-model.md), [end-to-end lifecycle](../../docs/workflows/end-to-end.md), [ADR-0001](../../decisions/ADR-0001-responsibility-as-core-object.md).