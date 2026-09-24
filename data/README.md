# Data Documentation

## Included data

`sample.csv` contains synthetic, already-derived features created only for smoke tests and demonstrations.

No raw audio, video, eye-tracking recordings, biometric media, or identifiable learner data are included.

## Expected schema

The current example uses:

- `learner`: learner identifier
- `session`: session identifier
- `timestamp`: non-negative event time
- `speech_ratio`: derived continuous feature in the range 0 to 1
- `gaze_focus`: derived continuous feature in the range 0 to 1
- `clicks`: non-negative observed click count

A missing modality should be represented as missing data, not as a fabricated zero. An observed click count of zero is valid and remains distinguishable from an unavailable click stream.

## Windowing rule

Use `window_events_by_entity` when a table contains multiple learners or sessions. The function groups by learner, session, and time window so observations from different people or sessions are not fused together.

`window_events` is intended only for data that have already been restricted to one learner-session sequence and rejects mixed identities.

## Production checks

Before real analysis, validate field types, missingness, timestamp semantics, clock synchronization, learner/session boundaries, modality provenance, and feature-extraction procedures.

## Do not commit

Do not commit personally identifiable information, raw student submissions, private LMS exports, proprietary course content, raw video/audio, eye-tracking recordings, or licensed datasets that prohibit redistribution. Keep sensitive material outside Git and reference it through approved secure storage.

## Dataset card requirement

For any real experiment, record source, license or consent basis, population, collection period, exclusions, preprocessing, missingness, synchronization method, known biases, feature provenance, and permitted uses.
