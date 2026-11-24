#!/usr/bin/env python3
"""Check internal links, images and anchors in the built Jekyll site.

Usage: python3 tools/check_links.py [site_dir] [--baseurl /base]

The site must have been built with the same --baseurl. Use a non-empty one,
otherwise root-absolute links that miss the base path cannot be detected.
External links are not checked. Exits with status 1 if anything is broken.
"""
import argparse
import pathlib
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlsplit

HOST = "site.invalid"
# Links emitted by the remote theme that we have no control over
IGNORED = {("404.html", "#main")}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.anchors.update(attrs[k] for k in ("id", "name") if attrs.get(k))
        self.links.extend(attrs[k] for k in ("href", "src") if attrs.get(k))


def find_target(root, path):
    """Resolve a path the way GitHub Pages does (extensionless URLs included)."""
    if not path or path.endswith("/"):
        candidates = [root / path / "index.html"]
    else:
        candidates = [root / path, root / f"{path}.html", root / path / "index.html"]
    return next((c for c in candidates if c.is_file()), None)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("site_dir", nargs="?", default="_site", type=pathlib.Path)
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()
    root = args.site_dir
    base = args.baseurl.rstrip("/")

    pages = {}
    for file in root.rglob("*.html"):
        page = PageParser()
        page.feed(file.read_text(encoding="utf-8"))
        pages[file] = page
    if not pages:
        sys.exit(f"No HTML files found in {root}")

    broken = set()
    for file, page in pages.items():
        name = file.relative_to(root).as_posix()
        short = name.removesuffix("index.html") if name.endswith("index.html") else name.removesuffix(".html")
        page_url = f"https://{HOST}{base}/{short}"
        for link in page.links:
            url = urlsplit(urljoin(page_url, link))
            if url.netloc != HOST or (name, link) in IGNORED:
                continue
            if not (url.path == base or url.path.startswith(f"{base}/")):
                broken.add((name, link, "missing base URL"))
                continue
            target = find_target(root, unquote(url.path[len(base):]).lstrip("/"))
            if target is None:
                broken.add((name, link, "target not found"))
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].anchors:
                broken.add((name, link, "anchor not found"))

    for name, link, reason in sorted(broken):
        print(f"{name}: {link} ({reason})")
    print(f"{len(broken)} broken link(s) in {len(pages)} page(s)")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
