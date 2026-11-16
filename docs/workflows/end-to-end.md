# Lifecycle and workflows

## Core pipeline
`observe -> normalize -> resolve -> hypothesize -> validate -> reconcile -> store belief -> forecast -> evaluate alternatives -> select initiative -> authorize -> prepare/act -> verify -> incorporate feedback -> revise`

## Workflow A: Email implies a new responsibility
1. Provider event arrives; verify cursor and freshness; deduplicate.
2. Extract request modality, actor, due interval and source span; maintain alternatives.
3. Resolve owner/counterparty and link to known responsibility; do not create duplicate tasks.
4. Promote to confirmed only on sufficient evidence or explicit user instruction.
5. Check dependency chain, expected external reply and capacity.
6. Choose silent preparation, display, clarification or authorized action.
7. Verify external result; leave unconfirmed replies waiting.
8. Record explicit correction and decision exposure for later learning.

## Workflow B: New meeting would overcommit
Compare feasible schedules with/without new request. Check protected personal time, travel, uncertainty, schedule displacement. Decline/negotiate/ask for approval only within explicit permission. Do not fill all rescued time.

## Workflow C: Interrupted focus
Estimate interruption urgency and deadline. If deferrable, batch. If necessary, capture current state, next concrete step and return context (resumption capsule) with minimal interaction; schedule feasible recovery.

## Workflow D: Goal/routine disruption
Distinguish lapse from changed intention. Test time/strategy alternatives before questioning the overarching goal. Protected user choice overrides inferred behavior. Ask only if consequential.

## Workflow E: Uncertain external action
Persist intent and business key, recheck authorization, send once under provider capabilities, reconcile after timeout before retry, verify provider outcome and final real-world state. If outcome remains unknown, escalate.

## Workflow F: User corrects Routin
Patch local proposed action; append feedback to decision log; validate whether correction is global, scoped or one-off; do not rewrite permanent preferences without evidence.