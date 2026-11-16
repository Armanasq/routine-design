from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Literal


class EvidenceKind(StrEnum):
    OBSERVATION = "observation"
    PROPOSAL = "proposal"
    CONDITIONAL = "conditional"
    CONFIRMED = "confirmed"


class PreferenceOrigin(StrEnum):
    OBSERVED = "observed"
    INFERRED = "inferred"
    CONFIRMED = "confirmed"
    EXPLICIT = "explicit"


class Intervention(StrEnum):
    MONITOR = "monitor"
    PREPARE = "prepare"
    SURFACE = "surface"
    INTERRUPT = "interrupt"
    ASK = "ask"
    REQUEST_APPROVAL = "request_approval"
    EXECUTE = "execute"


@dataclass(frozen=True)
class Claim:
    id: str
    kind: EvidenceKind
    evidence_id: str
    confidence: float
    valid_at: datetime


@dataclass(frozen=True)
class Preference:
    key: str
    value: str
    scope: str
    origin: PreferenceOrigin
    valid_from: datetime
    valid_until: datetime | None
    recorded_at: datetime
    evidence_id: str


@dataclass(frozen=True)
class Commitment:
    id: str
    source_claim: Claim
    due_at: datetime
    estimate_minutes: int
    outcome_evidence_id: str | None = None


@dataclass(frozen=True)
class ProtectedInterval:
    id: str
    start: datetime
    end: datetime
    declared_by_user: bool


@dataclass(frozen=True)
class ConnectorCoverage:
    provider: str
    observed_through: datetime | None
    gaps: bool
    revoked: bool
    scope_complete: bool


@dataclass(frozen=True)
class Authorization:
    operation: str
    target: str
    valid_until: datetime
    revoked: bool = False


@dataclass(frozen=True)
class Execution:
    id: str
    operation: str
    target: str
    transport_state: Literal["not_started", "acknowledged", "unknown"]
    provider_effect_evidence: str | None
    goal_outcome_evidence: str | None


@dataclass(frozen=True)
class Clock:
    now: datetime
    focus_active: bool
    focus_free_after: datetime | None


@dataclass(frozen=True)
class Admission:
    feasible: bool
    requires_acceptance: bool
    reason: str
    displaced: tuple[str, ...]


@dataclass(frozen=True)
class Decision:
    action: Intervention
    reason: str
    evidence_id: str | None


def _check_time(t: datetime) -> None:
    if t.tzinfo is None or t.utcoffset() is None:
        raise ValueError("timestamps must include timezone")


def current_preference(
    preferences: tuple[Preference, ...], key: str, scope: str, now: datetime
) -> Preference | None:
    _check_time(now)
    candidates = [
        p for p in preferences
        if p.key == key
        and p.scope in (scope, "global")
        and p.valid_from <= now
        and (p.valid_until is None or now < p.valid_until)
        and p.recorded_at <= now
    ]
    if not candidates:
        return None
    origin_rank = {
        PreferenceOrigin.EXPLICIT: 4,
        PreferenceOrigin.CONFIRMED: 3,
        PreferenceOrigin.INFERRED: 2,
        PreferenceOrigin.OBSERVED: 1,
    }
    return max(
        candidates,
        key=lambda p: (origin_rank[p.origin], int(p.scope == scope), p.valid_from, p.recorded_at),
    )


def learn_preference(
    origin: PreferenceOrigin,
    exposure_recorded: bool,
    user_confirmed: bool,
) -> Literal["accepted", "hypothesis_only", "reject"]:
    if origin == PreferenceOrigin.EXPLICIT and user_confirmed:
        return "accepted"
    if origin == PreferenceOrigin.CONFIRMED and user_confirmed:
        return "accepted"
    if origin in (PreferenceOrigin.INFERRED, PreferenceOrigin.OBSERVED):
        return "hypothesis_only" if exposure_recorded else "reject"
    return "reject"


