# Dynamic Tool Discovery and Grounded Capability Binding

## Research evidence

Apple's October 2026 EMNLP industry paper, "Plan or Retrieve First? A Scale Study of Tool Discovery Architectures", compares query-based Retrieve-then-Plan (RtP) with generating abstract function signatures before retrieval (Plan-then-Retrieve, PtR). Across ToolBench subsets involving 46,984 API endpoints, RtP is stronger on simpler single-tool requests; PtR is stronger for multi-tool requests. The abstract-stub method can hallucinate function names, and its extra inference has a cost. Source: https://aclanthology.org/2026.emnlp-industry.19/ .

Arcade's October 2026 "Tool Recommendation for Multi-Step Agents" studies a deployment with approximately 8,200 tools, far beyond practical all-tools-in-prompt context. The proposed gateway discovers tools on demand and enforces user credentials and agent consent; reported recommendation coverage and token savings are specific to their evaluation. Source: https://arxiv.org/abs/2610.23707 .

These are substantial prior art. Routin should not claim dynamic tool discovery as a new invention.

## Proposed hybrid discovery policy

1. Normalize the user-end to goal predicates and resource/authority requirements.
2. Check mandatory capability requirements against the live authorized registry, without model reasoning where exact matching suffices.
3. For simple, specific needs, use direct lexical/embedding retrieval against operator descriptions and schema.
4. When a request spans multiple effects or direct retrieval has low coverage, generate **abstract capability stubs** for missing effects and retrieve candidates for each.
5. Never execute a hallucinated stub: only names resolved to trusted versioned registry entries can be selected.
6. Rank candidate sets by complete effect coverage, precondition satisfiability, permissions, risk, predicted downstream usefulness and cost.
7. Reject irreconcilable tool semantics; an operator called "book" that only drafts a reservation cannot satisfy "provider booking confirmed".
8. If no compatible operator exists, find a supported partial goal, request a new authorized integration, suggest a manual step or abstain.
9. Refresh the registry when provider capabilities change, but do not use tool discovery to bypass consent.

The complexity switch is a **proposal**. It must be calibrated on realistic multi-step personal tasks, with comparisons to always-RtP and always-PtR. No universal threshold is claimed.

## Registry lifecycle

CONNECTING -> DISCOVERED -> SCHEMA_VERIFIED -> OPERATION_CLASSIFIED -> POLICY_APPROVED -> AVAILABLE -> DEGRADED -> REVOKED / REMOVED.

Discovery may be asynchronous; operations may vanish or become unauthorized between plan proposal and dispatch. Cache with explicit TTL, account and permission scope, cache provenance and registry revision. Rebind the proposed abstract operation if the provider changes; never blindly call a stale tool ID.

## Current MCP technical assumptions

The publicly released MCP 2026-07-28 spec uses a stateless core with optional server discovery, self-described requests, cacheable tool lists and tool-list-change notifications in supported configurations. For each tool, obtain schema metadata and use a separate authoritative user grant; tool descriptions and annotations can be untrusted. Reference: https://blog.modelcontextprotocol.io/posts/2026-07-28/ and https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/server/tools.mdx .

Adapter rules should be protocol-version aware; do not hardcode obsolete initialization/session expectations when implementing the 2026-07-28 MCP version. Neither tool discovery nor model recommendation is sufficient approval for an effectful call.

## Real failure cases

- Catalog contains 5,000 tools but the prompt describes only 100; missing one required tool makes the plan fail.
- The model invents a plausible abstract function; registry finds none.
- Tool name is unchanged but provider semantics or permissions changed.
- Semantically similar "submit" operation actually stores a draft.
- A health-domain tool carries sensitive data into a generic work context.
- A new connector offers a dangerous external write with an untrusted schema.
- Previously authorized tool is revoked while a workflow is waiting.
- Retrying an operation on an unknown remote state causes a duplicate charge.

## Experiment

Create paired tests of one-step and multi-step unknown-domain tasks. Randomize operator names while preserving typed effects, add distractor tools, remove required capabilities and vary grants. Measure all-required-tool recall, plan feasibility, incorrect tool selection, unsupported invented calls, permission errors, end-to-end verified success, p95 delay, token and gateway cost.

## Recommendation

Tool discovery is a separate service with a stable interface, not a giant prompt. Its output is a set of verified *candidate* capabilities; the planner and authorization service remain independent.