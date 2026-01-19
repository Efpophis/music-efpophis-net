
// ====== CONFIG ======
const BLOG_URL = "https://billcrossley.blogspot.com";
const MAX_POSTS = 5;

function renderBloggerFeed(data) {
const container = document.getElementById("news-feed");
const entries = (data.feed && data.feed.entry) ? data.feed.entry.slice(0, MAX_POSTS) : [];

if (!entries.length) {
  container.innerHTML = "<p>No updates yet.</p>";
  return;
}

const items = entries.map(e => {
  const title = e.title?.$t || "Untitled";
  const link = (e.link || []).find(l => l.rel === "alternate")?.href || "#";
  const published = e.published?.$t ? new Date(e.published.$t) : null;
  const dateStr = published ? published.toLocaleDateString() : "";

  return `<li>
    <a href="${link}" target="_blank" rel="noopener">${title}</a>
    <span class="news-date">${dateStr}</span>
  </li>`;
}).join("");

container.innerHTML = `<ul class="news-list">${items}</ul>`;
}

(function loadFeed() {
const s = document.createElement("script");
s.src = `${BLOG_URL}/feeds/posts/default?alt=json-in-script&callback=renderBloggerFeed`;
document.body.appendChild(s);
})();
