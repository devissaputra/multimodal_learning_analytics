import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from multimodal_learning_analytics import core


class CoreTests(unittest.TestCase):
    def test_all_modalities_are_fused(self):
        events = [
            {"speech_ratio": 0.4, "gaze_focus": 0.8, "clicks": 2},
            {"speech_ratio": 0.6, "gaze_focus": 0.7, "clicks": 1},
        ]
        result = core.fuse_window(events)
        self.assertAlmostEqual(result["speech"], 0.5)
        self.assertAlmostEqual(result["gaze"], 0.75)
        self.assertEqual(result["clicks"], 3)
        self.assertEqual(result["modalities"], 3)

    def test_observed_zero_clicks_are_not_missing(self):
        result = core.fuse_window([{"speech_ratio": 0.4, "clicks": 0}])
        self.assertEqual(result["clicks"], 0)
        self.assertTrue(result["clicks_observed"])
        self.assertEqual(result["modalities"], 2)

    def test_missing_modalities_are_explicit(self):
        result = core.fuse_window([{"speech_ratio": 0.4}])
        self.assertEqual(result["speech"], 0.4)
        self.assertIsNone(result["gaze"])
        self.assertIsNone(result["clicks"])
        self.assertTrue(result["speech_observed"])
        self.assertFalse(result["gaze_observed"])
        self.assertFalse(result["clicks_observed"])
        self.assertEqual(result["modalities"], 1)

    def test_empty_window_is_all_missing(self):
        result = core.fuse_window([])
        self.assertIsNone(result["speech"])
        self.assertIsNone(result["gaze"])
        self.assertIsNone(result["clicks"])
        self.assertEqual(result["modalities"], 0)

    def test_windowing_respects_boundaries(self):
        buckets = core.window_events(
            [{"timestamp": 0}, {"timestamp": 29.999}, {"timestamp": 30}],
            30,
        )
        self.assertEqual(len(buckets[0]), 2)
        self.assertEqual(len(buckets[1]), 1)

    def test_windowing_rejects_mixed_learners(self):
        events = [
            {"learner": "L01", "timestamp": 2},
            {"learner": "L02", "timestamp": 3},
        ]
        with self.assertRaises(ValueError):
            core.window_events(events)

    def test_windowing_rejects_mixed_sessions(self):
        events = [
            {"learner": "L01", "session": "S01", "timestamp": 2},
            {"learner": "L01", "session": "S02", "timestamp": 3},
        ]
        with self.assertRaises(ValueError):
            core.window_events(events)

    def test_entity_windowing_keeps_learners_and_sessions_separate(self):
        events = [
            {"learner": "L01", "session": "S01", "timestamp": 2},
            {"learner": "L02", "session": "S01", "timestamp": 2},
            {"learner": "L01", "session": "S02", "timestamp": 31},
        ]
        buckets = core.window_events_by_entity(events, 30)
        self.assertEqual(
            set(buckets),
            {("L01", "S01", 0), ("L02", "S01", 0), ("L01", "S02", 1)},
        )

    def test_entity_windowing_requires_identity_fields(self):
        with self.assertRaises(ValueError):
            core.window_events_by_entity([{"learner": "L01", "timestamp": 2}])

    def test_invalid_ratios_are_rejected(self):
        with self.assertRaises(ValueError):
            core.fuse_window([{"speech_ratio": 1.2}])
        with self.assertRaises(ValueError):
            core.fuse_window([{"gaze_focus": -0.1}])

    def test_negative_clicks_are_rejected(self):
        with self.assertRaises(ValueError):
            core.fuse_window([{"clicks": -1}])

    def test_non_numeric_features_are_rejected(self):
        with self.assertRaises(ValueError):
            core.fuse_window([{"speech_ratio": "high"}])

    def test_invalid_timestamps_are_rejected(self):
        with self.assertRaises(ValueError):
            core.window_events([{"timestamp": -1}])
        with self.assertRaises(ValueError):
            core.window_events([{}])

    def test_invalid_window_size_is_rejected(self):
        with self.assertRaises(ValueError):
            core.window_events([{"timestamp": 1}], 0)
        with self.assertRaises(ValueError):
            core.window_events([{"timestamp": 1}], -5)


if __name__ == "__main__":
    unittest.main()
