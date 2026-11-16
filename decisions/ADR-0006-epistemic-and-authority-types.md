# ADR-0006 — Separate evidence, intentions, permissions and outcomes

**Status:** architecture accepted for prototype; production validation pending.

## Problem
Generic LLM task systems often treat source statements as ground truth, user interest as commitment and plausible output as proof of success. More reasoning does not fix a category error.

## Decision
Introduce an epistemic type system and immutable-by-default decision trace. Enforce that observations require interpretation, social commitments require accepted grounding, side effects require current grants, and terminal outcomes require independent postcondition evidence.

## Rejected alternative
A single untyped LLM memory vector with confidence score. This cannot prove scope, authority or external effect and risks stale instructions from third-party sources.

## Costs
Additional entity reconciliation, state versions, provenance and audit storage. These are core requirements for a secretary that acts in the world.

## Falsification
Compare false promoted commitments, unauthorized external actions and premature verified completion against direct LLM automation. Supporting research: P037, P039, P040, P041, P044.