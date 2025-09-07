---
layout: post
title: "Voyages & Sea Exploration"
date: 2025-04-05 00:00:00 +0000
categories: [CityRPG]
tags:
  - CityRPG
  - Voyages
  - Sea Exploration
  - Cooperative
  - Resource Gathering
---

Voyages turn the open sea into a cooperative resource loop. Gather a crew, claim a ship, and sail to remote islands packed with stone and lumber. This post explains how voyages work, from planning to payouts.

![Ship setting sail](https://placehold.co/600x400?text=Placeholder&format=svg)

---

## Starting a Voyage

- Create a voyage with `/voyage create [payPerMinute|crewCut=<percent>] [label]`.
  - `payPerMinute` provides periodic wages to crew.
  - `crewCut=<percent>` splits a percentage pool when the voyage ends.
- Assign a ship using `/voyage set-ship <shipId>`. Each ship has a capacity and minimum crew.
- Update compensation or label later with `/voyage set-comp ...` and `/voyage set-label ...`.
- Kick misbehaving members with `/voyage kick <playerNameOrId>`.

![Voyage creation UI](https://placehold.co/600x400?text=Placeholder&format=svg)

---

## Recruiting and Launching

- Share the four-letter voyage ID so others can join via `/voyage join <id>` and confirm.
- Check progress with `/voyage info <id>` to see crew and status.
- When the minimum crew is met, the captain runs `/voyage start` to sail out.
- Captains can't leave until the voyage is ended with `/voyage end`.

---

## Life at Sea

- Remote islands contain trees and stone nodes that respawn continuously.
- Click the nodes to harvest; stone blocks break after five hits and roll for gems like rubies or sapphires.
- Carry up to 10 lumber and 10 stone at a time. Use `storeonship` bricks to stash resources in the ship's hold.
- Pay-per-minute voyages automatically pay crew over time. Crew-cut voyages distribute resources based on time spent when the captain ends the trip.

![Crew harvesting resources](https://placehold.co/600x400?text=Placeholder&format=svg)

---

## Wrapping Up

- Finish with `/voyage end` to distribute payouts and transfer stored materials to the captain.
- Resources can be sold at `depositresources` bricks or processed for crafting.
- Voyages broadcast major events to crew (joining, compensation changes, payouts).

---

## Quick Command Reference

```
/voyage create [payPerMinute|crewCut=<percent>] [label]
/voyage list
/voyage info <id>
/voyage join <id>
/voyage leave
/voyage start
/voyage kick <player>
/voyage end
/voyage set-ship <shipId>
/voyage set-comp [payPerMinute|crewCut=<percent>]
/voyage set-label <label>
```

![Command overlay screenshot](https://placehold.co/600x400?text=Placeholder&format=svg)

---

## Tips & Future Plans

- Bring a balanced crew to meet ship requirements and gather faster.
- Voyages are perfect for training new players and stocking the city economy.
- Future updates aim to add NPC encounters and cooperative combat, making the seas even more dangerous.

---

Voyages open up the world beyond the harbor. With the right ship and crew, the ocean becomes a lucrative playground for anyone willing to set sail.

