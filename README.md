# Multimodal Learning Analytics

> Windowed fusion baseline for timestamped speech, gaze, and click signals with explicit missing modality handling.

[![CI](https://github.com/devissaputra/multimodal-learning-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/devissaputra/multimodal-learning-analytics/actions/workflows/ci.yml)

![Multimodal Learning Analytics workflow](assets/architecture.svg)

**Area:** Learning Analytics & Multimodal Evidence    
**Status:** working research prototype  
**Author:** Devis Wawan Saputra

## What this project is for

Classroom and learning-process data often arrive from several channels at once. This repository shows a transparent way to align timestamps, build time windows, fuse simple features, and report what is missing instead of pretending every modality is always available.

**Who may find it useful:** Multimodal learning-analytics researchers working with synchronized classroom or interaction signals.

## Research questions

1. What does cross-modal alignment add beyond single-source analytics?
2. Which fused features are stable across sessions?
3. How can missing modalities be handled transparently?

## How it works

The baseline buckets events into fixed time windows, averages available speech and gaze values, sums click counts, and reports how many modalities were actually present. A click stream still counts as present when the observed count is zero.

![Multimodal Learning Analytics data and reasoning flow](assets/data_flow.svg)

Timestamped modality events are aligned into windows before fusion. Missing channels stay explicit instead of being silently interpreted as zero engagement.

![Synthetic demo snapshot for Multimodal Learning Analytics](assets/demo_snapshot.svg)

This snapshot shows the bundled synthetic example for Multimodal Learning Analytics. It checks the software path; it is not an empirical performance result.

## Methods in the current baseline

- fixed time windows
- timestamp alignment
- available signal averaging
- click aggregation
- modality presence count

## Data

Synthetic audio/video/log-derived features are included. No raw biometric or identifiable media are distributed.

`data/README.md` documents the sample schema and the conditions that should be recorded before any real dataset is connected. Restricted or identifiable learner data should stay outside the repository.

## Run the demo

```bash
git clone https://github.com/devissaputra/multimodal-learning-analytics.git
cd multimodal-learning-analytics
python scripts/run_demo.py
python -m unittest discover -s tests -v
```

The demo fuses two events in the same window and prints speech ratio, gaze focus, click count, and the number of observed modalities.

## What to evaluate next

A useful next study should test whether fused features improve a clearly defined learning process outcome over single modality baselines. Missing sensor periods and synchronization error need their own robustness checks.

## Evaluation view

![Multimodal Learning Analytics evaluation dashboard](assets/evaluation_dashboard.svg)

The Multimodal Learning Analytics dashboard is an evaluation checklist rather than a result chart. The bars are illustrative only; the labels show the evidence a real study would need to collect.

## Limits and responsible use

Speech, gaze, and click features are behavioral signals, not direct measures of attention, understanding, emotion, or ability. The current code performs simple feature fusion only. See `docs/ethics_and_risks.md` for the broader risk review.

## Repository map

```text
.
├── .github/workflows/ci.yml
├── assets/
│   ├── architecture.svg
│   ├── data_flow.svg
│   ├── demo_snapshot.svg
│   └── evaluation_dashboard.svg
├── data/
│   ├── README.md
│   └── sample.csv
├── docs/
│   ├── ethics_and_risks.md
│   ├── related_work.md
│   └── research_protocol.md
├── reports/model_card.md
├── scripts/run_demo.py
├── src/multimodal_learning_analytics/core.py
├── tests/test_core.py
├── CITATION.cff
├── LICENSE
├── pyproject.toml
└── README.md
```

## Research path

A credible next version would:

1. connect synchronized public or consented multimodal traces
2. compare single modality and fused baselines
3. stress test missing channels and timestamp misalignment

## Related work

`docs/related_work.md` points to open projects that are relevant to this problem area. They are context for comparison and study design; this repository does not present their code as its own.

## Citation and license

`CITATION.cff` contains the software citation. The code and original SVG visuals use the MIT License. Any external dataset keeps its own license and usage conditions.
