# music.efpophis.net site template

This is a minimal, fast GitHub Pages (Jekyll) site intended to host:
- Project pages (e.g., The Redeemer Project)
- Album pages (with embedded players)
- Track pages (lyrics + notes)

## Quick start
1. Copy these files into your GitHub repo root.
2. In GitHub: Settings → Pages → Build and deployment → Source: **Deploy from a branch** → Branch: `main` (or `master`) → `/ (root)`.
3. Point your DNS for `music.efpophis.net` at GitHub Pages (CNAME) and add the custom domain in Settings → Pages.

## Editing content
- Projects live in `_projects/`
- Albums live in `_albums/`
- Tracks live in `_tracks/`

Each page is Markdown with YAML front matter. You can paste embed iframe snippets directly.

## Where to put images
- Place cover art in `assets/img/` and reference it in front matter:
  - `cover: /assets/img/orthodox-cover.jpg`

## Local dev (optional)
If you want to preview locally:
```bash
bundle install
bundle exec jekyll serve
```
Then open http://127.0.0.1:4000
