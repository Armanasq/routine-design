# Conversational intelligence and voice architecture

**Status:** architecture proposal. No working voice backend claimed.  
**Primary documentation:** [OpenAI Voice Agents](https://developers.openai.com/api/docs/guides/voice-agents), [Realtime API](https://developers.openai.com/api/docs/guides/realtime), [LiveKit pipeline comparison](https://docs.livekit.io/agents/models/pipelines/), [LiveKit Agent Session](https://docs.livekit.io/agents/logic/sessions/).

## Product contract
Speech and text should execute the same domain commands against the same responsibility, memory, authorization and workflow state. No parallel speech-specific task database. Voice exists to reduce input effort, not to impose a conversational ritual. Always provide text access to essential operations.

## Architecture alternatives
- **Chained STT -> interpret/plan -> TTS:** explicit intermediate text, auditable tool arguments and easy component substitution; often more predictable for effectful personal-agent operations, at cost of latency/prosodic context. Start here for correctness.
- **Turn-based speech-to-speech:** low latency and natural prosody; separate the spoken conversation from the trusted backend action gate; track transcript reliability.
- **Full duplex speech-to-speech:** can listen while speaking; stronger interruption experience but complex turn finalization, side-effect cancellation and auditability. Introduce only after measuring benefit and reliability.

## Structured conversation events
`SpeechSegment {session_id, turn_id, sequence, speaker, text_candidate, confidence, start/end, finality, interrupted}`
`UserIntent {utterance_refs, speech_act: request|question|hypothesis|preference|correction|confirmation, target, scope, temporal_constraint, uncertainty}`
`CommandProposal {intent_id, state_version, domain_action, preconditions, unresolved_slots, authority_requirement}`.

The conversational model never issues direct provider writes. It can only create proposals validated by domain services. A `yes` is valid only if grounded in the exact active approval, time window, action identity and state version. Partial speech cannot authorize a side effect.

## Voice-specific failure cases
- **Barge-in before commitment:** cancel uncommitted proposal; user corrections supersede prior partial text.
- **Barge-in during real-world action:** do not pretend cancellation reverses external effects; report `submitted/unknown`, reconcile remotely.
- **ASR entity confusion:** verify recipients, amounts, times and scope before consequential actions; avoid auto-matching by names alone.
- **Bad end-of-turn detection:** delay interpretation until a sufficiently stable turn boundary; tolerate interruptions and repairs.
- **Unexpected network loss:** persist conversation state and in-flight workflow independently; surface accurate last-known outcome.
- **TTS says done too early:** user-visible completion language must be generated from verified execution state, not the original plan.
- **Privacy and retained audio:** set explicit storage/retention and consent controls per provider; avoid persisting raw recordings without need.

## Tests
Interrupted speech; revised intent within same turn; consent ambiguity; transcript divergence; wrong-recipient similarity; forced tool timeout; approval expiration; reply while speaking; text/voice handover; disconnected session; latency and task-success comparisons.

## Information hierarchy
Voice response levels: acknowledgement (no invented progress) -> one consequence -> decision request only if necessary -> longer explanation on demand. Do not read full Cartable by default.