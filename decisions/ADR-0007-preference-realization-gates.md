# ADR-0007 — Preference memory requires independent realization checks

**Status:** adopted for research design; learning not yet implemented.

## Problem
A memory entry can be retrieved correctly yet applied in the wrong context, or the assistant can select the right preference but fail to follow it. MemPABench (2026) specifically tests these separable errors.

## Decision
Use: (A) validity-filtered retrieval; (B) scoped preference selection; (C) output/tool-plan behavior enforcement. Keep preferences separate from authorization. Record selection and realized behavior distinctly.

## Alternative
Prompt the LLM with all remembered preferences. Rejected due to scope conflicts, stale memory and absence of a behavioral correctness gate.

## Evaluation
Measure selection accuracy, context sensitivity, temporal change tracking, actual realization, unnecessary confirmations and incorrect autonomy. Compare no memory, flat RAG, file memory and structured scoped memory under identical baselines.