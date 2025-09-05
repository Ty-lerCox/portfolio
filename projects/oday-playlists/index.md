---
title: Oday — YouTube Playlists Web App
layout: project
tags: [web, angular]
demo: https://example.com
---

# Oday — YouTube Playlists Web App

**TL;DR:** Curates and surfaces multi-playlist learning tracks with a minimal, distraction-free UI.

## Why
Existing YouTube playlist tools made it hard to track progress across multiple series; I wanted a lightweight way to organize learning paths.

## What
- **Playlist aggregation:** pulls in multiple playlist feeds
- **Progress tracking:** local storage remembers where you left off
- **Clean UI:** minimal, responsive layout

## How (selected details)
- **Frontend:** vanilla TypeScript with modular components
- **Data fetch:** YouTube Data API v3
- **Hosting:** GitHub Pages

```ts
// Example: mark video as completed and store progress
function markComplete(videoId: string) {
  const progress = JSON.parse(localStorage.getItem('progress') || '{}');
  progress[videoId] = true;
  localStorage.setItem('progress', JSON.stringify(progress));
}
```

## Outcome

* **Learning continuity:** users resume exactly where they left off
* **Simplicity:** zero-build static site keeps maintenance low
* **Shareability:** easy to send curated tracks to friends

