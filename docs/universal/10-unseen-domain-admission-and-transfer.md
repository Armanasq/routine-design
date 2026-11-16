# Unseen Domain Admission: How Routin Grows Without Becoming Unsafe

## Problem

A universal assistant must deal with intentions not anticipated by the developers: preparing a community event, volunteering, handling housing paperwork, organizing a family ceremony, maintaining an aquarium, managing lab equipment, participating in a creative project, or learning a sport.

Hardcoding an exhaustive list of life domains is impossible. But automatic creation of a fully privileged specialist agent is unsafe.

## Bounded generalization algorithm

**Recognize:** detect new intent, desired outcome, counterparties, timing, resources and whether the user wants completion or development. Preserve alternative interpretations.

**Decompose:** split the request into generic primitives (research, compare, prepare document, coordinate person, reserve time, monitor expected event) and any specialist substeps requiring domain knowledge.

**Discover:** resolve each primitive to an active validated capability; an absent domain pack is not automatically created from the internet.

**Classify risk and evidence:** identify private/sensitive data, external effects, financial/legal/physical/health consequences, and what source would be authoritative. Do not rely on an LLM numerical risk score without policy.

**Plan partial support:** generic low-risk actions may proceed within grants, while specialist uncertainty is surfaced as a narrow knowledge limitation, source research, professional referral or user-specified input.

**Test composition:** check that pack combinations do not leak data, override explicit goals, induce conflicting work or transport risk, or use inappropriate outcome verifiers.

**Request permission separately:** a new capability cannot infer authorization from previous behavior or from source documents.

**Verify and learn:** store a scoped successful episode and domain-specific questions for later pack development. Do not self-publish a newly synthesized executable pack.

## Example: new hobby

The user says "Help me organize a beekeeping course and purchase equipment."

Routin may maintain scheduling constraints, compare courses and organize a checklist from reliable sources. It must not infer expertise in live animal handling, use unverified safety instructions, or purchase equipment without an explicit operation-and-target grant. It can suggest consultation of qualified local resources for specialist issues and treat unresolved facts as unknown.

## Example: professional certification

The user wants a licensing examination and documentation. Routin handles prerequisites, materials and time coordination, but final eligibility must come from current official authority. Educational mode may provide practice if the user's goal is mastery; administrative mode may prepare submissions under explicit grants.

## Permission-/outcome-preserving skill transfer

Represent transfer compatibility as a typed vector:
(subject identity, outcome type, authorized action class, data sensitivity, source reliability, temporal assumptions, validation level, reversibility, error recovery).

A procedure transfers only when all mandatory dimensions are checked; unknown compatibility invokes shadow/simulated mode rather than actual execution. "Email a university professor" and "email a clinician" share transport mechanics but not necessarily context disclosure rules, risk and recipient permissions.

## Future proofing

Pack schemas and capability IDs are versioned; migrations must preserve temporal meaning and user consent. Provider capability changes can suspend a pack. A new research result can update domain evidence, but cannot silently change user values or grant high-risk autonomy.

## What would count as a research contribution

Demonstrate that domain-composition rules generalize to genuinely unseen task classes while maintaining safety and reducing administrative burden against strong baselines. Measure negative transfer, cost and actual outcomes. A configurable pack DSL alone is established prior art (e.g., adaptive-intervention frameworks).
