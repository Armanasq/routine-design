# Failure taxonomy and recovery design

| Failure | Signal | Recovery | Never do |
|---|---|---|---|
| Missed webhook | Stale watermark/reconciliation gap | incremental backfill or full sync | claim no one replied |
| Revoked authorization | Provider 401/403 or grant revocation | freeze dependent actions and erase/expire inaccessible data as policy requires | replay permission |
| Contradictory deadlines | Two incompatible explicit sources | preserve evidence and ask when consequential | pick arbitrary latest |
| Ambiguous identity | Low match confidence | keep unresolved identity and verify | merge contacts by name alone |
| Timezone uncertainty | Source zone missing or conflicting | retain UTC+source zone, clarify near deadlines | silently shift hours |
| Provider timeout after write | unknown remote effect | reconcile with idempotency token and remote read | immediately resend |
| Provider accepted send | accepted response but recipient state unknown | record submitted; await acknowledgment | mark obligation completed |
| Plan invalidation | new event breaks resource constraints | bounded replan, preserve accepted commitments | churn all calendar items |
| Model hallucination | missing source span / unsupported claim | demote to uncertain hypothesis | commit as operational fact |
| Preference drift | repeated contradictory feedback | test context specificity, propose update | overwrite standing constraint |
| Retrieval from deleted source | provenance absent | invalidate dependent belief and cache | continue using orphan memory |
| Prompt injection | third-party instruction in source content | treat as data only; policy enforces grants | execute source text |
| Critical omission | known hard deadline not surfaced | deterministic exception watchdog | trust learned ranker alone |
| Bad feedback loop | user sees only work, model infers only work matters | exposure log and explicit-goal safeguards | treat silence as preference |
| Failed compensation | nonreversible action occurred | disclose state, repair forward, request help | claim rollback |

## Reliability contract
At-least-once delivery is assumed. Outbox events have stable business IDs; workflows and tools are retriable with idempotency where providers support it; provider verification is separate from task completion. Every unexpected state has an owner, a terminal/unknown distinction and a recovery policy.