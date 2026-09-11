#!/usr/bin/env python3
"""
Build the FTS5 search index consumed by the client-side search widget
(assets/js/search.js).

Walks `_data/navigation.yml` (the same source of truth used for the site's
sidebar nav) to find which pages to index, renders each page's markdown body
to HTML via `tools/render_markdown.rb` (real kramdown, the same settings
Jekyll builds with -- see that script), splits the HTML on <h2> into
sections, and writes a SQLite database with two FTS5 virtual tables:
`search_titles` (page_title, section_title, url) and `search_body`
(page_title, section_title, body, url) -- see .claude/search-plan.md for why
titles get their own table rather than sharing one with body text.

Rendering through actual kramdown (rather than approximating markdown parsing
in Python) means heading ids/anchors match exactly what the built site
produces, and section text is extracted by walking the parsed HTML tree
(BeautifulSoup) rather than by regex.

Known limitation: page content is Liquid-preprocessed by Jekyll before
kramdown ever sees it (includes, `{{ site.* }}`, capture blocks, etc.). This
script does not run the Liquid engine -- it strips `{% ... %}` / `{{ ... }}`
tags outright before rendering. For the two pages that use Liquid for more
than simple substitution (`_pages/create/validation.md`'s
capture/markdownify notice, `_pages/create/postprocessing.md`'s
`{{ secrets.* }}` placeholders), the indexed text will be a close but
imperfect match for the rendered page.

Output:
  - assets/search/search-index.<hash>.sqlite  (gitignored build artifact;
    any stale search-index.*.sqlite in that dir is removed first)
  - _data/search_index.yml  ({filename: search-index.<hash>.sqlite}), so the
    client can load the current hashed filename without manual cache-busting

Usage:
  python3 tools/build_search_index.py [--repo-root PATH]

Run this before `jekyll serve`/`jekyll build` (also wired into CI, see
.github/workflows/jekyll.yml). Requires: PyYAML, beautifulsoup4, and a Ruby +
`bundle install` environment (uses this repo's own Gemfile.lock, so the
kramdown version matches exactly what Jekyll builds with).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

import yaml
from bs4 import BeautifulSoup, NavigableString, Tag

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?\n)---\s*\n", re.DOTALL)
LIQUID_TAG_RE = re.compile(r"\{%.*?%\}", re.DOTALL)
LIQUID_VAR_RE = re.compile(r"\{\{.*?\}\}", re.DOTALL)
WHITESPACE_RE = re.compile(r"\s+")
# Cosmetic cleanup of the plain text BeautifulSoup extracts: get_text(" ", ...)
# needs a separator to keep word boundaries between block elements (table
# cells, list items) from running together, but that same separator also
# inserts spurious spaces around inline punctuation (e.g. inline `code`
# wrapped in parens: "Profiling ( profileOf )"). Tidy that up after the fact
# rather than trying to special-case it during extraction.
SPACE_BEFORE_PUNCT_RE = re.compile(r"\s+([,.:;!?)])")
SPACE_AFTER_OPEN_PAREN_RE = re.compile(r"([(])\s+")


def tidy_text(text: str) -> str:
    text = collapse_whitespace(text)
    text = SPACE_BEFORE_PUNCT_RE.sub(r"\1", text)
    text = SPACE_AFTER_OPEN_PAREN_RE.sub(r"\1", text)
    return text


def read_frontmatter(text: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, text[m.end():]


def strip_liquid(text: str) -> str:
    """Drop Liquid tags/variables before handing the body to kramdown (which
    doesn't understand Liquid). See the module docstring's known limitation
    for the couple of pages where this loses real content."""
    text = LIQUID_TAG_RE.sub(" ", text)
    text = LIQUID_VAR_RE.sub(" ", text)
    return text


def render_bodies(repo_root: Path, pages: list[dict]) -> dict[str, str]:
    """Batch-render page bodies to HTML via real kramdown (tools/render_markdown.rb),
    matching Jekyll's own build settings. Returns {path: html}."""
    script = repo_root / "tools" / "render_markdown.rb"
    payload = json.dumps([{"path": p["path"], "body": p["body"]} for p in pages])
    proc = subprocess.run(
        ["bundle", "exec", "ruby", str(script)],
        input=payload,
        capture_output=True,
        text=True,
        cwd=repo_root,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"render_markdown.rb failed:\n{proc.stderr}")
    return {row["path"]: row["html"] for row in json.loads(proc.stdout)}


def collapse_whitespace(text: str) -> str:
    return WHITESPACE_RE.sub(" ", text).strip()


def split_sections(html: str) -> list[tuple[str | None, str | None, str]]:
    """Walk the rendered HTML tree and split on <h2> into
    (heading_text_or_None, heading_id_or_None, plain_text) chunks, using
    BeautifulSoup rather than regex so nested/edge-case markup (tables,
    nested emphasis, embedded HTML) is handled correctly."""
    soup = BeautifulSoup(html, "html.parser")
    top_level = [
        el for el in soup.contents
        if not (isinstance(el, NavigableString) and not el.strip())
    ]

    sections: list[tuple[str | None, str | None, str]] = []
    heading_text: str | None = None
    heading_id: str | None = None
    body_parts: list[Tag] = []

    def flush() -> None:
        text = tidy_text(
            " ".join(part.get_text(" ", strip=True) for part in body_parts)
        )
        if text or heading_text is not None:
            sections.append((heading_text, heading_id, text))

    for el in top_level:
        if isinstance(el, Tag) and el.name == "h2":
            flush()
            heading_text = tidy_text(el.get_text(" ", strip=True))
            heading_id = el.get("id")
            body_parts = []
        else:
            if isinstance(el, Tag):
                body_parts.append(el)
    flush()
    return sections


def flatten_nav(nav: dict) -> list[dict]:
    pages = []
    for section in nav.get("docs", []) or []:
        for child in section.get("children", []) or []:
            if child.get("url"):
                pages.append(child)
    return pages


def build_permalink_map(pages_dir: Path) -> dict[str, Path]:
    mapping: dict[str, Path] = {}
    for path in sorted(pages_dir.rglob("*.md")):
        fm, _ = read_frontmatter(path.read_text(encoding="utf-8"))
        permalink = fm.get("permalink")
        if permalink:
            mapping[permalink.rstrip("/")] = path
    return mapping


def build_index(repo_root: Path) -> Path:
    pages_dir = repo_root / "_pages"
    nav_path = repo_root / "_data" / "navigation.yml"
    search_dir = repo_root / "assets" / "search"
    data_dir = repo_root / "_data"

    nav = yaml.safe_load(nav_path.read_text(encoding="utf-8"))
    nav_pages = flatten_nav(nav)
    permalink_map = build_permalink_map(pages_dir)

    resolved: list[dict] = []
    missing = []
    for nav_page in nav_pages:
        url = nav_page["url"].rstrip("/")
        path = permalink_map.get(url)
        if path is None:
            missing.append(url)
            continue
        text = path.read_text(encoding="utf-8")
        fm, body = read_frontmatter(text)
        page_title = fm.get("title") or nav_page.get("title") or url
        resolved.append({
            "path": str(path),
            "url": url,
            "page_title": page_title,
            "body": strip_liquid(body),
            "source_path": path,
        })

    if missing:
        print(f"warning: {len(missing)} nav url(s) had no matching page "
              f"permalink, skipped: {missing}", file=sys.stderr)

    html_by_path = render_bodies(repo_root, resolved)

    rows: list[tuple[str, str, str, str]] = []
    for page in resolved:
        html = html_by_path[page["path"]]
        for heading_text, heading_id, text in split_sections(html):
            if heading_text is None:
                # Top-level content with no h2 above it yet (the page's
                # intro, or a whole short page with no headings at all).
                # Copy page_title in here instead of leaving it blank, so
                # this chunk gets the section_title bm25 weight too -- a
                # match against what the page is actually about shouldn't
                # rank behind an incidental heading mention on some other
                # page just because it landed in the "wrong" column.
                section_title = page["page_title"]
                section_url = page["url"]
            else:
                section_title = heading_text
                section_url = f"{page['url']}#{heading_id}" if heading_id else page["url"]
            rows.append((page["page_title"], section_title, text, section_url))

    # Content hash over the indexed source files, for cache-busting.
    hasher = hashlib.sha256()
    for page in sorted(resolved, key=lambda p: p["path"]):
        hasher.update(page["source_path"].read_bytes())
    content_hash = hasher.hexdigest()[:12]

    search_dir.mkdir(parents=True, exist_ok=True)
    for stale in search_dir.glob("search-index.*.sqlite"):
        stale.unlink()

    db_filename = f"search-index.{content_hash}.sqlite"
    db_path = search_dir / db_filename
    con = sqlite3.connect(db_path)
    # Two tables, queried in sequence by the client (title tier first, body
    # tier as fallback) -- see .claude/search-plan.md ("Plan: split into a
    # title index + a body index"). SQLite FTS5's bm25() normalizes term
    # frequency against a *row's* total token count across every column, not
    # just the matched column (confirmed against the FTS5 docs' own bm25()
    # formula) -- so on a single shared table, a title match on a row with a
    # long body always scores worse than the same match on a short-bodied
    # row, and no column weight can fix that. Splitting the title-only
    # signal into its own table (short, uniform-length rows) sidesteps the
    # problem entirely instead of fighting it.
    #
    # search_titles has no `body` column at all. search_body carries
    # page_title/section_title too, but UNINDEXED -- confirmed empirically
    # that UNINDEXED columns aren't tokenized and so don't count towards
    # `|D|`/`avgdl` either, so they're free to include purely so the widget
    # can render a body-tier result's title without a second lookup.
    con.execute(
        "CREATE VIRTUAL TABLE search_titles USING fts5("
        "page_title, section_title, url UNINDEXED)"
    )
    con.execute(
        "CREATE VIRTUAL TABLE search_body USING fts5("
        "page_title UNINDEXED, section_title UNINDEXED, body, url UNINDEXED)"
    )
    con.executemany(
        "INSERT INTO search_titles (page_title, section_title, url) VALUES (?, ?, ?)",
        [(pt, st, url) for pt, st, _body, url in rows],
    )
    con.executemany(
        "INSERT INTO search_body (page_title, section_title, body, url) VALUES (?, ?, ?, ?)",
        rows,
    )
    con.commit()
    con.close()

    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "search_index.yml").write_text(
        yaml.safe_dump({"filename": db_filename}, sort_keys=False),
        encoding="utf-8",
    )

    print(f"Indexed {len(rows)} sections from {len(resolved)} pages "
          f"-> {db_path.relative_to(repo_root)}")
    return db_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root", type=Path, default=Path(__file__).resolve().parent.parent
    )
    args = parser.parse_args()
    build_index(args.repo_root)


if __name__ == "__main__":
    main()
