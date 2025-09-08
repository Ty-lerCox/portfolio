---
title: Projects
layout: default
---

# Projects

A curated set of systems and apps. Each write-up is a quick read with code and outcomes.

## Active
{% for project in site.data.projects.active %}
- **[{{ project.title }}]({{ '/projects/' | append: project.slug | append: '/' | relative_url }})** — {{ project.description }}
  
  Tags:
  {% for tag in project.tags %}
  [{{ tag }}]({{ '/project-tags/' | append: tag | relative_url }}){% unless forloop.last %}, {% endunless %}
  {% endfor %}
  {% if project.sub_projects %}
  - Sub-projects:
    {% for sub in project.sub_projects %}
    - [{{ sub.title }}]({{ '/projects/' | append: sub.slug | append: '/' | relative_url }})
    {% endfor %}
  {% endif %}
{% endfor %}

## Completed
{% for project in site.data.projects.completed %}
- **[{{ project.title }}]({{ '/projects/' | append: project.slug | append: '/' | relative_url }})** — {{ project.description }}
  
  Tags:
  {% for tag in project.tags %}
  [{{ tag }}]({{ '/project-tags/' | append: tag | relative_url }}){% unless forloop.last %}, {% endunless %}
  {% endfor %}
{% endfor %}
