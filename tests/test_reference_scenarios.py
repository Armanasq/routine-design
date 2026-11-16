import unittest
from datetime import datetime, timedelta, timezone

from reference_kernel.coordination import (
    Authorization, Claim, Clock, Commitment, ConnectorCoverage, EvidenceKind,
    Execution, Intervention, Preference, PreferenceOrigin, ProtectedInterval,
    admit_commitment, choose_intervention, current_preference,
    infer_missing_reply, learn_preference, verify_completion,
)

T = datetime(2026, 11, 16, 14, 0, tzinfo=timezone.utc)


class EndToEndScenarioTests(unittest.TestCase):
    def test_proposal_to_approved_send_to_verified_agreement(self):
        incoming = Claim("meeting", EvidenceKind.PROPOSAL, "email:100", 0.9, T)
        candidate = Commitment("meeting", incoming, T+timedelta(hours=6), 30)
        admission = admit_commitment(candidate, (), 90, (), T, None)
        self.assertTrue(admission.feasible)
        self.assertTrue(admission.requires_acceptance)
        initial = choose_intervention(Clock(T, False, None), incoming, True, T+timedelta(minutes=20))
        self.assertEqual(initial.action, Intervention.ASK)
        confirmed = Claim("meeting", EvidenceKind.CONFIRMED, "user:accepted", 1.0, T)
        no_grant = choose_intervention(Clock(T, False, None), confirmed, True, T+timedelta(minutes=20), "send", "recipient@example.org")
        self.assertEqual(no_grant.action, Intervention.REQUEST_APPROVAL)
        granted = Authorization("send", "recipient@example.org", T+timedelta(minutes=30))
        permitted = choose_intervention(Clock(T, False, None), confirmed, True, T+timedelta(minutes=20), "send", "recipient@example.org", (granted,))
        self.assertEqual(permitted.action, Intervention.EXECUTE)
        sent = Execution("send-1", "send", "recipient@example.org", "acknowledged", "provider:receipt", None)
        self.assertFalse(verify_completion(sent))
        agreed = Execution("send-1", "send", "recipient@example.org", "acknowledged", "provider:receipt", "reply:acceptance")
        self.assertTrue(verify_completion(agreed))

    def test_protected_goal_overrides_history_and_survives_outage(self):
        preference_history = (
            Preference("late_work", "yes", "global", PreferenceOrigin.OBSERVED, T-timedelta(days=60), None, T-timedelta(days=60), "calendar:history"),
            Preference("late_work", "no", "global", PreferenceOrigin.EXPLICIT, T-timedelta(days=2), None, T-timedelta(days=2), "user:instruction"),
        )
        self.assertEqual(current_preference(preference_history, "late_work", "work", T).value, "no")
        study = ProtectedInterval("robotics", T+timedelta(hours=2), T+timedelta(hours=3), True)
        incoming = Commitment("late_meeting", Claim("m2", EvidenceKind.PROPOSAL, "email:200", .9, T), T+timedelta(hours=6), 60)
        admission = admit_commitment(incoming, (), 180, (study,), T, (T+timedelta(hours=2), T+timedelta(hours=3)))
        self.assertFalse(admission.feasible)
        self.assertEqual(admission.reason, "protected_goal_conflict")
        self.assertFalse(admission.requires_acceptance is False)
        stale = ConnectorCoverage("gmail", T-timedelta(minutes=20), True, False, True)
        self.assertEqual(infer_missing_reply(T-timedelta(hours=1), stale, T), "unknown_coverage")
        decision = choose_intervention(Clock(T, True, T+timedelta(minutes=30)), Claim("m2", EvidenceKind.CONFIRMED, "user:accepted", 1, T), True, T+timedelta(minutes=40))
        self.assertEqual(decision.action, Intervention.PREPARE)

    def test_observed_attention_cannot_rewrite_chosen_goal(self):
        goal = Preference("growth_priority", "protected", "global", PreferenceOrigin.EXPLICIT, T-timedelta(days=3), None, T-timedelta(days=3), "user:goal")
        observed = Preference("growth_priority", "defer", "global", PreferenceOrigin.OBSERVED, T-timedelta(hours=2), None, T-timedelta(hours=2), "policy:work_only_display")
        self.assertEqual(learn_preference(PreferenceOrigin.OBSERVED, True, False), "hypothesis_only")
        selected = current_preference((goal, observed), "growth_priority", "work", T)
        self.assertEqual(selected.value, "protected")


if __name__ == "__main__":
    unittest.main()
