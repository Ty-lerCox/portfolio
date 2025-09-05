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

## Projects {#projects}

### Active
{% for project in site.data.projects.active %}
#### {{ project.title }}
{{ project.description }}
Tags: {% for tag in project.tags %}[{{ tag }}]({{ '/tags/' | append: tag | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}
{% if project.sub_projects %}
Sub-projects:
{% for sub in project.sub_projects %}
- [{{ sub.title }}]({{ '/projects/' | append: sub.slug | append: '/' | relative_url }})
{% endfor %}
{% endif %}
[Read the case study →]({{ '/projects/' | append: project.slug | append: '/' | relative_url }})

---
{% endfor %}

### Completed
{% for project in site.data.projects.completed %}
#### {{ project.title }}
{{ project.description }}
Tags: {% for tag in project.tags %}[{{ tag }}]({{ '/tags/' | append: tag | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}
[Read the case study →]({{ '/projects/' | append: project.slug | append: '/' | relative_url }})

---
{% endfor %}

## Skills (snapshot)
{% assign group = site.data.resume.skills[0] %}
**{{ group.title }}:** {{ group.skills | slice: 0,5 | join: ', ' }}{% if group.skills.size > 5 %}, ...{% endif %}

> Full details on the [Resume]({{ '/resume/' | relative_url }}).

---

## Recent Experience (snapshot)
{% assign job = site.data.resume.workExperience[0] %}
**{{ job.position }} — {{ job.company }}**
{% assign bullets = job.keyAchievements | split: '\n' | slice: 0,2 %}
{% for line in bullets %}
- {{ line }}
{% endfor %}

See the full history on the [Resume]({{ '/resume/' | relative_url }}).

---

## Contact {#contact}
**Email:** <a href="mailto:{{ site.data.resume.email }}">{{ site.data.resume.email }}</a>
{% for profile in site.data.resume.socialMedia %}
- **{{ profile.socialMedia }}:** <a href="{{ profile.link }}">{{ profile.link }}</a>
{% endfor %}

_Last updated: {{ site.time | date: "%B %Y" }}_

