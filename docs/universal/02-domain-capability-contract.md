# Capability Packs — Extend Domains Without Fragmenting Routin

## Concept

A **domain capability pack** is a validated specification that teaches the shared coordinator how to interpret a domain, what facts and knowledge are required, what safe actions are permitted, how outcomes are verified and how uncertainty is handled. It is *not* an autonomous account-spanning agent with separate permissions.

Packs can compose. "Apply for an overseas PhD" combines research, learning, documents, communications, scheduling and application submission. "Train for a race" combines fitness, recovery, calendar, travel and possibly clinical constraints. No pack gets to set or override user values.

## Mandatory pack contract

1. Domain and subdomain taxonomy, supported intent classes, exclusions and known unknowns.
2. Capability list: READ, RESEARCH, SUMMARIZE, ANALYZE, DRAFT, SCHEDULE_INTERNAL, PROPOSE_EXTERNAL, EXECUTE_EXTERNAL, MEASURE, MONITOR, ESCALATE; each with expected data sources and source-health requirements.
3. Core entities and temporal state transitions; whether missing information can be interpreted as a non-event.
4. Domain evidence standards: official source vs third party vs wearable vs self-report; units, ranges, uncertainty, freshness and contraindications.
5. Outcome contracts: proxy signals vs real achievements; success/partial/unverified/failed; postcondition verifier.
6. Intervention policy: appropriate decision points, receptivity, burden, expected proximal and distal outcomes, default NOOP, interruption limits.
7. Permission model: required scopes, allowed recipients, sensitive data boundaries and operations needing explicit user approval.
8. Risk envelope: physical, psychological, financial, reputational, privacy or legal; deterministic hard stops and human expertise required.
9. Competence provenance: which scientific/technical documents justify domain logic; current version and expiration.
10. Learning policy: what can be inferred, what needs explicit confirmation, whether adaptation is validated, drift and rollback rules.
11. Runtime dependencies: tools, providers, query budgets and fallback behaviors.
12. Evaluation fixture set: positive, negative, time-change, permission, source-coverage, cross-domain and unintended-consequence cases.

## Runtime capability resolution

Given user instruction U and current state:
1. Parse intended **end**, requested delegation mode and implicated domains without inferring permission.
2. Resolve needed primitive and domain capabilities from pack manifests.
3. Reject unsupported specialist claims and unknown provider operations; substitute narrower support: organize data, prepare questions, refer to trusted sources or a professional.
4. Compose a plan whose steps each declare pack, evidence and grant requirements.
5. Validate **cross-pack interference**: data sharing, risk escalation, schedule/resource conflicts, unresolved values, procedural negative transfer.
6. Check each side effect against independent authority grants immediately before execution.
7. Verify outcome according to *domain's* standard, record partial work and learn only from qualified evidence.

No arbitrary plugin code executes automatically from a memory note or external document.

## Pack layering and trust

Base pack: universal time/attention/relationships/evidence/consent.
Domain pack: e.g., education, training, wellbeing, health navigation, work communications, applications.
Subdomain refinement: e.g., language vs math learning; strength vs endurance training; wellness behavior vs clinical decision support.
Provider adapter: Google Calendar, course LMS, wearable, applicant portal, email; handles sync and actual tool capabilities.

A pack does not require its own database. Same underlying event ledger with partitioned access, typed projections and pack version is preferable at first.

## Cross-domain transfer safeguards

A procedure may transfer only if its preconditions, outcome semantics and authority class match. "Successfully sent an email" transfers as a safe provider-operation pattern, *not* as evidence to auto-send clinician instructions or scholarship applications. Exercise time forecasting may transfer as a duration prior but cannot transfer as a claim about physical fitness or clinical improvement.

Every transfer requires:
- capability compatibility;
- user-intention compatibility;
- source/provenance policy compatibility;
- authorization equivalence;
- outcome-verifier equivalence;
- negative-applicability screening;
- confidence downgrade and shadow testing outside its original domain.

## Pack lifecycle

DRAFT -> LITERATURE_REVIEWED -> SCHEMA_VALIDATED -> SAFETY_REVIEWED -> SIMULATED -> SHADOW_EVALUATED -> PILOT_AUTHORIZED -> ACTIVE -> SUSPENDED/RETIRED.

Provider API changes, clinical guideline updates, privacy-rule changes, observed failures or evidence invalidation trigger pack review and may force suspension. Do not infer validation from one high-level agent benchmark or from the fact that the pack composes syntactically.

## Decision whether specialist agents are necessary

The October 2026 Nature personal health agent uses specialized data-science, domain-expert and coaching subagents because they have materially different technical and evaluation demands. Routin can invoke specialized analyses as typed tools with distinct verification, or internally use models when measured quality demands it. A multi-agent swarm is not a design requirement or claim of novelty; preserve a single responsibility state and policy owner.
