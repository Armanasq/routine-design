# S10 — Biological Memory Analogies vs Engineering Memory

**Evidence:** Baddeley P056 + McClelland et al. P057 + MemGPT P048 + Mem0 P054 + Agent Memory P047 + MemPABench P041.

## Derivation

Human working memory can bind information from different sources into a temporary episode; complementary-learning-systems theory models a distinction between rapid recording of specifics and slower extraction of shared structure. These concepts **do not specify** a storage database or prove equivalence between LLM prompts and the brain.

MemGPT contributes virtual context paging. Mem0 contributes dynamic factual memory consolidation. Agent Memory measures the construction/serving costs of these approaches. MemPABench finds that accurate retrieval may still fail at context-specific interaction behavior.

The combined practical conclusion: Routin needs a small *trusted current-state projection*, bounded *task-conditioned working capsule*, durable *episodic evidence*, slowly promoted *scoped beliefs*, and **an independent behavior-realization validator**. They may use a shared datastore; conceptually they have different trust and update contracts.

## Critical mechanism

Given a decision, retrieve active owner/outcome, current grant and confirmed deadlines before approximate semantic context. If any indispensable information is missing, abstain or acquire it. Retrieval of a user brevity preference is not enough: after generation, check whether the response actually obeyed it within the current domain.

New episodes do not immediately rewrite long-term aspirations. Periodic consolidation may propose a routine only when independent evidence supports that precise scope and the change would help future decisions.

## Distinguishing experiment

Hold token budgets and LLM fixed. Compare full chat, BM25, dense RAG, Mem0-style facts, temporal SQL + optional retrieval, and typed current-state+working-capsule+behavior validator. Measure authorization mistakes, stale preference selection, realized behavior, user corrections, time saved and full lifecycle cost.

## Non-transferable assumptions

Neural cognitive timescales are not Routin schedule defaults. BM25's superiority in some recall-focused benchmarks does not imply superior dynamic tool-state tracking. A successful benchmark memory item cannot automatically be promoted into a durable normative user preference.

## Output documents

[Memory ontology](../../docs/cognitive/01-memory-ontology-and-lifecycle.md), [context compiler](../../docs/cognitive/02-working-context-compiler.md), [evaluation](../../docs/cognitive/07-cognitive-research-evaluation.md).