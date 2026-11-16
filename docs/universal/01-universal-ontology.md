# Universal Intent–Responsibility–Outcome Ontology

## Why task is insufficient

A learner wants mastery, not a checkbox. A patient wants a clinician follow-up, not a completed message. A job applicant wants a valid submission and an eventual decision, not merely a filled calendar slot. A user may intend to exercise, but a wearable recording is not the same as a safe or useful training session. Routin needs a shared language for *the real-world outcome and its evidence*.

## Domain-independent primitives

| Primitive | Meaning | Example |
|---|---|---|
| Actor | User, delegate, recipient, clinician, coach, employer, system | Supervisor |
| Role/relationship | Context-bounded obligations and communication norms | Referee and applicant |
| Intention | User-end with selected support mode | Learn motion planning |
| Responsibility | Accountable state over time | Prepare research proposal |
| Proposed commitment | Pending agreement, not yet binding | Meeting request |
| Accepted commitment | Explicitly adopted duty with verifiable conditions | Submit application by deadline |
| Evidence observation | Timestamped, authorized source claim | University posted call |
| Belief | Defeasible scoped hypothesis grounded in evidence | User prefers morning reading |
| Resource | Time, attention, energy budget if explicitly provided, money, equipment | 45 minutes available |
| Constraint | Hard/soft limit with source and ownership | No evenings, physician restriction |
| Capability | What Routin can read, assess, draft or execute, with proof | Draft but do not send |
| Domain state | Specialist facts with typed units, provenance and restrictions | Exercise volume; exam score |
| Action/plan | Proposed sequence and expected effects | Schedule practice test |
| Decision point | Moment to act, defer, clarify, check or abstain | After a task cancellation |
| Intervention | Agent-initiated or user-requested support and dose | Brief reminder, targeted practice |
| Expected event | External non-event monitored under source coverage | Reference letter still pending |
| Outcome | Satisfied condition with evidence, or explicitly unknown | Application confirmation receipt |
| Feedback/experience | What worked, failed, was corrected and why | Prior rescheduling attempt failed |

These primitives exist at shared layer; domain packs supply narrower types, constraints and evidence schemas. The same term "completed" may require a provider receipt for an application but independent performance evidence for learning.

## Objective hierarchy and causality

Life intention > goal > outcome contract > strategy/means > responsibility > action > observation/verification.

A single action can support several goals and can harm others. A new commitment may require both approval and displacement of existing capacity. The graph represents **supports, conflicts, depends_on, fulfills, blocks, prepares, verifies, supersedes** edges with provenance and valid time.

Do not assert a causal relation merely because two activities correlate. Evidence of increased sleep duration does not automatically prove improved health. User satisfaction is not a substitute for valid external outcomes, and physiological data is not a diagnosis.

## Outcome contract

Each domain outcome must declare:
- kind: binary, incremental, continuous, episodic, interpretive or externally adjudicated;
- actual success condition and who can verify it;
- observable proxy and limitations;
- earliest/later meaningful measurement window;
- acceptable uncertainty, risk and clinical/legal boundary;
- what remains partial and what cannot be inferred from silence;
- user correction and appeal path.

Examples:
- Job application: confirmation by authoritative portal; draft saved is partial.
- Language learning: independent recall/use over spaced assessments; minutes studied are activity.
- Fitness: completed authorized session is activity, progress depends on chosen performance/consistency signals; do not equate steps with recovery or readiness.
- Wellbeing: self-reported user-defined experience or explicitly chosen behavior, not psychological state guessed from calendar.
- Medication: prescribing/clinical changes remain with authorized clinicians; reminder adherence data cannot confirm treatment effectiveness.
- Interpersonal coordination: sent != received != understood != agreed != resolved.

## Type and permission separation

"User is frequently stressed" is not an appropriate persistent clinical belief from email and calendar inferences. Personal health data belongs to explicit purpose-bound partitions; a work scheduling agent should not retrieve or reveal it unless user authorized the specific use and disclosure.

Observations do not become intentions, intentions do not become action grants, and provider success does not become verified human outcome.

## Cross-domain entities

A person may be coworker, doctor, family member or reference writer. Keep role- and context-specific relationship representations; identity matching is evidence-based and conservative. Cross-domain joins require explicit policy, least-necessary fields and a recorded justification. "Universal memory" must not mean indiscriminate access.

## State evolution

Observation -> source-backed claim -> scoped belief -> goal/commitment reconciliation -> feasible plan -> allowed initiative -> authorized action -> verified outcome -> experience -> possible memory update.

At every stage the system must preserve rejected alternatives, source freshness and what remains unknown. A hypothesis can be disputed or expired; a goal may be paused without being erased; an action may remain verification_unknown indefinitely rather than being falsely closed.
