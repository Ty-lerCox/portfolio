---
title: Resume — {{ site.data.resume.name }}
layout: default
---

# Resume

[Download PDF]({{ '/resume/resume.pdf' | relative_url }})

## Summary
{{ site.data.resume.summary }}

## Skills
{% for group in site.data.resume.skills %}
- **{{ group.title }}:** {{ group.skills | join: ', ' }}
{% endfor %}

## Work Experience
{% for job in site.data.resume.workExperience %}
**{{ job.position }} — {{ job.company }} ({{ job.startYear | slice: 0,4 }}–{{ job.endYear }})**
{{ job.description }}
{% assign bullets = job.keyAchievements | split: '\\n' %}
{% for line in bullets %}
- {{ line }}
{% endfor %}
{% endfor %}

## Education
{% for edu in site.data.resume.education %}
**{{ edu.degree }} — {{ edu.school }}**
{% endfor %}

## Links
{% for profile in site.data.resume.socialMedia %}
- {{ profile.socialMedia }} — {{ profile.link }}
{% endfor %}
- Email — {{ site.data.resume.email }}
