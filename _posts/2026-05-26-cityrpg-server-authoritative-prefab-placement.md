---
layout: post
title: 'Server-Authoritative Prefab Placement With Responsive Client Previews'
date: 2026-05-26 18:00:00 -0400
description: Coordinating build mode, ghost previews, input capture, plot containment, inventory consumption, persistence, and immediate transform selection.
categories: [CityRPG]
tags: [Unreal Engine 5, C++, Multiplayer, Building Systems, NoesisGUI, Server Authority, Automation Testing]
mermaid: true
---

A placement preview should feel immediate. The decision to create a persistent multiplayer object cannot be trusted to the preview.

CityRPG's prefab flow separates those responsibilities while still behaving like one continuous build-mode interaction.

## One placement intent at a time

The game supports normal recipe placement and larger prefab groups. Allowing both tools to believe they own the next click creates duplicate placements and confusing cancellation behavior.

Selecting a prefab cancels the normal recipe preview, marks external placement active, spawns a lightweight ghost, captures the placement input, and returns the menu to quick slots. Selecting a normal recipe performs the reverse transition.

```mermaid
sequenceDiagram
  participant Player
  participant UI as Build Mode UI
  participant Preview as Prefab Preview Controller
  participant Server as Player Command Proxy
  participant World as World Buildables
  Player->>UI: Select prefab
  UI->>Preview: Arm external placement
  Preview->>Preview: Trace cursor and update ghost
  Player->>Preview: Confirm
  Preview->>Server: Entry ID, target, rotation
  Server->>Server: Validate catalog, license, inventory, plot
  Server->>World: Spawn group and persist provenance
  World-->>Player: Replicated actors and active selection
```

## Preview fast, validate twice

The client checks the target continuously so invalid placement is visible before the click. For a normal player, every preview child must remain within an owned plot. Admins use the same interaction but can bypass plot containment through an explicit server rule.

The server repeats the important checks using authoritative data:

- The catalog entry exists and is permitted.
- The player owns the required license or inventory item.
- The target is valid.
- Every saved child pivot remains inside the owned plot when required.
- Inventory is consumed only after validation succeeds.

Client validation improves experience. Server validation protects the world.

## Preserve provenance

A prefab is a group, not a bag of unrelated spawned actors. Placement stamps provenance, creates a runtime group, marks persistence dirty, and returns the spawned actors to the owning client.

The build manager immediately selects the new group and enables its move, rotate, and resize tools. That small handoff is important: a successful server round trip should not make the player hunt for the object they just placed.

## Test the coordination failures

Automation covers plot containment, admin bypass, selection handoff, catalog persistence, cancellation, quick-slot ordering, recovery, and disagreement between normal recipe placement and external prefab placement.

Most build-mode bugs live between systems rather than inside one algorithm. The solution was to make ownership transitions explicit and ensure that the fast client path and durable server path describe the same placement intent.
