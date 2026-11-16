# Memory Ontology, Lifecycle and Trust Boundaries

**Research:** Baddeley (2000); McClelland et al. (1995); MemGPT (2023); Generative Agents (2023); Mem0 (2025); A-MEM (2025); Memory-R1 (ACL 2026); Agent Memory (2026); MemPABench (2026).

## Distinguish the terms

The model's *context window* is not a durable memory database. It is a limited prompt budget for a particular inference. "Working memory" in Routin means a compact, versioned operational representation assembled for a decision; it is not a claim about the model's hidden activations. Short-term dialogue state and episodic execution state are different: a long workflow can survive many conversations.

## Storage classes and invariants

| Class | What it means | Typical retention | Primary operation | Trust rule |
|---|---|---|---|---|
| Source/evidence | Authorized provider facts and event versions | Governed by consent/retention | append, reconcile, revoke | provenance, source coverage and access are mandatory |
| Window/context | Tokens chosen for the next model inference | one inference | assemble, replace | never authoritative; generated summary is not evidence |
| Working state | Current unresolved decision, dependencies, time constraint, cursor | active decision until resolved | update/validate | reconstructible from source-backed state |
| Session state | Utterances, revisions, acknowledgements in ongoing interaction | session with bounded handoff | segment, resolve, expire | partial voice output cannot grant permission |
| Episodic | What happened, including outcomes and failed attempts | bounded historical policy | record, index, invalidate | distinguish observation from interpretation |
| Semantic | Stable scoped propositions and relational knowledge | until superseded or withdrawn | version, contradict, supersede | descriptive habits do not become user values |
| Prospective | Future intentions and expected external non-events | until resolved or expired | monitor, trigger, revise | a promise requires adequate grounding |
| Procedural | Validated reusable plans and recovery playbooks | versioned, revocable | shadow, certify, deploy, suspend | never synthesize executable authority from memory |
| Meta/self model | Forecast calibration, known failure modes, policy exposure, cost estimates | aggregate within consent | update, audit | cannot alter policy grants |

No "evergreen memory" is irrevocable; legitimate deletion/revocation propagates to derived stores.

## Four independent axes for memory items

Every memory item must preserve:
1. **Validity:** when the proposition was true or applicable in the world.
2. **Knowledge time:** when Routin learned or revised it.
3. **Scope:** user, person, project, channel, place, role and action type as appropriate.
4. **Epistemic status:** observed, inferred, explicitly stated, independently confirmed, superseded, disputed or unknown.

An inferred meeting preference can be strong within one project but invalid for the person's broader life. An old confirmed fact can be less appropriate than a new explicit instruction in the applicable context, but source conflicts must still be surfaced when consequential.

## Memory lifecycle

**Observe -> extract candidates -> validate type -> attach evidence and lineage -> route to working/episodic/state -> consolidate where justified -> retrieve under scope -> compare with outcomes -> maintain or invalidate -> forget in accordance with retention policies.**

Explicit write actions: ADD, UPDATE/SUPERSEDE, LINK, DEPRECATE, QUARANTINE, PURGE, NOOP. Memory-R1 studies learned ADD/UPDATE/DELETE/NOOP selection in QA benchmarks; that is prior art, not proof these operations are safe for an agent with external side effects.

## Consolidation: fast experiences, slow generalization

The complementary-learning-systems literature motivates keeping idiosyncratic experiences separate from gradually inferred structure. For Routin:
- New one-off events remain episodic rather than becoming standing rules.
- Repeated high-quality outcomes may support a proposed semantic or procedural hypothesis.
- A promoted belief retains references to original episodes and an evidence summary.
- Contradictory episodes cause uncertainty or contextual refinement, not automatic deletion of inconvenient evidence.
- Critical preferences and authorizations are not updated by frequency counts.

This is not biological replay or online parameter training; it is a provenance-aware software consolidation policy.

## Forgetting is conditional, not decay-by-age

Forget or remove data due to retention expiry, consent revocation, invalidation or obsolescence. Down-rank irrelevant episodes based on task-conditioned utility. Preserve source lineage for decisions requiring audit, consistent with retention rules. A negative outcome may be rare but essential for preventing a duplicate-send bug. Recency and similarity cannot capture that value alone.

## Retrieval priority order

(1) Required current operational state, (2) hard constraints and grants, (3) active goal/dependencies and source freshness, (4) scoped preferences, (5) relevant verified episodes and procedures, (6) optional context or background. Stage (5) may use hybrid BM25/vector/graph search; stages (1)–(4) must rely on typed filtering and current-state queries before approximate similarity.

## Limits

Layer names are conceptual and can share one PostgreSQL database. Avoid dedicated services or vector databases per layer. Do not assert that more layers imply better intelligence: baseline the complete system against an indexed event log plus a current-state table.