---
title: Portfolio — {{ site.data.resume.name }}
layout: home
image: /assets/img/social-card.svg
---

# {{ site.data.resume.name }}

{{ site.data.resume.summary }}

{% for group in site.data.resume.skills %}
{{ group.skills | join: ', ' }}
[{{ group.title }} Resume]({{ group.resume | relative_url }})
{% unless forloop.last %}
{% endunless %}
{% endfor %}

## Contact {#contact}
**Email:** <a href="mailto:{{ site.data.resume.email }}">{{ site.data.resume.email }}</a>
{% for profile in site.data.resume.socialMedia %}
- **{{ profile.socialMedia }}:** <a href="{{ profile.link }}">{{ profile.link }}</a>
{% endfor %}

## Pinned
