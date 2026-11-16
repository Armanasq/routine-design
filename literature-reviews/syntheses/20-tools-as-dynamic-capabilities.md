# S20 — Tool Discovery Is a Decision, Not a Static Prompt

**Linked research:** P071 (retrieve vs plan first), P072 (multi-tool retrieval gateway), P073 (planning with broken/extra tools), P080 (ReAct), P081 (SHOP2).

## What follows from evidence

The 2026 EMNLP industry study directly establishes a task-complexity-dependent tradeoff between retrieving tools from the user query and first generating abstract capability stubs. Multi-tool tasks benefit from decomposition in the reported ToolBench evaluation, whereas direct retrieval often wins on one-tool tasks; stubs may hallucinate nonexistent tool names. Tool Recommendation demonstrates a fixed discovery interface can mediate thousands of tools without placing all schemas in context, but retrieval metrics do not prove safe execution.

## New architectural connection

A user's goal should be expressed as a **desired world effect**, not an API name. Capability discovery is a budgeted search for trusted operators that can produce that effect under valid preconditions. The planner uses registry-grounded operators; abstract stubs never grant themselves executable status. The authorization service uses user grants and provider-specific schemas and must not rely on natural-language tool descriptions.

## Conflict

A tool that appears semantically correct may only prepare a document, while the user asked to submit it. Discovery recall alone is insufficient. Conversely, always generating a complex decomposition for a trivial call wastes tokens and time. The controller should be conditional, not universally complex.

## Discriminating experiment

Use randomly renamed tools, new provider versions and multi-domain goals. Compare direct tool retrieval, abstract decomposition, hybrid, and fixed 100-tool context under equal model/tool budgets. Report all-required-tool coverage, missing/unsupported effects, unsafe calls, provider verification and total cost. Source evidence is benchmark-specific; Routin benefit remains unproven.

**Engineering:** docs/backbone/02-dynamic-tool-discovery.md and reference_kernel/adaptive_planner.py.