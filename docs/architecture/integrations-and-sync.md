# Integration reliability and evidence coverage

## Provider documents
- [Gmail Push API](https://developers.google.com/workspace/gmail/api/guides/push): watches must be renewed at least every 7 days; Pub/Sub notifications can be dropped/delayed; history.list and periodic resynchronization are required.
- [Calendar push](https://developers.google.com/workspace/calendar/api/guides/push): channels expire, require replacement, and notifications are not a 100% reliable event ledger.
- [Calendar quota strategies](https://developers.google.com/workspace/calendar/api/guides/quota): jitter and avoid synchronous full-account polling.

## Connector contract
`ConnectorCapability {provider, operations, scopes, rate_limits, sync_semantics, supported_identity, event_revisions, source_reliability}`.
`ConnectorHealth {account_id, last_successful_sync, gap_status, cursor, watch_expiry, auth_status, coverage_window}`.

Ingest only authorized scoped data. Maintain provider ids and revision; deduplicate deliveries; retain source event time, fetch time, time zone and content deletion indicators. Use event inbox/outbox with at-least-once semantics. Trigger periodic reconciliation even after seemingly successful webhooks.

**Evidence absence:** `no_message_found` is not evidence of `person_did_not_reply` unless source coverage overlaps the relevant time window, account scope is sufficient and the matching algorithm is credible.

## State transitions
`connected -> backfilling -> current -> degraded -> reconciling -> current`; `revoked` and `disabled` override all active processing. External action requires both service OAuth scope and independent user-granted operation authorization.

## Security boundary
A message may contain an instruction to the assistant; that instruction is third-party data and cannot alter system prompts or grant permissions. Tool calls are validated against explicit user authority, approved recipient/entity and resource scope. Source links used for retrieval must not be allowed to trigger arbitrary network calls.

## Verification plan
Replay out-of-order/duplicate events, expired watch, cursor invalidation, retention deletion, oauth revoke, provider rate limit, partial sync and cross-provider contradictory timezones. Test source freshness before pending-non-event detection.