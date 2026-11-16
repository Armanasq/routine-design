# ADR-0014 — User intent selects assistance mode; policy selects permissible actions

**Status:** proposed.

## Problem

Automatically performing a task can conflict with the user trying to develop the ability to perform it. Providing repeated coaching when the person simply wants a completed administrative action is also harmful. In high-risk contexts, a learned preference cannot expand action authority.

## Decision

Support delegation, collaboration, learning/practice, support/coaching and observation modes, scoped to each intention and context. Modes change interaction and outcome semantics, not permissions. Use JITAI-style NOOP and receptivity rules for proactive interventions. Require independent grants for provider writes and preserve user override.

## Gate

Same wording across education and administrative contexts; user changes mode mid-task; temporary exception; late-evening observations vs explicitly protected evenings; coaching prompt delivered during important focus; clinical information requested beyond competence.

## Evidence

P061, P062, P063, P065, P067, P068, P041.