# ADR-0012 — One coordinator, versioned specialist competence contracts

**Status:** proposed for research architecture; no runtime integration implemented.

## Context

Users want to coordinate learning, fitness, wellbeing, health navigation, work, applications, family and other life responsibilities. Independent domain agent silos lose cross-domain capacity conflicts and fragment preferences. A single omnipotent LLM oversteps specialist competence and creates false universal completion semantics.

## Decision

Use one versioned shared intention/responsibility/goal/evidence state. Resolve specialized capability packs when a task needs domain knowledge, a specific intervention, outcome verifier or safety protocol. A pack's contract is declarative and cannot grant itself side-effect authority. All effectful plans are checked against current user permissions and provider capability at dispatch.

## Alternatives

One LLM for every domain (low modularity, unverifiable semantics); independent domain agents (state/consent fragmentation); hardcoded fixed list of domains (poor extensibility); unrestricted agent-generated plugins (tool security risk). Prefer capability compatibility with typed state and explicit coverage.

## Proof requirements

Cross-domain scenario evaluation, irrelevant sensitive data isolation, temporal validity, no accidental permission transfer, correct domain outcomes and measured benefit over simple event-ledger baseline.

## Source grounding

P059, P060, P061, P069 and P058. This combines substantial prior art; no novelty claimed.