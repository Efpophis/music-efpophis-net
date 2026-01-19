---
layout: default
title: "Bill Crossley's Music Catalog"
---
<div class="hero"> 
  <h1>Bill's Music Page</h1>
  <p>The canonical home for my catalog: liner notes, lyrics, and links to stream/download elsewhere.</p>
  <p>All music is generated using <a href="https://suno.com">Suno</a> unless otherwise indicated.</p>
</div>

<div class="grid">
  <div class="card">
    <h2>Projects</h2>
    <p>Organized by era/project to keep the catalog coherent.</p>
    <ul>
      {% assign sorted = site.projects | sort: 'sort_order' %}
      {% for p in sorted %} 
        <li><a href="{{ p.url | relative_url }}"><strong>{{ p.title }}</strong></a> — {{ p.summary }}</li>
      {% endfor %}
    </ul>
  </div>

  <div class="card half">
    <h2>Latest News</h2>
    <div id="news-feed">
      <p>Loading updates ...</p>
      <script src="/assets/js/news.js"></script>
    </div>
  </div>

  <div class="card half">
    <h2>Quick links</h2>
    <div class="tagrow">
      <span class="tag"><a href="{{ '/albums/' | relative_url }}">Browse all albums</a></span>
      <span class="tag"><a href="{{ '/tracks/' | relative_url }}">Browse tracks / lyrics</a></span>
      <span class="tag"><a href="{{ '/about/' | relative_url }}">About</a></span>
    </div>
    <div class="tagrow"> 
      <span class="tag"><a href="https://youtube.com/@theredeemerprojectmetal" target=_blank>YouTube</a></span>
      <span class="tag"><a href="https://www.facebook.com/profile.php?id=61558951555423" target=_blank>FaceBook</a></span>
      <span class="tag"><a href="https://audiomack.com/billcrossley/albums" target=_blank>Audiomack</a></span>
    </div>
    <hr>
    <h2>License</h2>
    <p>Unless otherwise indicated, all works on this site are licensed under Creative Commons CC-BY-NC-ND 4.0 <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/" target=_blank>Some rights reserved.</a></p>
    <p>Short version: You can freely download, listen, make copies, and distribute everything here as long as you
    don't claim it as your own work, modfiy it, or use it to make money. See the link for details.</p>
  </div>
</div>
