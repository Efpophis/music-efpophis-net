---
layout: page
title: Tracks
subtitle: "Track pages with lyrics and notes."
---

<ul>
{% assign sorted = site.tracks | sort: 'title' %}
{% for t in sorted %}
  <li>
    <a href="{{ t.url | relative_url }}"><strong>{{ t.title }}</strong></a>
    {% if t.album %} — <span class="meta">{{ t.album }}</span>{% endif %}
  </li>
{% endfor %}
</ul>
