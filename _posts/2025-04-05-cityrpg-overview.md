---
layout: post
title: 'CityRPG Overview'
date: 2025-08-01 00:00:00 +0000
pin: true
categories: [CityRPG]
tags:
    - CityRPG
    - Game Development
    - Angular
    - TypeScript
    - Firebase
    - AngularFire
    - RxJS
    - NgRx
    - Github Actions
    - CI/CD
    - Service-Oriented Architecture
    - Serverless
    - Cloud Services
    - Cloud
    - Document Database
    - NoSQL
    - Cloud Functions
    - Real-time Database
    - Real-Time
    - Firestore
    - Scripting
    - State Management
    - Angular Material
    - Material
    - AG-Grid
    - UI/UX

image:
    path: /assets/img/cityrpghomepage.png
    alt: 'CityRPG homepage'
---

_CityRPG_ is an ambitious mod for **Brickadia** that transforms its open-ended building sandbox into an active, living city. It pairs a robust back-end service with an Angular-based UI to keep the game scalable, responsive, and ready for future server expansion.

---

## Introduction

CityRPG is both:

-   **A Game Mod** – expanding Brickadia with deep RPG systems.
-   **A Web-Based UI** – the UI is built in Angular and interacts with a service-based backend (e.g., Firebase), offloading significant logic to the cloud for scalability.
-   **A Website** – enabling players to manage accounts, track stats, and eventually connect across multiple servers/regions.

![](/assets/img/cityrpg-home-embedded.png)

## Key Features

### Expansive Economy

-   **Currency & Trading**

    -   In-game currency and a Grand Exchange (inspired by RuneScape) for automated buying/selling.
    -   Run shops, set custom prices, and collect profits.

-   **Property Ownership**
    -   Purchase lots, build storefronts, or craft unique items to sell.
    -   Set taxes as the city evolves (tied to the election system below).

![](/assets/img/cityrpg-exchange.png)

### Skills & Jobs

-   **RuneScape-Inspired Skill Progression**

    -   Gain XP in various skills to unlock advanced abilities.
    -   Law enforcement can earn “Law XP” for capturing criminals.
    -   Crafting, gathering, and restaurant work all reward skill XP.

-   **Job System**
    -   **Law Enforcement** – Official role with structured progression and XP.
    -   **Criminal Route** – Not an official “job,” but a set of activities (e.g., weapon crafting, bank heists, laptop hacking) for players who prefer to live on the edge.

![](/assets/img/cityrpg-edu.png)

### Quests & Activities

-   Branching quests and task systems that provide currency, XP, or rare items.
-   Minigame-style bank heists:
    -   Text-based hacking sequence requiring concentration and teammates for protection.
    -   Rewards depend on success and skill level.

### Business & Community

-   **Business System**

    -   Players can form or join multi-player businesses for advanced crafting, storage, and sales.
    -   Manage inventory and profits collectively.

-   **Restaurant & Crafting**
    -   Craft meals, set restaurant pricing, and manage stock.
    -   Profits feed back into personal or business finances.

![](/assets/img/cityrpg-inventory.png)

### Political System

-   **Elections & Taxes**
    -   Run for mayor and influence city policy.
    -   Set taxes, manage city finances, and face potential impeachment if citizens are unhappy.

### Voyages & Sea Exploration

-   Plan a voyage, recruit crew members, and sail out from the city.
-   Currently focuses on resource-gathering at sea, with future plans for:
    -   NPC encounters.
    -   Cooperative combat and loot return loops similar to _Sea of Thieves_.

![](/assets/img/cityrpg-voyage-manage.png)

---

## Technical Backbone

-   **Angular UI**

    -   All game menus and interactions are rendered with Angular, blending seamlessly into the Brickadia environment.

-   **Service-Based Architecture**

    -   Game logic runs against cloud services (e.g., Firebase).
    -   Player state is synchronized across servers, ready for multi-region scaling.

-   **Scalability**
    -   If one city runs out of lots, new servers/regions can spin up with shared accounts and inventory, helping reduce latency worldwide.

![](/assets/img/cityrpg-firestore.png)

---

## Final Thoughts

CityRPG expands Brickadia into a full-fledged RPG experience, blending **economy**, **job roles**, **player politics**, and **cooperative adventures**. Thanks to its service-oriented architecture and Angular UI, the mod is built for the long term—ready to scale and evolve with its community.

![](/assets/img/cityrpg-firebase.png)

Feel free to adjust the text, add/remove sections, and insert screenshots or concept art wherever placeholders appear to create a polished overview that captures the depth and excitement of CityRPG.
