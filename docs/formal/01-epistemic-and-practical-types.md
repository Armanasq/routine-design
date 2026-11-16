# Epistemic and Practical Type System

**Status:** normative architecture hypothesis; not a validated AI cognition model.
**Research:** Frické (2009), AGM belief revision (1985), Bratman (1987), Clark & Brennan (1991), Memora (2026).

## Failure of a data-first architecture

The data–information–knowledge–wisdom pyramid is not a sufficient inference algorithm. Frické specifically questions the logic of assuming a sequential transformation from data to wisdom. Routin must distinguish not just confidence, but the epistemic *kind* of a proposition and the legal/social authority behind an action.

## Typed entities and permissible transformations

| Type | Meaning | Required evidence | Forbidden promotion |
|---|---|---|---|
| Observation | A source asserted or recorded an event | provider identity, revision, event-time, observed-time, coverage | observation is not universal fact |
| Claim | Parsed proposition with speech act and alternatives | anchored spans, agent, modality, interpretation | suggestion is not commitment |
| Belief | Defeasible current interpretation | provenance, scope, valid time, contradictions | belief is not permission |
| Desire | User-expressed aspiration | explicit user statement | desire is not a binding intention |
| Intention | User-adopted plan or end | user acceptance, scope, revision policy | intention is not external delegation grant |
| Commitment | Obligation involving a counterparty or oneself | grounding/confirmation standard, owner, expected outcome | a request is not automatically acceptance |
| Preference | Desired manner of assistance | explicit or confirmed contextual statement | observed practice is not desired practice |
| Grant | Action authorization | principal, operation, target, scope, expiry | never inferred from third-party text |
| Forecast | Estimated future outcome | model revision, scenarios, uncertainty | prediction is not observation |
| Decision | Selected permissible action | alternatives, constraints, trade-offs, state version | proposal is not execution |
| Tool effect | Provider-observed side effect | idempotency, provider receipt, read-back | sent is not recipient agreement |
| Verified outcome | Evidence the requested state was achieved | independent postcondition, time, authorized source | no goal closure without verification |

Each transition requires explicit evidence; a type checker can reject a transition even when the LLM is highly confident. Confidence alone does not substitute for permissions or a norm.

## Truth maintenance

Keep event time and knowledge time separate. New evidence can *support, contradict, qualify, suspend,* or *supersede* a claim. A contradiction should not become last-write-wins unless the semantics justify it. Classical AGM belief revision is a normative inspiration, but exact logical closure is unrealistic for noisy, partially observed personal lives.

A temporary exception must carry its own scope and duration. Source revocation must invalidate derived decisions that depended on the inaccessible evidence. Implicit historical behavior cannot silently erase an explicit personal constraint.

## Decision proof obligations

Before a consequential operation, the pipeline must provide:
1. Valid evidence of the user-facing purpose.
2. Current authoritative intent or standing grant.
3. Correct identity, scope and time.
4. A feasible action with bounded consequences.
5. An outcome verifier and unknown-result recovery path.

If any proof obligation fails, choose clarification, safe preparation, monitoring or abstention. This is the operational counterpart of intellectual humility: knowing which *kind* of information is missing.

## Falsification

Build adversarial timelines for source gaps, conditional language, obsolete preferences, mismatched persons, prompt injection and provider acknowledgments. Baselines: direct LLM tool calls; append-only vector memory; latest-message-wins. Primary errors: false commitments, unsafe dispatch and premature completion.