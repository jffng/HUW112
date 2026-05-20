#!/usr/bin/env python3
"""
Sync lecture notes from the Obsidian vault into this Jekyll site.

Workflow:
  1. Edit notes in Obsidian as normal (SECONDBRAIN/HUW112/).
  2. Run:  python3 sync.py
  3. Review, then:  git add -A && git commit -m "Update lecture notes" && git push

What it does:
  - Copies the dated lecture notes (files named like "5.21 — Title.md")
    into lectures/, converting Obsidian syntax to standard Markdown.
  - Rewrites  ![[image.png]]  embeds and copies the referenced images
    (found anywhere in the vault) into assets/lectures/.
  - Rewrites  [[Note]]  wikilinks into real links between lecture pages.
  - Adds Jekyll front matter, a page title, the date, and nav links.
  - Regenerates lectures/index.html as a landing page listing every note.

Only the dated lecture notes are published. Planning docs and other files
in the HUW112 folder are ignored.
"""

import re
import shutil
from datetime import date
from pathlib import Path

# --- Configuration ----------------------------------------------------------
YEAR = 2026
VAULT = Path.home() / "Documents" / "SECONDBRAIN"
NOTES_DIR = VAULT / "HUW112"
REPO = Path(__file__).resolve().parent
LECTURES_DIR = REPO / "lectures"
ASSETS_DIR = REPO / "assets" / "lectures"

# A lecture note's filename looks like:  "5.21 — Poetic Web.md"
DATED_NOTE = re.compile(r"^(\d+)\.(\d+) — (.+)\.md$")
MONTHS = ["", "January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def image_filename(name: str) -> str:
    """Slugify an image filename but keep its extension."""
    stem, _, ext = name.rpartition(".")
    return f"{slugify(stem)}.{ext.lower()}"


def find_in_vault(name: str) -> Path | None:
    """Obsidian resolves embeds vault-wide; mirror that by searching the vault."""
    for path in VAULT.rglob(name):
        if path.is_file():
            return path
    return None


def collect_notes():
    """Return list of dicts for every dated lecture note, sorted by date."""
    notes = []
    for md in NOTES_DIR.glob("*.md"):
        m = DATED_NOTE.match(md.name)
        if not m:
            continue
        month, day, title = int(m.group(1)), int(m.group(2)), m.group(3).strip()
        notes.append({
            "path": md,
            "stem": md.stem,                       # "5.21 — Poetic Web"
            "title": title,                        # "Poetic Web"
            "month": month,
            "day": day,
            "date_str": f"{MONTHS[month]} {day}, {YEAR}",
            "slug": f"{month:02d}-{day:02d}-{slugify(title)}",
        })
    notes.sort(key=lambda n: (n["month"], n["day"]))
    return notes


def convert(note, link_map):
    """Read an Obsidian note and return Jekyll-ready Markdown."""
    text = note["path"].read_text(encoding="utf-8")

    # ![[image.png]] or ![[image.png|320]]  ->  standard image, copy the file.
    def repl_embed(m):
        target = m.group(1).split("|")[0].strip()
        src = find_in_vault(target)
        if not src:
            print(f"  ! image not found, left as text: {target}")
            return f"*(missing image: {target})*"
        out_name = image_filename(target)
        shutil.copy2(src, ASSETS_DIR / out_name)
        return f"![{Path(target).stem}](../assets/lectures/{out_name})"

    text = re.sub(r"!\[\[([^\]]+)\]\]", repl_embed, text)

    # [[Note]] or [[Note|alias]]  ->  link to that lecture page, or plain text.
    def repl_link(m):
        target = m.group(1).split("|")[0].strip()
        alias = m.group(1).split("|")[-1].strip()
        slug = link_map.get(target)
        return f"[{alias}]({slug}.html)" if slug else alias

    text = re.sub(r"\[\[([^\]]+)\]\]", repl_link, text)

    text = text.strip()
    return (
        "---\n"
        "layout: default\n"
        f'title: "{note["title"]}"\n'
        "---\n\n"
        f"# {note['title']}\n\n"
        f"*{note['date_str']}* · [← All lectures](index.html)\n\n"
        f"{text}\n"
    )


def write_index(notes):
    items = "\n".join(
        f"- [{n['title']}]({n['slug']}.html) — *{MONTHS[n['month']]} {n['day']}*"
        for n in notes
    )
    (LECTURES_DIR / "index.md").write_text(
        "---\n"
        "layout: default\n"
        'title: "Lecture Notes"\n'
        "---\n\n"
        "# Lecture Notes\n\n"
        "Notes from each class meeting. If you missed a class, start here.\n\n"
        f"{items}\n\n"
        "[← Back to syllabus](../)\n",
        encoding="utf-8",
    )


def main():
    if not NOTES_DIR.is_dir():
        raise SystemExit(f"Notes folder not found: {NOTES_DIR}")

    # Fresh build: wipe generated output so deleted/renamed notes don't linger.
    if LECTURES_DIR.exists():
        shutil.rmtree(LECTURES_DIR)
    if ASSETS_DIR.exists():
        shutil.rmtree(ASSETS_DIR)
    LECTURES_DIR.mkdir(parents=True)
    ASSETS_DIR.mkdir(parents=True)

    notes = collect_notes()
    if not notes:
        raise SystemExit("No dated lecture notes found.")

    link_map = {n["stem"]: n["slug"] for n in notes}

    for n in notes:
        print(f"  {n['path'].name}  ->  lectures/{n['slug']}.html")
        (LECTURES_DIR / f"{n['slug']}.md").write_text(
            convert(n, link_map), encoding="utf-8"
        )

    write_index(notes)
    print(f"\nDone. {len(notes)} lecture notes synced to lectures/.")
    print("Next:  git add -A && git commit -m 'Update lecture notes' && git push")


if __name__ == "__main__":
    main()
