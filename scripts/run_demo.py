import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from multimodal_learning_analytics.core import window_events, fuse_window

events=[{'timestamp':2,'speech_ratio':.4,'gaze_focus':.8,'clicks':2},{'timestamp':10,'speech_ratio':.6,'gaze_focus':.7,'clicks':1}]
summary=fuse_window(window_events(events)[0])
for key,value in summary.items():
    print(f"{key.replace('_',' ').title()}: {value}")
