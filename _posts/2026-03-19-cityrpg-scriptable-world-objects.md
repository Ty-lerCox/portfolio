---
layout: post
title: 'Scriptable World Objects Without Surrendering Server Authority'
date: 2026-03-19 18:00:00 -0400
description: How CityRPG lets TypeScript define rapidly changing world behavior while native Unreal code retains identity, validation, and authoritative execution.
categories: [CityRPG]
tags: [Unreal Engine 5, C++, TypeScript, Scripting, Multiplayer, Firebase, Automation Testing]
mermaid: true
---

World objects in an RPG accumulate behavior quickly. A tree can be harvested, a shop can sell inventory, a pressure plate can open a bank flow, and a civic building can expose an election or law service. Encoding every variation as a new native class would make iteration slow; allowing arbitrary scripts to control the world would weaken authority.

CityRPG uses a narrower model: TypeScript can define behavior, but native code owns the actor, identity, event source, and final side effect.

## The event boundary

Buildable actors publish explicit lifecycle and interaction events. The runtime resolves a stable buildable ID, attaches authored configuration, and produces a structured payload. TypeScript evaluates the corresponding script and returns requests through a constrained bridge.

```mermaid
sequenceDiagram
  participant Player
  participant Actor as UE5 Buildable
  participant Bridge as Native Script Bridge
  participant Rules as TypeScript Script
  participant World as Authoritative World
  Player->>Actor: Interact / hit / overlap
  Actor->>Bridge: Stable ID + event payload
  Bridge->>Rules: Execute bound behavior
  Rules-->>Bridge: Requested effects
  Bridge->>World: Validate and apply
  World-->>Player: Replicated result and UI feedback
```

Scripts can request supported operations such as audio, visual effects, inventory changes, persistence, or UI messages. They do not receive unrestricted access to engine memory or authoritative player state.

## Publishing and binding

A script is useful only when the right world object runs the right version. I added publishing and binding workflows that treat scripts as deployable content rather than loose files.

The tooling can:

- Validate script metadata and configuration.
- Publish known scripts into persistent storage.
- Bind scripts to authored buildables.
- Refresh runtime script state deliberately.
- Audit civic and starter-gathering surfaces.
- Exercise the same workflow against fixtures before live use.

This makes script changes traceable and repeatable. It also avoids a class of errors where a local script works but no deployed object references it.

## Testing across the seam

The test harness captures behavior at the native boundary. It can represent players with different roles, skill levels, inventory, currency, and persistence state. Tests then assert both the TypeScript decision and the native effect request.

That approach supports realistic cases such as a resource node paying out once, a shop rejecting an invalid purchase, an admin-only surface refusing a normal player, or a quest object emitting the expected progression signal.

## Why not put everything in one language?

The split is deliberate. Native C++ is the right place for replication, actor lifecycle, collision, combat, and operations that must be difficult to spoof. TypeScript is the right place for content-heavy rules where short feedback loops matter.

The bridge turns that difference into an advantage as long as it stays explicit. The important design choice was not adding scripting. It was deciding what scripts are allowed to ask for, and preserving one authoritative place where those requests become reality.
