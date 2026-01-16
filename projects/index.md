---
layout: page
title: Projects
subtitle: "Catalog organized by project/era."
---

<ul>
{% for p in site.projects %}
  <li><a href="{{ p.url | relative_url }}"><strong>{{ p.title }}</strong></a> — {{ p.summary }}</li>
{% endfor %}
</ul>
