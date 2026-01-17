---
layout: page
title: Albums
subtitle: "All releases in one list, sorted by release date."
---

<ul>
{% assign sorted = site.albums | sort: 'release_date' %}
{% for a in sorted %}
  <li>
    <a href="{{ a.url | relative_url }}"><strong>{{ a.title }}</strong></a>
    {% if a.release_date %} — {{ a.release_date | date: '%Y-%m-%d' }}{% endif %}
    {% if a.artist %} — {{ a.artist }}{% endif %}
  </li>
{% endfor %}
</ul>
