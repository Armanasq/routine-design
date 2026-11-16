# Technical Backbone: Minimal Core, Replaceable Intelligence

**Status:** proposed production architecture; dependencies must be pinned/verified at actual implementation time.

## Design constraint

The core runtime must support hundreds of changing tools and long-running responsibilities without placing all tool schemas or user memories into every LLM request. It must learn from outcomes while keeping privileges, important state and external effects outside generative text.

## Recommended deployment topology

**Web/PWA or voice interface:** one fast task input and tiny attention directive. Business state lives server-side. PWA service worker does not guarantee 24/7 background monitoring.

**API/backend:** typed Python 3.13+ or TypeScript for coordination and validation; use FastAPI/Pydantic or equivalent with JSON Schema contracts when implementation is justified. Avoid framework-specific control flow in the domain model.

**Evidence/state:** PostgreSQL transactional tables for source observations, valid/recorded-time beliefs, goals, commitments, authority grants, capability registry, operation intent and outcome receipts; JSONB for evidence payloads; selective full text and pgvector if measured useful. Begin with relational joins + lexical search before adding graph DB or multiple embedding services.

**Events:** source-specific watches/webhooks with durable cursor, dedupe, retries, stale-state detection and periodic reconciliation. Do not assume all social platforms provide uniform APIs.

**Capability registry/gateway:** approved connectors expose stable typed operator descriptions and model-independent tool invocation. MCP 2026-07-28 is a current interoperability reference for tool list, schema, auth and cache semantics. Bound adapters by user accounts and operation grant; no raw arbitrary URL execution from model content.

**Planner:** hybrid constrained goals/operators plus LLM reasoning for novel decompositions, abstract capability demands and natural-language ambiguity. Deterministic validators check typed effects and consent. Use a bounded search for small exact plans; temporal/partial-observability and resource scheduling require more powerful solvers and causal models. Do not require an LLM to solve easy deterministic cases.

**Execution:** Temporal or another durable event-driven workflow engine, with side-effect activities, stable idempotency keys, provider reconciliation and verifiable terminal outcomes. Do not conflate workflow retry with exactly-once provider effects.

**Memory:** ephemeral working context compiler, operational current-state DB, episodic experience, scoped semantic beliefs, prospective commitments and certified procedural skills. Invalidation/revocation is synchronous for critical state; LLM consolidation is optional and asynchronous.

**Meta-controller:** budgeted routing for direct response, short research, extra reasoning, clarification, preparation, execution and abstention. Learning may adjust heuristics after offline/online validation but cannot modify hard permissions or safety policies.

**Observability:** versioned decision trace records alternative plans, retrieved memories, tool candidates, prompt/model, grants, source freshness, proposed/actual effects, correct/incorrect predictions and user/counterparty effort. Redact sensitive content and isolate accounts.

## Current relevant references

- MCP 2026-07-28 release: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- MCP tools spec: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/server/tools.mdx
- Temporal workflows: https://docs.temporal.io/workflows
- Temporal activity definition and idempotency: https://docs.temporal.io/activity-definition
- LangGraph architectural alternative: https://docs.langchain.com/oss/python/langgraph/overview
- Tool recommendation across 8K tools: https://arxiv.org/abs/2610.23707
- Plan-first versus retrieve-first tools: https://aclanthology.org/2026.emnlp-industry.19/

## Framework trade-off

LangGraph is useful for explicit state/graph control and human-in-loop, but it does not by itself solve consent, generalization or durable provider effects. Temporal focuses on durable workflow replay but does not provide a general AI planner. A combination may be appropriate; only use both if fault-injection experiments justify the operational complexity. A single coordinator with clear adapters is preferable to a swarm by default.

## Example service interfaces

- intent.parse(utterance, context) -> GoalContract candidates with missing questions
- world.snapshot(user, context_version) -> authorized source-backed state
- capabilities.discover(abstract_needs, registry_version, identity_scope) -> trusted candidate operators
- planner.propose(goal, world, operators, constraints, budget) -> PlanProposal + reasons, uncertainties and alternatives
- policy.check(plan_step, exact_grant, source_revision, target) -> allowed, approval_needed, blocked
- executor.start(authorized_step, idempotency_key) -> durable OperationHandle
- verifier.observe(handle, authoritative_source) -> verified, partial, unknown, failed
- learner.observe(episode, correction, outcomes) -> scoped evidence/update candidate, never a new grant

Interfaces are design contracts, not existing deployed APIs.

## Security

Never let a language model directly assemble unverified provider URLs, install arbitrary code or promote external text into policy. Isolate personal/work/clinical data by purpose. Expose read-only default capability and upgrade to writes only after explicit authority checks.

## Scaling approach

Start with one relational store and one durable worker queue. Scale provider ingestion and retrieval only after measuring actual rates. Context and tool-selection latency should be bounded by separate budgets. Do not add a graph database, vector store, separate agent per domain, persistent full-time inference loop or on-device trained model by default.

## Acceptance

System remains useful if source adapter is disconnected; never invent an action in a missing tool. A proposed state and a verified external outcome remain distinct. New tools are discovered without code changes in the planner; no user permission bypass occurs on tool updates. Multi-hour waits and failure recovery remain durable across process restart.