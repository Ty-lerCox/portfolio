---
layout: post
title: 'odeya Overview'
date: 2025-03-15 00:00:00 +0000
pin: true
categories: [ODEYA]
tags:
    - ODEYA
    - Angular
    - Angular Universal
    - SSR
    - RxJS
    - NgRx
    - TypeScript
    - Firebase
    - SEO
    - YouTube
    - YouTube API
    - Playlists
    - Video Curation
    - Content Aggregation
    - Web App
    - Personal Project
    - Productivity
    - Automation
    - Web Development
    - Selenium
image:
    path: /assets/img/odeya-overview.png
---

_ODEYA_ is a focused utility for heavy YouTube users: create **channel collections** (e.g., Cruise News, Gaming, Tech) and let ODEYA automatically **populate a single playlist** every time any channel in that collection publishes a new video. It started as a personal tool to eliminate manual playlist maintenance—and it stuck.

Link: [https://odeya.app](https://odeya.app)

---

## Introduction

ODEYA is:

-   **A Web App** — built with Angular for a fast, clean curation experience.
-   **A Playlist Engine** — many‑to‑one mapping from multiple channels to one rolling playlist.
-   **A Sharing Layer** — server‑side rendering (SSR) makes shared playlists discoverable by search engines.

![](/assets/img/odeya-playlist-edit.png)

---

## Key Features

### Channel Collections

-   Group multiple channels under a single topic (e.g., _Cruise News_, _VR & Gaming_, _Tech Daily_).
-   One click to target a **single destination playlist** for the whole collection.

### Auto‑Population

-   New uploads from any channel in the collection are **auto‑added** to the playlist.
-   No more manual copy/paste or scripts to keep up with frequent uploads.

### Shareable & Searchable Playlists (SSR)

-   **Server‑Side Rendering** ensures shared playlist pages are crawlable and indexable.
-   Friends can follow public playlists; search engines can surface your curated collections.

![](/assets/img/odeya-discover-ue5.png)

### Practical Curation

-   Create separate playlists for different interests or times of day (e.g., _Morning News_, _Deep Dives_, _Weekend Watch_).
-   Keep your YouTube “Watch Later” uncluttered by offloading discovery into themed lists.

---

## Example Use Cases

-   **Cruise News Aggregator:** follow multiple cruise‑focused channels and keep a single, always‑fresh playlist for updates.
-   **Gaming & Tech Roundups:** track daily uploads across many creators without hopping between subscriptions.
-   **Education Playlists:** bundle a set of instructors/channels into a rolling curriculum.

![](/assets/img/odeya-discover-mobile.png)

---

## Technical Backbone

-   **Angular + SSR**  
    ODEYA renders playlist and share pages on the server so titles, descriptions, and content are available to crawlers.

-   **Aggregation Logic**  
    A many‑to‑one mapping model ties **channel collections → a destination playlist**, so any new upload routes to the right place without manual steps.

-   **Performance & Stability**  
    Built to be lightweight for personal use, with room to evolve if broader adoption happens later.

![](/assets/img/odeya-youtube.png)

---

## Final Thoughts

ODEYA removes the friction of staying up to date on YouTube by **automating curation** and **making playlists easy to share and find**. It began as a personal project, but the approach scales naturally: define your interests once, and let fresh content flow where you want it—without the busywork.
