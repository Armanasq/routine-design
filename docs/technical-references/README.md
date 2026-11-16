# Technical documentation and current specifications

Documentation is **engineering evidence**, not empirical proof of usefulness or scientific novelty.

- [OpenAI Voice Agents](https://developers.openai.com/api/docs/guides/voice-agents) — architecture selection among full-duplex, Realtime and chained STT/LLM/TTS.
- [OpenAI Realtime](https://developers.openai.com/api/docs/guides/realtime) — ephemeral session credentials, browser voice connection and realtime tool calls.
- [LiveKit voice pipeline comparison](https://docs.livekit.io/agents/models/pipelines/) — cascaded vs turn-based realtime vs full-duplex, including auditability and interruption trade-offs.
- [LiveKit Agent Sessions](https://docs.livekit.io/agents/logic/sessions/) — lifecycle and model pipeline control.
- [Gmail Push](https://developers.google.com/workspace/gmail/api/guides/push) — watch renewal, data loss cases, history synchronization.
- [Google Calendar Push](https://developers.google.com/workspace/calendar/api/guides/push) — channel expiry and notifications.
- [Google Calendar Quotas](https://developers.google.com/workspace/calendar/api/guides/quota) — stagger polling/jitter and quota limits.
- [Temporal Activities](https://docs.temporal.io/activity-definition) — retry/idempotency semantics.
- [OR-Tools Scheduling](https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md) — CP-SAT scheduling primitives.

Review and pin model/library versions at actual implementation time; do not commit speculative version requirements from documentation samples.