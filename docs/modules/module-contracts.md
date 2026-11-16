# Module contracts and ownership

| Module | Inputs | Outputs | State owner | Constraints |
|---|---|---|---|---|
| Connector | Credentials, cursors, provider change | Canonical source event and freshness | Source state | No inferred task creation |
| Claim extractor | Authorized source spans | Typed competing claims | Candidate claims | No direct side effects |
| Entity resolver | Claims, scoped identities | Links + unresolved identities | Identity map | Avoid unsafe merges |
| Reconciler | Claims, existing state | Versioned responsibility transitions | Responsibility store | Evidence required |
| Personal model | Explicit and inferred evidence | Scoped bitemporal beliefs | Belief ledger | No permission promotion |
| Time forecaster | Tasks, durations, constraints | Duration distributions and coverage | Calibration store | Uncertainty disclosed |
| Admission planner | New requests, budgets, goals | Feasible options and external impacts | Plan versions | Protect hard constraints |
| Initiative policy | Beliefs, context, costs | Ranked **actions**, time, detail | Decision trace | Critical omission guard |
| Dialogue/voice | User utterance, allowed current context | Intent/clarification and proposed actions | Conversation | Barge-in/corrections |
| Workflow executor | Validated plan + current grant | Activity states and provider receipts | Execution state | Idempotency/reconcile |
| Verifier | Provider state and expected postconditions | Outcome evidence/unknown | Outcome store | No tool-success shortcut |
| Learning evaluator | Feedback, exposure, outcomes | Gated updates and candidate policies | Model registry | Guardrail tests |

## Non-functional requirements
Replayable event processing; tenant isolation; explicit retention/deletion; monitoring source freshness; untrusted-content boundaries; bounded reasoning latency; versioned prompts/models; structured logs; full operation trace; accessible correction paths in eventual UI; exportable and removable personal data; no secrets committed.

## Initial system topology
API + modular domain services + PostgreSQL + transactional outbox + worker pool. Add Temporal for long-running workflows, OR-Tools for complex constrained scheduling, vector search only for measured retrieval needs. Avoid distributed monolith from premature microservices.