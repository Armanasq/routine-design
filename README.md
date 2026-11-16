# Routin — Evidence-Grounded Research and Systems Design

**Repository:** `Armanasq/routine-design`  
**Scope:** Routin, an adaptive, permission-bound, continuously learning personal AI secretary.  
**Research cutoff:** 2026-11-16. **Status:** design/research only; **no functional product or UI implementation is claimed**.

## The thesis
Routin continuously reconciles the user's authorized professional and personal context, maintains evidence-backed responsibilities, learns evolving intentions without equating behavior with desire, prevents avoidable overcommitment, protects scarce attention and user-chosen goals, delegates only within authority, and verifies external outcomes.

Its success metric is real-world administrative burden **avoided** without increasing missed commitments, user corrections, unauthorized actions or displaced personal growth.

## Recommended reading sequence
1. [Product thesis](docs/00-vision/product-thesis.md) and [non-goals](docs/00-vision/non-goals-and-threats.md).
2. [System topology](docs/architecture/system-context.md), [domain ontology](docs/architecture/domain-model.md) and [decision topology](docs/architecture/decision-topology.md).
3. [Temporal memory](docs/architecture/memory-and-learning.md), [capacity/admission](docs/algorithms/capacity-and-admission.md), [attention policy](docs/algorithms/attention-and-initiative.md), and [learning biases](docs/algorithms/learning-and-counterfactuals.md).
4. [Conversation/voice](docs/architecture/conversation-and-voice.md), [connectors](docs/architecture/integrations-and-sync.md), [consent](docs/architecture/security-consent-and-policy.md), [workflow execution](docs/workflows/execution-and-recovery.md).
5. [Paper reviews](literature-reviews/README.md), [cross-paper syntheses](literature-reviews/syntheses/), [technical docs](docs/technical-references/README.md) and [full previous analyses](research/historical/README.md).
6. [Hypotheses](research/hypotheses.md), [evaluation](research/evaluation.md), [research backlog](research/backlog.md) and [phased roadmap](research/roadmap.md).

## Corpus status
- **35 individually reviewed papers**, each with a dedicated review in `literature-reviews/<field>/Pxxx.md`.
- **35 source records** in `papers/<field>/Pxxx/SOURCE.md`; machine-readable [catalog](papers/catalog.json).
- **9 cross-paper syntheses** in `literature-reviews/syntheses/`.
- **12 evidence-linked mechanism specifications**, [knowledge graph](research/knowledge-map.json).
- Prior research and two historical graphs in [research/historical](research/historical/README.md).
- **Full-text PDFs/TeX in repository: 0.** Download from canonical links only after redistribution rights are verified. This environment did not support binary acquisition. See [source-acquisition policy](papers/acquisition.md) and [acquisition script](scripts/acquire_open_sources.py). Never call a link-only record a downloaded paper.
- Individual reviews are structured critical analyses based on available abstracts and/or scholarly extractions, not verified exhaustive full-text reads. More rigorous full-text critical reviews are a tracked research priority.

## Repository layout
```
docs/                 Product vision, ontology, topology, modules, algorithms, workflows
literature-reviews/   Individual paper assessments, cross-paper integrations
papers/              Canonical source records, catalog, lawful acquisition procedures
research/            Hypotheses, evaluations, historical analyses, evidence graph, backlog
decisions/           Architecture decision records
schemas/             Versioned JSON contracts
tests/scenarios/     Synthetic failure/adversarial event timelines
scripts/             Corpus and architecture consistency checks; rights-gated fetching
```

## Research integrity
Evidence classes: experiment/meta-analysis, ethnographic/conceptual, algorithm/benchmark, engineering docs, preprint. **Mechanisms derived for Routin are proposals; no product efficacy or research novelty is established.** Every accepted behavior requires a source claim, boundary assumptions, failure example, typed state transition and falsifiable comparison. Publicly hosted PDFs may still be copyrighted and unsuitable for rehosting.

## Validation
```bash
python scripts/verify_corpus.py
python scripts/validate_architecture.py
```

No GitHub Actions workflows were configured, to avoid unwanted CI charges. Changes to research data should pass these checks locally.

## Development principle
**Maximize verified backend usefulness, minimize required human attention.** Do not implement the UI before the decision policy and information output contract are stable. See [contribution guide](CONTRIBUTING.md).
