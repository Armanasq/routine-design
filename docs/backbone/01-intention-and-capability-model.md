# Intention, Capability, and Actual Outcome: Three Different Contracts

## Problem

A user asks "Handle the upcoming certification." A weak assistant detects the word "certification" and selects a feature. A generalist must determine the requested end, what evidence defines success, what parts need the user's participation, and what capabilities would be necessary independent of tool names.

## GoalContract

The goal is a versioned object:
- principal and accountable actor; user-end description and authoritative expression;
- acceptance mode: proposed, explicitly adopted, accepted on behalf of others with authority, paused, withdrawn;
- success predicate and independent verification source; possible partial outcomes and unknowns;
- domain competence requirements, optional specialist restrictions and user-selected assistance mode;
- hard constraints, protected time, resources, budget, deadline windows and dependency relationships;
- currently known source evidence, contradictions and missing decisions;
- operation grant references only (the goal does not itself grant permissions);
- context version, change history and privacy classification.

Success is not "the agent has produced text". A course application draft is not a submission; a learning session is not demonstrated mastery; a notification is not a confirmed behavior change; a submitted email is not counterparty agreement.

## AbstractCapabilityRequest

Before naming an API, the planner describes an operational need:
- desired effect (e.g., an authoritative requirement is fetched, a document is prepared, a calendar block is reserved);
- required observations and entity types;
- risk, data class and external side-effect category;
- required authority and acceptable evidence of completion;
- reversibility, idempotency and time sensitivity;
- search constraints such as cost or exact account scope.

This descriptor is a **query**, not an executable declaration. A proposed "call_professor" capability means "we need a way to contact this recipient"; no API is assumed to exist.

## RegisteredOperator

A registry entry describes a *real, verifiably available* capability:
- immutable provider/tool ID, fully qualified operation name, version, auth scopes;
- parameter and output schemas, domain/input/output types and identity constraints;
- preconditions, expected local effect, externally verifiable effect and explicit prohibitions;
- sensitive-data class, recipient/target binding, side-effect severity and reversibility;
- execution/retry semantics, idempotency support, source freshness and failure modes;
- observed reliability and cost with denominators; last verification and health.

The model may suggest operator use, but a deterministic validator checks scope, schema and current authorization. Registry contents from untrusted tool servers or third-party documents are not promoted automatically.

## WorldState is open-world, not closed-world

Absence of an event in one app is not proof the external event did not occur. Facts carry source visibility, valid time, observation time, provenance, consent scope, epistemic type and confidence when calibrated. Maintain explicit UNKNOWN as a possible state.

A fact "no reply seen" and a claim "recipient has not replied" are different. A model-generated expected effect is not equivalent to a provider-confirmed external effect.

## Example: an unfamiliar task

"I want to organize a community telescope night."

Goal interpretation: safe event, participants aware, venue available, equipment prepared, user-selected budget.

Abstract needs: identify appropriate regulations/venue; find equipment and logistics; coordinate invitees; prepare a schedule; verify actual confirmations.

Discovery can find existing search, calendar, email and document tools. Specialist matters remain unresolved until authoritative resources or qualified people are available. Existing coordination primitives compose without an astronomy-specific workflow.

## Invariants

- A proposed request never becomes a user-adopted commitment without appropriate evidence.
- A retrieved preference never becomes action authority.
- An abstract operation never becomes an executable tool without a real registry binding.
- A predicted effect never becomes verified reality without evidence from the outcome verifier.
- A novel goal never forces the planner to pretend domain expertise exists.

## Formalization direction

Represent goal predicates over typed, temporal state. Represent available operations with guarded preconditions and possible effects. A bounded planning algorithm searches legal transitions and can return: satisfied, feasible proposal, approval needed, information needed, unsupported capability, or search-budget exhausted. Do not conflate the final three.

The current standard-library reference code demonstrates only propositional planning; its string facts cannot enforce the typed real-world contract described here.