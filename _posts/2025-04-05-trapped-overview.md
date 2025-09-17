---
layout: post
title: 'Unreal Engine Gameplay Overview'
date: 2024-03-05 00:00:00 +0000
pin: true
categories: [Trapped (UE5 Game)]
tags:
    - Trapped
    - Unreal Engine 5
    - C++
    - Enhanced Input
    - Behavior Trees
    - EQS
    - AI Perception
    - Gameplay Framework
    - Actor Component
    - UDataAsset
    - Data Tables
    - Subsystems
    - World Partition
    - Data Layers
    - Nanite
    - Lumen
    - Niagara
    - MetaSounds
image:
    path: /assets/img/trapped-ships.png
    alt: 'Trapped ships'
---

_Trapped_ is an ambitious game project developed in **Unreal Engine 5** using **C++**. It features a rich, open-world environment where players can explore, complete quests, and engage in dynamic gameplay mechanics.

---

## Premise

You awaken in a hostile seascape dotted with wrecks and strange signals. The world shifts between calm and chaos; resources are scarce; every expedition is a choice between risk and reward.

-   **Vibe:** moody survival-adventure across foggy waters and forgotten outposts.
-   **Goal:** explore, learn the rules of the place, and chart a path out.
-   **Pillars:** exploration, tension, and meaningful upgrades that enable longer runs.

![](/assets/img/trapped-hud.png)

---

## Core Loop

1. **Scout** new areas, signals, and points of interest.
2. **Gather** materials, intel, and tools while managing risk and capacity.
3. **Upgrade** gear, vessel, or skills to push further next time.
4. **Attempt** deeper incursions, unlock shortcuts, and uncover story threads.

---

## Key Features

-   **Exploration & Navigation:** Traverse open waters and island hubs; discover routes, hazards, and shortcuts.
-   **Encounters:** Environmental challenges, AI patrols, and timed opportunities that shape each run.
-   **Quests & Story Threads:** Lightweight objectives that reveal lore and unlock new capabilities.
-   **Progression:** Persistent upgrades and unlocks that expand options without trivializing tension.
-   **Atmosphere:** Audio, lighting, and FX tuned for mood and readability.

![](/assets/img/trapped-hud-2.png)

---

## Systems Overview

-   **Movement & Interaction:** Context-sensitive interaction, diegetic prompts, and clear affordances.
-   **Inventory & Items:** Stackable resources, key items, and crafted tools with simple rarity or tiering.
-   **Quests & Dialogue:** Objective tracking, optional dialogue prompts, and breadcrumb hints.
-   **Combat/Stealth (Prototype):** Simple threat behaviors and counterplay focused on positioning and timing.
-   **Save/Load:** Persistent profile plus run-based state where applicable.
-   **Accessibility:** Scalable UI, color safe choices, and configurable input.

![](/assets/img/trapped-ingame.png)

---

## Technical Backbone (UE5 + C++)

-   **Gameplay Framework:** Actor/Component architecture with clean ownership and lifecycle rules.
-   **Enhanced Input:** Context-driven mappings for keyboard/mouse and gamepad.
-   **AI Tools:** Behavior Trees, EQS, and perception for patrols and reactions.
-   **Data-Driven Content:** `UDataAsset` and tables for items, encounters, and tuning.
-   **Subsystems:** GameInstance and World subsystems for saving, progression, and services.
-   **World Building:** World Partition and Data Layers for streaming spaces and POIs.
-   **Rendering:** Nanite meshes and Lumen lighting for readability and performance.
-   **VFX/Audio:** Niagara for effects and MetaSounds for systemic audio cues.

![](/assets/img/trapped-ship-combat.png)

---

## Controls (Default)

-   **Move:** WASD
-   **Interact:** E
-   **Sprint:** Shift
-   **Inventory/Map:** I / M
-   **Confirm/Cancel:** Enter / Esc

> Map to gamepad via Enhanced Input contexts.

---

## Roadmap

-   **Now:** Core loop polish (scouting, gathering, upgrading) and readability passes.
-   **Next:** Quest scaffolding, encounter variety, and save/profile hardening.
-   **Later:** Broader content sweep, performance tuning, and optional co-op exploration.

![](/assets/img/trapped-basic-menu.png)