def infer_missing_reply(
    expected_by: datetime, coverage: ConnectorCoverage, now: datetime,
    reply_observed: bool = False, max_sync_lag_minutes: int = 5,
) -> Literal["waiting", "possibly_missing", "unknown_coverage", "reply_observed"]:
    _check_time(expected_by)
    _check_time(now)
    if reply_observed:
        return "reply_observed"
    if coverage.revoked or coverage.gaps or not coverage.scope_complete or coverage.observed_through is None:
        return "unknown_coverage"
    _check_time(coverage.observed_through)
    if (now - coverage.observed_through).total_seconds() > max_sync_lag_minutes * 60:
        return "unknown_coverage"
    if now <= expected_by:
        return "waiting"
    return "possibly_missing"


def admit_commitment(
    proposed: Commitment,
    existing: tuple[Commitment, ...],
    available_minutes: int,
    protected: tuple[ProtectedInterval, ...],
    schedule_start: datetime,
    proposed_interval: tuple[datetime, datetime] | None,
) -> Admission:
    _check_time(schedule_start)
    if proposed.source_claim.kind == EvidenceKind.OBSERVATION:
        return Admission(False, False, "not_an_obligation", ())
    if proposed.source_claim.kind == EvidenceKind.CONDITIONAL:
        return Admission(False, True, "conditional_terms_unresolved", ())
    needs_acceptance = proposed.source_claim.kind == EvidenceKind.PROPOSAL
    if available_minutes < 0 or proposed.estimate_minutes < 0:
        raise ValueError("invalid capacity")
    for t in protected:
        if proposed_interval and t.declared_by_user:
            start, end = proposed_interval
            if start < t.end and t.start < end:
                return Admission(False, needs_acceptance, "protected_goal_conflict", (t.id,))
    remaining = available_minutes - sum(
        c.estimate_minutes for c in existing if c.due_at >= schedule_start
    )
    if proposed.estimate_minutes > remaining:
        return Admission(False, needs_acceptance, "insufficient_capacity", ())
    return Admission(True, needs_acceptance, "proposal_feasible_pending_consent" if needs_acceptance else "confirmed_feasible_under_point_estimates", ())


def may_dispatch(
    operation: str, target: str, grants: tuple[Authorization, ...], now: datetime
) -> bool:
    _check_time(now)
    return any(
        g.operation == operation
        and g.target == target
        and not g.revoked
        and g.valid_until > now
        for g in grants
    )


def verify_completion(execution: Execution) -> bool:
    return execution.transport_state == "acknowledged" and bool(
        execution.goal_outcome_evidence
    )


def choose_intervention(
    clock: Clock,
    claim: Claim,
    actionability: bool,
    latest_safe_time: datetime,
    external_operation: str | None = None,
    target: str | None = None,
    grants: tuple[Authorization, ...] = (),
    source_current: bool = True,
) -> Decision:
    _check_time(clock.now)
    _check_time(latest_safe_time)
    if not source_current:
        return Decision(Intervention.ASK if clock.now >= latest_safe_time else Intervention.MONITOR, "source_state_uncertain", claim.evidence_id)
    if claim.kind in (EvidenceKind.CONDITIONAL, EvidenceKind.PROPOSAL):
        return Decision(Intervention.ASK, "intent_not_confirmed", claim.evidence_id)
    if not actionability:
        return Decision(Intervention.MONITOR, "not_actionable", claim.evidence_id)
    if external_operation is not None:
        if claim.kind != EvidenceKind.CONFIRMED:
            return Decision(Intervention.ASK, "unconfirmed_external_intent", claim.evidence_id)
        if not target or not may_dispatch(external_operation, target, grants, clock.now):
            return Decision(Intervention.REQUEST_APPROVAL, "missing_current_grant", claim.evidence_id)
    if clock.focus_active and clock.now < latest_safe_time:
        if clock.focus_free_after is not None and clock.focus_free_after <= latest_safe_time:
            return Decision(Intervention.PREPARE, "wait_for_safe_breakpoint", claim.evidence_id)
    if external_operation is not None:
        return Decision(Intervention.EXECUTE, "authorized_time_sensitive_action", claim.evidence_id)
    if clock.now >= latest_safe_time:
        return Decision(Intervention.INTERRUPT, "last_safe_intervention", claim.evidence_id)
    return Decision(Intervention.SURFACE, "actionable_not_urgent", claim.evidence_id)
