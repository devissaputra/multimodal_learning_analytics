# Research protocol

## Project

Multimodal Learning Analytics

## Questions

1. What does cross-modal alignment add beyond single-source analytics?
2. Which fused features are stable across sessions?
3. How can missing modalities be handled transparently?

## Baseline methods

- fixed time windows
- timestamp alignment
- available signal averaging
- click aggregation
- modality presence count

## Evidence to collect

Start from the current transparent baseline and record every transformation needed to produce window level averages for available continuous signals, click totals, and modality coverage. Keep a clear boundary between synthetic demonstration data and any future empirical dataset.

## Validation

Compare fused features with unimodal baselines under the same windows and outcome definition. Report missingness, synchronization error, robustness to dropped modalities, and whether the fused representation adds useful information.

## What counts as a useful result

A useful next study should test whether fused features improve a clearly defined learning process outcome over single modality baselines. Missing sensor periods and synchronization error need their own robustness checks.

## Threats to validity

Sensor error, clock drift, missing channels, classroom context, and construct validity are major risks in multimodal learning analytics.
