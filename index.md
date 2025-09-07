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

<h2 id="contact">Contact</h2><p>{% assign sep='' %}{% assign em=site.data.resume.email | default: '' | strip %}{% if em != '' %}<a href="mailto:{{ em }}">Email</a>{% assign sep=' · ' %}{% endif %}{% for profile in site.data.resume.socialMedia %}{% assign link=profile.link | default: '' | strip %}{% if link != '' and link | downcase != 'none' %}{{ sep }}<a href="{{ link }}">{{ profile.socialMedia }}</a>{% assign sep=' · ' %}{% endif %}{% endfor %}</p>
