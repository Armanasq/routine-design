# ADR-0011 — Strategy Refresh Has Independent Environmental Triggers

**Status:** proposed.

## Problem
Model self-judgment can rationalize persistent failures and keep obsolete plans (AdaMEM strategy inertia). Long-horizon agents can retain correct parts of a workflow even when a mid-step dependency breaks (MAGE).

## Decision
Run typed validity checks for source freshness, grants, preconditions, progress, provider effects and expected postconditions. On failure identify the earliest invalid subgoal, quarantine dependent working state, preserve verified unaffected effects, and revise locally. Real-world operations require explicit reconciliation/compensation; rolling back an agent branch is not external undo.

## Alternatives
Always refresh (cost), never refresh (stale), model self-refresh only (inertia), full task restart (duplicate effects and churn).

## Tests
Stale strategy, changed counterpart, partial provider success, no-progress loops, irreversible email dispatch, excessive reasoning cost and changed user intention.