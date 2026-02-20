#!/usr/bin/env python
import argparse
import re
import sys
import unicodedata
from pathlib import Path
import shutil

from mutagen.flac import FLAC  # pip install mutagen
 
def yaml_quote(s: str) -> str:
    """
    Safely quote a string for YAML front matter.
    Handles :, #, quotes, etc.
    """
    if s is None:
        return '""'
    s = str(s)
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    s = re.sub(r"^-+|-+$", "", s)
    return s or "untitled"


def first_tag(audio: FLAC, *keys: str) -> str | None:
    for k in keys:
        if k in audio and audio[k]:
            v = (audio[k][0] or "").strip()
            if v:
                return v
    return None


def parse_track_number(s: str | None) -> int | None:
    if not s:
        return None
    m = re.match(r"^\s*(\d+)", s)  # handles "3" or "03" or "3/12"
    if not m:
        return None
    try:
        return int(m.group(1))
    except ValueError:
        return None


def safe_write(path: Path, content: str, force: bool) -> bool:
    if path.exists() and not force:
        print(f"SKIP (exists): {path}")
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"WROTE: {path}")
    return True


def render_track_md(
    title: str,
    track_slug: str,
    track_number: int,
    album_slug: str,
    album_title: str,
    artist: str,
    embed_hint: str | None,
) -> str:
    embed_src_hint = embed_hint or "PASTE_EMBED_IFRAME_HERE"
    return f"""---
layout: track
title: {yaml_quote(title)}
slug: {track_slug}
album: {album_slug}
album_title: {yaml_quote(album_title)}
artist: {yaml_quote(artist)}
track_number: {track_number}

embed_html: |
  <!-- Paste the Audiomack TRACK embed iframe here -->
  <!-- Example:
  <iframe src="https://audiomack.com/embed/song/ARTIST/TRACKSLUG" width="100%" height="110" frameborder="0" scrolling="no"></iframe>
  -->
  {embed_src_hint}
---

<!-- Lyrics / commentary go here. -->

"""


def main():
    ap = argparse.ArgumentParser(
        description="Add tracks to an existing album on the Jekyll site by generating _albums/_tracks and copying cover art."
    )
    ap.add_argument("--title", required=True, help="Album title (display).")
#   ap.add_argument("--project", required=True, help="Project key (e.g. the-redeemer-project, solo-works).")
    ap.add_argument("--artist", required=True, help="Artist display name (e.g. Bill Crossley).")
    ap.add_argument("--year", default=None, help="Year (optional).")
    ap.add_argument("--album-slug", default=None, help="Album slug override. Default derived from title.")
#    ap.add_argument("--cover", default="cover.jpg", help="Cover filename in current folder (default: cover.jpg).")
    ap.add_argument("--repo-root", default=".", help="Repo root (default: current directory).")
    ap.add_argument("--tracks-out", default="_tracks", help="Tracks output dir under repo root (default: _tracks).")
 #   ap.add_argument("--albums-out", default="_albums", help="Albums output dir under repo root (default: _albums).")
#    ap.add_argument("--assets-img", default="assets/img", help="Images dir under repo root (default: assets/img).")
    ap.add_argument("--force", action="store_true", help="Overwrite existing generated files.")
    ap.add_argument("--dry-run", action="store_true", help="Print what would happen, but write nothing.")
    args = ap.parse_args()

    album_dir = Path(".").resolve()
    repo_root = Path(args.repo_root).expanduser().resolve()

    flacs = sorted([p for p in album_dir.iterdir() if p.is_file() and p.suffix.lower() == ".flac"])
    if not flacs:
        print("ERROR: No .flac files found in the current directory.", file=sys.stderr)
        sys.exit(2)

    album_slug = args.album_slug or slugify(args.title)

    #albums_out = (repo_root / args.albums_out).resolve()
    tracks_out = (repo_root / args.tracks_out).resolve()
    #assets_img = (repo_root / args.assets_img).resolve()

    #cover_src = album_dir / args.cover
    #if not cover_src.exists():
    #    print(f"WARNING: cover file not found: {cover_src} (continuing without copying cover)", file=sys.stderr)
    #    cover_ext = ".jpg"
    #    cover_dest_rel = f"/assets/img/{album_slug}.jpg"
    #    cover_dest_abs = assets_img / f"{album_slug}.jpg"
    #    will_copy_cover = False
    #else:
    #    cover_ext = cover_src.suffix.lower() or ".jpg"
    #    cover_dest_rel = f"/assets/img/{album_slug}{cover_ext}"
    #    cover_dest_abs = assets_img / f"{album_slug}{cover_ext}"
    #    will_copy_cover = True

    # Build track list from tags
    tracks = []
    for idx, p in enumerate(flacs, start=1):
        try:
            audio = FLAC(p)
        except Exception as e:
            print(f"WARNING: Could not read tags from {p.name}: {e}", file=sys.stderr)
            audio = None

        if audio:
            title = first_tag(audio, "TITLE", "title") or p.stem
            tn = parse_track_number(first_tag(audio, "TRACKNUMBER", "tracknumber"))
        else:
            title = p.stem
            tn = None

        track_number = tn if tn is not None else idx
        track_slug = f"{track_number:02d}-{slugify(title)}"
        tracks.append((track_number, title, track_slug, p.name))

    tracks.sort(key=lambda x: (x[0], x[3].lower()))

    #album_md_path = albums_out / f"{album_slug}.md"

    # Write album markdown
    #album_md = render_album_md(
    #    title=args.title,
    #    album_slug=album_slug,
    #    project=args.project,
    #    artist=args.artist,
    #    year=args.year,
    #    cover_dest=cover_dest_rel,
    #    embed_src_hint=None,
    #)

    # Generate track markdown files
    writes = []
    for track_number, title, track_slug, src_name in tracks:
        md_path = tracks_out / f"{track_slug}.md"
        md = render_track_md(
            title=title,
            track_slug=track_slug,
            track_number=track_number,
            album_slug=album_slug,
            album_title=args.title,
            artist=args.artist,
            embed_hint=None,
        )
        writes.append((md_path, md, src_name))

    # Execute
    if args.dry_run:
        print(f"DRY RUN. Album dir: {album_dir}")
#        print(f"Would create album: {album_md_path}")
#        if will_copy_cover:
#            print(f"Would copy cover: {cover_src} -> {cover_dest_abs}")
#        else:
#            print("Would not copy cover (missing).")
        for md_path, _, src in writes:
            print(f"Would create track: {md_path} (from {src})")
        sys.exit(0)

  #  safe_write(album_md_path, album_md, args.force)

    # Copy cover
 #   if will_copy_cover:
#        cover_dest_abs.parent.mkdir(parents=True, exist_ok=True)
#        if cover_dest_abs.exists() and not args.force:
#            print(f"SKIP (exists): {cover_dest_abs}")
#        else:
#            shutil.copy2(cover_src, cover_dest_abs)
#            print(f"COPIED: {cover_src.name} -> {cover_dest_abs}")

    # Write tracks
    created = 0
    for md_path, md, src in writes:
        if safe_write(md_path, md, args.force):
            created += 1

    print(f"\nDone. Generated {created} track file(s).")
    print("Next steps:")
#    print(f"- Edit {album_md_path} and paste album liner notes + album embed iframe.")
    print("- Edit each _tracks/*.md and paste lyrics/commentary + track embed iframes.")


if __name__ == "__main__":
    main()
