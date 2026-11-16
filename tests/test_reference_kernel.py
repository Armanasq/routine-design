import unittest
from datetime import datetime, timedelta, timezone

from reference_kernel.coordination import (
    Admission, Authorization, Claim, Clock, Commitment, ConnectorCoverage,
    EvidenceKind, Execution, Intervention, Preference, PreferenceOrigin,
    ProtectedInterval, admit_commitment, choose_intervention,
    current_preference, infer_missing_reply, learn_preference,
    may_dispatch, verify_completion,
)

NOW = datetime(2026, 11, 16, 12, 0, tzinfo=timezone.utc)


def claim(kind=EvidenceKind.CONFIRMED):
    return Claim("c1", kind, "email:1", 0.95, NOW)


def preference(value, origin, scope="global", from_offset=-10, to_offset=None):
    return Preference("meetings", value, scope, origin,
                      NOW + timedelta(days=from_offset),
                      NOW + timedelta(days=to_offset) if to_offset is not None else None,
                      NOW + timedelta(days=from_offset), "e1")


class DecisionKernelTests(unittest.TestCase):
    def test_explicit_preference_outweighs_observed_history(self):
        p = (preference("late", PreferenceOrigin.OBSERVED, from_offset=-1),
             preference("early", PreferenceOrigin.EXPLICIT))
        self.assertEqual(current_preference(p, "meetings", "work", NOW).value, "early")

    def test_scoped_exception_expires_without_overwriting_default(self):
        p = (preference("early", PreferenceOrigin.EXPLICIT),
             preference("late", PreferenceOrigin.EXPLICIT, "work", -2, -1))
        self.assertEqual(current_preference(p, "meetings", "work", NOW).value, "early")

    def test_active_scoped_explicit_preference_beats_global(self):
        p = (preference("early", PreferenceOrigin.EXPLICIT),
             preference("late", PreferenceOrigin.EXPLICIT, "work", -1, 1))
        self.assertEqual(current_preference(p, "meetings", "work", NOW).value, "late")

    def test_implicit_click_is_not_confirmed_preference(self):
        self.assertEqual(learn_preference(PreferenceOrigin.OBSERVED, True, False), "hypothesis_only")
        self.assertEqual(learn_preference(PreferenceOrigin.OBSERVED, False, False), "reject")

    def test_missing_reply_not_inferred_during_sync_gap(self):
        coverage = ConnectorCoverage("gmail", NOW, True, False, True)
        self.assertEqual(infer_missing_reply(NOW-timedelta(hours=1), coverage, NOW), "unknown_coverage")

    def test_missing_reply_not_inferred_if_stale(self):
        coverage = ConnectorCoverage("gmail", NOW-timedelta(minutes=6), False, False, True)
        self.assertEqual(infer_missing_reply(NOW-timedelta(hours=1), coverage, NOW), "unknown_coverage")

    def test_missing_reply_if_fresh_only_candidate(self):
        coverage = ConnectorCoverage("gmail", NOW, False, False, True)
        self.assertEqual(infer_missing_reply(NOW-timedelta(hours=1), coverage, NOW), "possibly_missing")

    def test_observed_reply_overrides_missing_hypothesis(self):
        coverage = ConnectorCoverage("gmail", NOW, False, False, True)
        self.assertEqual(infer_missing_reply(NOW-timedelta(hours=1), coverage, NOW, True), "reply_observed")

    def test_incomplete_scope_cannot_prove_missing(self):
        coverage = ConnectorCoverage("gmail", NOW, False, False, False)
        self.assertEqual(infer_missing_reply(NOW-timedelta(hours=1), coverage, NOW), "unknown_coverage")

    def test_proposed_obligation_can_be_simulated_but_not_accepted(self):
        pending = Commitment("m", claim(EvidenceKind.PROPOSAL), NOW+timedelta(hours=1), 30)
        result = admit_commitment(pending, (), 90, (), NOW, None)
        self.assertTrue(result.feasible)
        self.assertTrue(result.requires_acceptance)
        self.assertEqual(result.reason, "proposal_feasible_pending_consent")

    def test_conditional_commitment_requires_clarification(self):
        pending = Commitment("m", claim(EvidenceKind.CONDITIONAL), NOW+timedelta(hours=1), 30)
        self.assertEqual(admit_commitment(pending, (), 90, (), NOW, None).reason, "conditional_terms_unresolved")

    def test_confirmed_commitment_conflicting_with_protected_time_rejected(self):
        upcoming = Commitment("m", claim(), NOW+timedelta(hours=3), 45)
        protected = (ProtectedInterval("study", NOW+timedelta(hours=1), NOW+timedelta(hours=2), True),)
        interval = (NOW+timedelta(hours=1), NOW+timedelta(hours=1, minutes=45))
        decision = admit_commitment(upcoming, (), 120, protected, NOW, interval)
        self.assertEqual(decision.reason, "protected_goal_conflict")

    def test_insufficient_capacity_not_hidden_by_free_calendar(self):
        incoming = Commitment("m", claim(), NOW+timedelta(days=1), 45)
        existing = (Commitment("proposal", claim(), NOW+timedelta(days=1), 90),)
        self.assertEqual(admit_commitment(incoming, existing, 120, (), NOW, None).reason, "insufficient_capacity")

    def test_current_valid_grant_required(self):
        expired = Authorization("send", "alice@example.org", NOW-timedelta(seconds=1))
        self.assertFalse(may_dispatch("send", "alice@example.org", (expired,), NOW))
        valid = Authorization("send", "alice@example.org", NOW+timedelta(hours=1))
        self.assertTrue(may_dispatch("send", "alice@example.org", (valid,), NOW))
        self.assertFalse(may_dispatch("send", "bob@example.org", (valid,), NOW))

    def test_provider_ack_is_not_goal_completion(self):
        ack = Execution("ex", "send", "alice@example.org", "acknowledged", "provider:sent", None)
        self.assertFalse(verify_completion(ack))
        confirmed = Execution("ex", "send", "alice@example.org", "acknowledged", "provider:sent", "recipient:accepted")
        self.assertTrue(verify_completion(confirmed))

    def test_unknown_transport_outcome_not_complete(self):
        unknown = Execution("ex", "send", "alice@example.org", "unknown", None, None)
        self.assertFalse(verify_completion(unknown))

    def test_conditional_speech_does_not_execute(self):
        decision = choose_intervention(Clock(NOW, False, None), claim(EvidenceKind.CONDITIONAL), True, NOW)
        self.assertEqual(decision.action, Intervention.ASK)

    def test_focus_defers_until_breakpoint(self):
        decision = choose_intervention(Clock(NOW, True, NOW+timedelta(minutes=10)), claim(), True, NOW+timedelta(minutes=20))
        self.assertEqual(decision.action, Intervention.PREPARE)

    def test_critical_last_safe_moment_interrupts(self):
        decision = choose_intervention(Clock(NOW, True, NOW+timedelta(minutes=40)), claim(), True, NOW)
        self.assertEqual(decision.action, Intervention.INTERRUPT)

    def test_stale_source_rejects_risky_execution(self):
        grant = Authorization("send", "alice@example.org", NOW+timedelta(hours=1))
        decision = choose_intervention(Clock(NOW, False, None), claim(), True, NOW+timedelta(minutes=10), "send", "alice@example.org", (grant,), source_current=False)
        self.assertEqual(decision.action, Intervention.MONITOR)

    def test_external_effect_without_grant_requests_approval(self):
        decision = choose_intervention(Clock(NOW, False, None), claim(), True, NOW, "send", "alice@example.org")
        self.assertEqual(decision.action, Intervention.REQUEST_APPROVAL)

    def test_external_effect_with_grant_can_execute(self):
        grant = Authorization("send", "alice@example.org", NOW+timedelta(hours=1))
        decision = choose_intervention(Clock(NOW, False, None), claim(), True, NOW+timedelta(minutes=10), "send", "alice@example.org", (grant,))
        self.assertEqual(decision.action, Intervention.EXECUTE)

    def test_timezone_naive_rejected(self):
        with self.assertRaises(ValueError):
            current_preference((), "meetings", "work", datetime(2026,11,16,12,0))


if __name__ == "__main__":
    unittest.main()
