---
layout: post
title: 'From Combat Receipts to Live Cannon Fire and Whirlpools'
date: 2026-04-22 18:00:00 -0400
description: Connecting deterministic naval results to readable live presentation while keeping effects, hazards, and playback subordinate to authoritative state.
categories: [CityRPG]
tags: [Unreal Engine 5, C++, TypeScript, Game UI, Naval Combat, Visual Systems, Automation Testing]
---

Once naval combat produced deterministic receipts, the next problem was translation: how should an authoritative event become something a player can understand without letting presentation rewrite the result?

The live ocean layer treats combat output as a playback script. It stages ships, advances phases, animates movement, fires effects from known origins, and updates the HUD. Damage and terminal outcomes already exist in the receipt.

## Presentation follows the receipt

This boundary prevented several subtle errors. A cannon animation cannot apply damage a second time. A blocked movement still has an endpoint that presentation can show. A collision result maps to the same ship and turn regardless of how long the effect takes to play.

When combat transitions from turn to turn, the runtime carries stable encounter and ship identities instead of inferring ownership from nearby actors.

## Hazards needed to communicate rules

Rocks, wind, and whirlpools are not decorative board dressing. Each affects navigation, so a player must be able to read its footprint and direction before committing a phase.

The hazard presentation went through a concentrated series of changes:

- Route live encounter modes through the same hazard data used by the resolver.
- Preserve whirlpools while staging and replaying the board.
- Add dedicated wind and rock visuals rather than overloading one generic marker.
- Cluster generated hazards without creating accidental walls.
- Animate whirlpool motion along an arc while keeping its occupied cells legible.
- Tune rock waterlines and wind direction for readability.
- Remove or revert visual underlays when they added clutter.

That last point matters. Iteration included deletion. A technically correct visual can still make the tactical board harder to understand.

## Why a whirlpool took so many commits

The whirlpool work is a useful example of production-minded iteration. One change established the data path. Another proved the live footprint. Later changes addressed handedness, movement arc, clutter, phase stepping, cluster distribution, and automated coverage.

Treating the entire sequence as one giant commit would have made regressions difficult to locate. Small, evidence-backed changes made it possible to distinguish a resolver problem from staging, animation, or readability.

## Tests covered the live seam

Headless tests continued to prove the rules, while Unreal automation covered live board generation, forced encounter recovery, collision playback, phase stepping, effect origins, and HUD outcome mapping.

The result was not merely a prettier tactical board. It was a presentation layer that could evolve without becoming a second combat engine.
