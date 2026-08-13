---
layout: post
title: 'I Stopped Launching Unreal to Iterate on Game UI'
date: 2026-02-21 18:00:00 -0500
description: A standalone WPF harness for rendering the game's real Noesis XAML, injecting realistic data, and capturing UI screenshots without waiting for Unreal Editor.
categories: [CityRPG]
tags: [NoesisGUI, WPF, C Sharp, Unreal Engine 5, UI Engineering, Developer Experience, Automation]
---

Launching Unreal Editor is an expensive way to answer a small UI question.

When I only needed to check whether a menu wrapped correctly, whether a phone layout overflowed, or whether a catalog still looked readable with real data, the engine startup loop made each adjustment unnecessarily slow. I built a standalone WPF preview application that renders the same Noesis XAML used by the game.

## One source of truth

The preview tool does not maintain a second copy of the UI. It links directly to the XAML under the game's `Content/Noesis` tree. A layout change appears in both the standalone harness and the packaged client.

That constraint mattered. A mockup tool that slowly diverges from production is worse than no tool because it creates false confidence. The harness includes only the compatibility shims needed to parse game XAML in WPF, such as a small placeholder extension.

## Reproducing useful conditions

The application can switch among fullscreen, phone, HUD, build-mode, banking, inventory, voyage, and civic surfaces. It supplies realistic mock state rather than empty controls.

For example, catalog data intentionally overflows its container. This validates wrapping, scrolling, selection, and the visual hierarchy under stress. The tool can also load exported item icons instead of generic placeholders, which makes visual review much closer to the game.

Other useful details include:

- Live rebuilding while XAML or C# changes.
- UE-style shortest-side DPI scaling.
- Menu and surface selection from command-line options.
- Deterministic screenshot capture.
- Dedicated preview tests for important menus and theme tokens.

## Screenshot capture became a test primitive

Once the UI could render outside Unreal, screenshots stopped being a manual afterthought. The same entry point could create stable captures for review, compare dense states, and verify that a shared theme change did not make a secondary screen unreadable.

The harness later became valuable during larger refactors. When the primary UI implementation was decomposed into focused controllers, the preview surface provided quick evidence that layout contracts still held while C++ ownership moved underneath them.

## The broader lesson

Developer experience work is often treated as optional polish. In this case, removing the engine from the inner UI loop changed what was practical to test. It became cheap to exercise overflow, alternate surfaces, real icons, and responsive sizing repeatedly.

The best tool was not a replacement for in-engine validation. It was a way to reserve expensive engine runs for questions that actually required the engine.
