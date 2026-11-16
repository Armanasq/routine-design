# Universal Routin — A Personal Coordination Substrate

**Status:** architecture and research proposal, 2026-11-16. No functional product or measured benefit is claimed.

## The vision

Routin assists with whatever a person is *trying to accomplish or maintain*: work, learning, applications, communications, family, personal administration, fitness, wellbeing, health coordination, travel, creative projects, financial administration, community work and domains not known at product-design time.

"Universal" cannot mean unlimited domain competence, unrestricted action authority, or a single generic numerical objective. It means that a new life domain can be composed from shared, verified coordination primitives plus an explicit, domain-appropriate competence contract, without rewriting the underlying memory and responsibility system.

The ideal busy-user experience is: make a request or share a goal in natural language; Routin remembers accepted commitments, prepares next steps, reduces unnecessary coordination, asks only consequential questions, performs permitted work, verifies outcomes and adapts without silently changing the person's values.

## One universal model, three distinct concerns

**Life coordination core:** who wants what, for whom, by when, why, subject to which constraints, with what evidence of progress and completion.

**Domain competence packs:** how that outcome is defined and what can justifiably be inferred or recommended in that domain; its data sources, validated interventions, risk cases, escalation and specialist integrations.

**Human sovereignty boundary:** user-chosen ends, consented data uses, interpersonal agreements and action permissions. No memory or domain pack may invent an objective or expand an action grant.

Do not create an "education agent" or "health agent" that owns separate user identity, timeline and memory. Specialist models may be invoked as bounded domain tools, but the *operational truth*, authorization, responsibility graph and long-horizon goals remain shared.

## Universality requires capability honesty

The system must answer two questions before pretending to help:
1. Can Routin **understand and coordinate** this responsibility with available evidence and tools?
2. Can it **safely perform the requested substantive domain task** with validated knowledge, current consent, risk controls and relevant provider capability?

A general model can often assist with scheduling a checkup while lacking authority or qualifications to diagnose disease. It can reserve study time while needing educational evidence to assess mastery. It can prepare an application checklist while lacking a supported official submission connector. Different degrees of support are valid.

## Modes are human preferences, not authorization

- **Delegate:** user wants a verifiable outcome without doing every step.
- **Collaborate:** user and agent share planning and execution.
- **Learn/practice:** preserve effort necessary for competence, feedback and independent performance.
- **Support/coach:** help user pursue chosen wellbeing or routine goals without assuming a clinical role.
- **Observe/organize:** maintain information and proactively surface only the relevant changes.

A mode can vary by goal, person, project, task and time. A request to "handle appointments" does not authorize sending private health data to unrelated contacts.

## Whole-life coherence without universal rankings

A low-urgency personal-learning goal may deserve protected capacity even when it generates fewer notifications than work. A health follow-up can have a hard safety deadline but must not automatically authorize clinical treatment. Family obligations can be non-movable while some work tasks are negotiable.

The planner represents **commitment strength, constraints, consequences and user-declared priorities separately**. It may compare feasible alternatives but cannot impose a universal value ordering among family, career, rest, education and health.

## Architecture research contributions to investigate

A. Domain-composable responsibility and evidence state with *no cross-domain authority leakage*.
B. Context-adaptive initiative policy conditioned on domain-specific outcome, receptivity, risk, user support mode and actual source coverage.
C. Transfer of verified coordination procedures across domains only when their preconditions and evidence semantics match; prevent negative transfer from superficial similarity.
D. Longitudinal goal and resource stewardship across heterogeneous domains without converting all outcomes to task counts or engagement.
E. A reproducible cross-domain benchmark testing interference, unsafe action, false completion, retained goals and user intervention burden.

These are candidate research problems, not validated scientific novelties. Work by Nahum-Shani, Lin et al. (2026), Novari et al. (2026), Horvitz and other prior researchers already establishes substantial related art.

## Non-goals

No clinical diagnosis, emergency triage, treatment initiation, psychotherapy replacement, exercise clearance or high-risk financial decisions through a generic agent. Do not claim any domain is supported until its capability/evidence pack passes verification. No UI design in this phase. No universal optimization of "productivity" that treats a person's life as interchangeable tasks.

**Further reading:** [ontology](01-universal-ontology.md), [capability packs](02-domain-capability-contract.md), [cross-domain planning](04-cross-domain-decision-and-time.md), [safety](05-safety-and-boundaries.md).
