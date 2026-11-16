# Research Method: Construct, Challenge, Validate and Revise

This repository follows an engineering-and-research construction discipline. A document or citation is not a contribution until it changes a testable system decision.

## A single research brick

1. **Problem:** define one failure using real-world consequences, not a vague feature.
2. **Evidence:** establish which population, task and method the cited study actually investigated.
3. **Mechanism:** identify the mechanism and assumptions that could transfer to an assistant.
4. **Connection:** trace effects on other subsystems; identify both beneficial and harmful feedback.
5. **Design decision:** name the entity, state transition, interface, constraint and alternative design.
6. **Counterexample:** construct a case where applying the mechanism would be wrong.
7. **Falsification:** establish the baseline, oracle, test population, and disqualifying failure.
8. **Implementation gate:** introduce only the smallest additional capability that passes validation.
9. **Reflection:** preserve rejected hypotheses, negative results and decision revisions.

## Decision records must answer
- What explicit user benefit does this decision aim to create?
- What assumptions could make it wrong?
- Which competing proposal was considered, and why rejected?
- How does it affect time, attention, goals, relationships, permissions and the future data Routin learns from?
- What missing evidence should cause abstention or explicit clarification?
- What does the system observe to verify success?
- How do we know it did not make a different part of the user's life worse?

## Knowledge hierarchy

Do not apply a naive data -> information -> knowledge -> wisdom automatic pipeline. Research on the DIKW model disputes its logical status. Our operational sequence is **evidence -> defeasible claim -> scoped current belief -> constrained practical judgment -> verified outcome -> calibrated revision**. Human values and authorization are explicit inputs, not extracted facts.

Wisdom, operationally, is choosing *when not to act*, when not to infer, when to renegotiate commitments, and when to preserve the human's capacity for judgment. That is a product philosophy and testable decision objective, not a metaphysical claim that the software possesses wisdom.

## Quality levels
L0 bibliographic identity verified; L1 abstract/summary checked; L2 sections and empirical results independently inspected; L3 full paper and supporting material critically reviewed; L4 claim reproduced or validated in an appropriate Routin setting. Do not silently relabel L1 as L3.

## Workflow gates
Each proposed mechanism links at least two source-specific conclusions, one actual typed state transition, one counterexample, one measurable baseline, one test and one revision path. No auto-merge from generated text into accepted scientific truth; no UI-first shortcuts.
