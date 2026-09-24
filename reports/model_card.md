# Analytic system card

## System

Multimodal Learning Analytics

## Purpose

Windowed fusion baseline for timestamped speech, gaze, and click signals with explicit missing modality handling.

## Current maturity

Working research prototype. The bundled example checks the software path with synthetic inputs. It does not establish validity for real learners, instructors, courses, or workplaces.

## Inputs

See `../data/README.md` for the current synthetic schema and the documentation expected before real data are connected.

## Outputs

The current code produces window level averages for available continuous signals, click totals, and modality coverage. These outputs are research signals and should be interpreted with the educational context that produced them.

## Evidence needed before real use

Compare fused features with unimodal baselines under the same windows and outcome definition. Report missingness, synchronization error, robustness to dropped modalities, and whether the fused representation adds useful information.

## Main limitation

Speech, gaze, and click features are behavioral signals, not direct measures of attention, understanding, emotion, or ability. The current code performs simple feature fusion only.

## Human oversight

A person must review any output before it can affect a learner, instructor, applicant, or employee.
