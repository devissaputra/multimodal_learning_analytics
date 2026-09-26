# Calculation reading guide: ../CALCULATIONS.md (repository root).
# Window index = floor(timestamp/window width); speech/gaze = observed means; clicks = sum.
# Missing modalities remain None, not zero. Alignment does not establish that speech or gaze measures attention or learning. Clock origin, units and measurement quality must be consistent before fusion.

from collections import defaultdict
from numbers import Real


def _validate_timestamp(event):
    if "timestamp" not in event:
        raise ValueError("each event must include a timestamp")
    timestamp = event["timestamp"]
    if not isinstance(timestamp, Real) or isinstance(timestamp, bool) or timestamp < 0:
        raise ValueError("timestamps must be non-negative numbers")
    return timestamp


def _validate_single_entity(events, key):
    present = [key in event and event[key] is not None for event in events]
    if any(present) and not all(present):
        raise ValueError(f"all events must include {key} when any event does")
    if all(present) and len({event[key] for event in events}) > 1:
        raise ValueError(f"window_events received multiple {key} values")


def window_events(events, window_seconds=30):
    """Bucket one learner-session sequence into fixed-width time windows."""
    if not isinstance(window_seconds, Real) or isinstance(window_seconds, bool):
        raise ValueError("window_seconds must be a positive number")
    if window_seconds <= 0:
        raise ValueError("window_seconds must be positive")

    events = list(events)
    _validate_single_entity(events, "learner")
    _validate_single_entity(events, "session")

    buckets = defaultdict(list)
    for event in events:
        timestamp = _validate_timestamp(event)
        bucket = int(timestamp // window_seconds)
        buckets[bucket].append(event)
    return dict(buckets)


def window_events_by_entity(events, window_seconds=30):
    """Bucket events by learner, session, and fixed-width time window."""
    if not isinstance(window_seconds, Real) or isinstance(window_seconds, bool):
        raise ValueError("window_seconds must be a positive number")
    if window_seconds <= 0:
        raise ValueError("window_seconds must be positive")

    buckets = defaultdict(list)
    for event in events:
        if event.get("learner") is None or event.get("session") is None:
            raise ValueError("each event must include learner and session")
        timestamp = _validate_timestamp(event)
        bucket = int(timestamp // window_seconds)
        key = (event["learner"], event["session"], bucket)
        buckets[key].append(event)
    return dict(buckets)


def _numeric_values(events, field):
    values = [
        event[field]
        for event in events
        if field in event and event[field] is not None
    ]
    if any(not isinstance(value, Real) or isinstance(value, bool) for value in values):
        raise ValueError(f"{field} values must be numeric")
    return values


def fuse_window(events):
    """Fuse available speech, gaze, and click features while preserving missingness."""
    events = list(events)

    speech = _numeric_values(events, "speech_ratio")
    gaze = _numeric_values(events, "gaze_focus")
    click_values = _numeric_values(events, "clicks")

    if any(not 0.0 <= value <= 1.0 for value in speech):
        raise ValueError("speech_ratio values must be between 0 and 1")
    if any(not 0.0 <= value <= 1.0 for value in gaze):
        raise ValueError("gaze_focus values must be between 0 and 1")
    if any(value < 0 for value in click_values):
        raise ValueError("click counts must be non-negative")

    speech_observed = bool(speech)
    gaze_observed = bool(gaze)
    clicks_observed = bool(click_values)

    return {
        "speech": sum(speech) / len(speech) if speech_observed else None,
        "gaze": sum(gaze) / len(gaze) if gaze_observed else None,
        "clicks": sum(click_values) if clicks_observed else None,
        "speech_observed": speech_observed,
        "gaze_observed": gaze_observed,
        "clicks_observed": clicks_observed,
        "modalities": sum((speech_observed, gaze_observed, clicks_observed)),
    }
