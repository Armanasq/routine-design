# S07 — Tool invocation, provider state, and human outcome are separate

**Intersection:** [P001](../secretarial/P001.md), [P027](../distributed-workflows/P027.md), [P028](../distributed-workflows/P028.md), [P030](../human-ai-guidelines/P030.md).

## Derivation
Human secretary work is about real-world coordination, not the generation of messages. Saga patterns support controlled recovery from partial multi-step operations. Human-AI guidelines require correction and error handling. Their combination implies a **separate outcome ontology**: plan accepted by an LLM, API invoked, provider acknowledged, provider state verified, counterparty accepted, and substantive goal achieved are distinct stages.

## Algorithm
Plan has preconditions, current permission grant, business idempotency key, external target identity and verification method. Dispatch after precondition recheck. After timeout, query remote state; never assume transport failure implies side effect failure. Compensate only where genuinely reversible, otherwise repair forward. Keep `awaiting_external` after sending an invitation until confirmation. Log recovery paths.

## Explicit constraints
Email cannot be unsent by a software saga; no guarantee of exactly-once side effects from workflow retries. A successful provider event cannot prove a counterpart has read, agreed or performed. Need source freshness and identity resolution before marking outcomes.

## Tests
Fault injection at every boundary: before dispatch, between effect and response, after provider acknowledgement, before verification and during state reconciliation. Measure duplicate effects, unknown-outcome recovery time, unauthorized operations and false completion rate.

## Architecture
[Execution](../../docs/workflows/execution-and-recovery.md), [failure taxonomy](../../docs/architecture/failure-handling.md).