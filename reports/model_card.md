# Analytic system card

## System

Multimodal Learning Analytics

## Purpose

Transparent windowed fusion for timestamped speech, gaze, and click features with explicit missing-modality handling and learner/session separation.

## Current maturity

Working research prototype. The bundled example checks the software path with synthetic inputs. It does not establish validity for real learners, instructors, courses, or workplaces.

## Inputs

The current code expects already-derived event-level features. It does not process raw audio, video, or eye-tracking recordings. See `../data/README.md` for the synthetic schema and documentation expected before real data are connected.

## Outputs

For each fused window, the code can produce available speech and gaze averages, click totals, modality-specific observed flags, and the number of observed modalities. Missing modalities are returned as `None`, so absence is not silently converted to zero.

## Entity handling

`window_events_by_entity` groups observations by learner, session, and time window. The lower-level `window_events` function rejects mixed learners or sessions when identity fields are present.

## Evidence needed before real use

Compare fused features with unimodal baselines under the same windows and outcome definition. Report missingness, synchronization error, feature provenance, robustness to dropped modalities, and whether the fused representation adds useful information.

## Main limitation

Speech, gaze, and click features are behavioral signals, not direct measures of attention, understanding, emotion, or ability. The current code performs transparent feature aggregation only.

## Human oversight

A person must review any output before it can affect a learner, instructor, applicant, or employee.
