---
layout: post
title: "CityRPG Overview"
date: 2025-04-05 00:00:00 +0000
categories: [CityRPG]
tags:
  - CityRPG
  - Angular
  - UE5
  - C++
  - TypeScript
  - RxJS
  - NgRx
  - Firebase
---

*CityRPG* is an ambitious mod for **Brickadia** that transforms its open-ended building sandbox into an active, living city. It pairs a robust back-end service with an Angular-based UI to keep the game scalable, responsive, and ready for future server expansion.

![City skyline or logo](https://placehold.co/600x400?text=Placeholder&format=svg)

---

## Introduction
CityRPG is both:
- **A Game Mod** – expanding Brickadia with deep RPG systems.
- **A Web-Based UI** – the UI is built in Angular and interacts with a service-based backend (e.g., Firebase), offloading significant logic to the cloud for scalability.
- **A Website** – enabling players to manage accounts, track stats, and eventually connect across multiple servers/regions.

![Player exploring the city](https://placehold.co/600x400?text=Placeholder&format=svg)

---

## Key Features

### Expansive Economy
- **Currency & Trading**  
  - In-game currency and a Grand Exchange (inspired by RuneScape) for automated buying/selling.
  - Run shops, set custom prices, and collect profits.

- **Property Ownership**  
  - Purchase lots, build storefronts, or craft unique items to sell.
  - Set taxes as the city evolves (tied to the election system below).

![Lot management UI](https://placehold.co/600x400?text=Placeholder&format=svg)

### Skills & Jobs
- **RuneScape-Inspired Skill Progression**  
  - Gain XP in various skills to unlock advanced abilities.
  - Law enforcement can earn “Law XP” for capturing criminals.
  - Crafting, gathering, and restaurant work all reward skill XP.

- **Job System**  
  - **Law Enforcement** – Official role with structured progression and XP.  
  - **Criminal Route** – Not an official “job,” but a set of activities (e.g., weapon crafting, bank heists, laptop hacking) for players who prefer to live on the edge.

![Skill menu screenshot](https://placehold.co/600x400?text=Placeholder&format=svg)

### Quests & Activities
- Branching quests and task systems that provide currency, XP, or rare items.
- Minigame-style bank heists:
  - Text-based hacking sequence requiring concentration and teammates for protection.
  - Rewards depend on success and skill level.

### Business & Community
- **Business System**  
  - Players can form or join multi-player businesses for advanced crafting, storage, and sales.
  - Manage inventory and profits collectively.

- **Restaurant & Crafting**  
  - Craft meals, set restaurant pricing, and manage stock.
  - Profits feed back into personal or business finances.

![Crafting bench screenshot](https://placehold.co/600x400?text=Placeholder&format=svg)

### Political System
- **Elections & Taxes**  
  - Run for mayor and influence city policy.
  - Set taxes, manage city finances, and face potential impeachment if citizens are unhappy.

![Voting booth or election posters](https://placehold.co/600x400?text=Placeholder&format=svg)

### Voyages & Sea Exploration
- Plan a voyage, recruit crew members, and sail out from the city.
- Currently focuses on resource-gathering at sea, with future plans for:
  - NPC encounters.
  - Cooperative combat and loot return loops similar to *Sea of Thieves*.

![Players on a ship or sea horizon](https://placehold.co/600x400?text=Placeholder&format=svg)

---

## Technical Backbone

- **Angular UI**  
  - All game menus and interactions are rendered with Angular, blending seamlessly into the Brickadia environment.

- **Service-Based Architecture**  
  - Game logic runs against cloud services (e.g., Firebase).  
  - Player state is synchronized across servers, ready for multi-region scaling.

- **Scalability**  
  - If one city runs out of lots, new servers/regions can spin up with shared accounts and inventory, helping reduce latency worldwide.

![UI mockup or code snippet image](https://placehold.co/600x400?text=Placeholder&format=svg)

---

## Getting Involved
1. **Visit the Website** to create or manage your account.  
2. **Download/Install the Mod** and connect to the CityRPG server.  
3. **Choose Your Path** – start a job, craft items, or delve into criminal activities.  
4. **Climb the Ranks** in your chosen skills to unlock advanced features.

![Player showcase or feature highlight image](https://placehold.co/600x400?text=Placeholder&format=svg)

---

## Tips for Adding Images
- **Markdown**: `![Alt text](https://placehold.co/600x400?text=Placeholder&format=svg)`
- **HTML**: `<img src="https://placehold.co/600x400?text=Placeholder&format=svg" alt="Description" width="600"/>`
- Use descriptive file names and alt text for accessibility.
- Maintain consistent sizing and styling for a clean visual flow.

---

## Final Thoughts
CityRPG expands Brickadia into a full-fledged RPG experience, blending **economy**, **job roles**, **player politics**, and **cooperative adventures**. Thanks to its service-oriented architecture and Angular UI, the mod is built for the long term—ready to scale and evolve with its community.

![Closing concept art or logo](https://placehold.co/600x400?text=Placeholder&format=svg)

Feel free to adjust the text, add/remove sections, and insert screenshots or concept art wherever placeholders appear to create a polished overview that captures the depth and excitement of CityRPG.

