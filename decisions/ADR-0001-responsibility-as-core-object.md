# ADR-0001 — Responsibility is the root operational object

Status: accepted for architecture proposal (not implemented).

## Context
A single request can arrive as email, meeting, voice and document; each may revise a persistent obligation. A task-only model duplicates them and loses waiting and verification states. Secretarial ethnography emphasizes coordination and monitoring absent responses.

## Decision
Store source-backed `Responsibility` linked to evidence, parties, goals, actions, dependencies and expected outcomes. Tasks are optional derived actions. State evolves with evidence and authorization; no completion from an API acknowledgment alone.

## Alternatives
Tasks as primary (familiar, loses cross-channel identity); conversations as primary (unstructured); event-only design (difficult current-state queries). Use domain model with event lineage.

## Consequences and verification
More complex reconciliation and identity logic; supports expected non-events and outcome tracking. Prove via duplicate/miss benchmarks against task extraction. Sources: Erickson et al. 2008; distributed cognition Hollan et al. 2000.