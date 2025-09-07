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

<h2 id="contact">Contact</h2><p><strong>Email:</strong> <a href="mailto:{{ site.data.resume.email }}">{{ site.data.resume.email }}</a></p><ul>{% for profile in site.data.resume.socialMedia %}<li><strong>{{ profile.socialMedia }}:</strong> <a href="{{ profile.link }}">{{ profile.link }}</a></li>{% endfor %}</ul>

## Pinned Projects
