# Calculation guide

## Question and evidence

How can asynchronous modalities be aligned without mixing learners?

Synthetic timestamped speech, gaze and click events with learner/session identifiers.

**Status:** SYNTHETIC / RULE-BASED PROTOTYPE | no educational validity claim.

## Design

Bucket by learner, session and time; aggregate observed fields; preserve modality missingness.

## Calculation and interpretation

`Window index = floor(timestamp/window width); speech/gaze = observed means; clicks = sum.`

Missing modalities remain None, not zero. Alignment does not establish that speech or gaze measures attention or learning. Clock origin, units and measurement quality must be consistent before fusion.

## Evidence table

Worked example — illustrative, not a measured research result. Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| speech | 0.5 | unitless | `outputs.speech` |
| gaze | 0.75 | unitless | `outputs.gaze` |
| clicks | 3 | unitless | `outputs.clicks` |
| speech_observed | True | unitless | `outputs.speech_observed` |
| gaze_observed | True | unitless | `outputs.gaze_observed` |
| clicks_observed | True | unitless | `outputs.clicks_observed` |

Source: [results/review_examples.json](results/review_examples.json). Values resolve directly from this file when figures are regenerated.

This event-alignment prototype groups multimodal observations by learner, session, and fixed time window before summarizing available speech, gaze, and click fields. Missing modalities remain explicit, and the API prevents accidental mixing of identified learner sessions. The result is a testable data-processing baseline, not an inference engine for attention, emotion, or learning.

## Verification performed in this review

14 existing unittest checks passed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

For the explicitly illustrative example:

```bash
python scripts/review_examples.py
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`window_events`](src/multimodal_learning_analytics/core.py#L26) | Bucket one learner-session sequence into fixed-width time windows. |
| [`window_events_by_entity`](src/multimodal_learning_analytics/core.py#L45) | Bucket events by learner, session, and fixed-width time window. |
| [`fuse_window`](src/multimodal_learning_analytics/core.py#L74) | Fuse available speech, gaze, and click features while preserving missingness. |

## What remains before a stronger research claim

Missing modalities remain None, not zero. Alignment does not establish that speech or gaze measures attention or learning. Clock origin, units and measurement quality must be consistent before fusion. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.
