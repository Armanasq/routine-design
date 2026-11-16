# Consent, authority, user agency and threat boundaries

A personal secretary has access to intimate context; authorization is not a formality to add after functionality. Required by first effectful integration, even in a research prototype that uses real user accounts.

## Separate five notions
- **Read permission:** service API scope.
- **Data retention consent:** which evidence may be stored and for how long.
- **Preference:** what the user usually likes.
- **Authority grant:** what external operation may be performed without per-action approval.
- **Approval:** explicit decision authorizing an immutable action specification at a particular state version.

No inference or LLM-generated rationale can upgrade an authorization grant. Revocation takes priority over retries. An old consent is not automatically valid for a new target or side-effect class.

## Policy decisions
Grant keys: principal, operations, resources, recipients, risk class, conditions, expiry, revocation version. Every workflow checks current grant immediately before dispatch and records grant version. A preapproved policy can permit recurring low-risk operations only within explicit bounds.

## Risks
Prompt injection through email/docs; mistaken recipients; confidential cross-account leakage; silent external disclosure; extracted inferred sensitive traits; source revocation with retained derived memory; behavioral manipulation through attention policy; unbounded learning experiments.

## Safeguards
Tenant/account isolation; provenance; tool allowlists; context minimization; explicit inspection and deletion; audit trail; privilege separation between reasoning and effectful tools; no hidden behavior-targeting reward; independent policy engine and fail-closed permission checks.

## Evaluation
Unauthorized-effect zero tolerance; prompt injection replay; deletion propagation; recipient confusion; memory access denied after revocation; negative-inference failures; provider state discrepancies.