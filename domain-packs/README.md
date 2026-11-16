# Routin domain capability packs

**All 11 manifests are DRAFT RESEARCH EXAMPLES, not active applications or safety-validated modules.** They do not register runtime tools or authorize external effects.

The common coordination engine owns the user's intentions, responsibility state, temporal memory and operation grants. A pack refines specialized evidence types, supported operations, safe fallback, intervention options, risk rules and outcome verifiers.

Pack directory:
- [core-coordination](./core-coordination/manifest.json) — Core coordination (fallback)
- [learning](./learning/manifest.json) — Study, learning and skill acquisition
- [fitness](./fitness/manifest.json) — Gym, training and physical activity
- [wellbeing](./wellbeing/manifest.json) — Wellbeing, recovery and routines
- [health-navigation](./health-navigation/manifest.json) — Health information and appointment coordination
- [work-projects](./work-projects/manifest.json) — Work, projects and deadlines
- [applications](./applications/manifest.json) — Academic, employment and program applications
- [communication](./communication/manifest.json) — Professional and personal communication
- [family-life](./family-life/manifest.json) — Family and shared personal logistics
- [travel-logistics](./travel-logistics/manifest.json) — Travel and personal logistics
- [finance-admin](./finance-admin/manifest.json) — Bills, claims and financial administration

## Non-negotiable constraints

No pack can modify its own authority; a support mode is not permission. Sensitive personal data is disclosed across packs only after explicit purpose-bound authorization, with minimization and auditable justification. A user cannot be forced into coaching or tutoring if they requested an administrative outcome. Specialist health and financial outcomes cannot be inferred from generic engagement or completion checks.

A new pack follows: draft -> source verification -> schema and policy validation -> adversarial simulation -> shadow evaluation -> limited consented pilot -> authorized activation. All manifests here remain `draft_research_only`.

## Concept

Pack manifests are **design contracts**, not executable code. Real deployment requires a typed capability resolver, safe runtime tool binding, source and license validation, domain-expert review where appropriate, and server-side verification. See [pack design](../docs/universal/02-domain-capability-contract.md), [universal architecture](../docs/universal/08-architecture-and-roadmap.md), [safety boundary](../docs/universal/05-safety-and-boundaries.md).
