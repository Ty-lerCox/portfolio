---
title: Projects
layout: default
---

# Projects

Selected engineering work across full-stack products, developer platforms, observability, and game systems.

## Current

{% for project in site.data.projects.active %}
### [{{ project.title }}]({{ project.url | relative_url }})

{{ project.description }}

{% for tag in project.tags %}<span class="project-tag">{{ tag }}</span>{% endfor %}
{% endfor %}
## Earlier work

{% for project in site.data.projects.completed %}
### [{{ project.title }}]({{ project.url | relative_url }})

{{ project.description }}

{% for tag in project.tags %}<span class="project-tag">{{ tag }}</span>{% endfor %}
{% endfor %}
