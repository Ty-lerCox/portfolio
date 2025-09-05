---
title: Tags
layout: default
---

# Tags

{% assign all = site.data.projects.active | concat: site.data.projects.completed %}
{% assign tag_list = '' | split: '' %}
{% for project in all %}
  {% assign tag_list = tag_list | concat: project.tags %}
  {% if project.sub_projects %}
    {% for sub in project.sub_projects %}
      {% assign tag_list = tag_list | concat: sub.tags %}
    {% endfor %}
  {% endif %}
{% endfor %}
{% assign tag_list = tag_list | uniq | sort %}

{% for tag in tag_list %}
- [{{ tag }}]({{ '/tags/' | append: tag | relative_url }})
{% endfor %}
