---
title: Portfolio — {{ site.data.resume.name }}
layout: home
image: /assets/img/social-card.svg
---

# {{ site.data.resume.name }}
_{{ site.data.resume.position }}_
Designing developer-friendly systems and shipping neat, usable tools.

<img src="{{ '/assets/img/headshot.svg' | relative_url }}" alt="{{ site.data.resume.name }} headshot" width="120" align="right">

<a href="#projects">View Projects</a> • <a href="{{ '/resume/resume.pdf' | relative_url }}">Download Resume (PDF)</a> • <a href="#contact">Contact</a>

---

## Highlights
- **Systems-first:** I build reusable gameplay systems (dialogue, quests, AI behaviors) that designers can iterate on quickly.
- **Production-minded:** I value reliability, clear docs, and profiling/debug tooling.
- **User empathy:** Even for dev tools, I focus on discoverability and fast feedback loops.

---

## Featured Projects {#projects}

{% assign featured = site.data.projects.active | concat: site.data.projects.completed %}
{% for project in featured %}
### {{ project.title }}
{{ project.description }}
{% if project.sub_projects %}
Sub-projects:
{% for sub in project.sub_projects %}
- [{{ sub.title }}]({{ '/projects/' | append: sub.slug | append: '/' | relative_url }})
{% endfor %}
{% endif %}
[Read the case study →]({{ '/projects/' | append: project.slug | append: '/' | relative_url }})

---
{% endfor %}

## Skills (snapshot)
**Languages:** C++, TypeScript/JavaScript  
**Engines/Frameworks:** Unreal Engine 5, HTML5/CSS  
**Tools:** Git, GitHub Actions, (add your favorites)

> Full details on the [Resume]({{ '/resume/' | relative_url }}).

---

## Recent Experience (snapshot)
**Most Recent Role — Company**  
- Built [system/tool] that [result/impact].  
- Partnered with designers to [collaboration outcome].

**Previous Role — Company**  
- Shipped [feature] that [metric/impact].  
- Improved [pipeline/tooling] which reduced [time/bugs].

See the full history on the [Resume]({{ '/resume/' | relative_url }}).

---

## Contact {#contact}
**Email:** <a href="mailto:{{ site.data.resume.email }}">{{ site.data.resume.email }}</a>
{% for profile in site.data.resume.socialMedia %}• **{{ profile.socialMedia }}:** <a href="{{ profile.link }}">{{ profile.link }}</a> {% endfor %}

_Last updated: {{ site.time | date: "%B %Y" }}_
