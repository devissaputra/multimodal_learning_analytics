import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from multimodal_learning_analytics import core


class CoreTests(unittest.TestCase):
    def test_fusion_counts_available_modalities(self):
        result = core.fuse_window([{"speech_ratio": 0.4, "clicks": 0}])
        self.assertEqual(result["clicks"], 0)
        self.assertEqual(result["modalities"], 2)

    def test_windowing(self):
        buckets = core.window_events([{"timestamp": 2}, {"timestamp": 31}], 30)
        self.assertEqual(set(buckets), {0, 1})

    def test_invalid_ratio_is_rejected(self):
        with self.assertRaises(ValueError):
            core.fuse_window([{"speech_ratio": 1.2}])


if __name__ == "__main__":
    unittest.main()
