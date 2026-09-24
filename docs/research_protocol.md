# Research protocol

## Project

Multimodal Learning Analytics

## Questions

1. What does cross-modal alignment add beyond single-source analytics?
2. Which fused features are stable across sessions?
3. How can missing modalities be handled transparently?

## Baseline methods

- learner and session aware windowing
- fixed time windows
- timestamp alignment
- available signal averaging
- click aggregation
- explicit modality presence flags
- modality coverage count

## Evidence to collect

Start from the transparent baseline and record every transformation needed to produce window-level averages for available continuous signals, click totals, missingness indicators, and modality coverage. Keep a clear boundary between synthetic demonstration data and any future empirical dataset.

Derived features should retain their provenance. If speech or gaze variables come from upstream models, document the model, calibration procedure, sampling rate, and known failure modes instead of treating those variables as ground truth.

## Validation

Compare fused features with unimodal baselines under the same learner/session boundaries, time windows, and outcome definition. Report missingness, synchronization error, robustness to dropped modalities, and whether fusion adds information beyond each individual modality.

## What counts as a useful result

A useful next study should test whether fused features improve a clearly defined learning-process outcome over unimodal baselines. The comparison should include robustness checks for missing channels, clock drift, and alternate window sizes.

## Threats to validity

Sensor error, clock drift, missing channels, feature-extraction error, classroom context, construct validity, and accidental pooling across learners or sessions can all make multimodal summaries misleading.
