---
layout: post
title: 'Odeya — Archived Product Case Study'
date: 2025-03-15 00:00:00 +0000
pin: false
categories: [Odeya]
tags: [Angular, SSR, RxJS, NgRx, TypeScript, Firebase, YouTube API, Product Engineering]
image:
  path: /assets/img/odeya-overview.png
  alt: 'Odeya playlist curation interface'
---

> **Project status:** Odeya was retired in 2026. This page is preserved as a product and engineering case study; the hosted service is no longer available.

_Odeya_ was a focused utility for heavy YouTube users. It grouped channels into collections and automatically maintained a single destination playlist whenever those channels published new videos.

## Product idea

The problem was simple but repetitive: keeping topic-based playlists current required constant manual work. Odeya let a user define the grouping once and automated the ongoing curation.

- **Channel collections** grouped creators by topic.
- **Automatic population** routed new uploads into the correct playlist.
- **Shareable pages** made curated collections useful beyond a single account.
- **Server-side rendering** exposed meaningful page content to crawlers and link previews.

![](/assets/img/odeya-playlist-edit.png)

## Engineering approach

The application used Angular, RxJS, NgRx, TypeScript, Firebase, and the YouTube API. Its data model represented a many-to-one relationship between a group of source channels and a destination playlist, while background workflows handled new-video discovery and playlist updates.

Server-side rendering supported searchable, shareable collection pages without giving up the interaction model of an Angular application.

![](/assets/img/odeya-discover-mobile.png)

## What I took from it

Odeya was a useful exercise in shipping and operating a focused product: defining a narrow user problem, integrating with a third-party platform, handling authentication and quotas, and deciding when a service had reached the end of its useful life.

Retiring it also created room to focus on projects with deeper systems work, including CityRPG and the reverse-engineered game server modding framework.
