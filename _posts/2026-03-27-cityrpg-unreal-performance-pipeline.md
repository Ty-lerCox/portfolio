---
layout: post
title: 'Turning Unreal Performance Debugging Into a Repeatable Pipeline'
date: 2026-03-27 18:00:00 -0400
description: Moving from anecdotal PIE hitch reports to scripted capture, CSV analysis, subsystem isolation, and targeted polling reductions.
categories: [CityRPG]
tags: [Unreal Engine 5, Performance, Profiling, Python, PowerShell, NoesisGUI, Developer Tooling]
---

"The editor feels slow" is not a useful performance report. It does not identify the phase, subsystem, trigger, or regression window, and it is difficult for another developer to reproduce.

I built a small performance-triage pipeline around CityRPG so startup hitches and Play-in-Editor slowdowns could be investigated as evidence instead of impressions.

## Capture first

The entry point launches a controlled capture with known metadata. Unreal writes CSV performance data while diagnostic probes record the scenario being exercised. A Python analyzer then turns the raw capture into a report that highlights frame-time behavior and likely investigation targets.

The workflow makes several questions explicit:

- Was this editor startup, PIE startup, steady-state play, or a UI interaction?
- Which systems were active during the expensive window?
- Can the same capture be reproduced after a code change?
- Did the change improve the expensive path or only move work elsewhere?

This is deliberately more lightweight than building a complete observability platform around a development editor. The goal is a repeatable first pass that tells me where deeper Unreal Insights work is justified.

## Reduce polling before optimizing polling

The first useful changes were not exotic. Several UI and authentication surfaces were refreshing state more often than the product required. Notifications, interaction prompts, and session-related UI had accumulated polling behavior because it was easy to add and difficult to notice in isolation.

I moved suitable work toward event-driven updates and added guards around expensive refresh paths. That reduced background churn while preserving the states that genuinely needed periodic evaluation.

The distinction matters. Optimizing a poll can produce a small local win; removing an unnecessary poll changes the scaling behavior.

## Separate editor noise from game cost

PIE is not a packaged client. The editor adds background work, asset behavior, tooling, and different lifecycle conditions. The pipeline therefore treats editor capture as triage evidence, not final production proof.

Later probes could isolate UI work, skeletal presentation, ocean traffic, and background throttling. This made it easier to distinguish a game-system regression from an editor-only artifact before spending time in the wrong subsystem.

## Performance tooling compounds

The immediate benefit was faster diagnosis. The longer-term benefit was a common investigation language: named scenarios, captured artifacts, machine-readable summaries, and a way to rerun the same question.

That is how I prefer to approach performance work. Start by making the claim reproducible, improve the ownership boundary, and keep the measurement close enough to the feature that future changes cannot quietly erase it.
