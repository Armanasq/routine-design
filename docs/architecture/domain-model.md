# Domain ontology and state invariants

| Entity | Meaning | Required attributes |
|---|---|---|
| SourceObservation | Provider event and effective revision | origin, source ID, timestamps, cursor, scope, freshness |
| CandidateClaim | Uncertain proposition supported by observations | actor, modality, alternatives, source spans, valid time |
| Responsibility | Persistent obligation/intention/commitment | owner, counterparty, outcome, dependencies, deadline interval, verification |
| ExpectedEvent | A response or handoff expected but not yet observed | who, trigger, expected window, freshness precondition |
| Goal | Intentionally chosen desired outcome | user declaration, boundary, alternative means, revision rule |
| Routine | Contextual repeated pattern or desired behavior | observed/declared origin, triggers, suspension, recovery |
| ScopedPreference | What the user wants in a specified context | explicitness, evidence, valid interval, supersession |
| Relationship | Relevant person/role and coordination boundaries | source-backed identity, communication norms, permissions |
| AuthorityGrant | Specific allowed external action class | scopes, recipients, value/risk caps, expiry, revocation |
| ActionPlan | Validated proposal with effects and checks | preconditions, idempotency, postconditions, compensator |
| DecisionTrace | Why action presented/hidden/selected | candidate set, exposure probability, policy versions, trade-offs |
| OutcomeEvidence | Measured external state | provider revision, verification time, source freshness |

## Epistemic separation
**Observation:** what external data says. **Belief:** interpretation, may be false. **Intention:** what user expressly wants. **Norm:** authorization/prohibition. **Execution:** attempt to act. **Outcome:** condition subsequently observed. Never promote one category into another silently.

## Temporal semantics
Store valid-time and system-time intervals. Claims can contradict or supersede other claims. A historical preference remains explainable yet must not influence current decisions after invalidation. Apply deletion/retention rules to all descendants of source records.

## Responsibility states
`candidate -> inferred -> confirmed -> actionable -> prepared -> approval_pending -> executing -> submitted -> awaiting_external -> verified_complete`.
Other states: `disputed, deferred, blocked, failed_retryable, failed_terminal, verification_unknown, cancelled, superseded`.

No `verified_complete` without outcome evidence; no external side effect without current grant; a timeout is not proof of failure; waiting for someone else is not user completion.

## Identity
Use tenant-scoped identifiers, explicit identity confidence, provider IDs where possible. A wrong person match is more costly than two provisional profiles; use an unresolved entity rather than guess.

See [JSON schemas](../../schemas/) for initial machine-readable examples.