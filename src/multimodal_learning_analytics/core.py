from collections import defaultdict


def window_events(events, window_seconds=30):
    """Bucket timestamped events into fixed width windows."""
    if window_seconds <= 0:
        raise ValueError("window_seconds must be positive")
    buckets = defaultdict(list)
    for event in events:
        if "timestamp" not in event or event["timestamp"] < 0:
            raise ValueError("each event must include a non-negative timestamp")
        bucket = int(event["timestamp"] // window_seconds)
        buckets[bucket].append(event)
    return dict(buckets)


def fuse_window(events):
    """Average available continuous signals and sum click events in one window."""
    if not events:
        return {"speech": 0.0, "gaze": 0.0, "clicks": 0.0, "modalities": 0}

    speech = [
        event.get("speech_ratio")
        for event in events
        if event.get("speech_ratio") is not None
    ]
    gaze = [
        event.get("gaze_focus")
        for event in events
        if event.get("gaze_focus") is not None
    ]
    click_values = [
        event.get("clicks", 0)
        for event in events
        if "clicks" in event and event.get("clicks") is not None
    ]
    if any(not 0.0 <= value <= 1.0 for value in speech):
        raise ValueError("speech_ratio values must be between 0 and 1")
    if any(not 0.0 <= value <= 1.0 for value in gaze):
        raise ValueError("gaze_focus values must be between 0 and 1")
    if any(value < 0 for value in click_values):
        raise ValueError("click counts must be non-negative")

    return {
        "speech": sum(speech) / len(speech) if speech else 0.0,
        "gaze": sum(gaze) / len(gaze) if gaze else 0.0,
        "clicks": sum(click_values),
        "modalities": int(bool(speech)) + int(bool(gaze)) + int(bool(click_values)),
    }
