# Durable Execution, Evidence, and Unknown Outcomes

## The failure that matters

An LLM says "done" after scheduling, emailing or paying. The actual provider operation may have failed, partially succeeded, or succeeded while the acknowledgment was lost. Repeating it may send duplicates; reverting an internal plan cannot undo an irreversible message.

The backbone must separate model proposals, validated operation intent, granted authority, provider state and substantive human outcome.

## Execution state machine

PROPOSED -> PRECONDITIONS_CHECKED -> APPROVAL_REQUIRED (if needed) -> PREPARED -> DISPATCH_REQUESTED -> PROVIDER_ACKNOWLEDGED or EFFECT_UNKNOWN -> VERIFIED_POSTCONDITION or AWAITING_EXTERNAL -> TERMINAL_RESOLVED / REPAIR_FORWARD / FAILED.

Every transition records evidence, state version and timestamp. Approval is specific to exact operation/target/payload limits/time and may expire. Provider ACK is not necessarily the intended user outcome. A real-world task can remain AWAITING_EXTERNAL for days or weeks.

## Independent dispatch boundary

Before each effect:
- Read current user identity, account and grant. A learned autonomy preference never substitutes for a grant.
- Re-resolve provider/tool ID, registry revision, schema, recipient/target, version and source freshness.
- Recheck live preconditions, hard policy and cross-domain confidentiality.
- Persist intent plus stable operation/business key; use transactional outbox where local DB consistency requires it.
- Dispatch through trusted adapter; do not let LLM directly construct arbitrary endpoint/URL or code.
- Record provider ACK, error or UNKNOWN; perform remote read-after-write/reconciliation after ambiguous timeout before retry.
- Verify domain-specific outcome using appropriate independent source.
- Report only the verified state to the user.

## Exactly-once myth

A workflow engine can keep deterministic history and retry activities, but real external APIs may execute side effects more than once unless idempotency is provided. Temporal's documentation explicitly recommends idempotent Activities and notes that completed Activities are not replayed, while a crash before completion reporting can cause retry.

Use provider idempotency key where supported; otherwise check remote state and limit retries. For sensitive irreversible effects, ambiguous outcome may require human resolution rather than automated resend.

## Long-horizon durability

Use a durable workflow/state machine. Each responsibility or operation has event history and stable IDs, not a single constantly growing prompt. The planner itself can be re-invoked when source or grant state changes; side effect orchestration remains reproducible and versioned.

Workflow nodes include WAIT_FOR_SOURCE, WAIT_FOR_USER, WAIT_FOR_COUNTERPARTY, PREPARE, DISPATCH, RECONCILE, VERIFY, REPLAN, ESCALATE. They are generic operational primitives; application-specific details are data/typed outcome contracts.

## Revision semantics

When a plan becomes invalid: find the earliest violated dependency; retain externally verified unaffected subgoals; quarantine unverified branches; reconcile unknown side effects; replan only downstream. A user changing a goal does not automatically cancel third-party agreements made under an earlier goal.

## Example

The user approves an email proposing Thursday 15:00. The send call times out. The system enters EFFECT_UNKNOWN, checks provider message ID/outbox, and avoids another send until its side effect state is established. Even if the send is verified, the meeting is still not accepted by its recipient.

## Testing

Out-of-order webhook, duplicate event delivery, source revocation while waiting, provider write after timeout, expiration between plan/dispatch, permission change, wrong target, new tool version, rollback after irreversible effect, counterpart rejection, asynchronous recovery and required audit retrieval.

## Reference choice

- Temporal workflow/event history and activity idempotency: https://docs.temporal.io/workflows and https://docs.temporal.io/activity-definition .
- Prior saga theory: Garcia-Molina and Salem (1987), P027.
- MAGE selective execution-state revision (2026), P046.

Do not hardwire the planning policy into workflow execution code. Durable execution answers **what happened**; reasoning decides **what is appropriate next**.