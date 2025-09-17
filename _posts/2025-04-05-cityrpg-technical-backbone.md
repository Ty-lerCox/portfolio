---
layout: post
title: 'Technical Backbone'
date: 2025-08-01 00:00:00 +0000
categories: [CityRPG]
tags:
    - CityRPG
    - Game Development
image:
    path: /assets/img/cityrpg-tech.png
    alt: 'CityRPG Technical Backbone'
---

CityRPG succeeds because its core systems are split across the game client, an Angular web interface, and a service-driven backend. This post explains how those pieces fit together and why the mod can scale beyond a single Brickadia server.


---

## Brickadia & Plugin Layer

-   **Omegga plugin** – A TypeScript plugin running on the Brickadia server mediates all gameplay events.
-   **Reactive pipeline** – RxJS streams process chat commands, inventory changes, and world events in real time.
-   **Native hooks** – When low-level control is required, C++/UE5 hooks surface data to the plugin for higher-level handling.

## Angular Web UI

-   **In-game overlay** – Menus and HUD elements render with Angular, sharing components with the external website for rapid iteration.
-   **State management** – NgRx keeps UI state predictable; actions from the plugin or backend flow into a single store.
-   **Offline-ready** – The UI caches essential data so players retain menus even during transient network hiccups.

## Cloud Services

-   **Firebase** – Firestore, Auth, and Cloud Functions persist player data, run server-side validation, and push realtime updates.
-   **Job queues & functions** – Long-running tasks (heist resolution, voyage logic) execute in functions to avoid blocking the game loop.
-   **Analytics** – Centralized logs and metrics feed future balancing and abuse detection.

## Scaling Across Servers

-   **Shared accounts** – Because identity and inventory live in Firebase, players can move between CityRPG regions without losing progress.
-   **Service boundaries** – Each server only owns session state; all persistent data is remote, allowing new shards to spin up quickly.
-   **Future extensions** – Additional microservices (matchmaking, trading post) can plug in without touching the core plugin.

---

## Developer Workflow

-   **TypeScript everywhere** – Both plugin and Angular code use TypeScript for type safety and tooling.
-   **Testing & CI** – Scripts validate gameplay logic with ts-node tests; GitHub Actions can run them on pull requests.
-   **Config-driven** – Environments and feature flags load from Firebase, letting admins tweak balance without redeploying.

---

## Summary

CityRPG’s technical backbone separates presentation, game logic, and persistence so the mod stays maintainable and ready for growth. The combination of an Angular UI, an Omegga plugin, and Firebase services turns Brickadia into a living world that can span many servers.
