---
layout: default
title: Home
---

<div class="hero">
  <h1>music.efpophis.net</h1>
  <p>The canonical home for my catalog: liner notes, lyrics, and links to stream/download elsewhere.</p>
</div>

<div class="grid">
  <div class="card">
    <h2>Projects</h2>
    <p>Organized by era/project to keep the catalog coherent (and future-proof).</p>
    <ul>
      {% for p in site.projects %}
        <li><a href="{{ p.url | relative_url }}"><strong>{{ p.title }}</strong></a> — {{ p.summary }}</li>
      {% endfor %}
    </ul>
  </div>

  <div class="card half">
    <h2>Latest</h2>
    <p>Pin whatever you want here: newest album, a featured track, or a short announcement.</p>
    <p class="kicker">Example embed slot</p>
    <div class="embed">
      <!-- Paste a YouTube/Audiomack/Audius iframe here -->
      <iframe height="180" src="about:blank"></iframe>
    </div>
  </div>

  <div class="card half">
    <h2>Quick links</h2>
    <div class="tagrow">
      <span class="tag"><a href="{{ '/albums/' | relative_url }}">Browse all albums</a></span>
      <span class="tag"><a href="{{ '/tracks/' | relative_url }}">Browse tracks / lyrics</a></span>
      <span class="tag"><a href="{{ '/about/' | relative_url }}">About</a></span>
    </div>
  </div>
</div>
