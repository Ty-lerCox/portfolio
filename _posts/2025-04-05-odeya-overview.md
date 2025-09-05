---
layout: post
title: 'ODEYA Overview'
date: 2025-03-15 00:00:00 +0000
categories: [ODEYA]
tags: [Angular, SSR, YouTube, Playlists, SEO]
---

_ODEYA_ is a focused utility for heavy YouTube users: create **channel collections** (e.g., Cruise News, Gaming, Tech) and let ODEYA automatically **populate a single playlist** every time any channel in that collection publishes a new video. It started as a personal tool to eliminate manual playlist maintenance—and it stuck.

> **Add a banner image here**
>
> Example (Markdown):  
> `![ODEYA banner or logo](path-or-url-to-banner-image)`

---

## Introduction

ODEYA is:

-   **A Web App** — built with Angular for a fast, clean curation experience.
-   **A Playlist Engine** — many‑to‑one mapping from multiple channels to one rolling playlist.
-   **A Sharing Layer** — server‑side rendering (SSR) makes shared playlists discoverable by search engines.

> **Insert UI screenshots or short clips**  
> `![Creating a channel collection](image-url)`

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

> `![Shared playlist page with preview cards](image-url)`

### Practical Curation

-   Create separate playlists for different interests or times of day (e.g., _Morning News_, _Deep Dives_, _Weekend Watch_).
-   Keep your YouTube “Watch Later” uncluttered by offloading discovery into themed lists.

---

## Example Use Cases

-   **Cruise News Aggregator:** follow multiple cruise‑focused channels and keep a single, always‑fresh playlist for updates.
-   **Gaming & Tech Roundups:** track daily uploads across many creators without hopping between subscriptions.
-   **Education Playlists:** bundle a set of instructors/channels into a rolling curriculum.

> `![Topic collection setup: Cruise News](image-url)`

---

## Technical Backbone

-   **Angular + SSR**  
    ODEYA renders playlist and share pages on the server so titles, descriptions, and content are available to crawlers.

-   **Aggregation Logic**  
    A many‑to‑one mapping model ties **channel collections → a destination playlist**, so any new upload routes to the right place without manual steps.

-   **Performance & Stability**  
    Built to be lightweight for personal use, with room to evolve if broader adoption happens later.

> `![Simplified data flow diagram](image-url)`

---

## Getting Started

1. **Visit**: `https://odeya.app`
2. **Create a Collection**: add your favorite channels for a topic.
3. **Choose a Playlist**: set the destination playlist (or create a new one).
4. **Share**: send the public link to friends or post it—SSR makes it discoverable.

> `![Sharing a playlist link](image-url)`

---

## Tips for Adding Images

-   **Markdown**: `![Alt text](image-url)`
-   **HTML**: `<img src="image-url" alt="Description" width="600" />`
-   Use specific alt text and descriptive filenames for accessibility and better previews.
-   Keep dimensions consistent for a clean visual rhythm.

---

## Final Thoughts

ODEYA removes the friction of staying up to date on YouTube by **automating curation** and **making playlists easy to share and find**. It began as a personal project, but the approach scales naturally: define your interests once, and let fresh content flow where you want it—without the busywork.

> `![Closing logo or UI detail](image-url)`
