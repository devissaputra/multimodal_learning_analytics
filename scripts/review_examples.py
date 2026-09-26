"""Reproduce the labeled worked example; this is not an empirical study."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from multimodal_learning_analytics import core
outputs=core.fuse_window([dict(speech_ratio=.4,gaze_focus=.8,clicks=1),dict(speech_ratio=.6,gaze_focus=.7,clicks=2)])
result={'kind':'illustrative_calculation','note':'Two synthetic events; ratios averaged, clicks summed.','outputs':outputs}
(ROOT/'results/review_examples.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
