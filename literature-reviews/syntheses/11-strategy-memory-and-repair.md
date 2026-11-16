# S11 — What Agents Must Remember About How They Are Acting

**Research connection:** AdaMEM P045 + MAGE P046 + Reflexion P050 + ExpeL P051 + Sagas P027.

## What each study contributes

AdaMEM: dynamically generate useful strategy memory at the current step from past trajectories; its low-refresh version can become inertial and fail.

MAGE: track an active hierarchical execution path, compress verified subgoals and revise failed branches while preserving unaffected work.

Reflexion: use language reflections from feedback to improve subsequent decisions; introspection must not be confused with an external truth oracle.

ExpeL: abstract prior task experience to reusable advice; transfer can fail in new domains.

Sagas: long-running workflows require compensation or repair-forward; logical revision does not undo real external effects.

## Derived policy

Maintain (1) verified execution path, (2) ephemeral strategy for the *current* state, (3) prior successful and failed episodes, (4) exact granted external effects. After a material state change, validate the strategy's premises. On mismatch, preserve only verified unaffected subgoals, quarantine the failed branch, refresh strategy from relevant episodes, and recheck tool authority.

A fail-to-send timeout must trigger read-after-write provider reconciliation, not "backtrack and send again." A user goal changes at the planning level; existing confirmed agreements are not silently undone.

## Contradiction

Aggressively refreshing every step can improve adaptation but spend much more compute. Rare refresh can produce strategy inertia. A deterministic threshold can be too brittle for new environments. The policy needs safety triggers plus a measured value-of-computation gate.

## Falsification

Stale strategy scenario with changed recipient and revoked permission; long social workflow with one broken middle dependency; injected incorrect reflection. Compare no memory, static strategy, always-refresh, model-self-refresh and independent evidence-trigger refresh.

Outcomes: verified completion, duplicate sends, permission violations, time-to-recovery, token cost and unaffected progress retained.