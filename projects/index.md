---
layout: page
title: Projects
subtitle: "Catalog organized by project/era."
---

<ul>
{% assign sorted = site.projects | sort: 'sort_order' %}
{% for p in sorted %}
  <li><a href="{{ p.url | relative_url }}"><strong>{{ p.title }}</strong></a> — {{ p.summary }}</li>
{% endfor %}
</ul>
