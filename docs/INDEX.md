# Research and Architecture Navigation

Follow an evidence-to-decision path rather than reading documents by filename.

## First principles
1. [Product thesis](00-vision/product-thesis.md) and [non-goals](00-vision/non-goals-and-threats.md).
2. [Epistemic/practical type system](formal/01-epistemic-and-practical-types.md), [intention theory](formal/02-partial-intentions-and-situated-plans.md).
3. [Human social coordination](formal/03-joint-coordination-and-grounding.md).
4. [Closed-loop decision policy](formal/05-closed-loop-decision-process.md) and [minimal information contract](formal/06-information-and-action-contract.md).

## Engineering modules
- [System context](architecture/system-context.md), [domain model](architecture/domain-model.md), [decision topology](architecture/decision-topology.md).
- [Integration and event freshness](architecture/integrations-and-sync.md), [memory](architecture/memory-and-learning.md), [preference realization](formal/04-policy-and-memory-realization.md).
- [Capacity admission](algorithms/capacity-and-admission.md) and [attention initiative](algorithms/attention-and-initiative.md).
- [Verified execution](workflows/execution-and-recovery.md), [authorization policy](architecture/security-consent-and-policy.md), [failure taxonomy](architecture/failure-handling.md).
- [Observability and evaluation](architecture/evaluation-and-observability.md).

## Traceability
- Paper-level evidence: [70 per-paper reviews](../literature-reviews/README.md).
- Mechanism-level reasoning: [19 cross-paper syntheses](../literature-reviews/syntheses/).
- Knowledge graph: [28 mechanisms](../research/knowledge-map.json) and [historical graph sources](../research/historical/).
- Architecture tradeoffs: [ADR-0001–0014](../decisions/).
- Adversarial proof examples: [synthetic scenarios](../tests/scenarios/), [reference unit and integration tests](../tests/).
- Research standards: [brick-by-brick method](../research/brick-by-brick-method.md), [quality audit](../research/quality-audit.md).
- Priority research gaps: [GitHub issues](https://github.com/Armanasq/routine-design/issues).

## Decision provenance rule
A proposed operation is not approved by a paper. A mechanism requires the source's actual result, transfer assumptions, a typed state transition, negative case, bounded decision rule, authority gate and measurable baseline. The user can override a preference or change a goal, but the model cannot infer permission from a habit.

## Implementation status
Research and architecture are partially specified and evolving. The Python reference kernel executes **deterministic examples only**. No user integration, LLM runtime, PWA interface or autonomous production workflow is implemented. Original paper full-text acquisition is incomplete.

## Cognitive and memory engineering

- [Cognitive research thesis](cognitive/00-research-thesis.md)
- [Memory hierarchy, temporal scope and retention](cognitive/01-memory-ontology-and-lifecycle.md)
- [Bounded working context compilation](cognitive/02-working-context-compiler.md)
- [Verified experience-to-procedure learning](cognitive/03-experience-to-procedure.md)
- [Strategy validity, meta-reasoning and selective repair](cognitive/04-metacognition-and-strategy-control.md)
- [Human agency and long-horizon personal growth](cognitive/05-agency-personal-growth.md)
- [Integrated end-to-end reasoning case](cognitive/06-end-to-end-case-and-failure-tree.md)
- [Ablations, falsification and evaluation](cognitive/07-cognitive-research-evaluation.md)
- [Candidate scientific contributions](../research/proposed-contributions-2026.md)
- [Cognitive source-to-contract traceability](../research/cognitive-traceability.json)

## Universal multi-domain personal secretary

- [Universal product thesis and limits](universal/00-vision-and-boundaries.md)
- [Universal ontology of intentions and outcomes](universal/01-universal-ontology.md)
- [Domain capability pack design](universal/02-domain-capability-contract.md)
- [Learning, coaching and adaptive intervention science](universal/03-intervention-modes-and-domain-learning.md)
- [Whole-life planning and cross-domain decision making](universal/04-cross-domain-decision-and-time.md)
- [Safety and privacy boundaries](universal/05-safety-and-boundaries.md)
- [Representative end-to-end scenarios](universal/06-domain-scenarios.md)
- [Contribution hypotheses and falsification](universal/07-research-and-evaluation.md)
- [Implementation roadmap and topology](universal/08-architecture-and-roadmap.md)
- [Gradual onboarding and earned autonomy](universal/09-adaptive-onboarding-and-earning-autonomy.md)
- [New and unseen domain admission](universal/10-unseen-domain-admission-and-transfer.md)
- [Draft pack examples](../domain-packs/README.md)
- [Evidence reference catalog](technical-references/universal-sources.md)
- [Cross-domain benchmark](../research/benchmarks/universal-cross-domain-evaluation.md)
- [16 synthetic scenario contracts](../tests/scenarios/universal/README.md)
