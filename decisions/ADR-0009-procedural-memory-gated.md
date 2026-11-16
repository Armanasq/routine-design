# ADR-0009 — Reusable Experience Requires Verification and Permission

**Status:** proposed.

## Problem
Skill libraries and reflection exist in prior art, but a successful trajectory or plausible lesson may be unsafe to execute in a new real-world context.

## Decision
Procedural memory is a typed, versioned, preconditioned, testable plan. Experience can only create *candidates*; promotion requires source-backed outcomes, applicability boundaries, negative examples, failure-injection checks and a separate current authorization at runtime.

## Alternatives
Text-only advice (not reliable for execution), auto-generated code skills (unsafe with private user data and irreversible actions), static scripts (safe but limited generalization).

## Consequences / tests
Slower skill promotion but improved inspectability. Measure negative transfer, false completion, duplicate side effects, adaptation to changed providers and cost per verified responsibility. Grounding: ExpeL, Reflexion, Voyager, AdaMEM, MAGE, Sagas.