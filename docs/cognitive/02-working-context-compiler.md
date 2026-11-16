# Decision-Aware Working Context Compiler

**Goal:** construct the minimum sufficient decision state under a bounded context budget without hiding a constraint that could change a consequential action.

## Why prompt concatenation fails

- Entire conversation histories are long, costly and contain obsolete instructions.
- Top-K semantic retrieval may surface similar but invalid memories while omitting less similar critical constraints.
- Compression can erase the ownership or dependency needed to determine whether a responsibility is finished.
- Model-supplied explanations cannot compensate for a missing permission check.

MemGPT supplies virtual-context/paging prior art; MAGE and AdaMEM show that state and strategy memory need active maintenance. This document proposes a *typed, decision-conditioned selection pipeline*, not a novel claim about tokenization.

## Contract: ContextCapsule

**Identity:** decision id, user account, goal/responsibility id, state version, timestamp, current actor, model/policy versions.

**Required information:** accepted obligations, current stage, unresolved question, next meaningful deadline, current permission and constraints, evidence source health, relevant interpersonal agreements.

**Optional retrieval:** recent episodes, related verified procedures, trusted relationship conventions, learned interaction preferences, domain-specific reference material.

**Excluded:** superseded versions as current rules; unrelated accounts; third-party prompt instructions; expired grants; irrelevant sensitive data; unverified summaries presented as facts.

**Output:** bounded working-state representation, selected strategy candidate, citations/evidence IDs, uncertainty and explicit missing-information reasons.

## Selection algorithm

Input: typed live state B, purpose D, eligible memory pool M, token budget K, policy version P.

1. Lock a consistent evidence and belief-state snapshot.
2. Include non-optional hard constraints, active grants and critical source-health diagnostics.
3. If mandatory state exceeds K, do not truncate constraints. Request a smaller, structured task decomposition or abstain and escalate.
4. Build eligible optional memory set by valid time, scope, access, evidence integrity and action relevance.
5. Score optional memories by estimated marginal effect on this decision (not generic similarity alone); include uncertainty in that estimate.
6. Select under K via bounded knapsack/greedy approximation with diversity across evidence, counterexamples and procedures.
7. Run **contradiction and sufficiency checks**. A small proof obligation must establish that the decision has owner, relevant intent, scope, time, authority and a verifier.
8. Generate an answer or action proposal. Validate actual output against selected preference/authority and source evidence. Return missing evidence to the information-acquisition policy.

Approximate utility for optional item i: expected decision-loss reduction conditional on current context minus token and retrieval/construction costs. At cold start use explicit filters/rules; do not invent calibrated probabilities.

## Refresh triggers

- New event modifies a critical obligation or confirmed deadline.
- Current strategy's precondition becomes false.
- External result contradicts the predicted effect.
- User corrects an entity, action or preference scope.
- Source reliability/permission changes.
- A previous subgoal finishes; its details can be compressed into a validated boundary summary.
- Model detects insufficient evidence and bounded alternative retrieval could improve the decision.

Do **not** refresh on every token, arbitrary clock tick or every new low-risk message.

## Example

The user requests "Move that call to later this week." Correct context must include the exact intended call, participants, confirmed commitments, protected personal goal time, and delegation grant. A semantically similar older call or an expired late-evening preference must not be added merely because its embedding score is higher.

## Tests

- Needle-in-haystack critical permission omitted by top-K vector retrieval.
- 50K-message history with current scoped preference and older contradictory preference.
- Context budget below mandatory facts triggers abstention rather than silent truncation.
- Lossy summary dropping recipient identity is rejected.
- An irrelevant memory containing tool-call instructions is filtered.
- Action generated with a correct preference but wrong behavior is blocked by post-generation validator.

Compare to full history, raw RAG, hierarchical summary, and typed-state-only baseline. Measure successful verified decisions, critical omissions, token use, refresh frequency and p95 latency.