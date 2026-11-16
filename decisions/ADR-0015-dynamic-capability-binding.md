# ADR-0015 — Capabilities Are Discovered, Never Invented Into Authority

**Status:** accepted design principle; production implementation pending.

Routin uses abstract capability requests to bridge unknown user goals to available tools. An abstract stub is only a search query and may name a nonexistent function. The trusted live registry binds real identifiers, version, type schema, user auth scope, risk policy, and observable outcome contract. No raw tool description or memory can grant permission. Discovery is adaptive, not static case-name routing.

Prior art: P071/P072. Alternatives: giant fixed tool list (context/cost and missing tools), plan-first alone (extra reasoning and hallucinated stubs), untrusted dynamic plugins (security). Test randomized tool renaming, missing tools, revoked scopes and large registries. Any ungrounded executable tool call fails.