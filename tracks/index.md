---
layout: page
title: Tracks
subtitle: "Track pages with lyrics and notes."
---

{% comment %}
<ul>
{% assign sorted = site.tracks | sort: 'title' %}
{% for t in sorted %}
  <li>
    <a href="{{ t.url | relative_url }}"><strong>{{ t.title }}</strong></a>
    {% if t.album_title %} - ({{ t.album_title }}){% endif %}
  </li>
{% endfor %}
</ul>
{% endcomment %}

{% assign albums_sorted = site.albums | sort: "release_date" %}

{% for album in albums_sorted %}
  {% assign album_tracks = site.tracks | where: "album", album.slug | sort: "track_number" %}
  {% if album_tracks.size > 0 %}

## {{ album.title }}{% if album.release_date %} ({{ album.release_date | date: "%Y-%m-%d" }}){% endif %}

{% for track in album_tracks %}
{{ track.track_number }}. [{{ track.title }}]({{ track.url }}) — {{ track.artist }}
{% endfor %}

  {% endif %}
{% endfor %}