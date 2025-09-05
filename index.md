---
title: Portfolio — {{ site.data.resume.name }}
layout: home
image: /assets/img/social-card.svg
---

# {{ site.data.resume.name }}
_{{ site.data.resume.position }}_

{{ site.data.resume.summary }}

---

## Core Skills {#skills}
{% for group in site.data.resume.skills %}
### {{ group.title }}
{{ group.skills | join: ', ' }}
[{{ group.title }} Resume]({{ group.resume | relative_url }})
{% unless forloop.last %}
---
{% endunless %}
{% endfor %}

---

## Contact {#contact}
**Email:** <a href="mailto:{{ site.data.resume.email }}">{{ site.data.resume.email }}</a>
{% for profile in site.data.resume.socialMedia %}
- **{{ profile.socialMedia }}:** <a href="{{ profile.link }}">{{ profile.link }}</a>
{% endfor %}

_Last updated: {{ site.time | date: "%B %Y" }}_

## Latest Posts
