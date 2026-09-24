import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from multimodal_learning_analytics.core import fuse_window, window_events_by_entity


events = [
    {
        "learner": "L01",
        "session": "S01",
        "timestamp": 2,
        "speech_ratio": 0.4,
        "gaze_focus": 0.8,
        "clicks": 2,
    },
    {
        "learner": "L01",
        "session": "S01",
        "timestamp": 10,
        "speech_ratio": 0.6,
        "gaze_focus": 0.7,
        "clicks": 1,
    },
]

window_key, window = next(iter(window_events_by_entity(events).items()))
summary = fuse_window(window)

print(f"Window: {window_key}")
for key, value in summary.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
