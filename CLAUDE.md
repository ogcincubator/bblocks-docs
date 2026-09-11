# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is the **OGC Building Blocks (bblocks) documentation site**: a Jekyll static site published to
https://ogcincubator.github.io/bblocks-docs via GitHub Pages. It documents the OGC Building Blocks framework
itself (how to author, publish, and consume "bblocks" registers) — it is not a bblocks register.

## Commands

Build/serve locally (requires Ruby + Bundler):

```
bundle exec jekyll serve
```

Site is then available at `http://127.0.0.1:4000/`. Do not start this server proactively — ask the user first,
since they often already have one running.

Before building/serving, (re)generate the docs search index — the site references
`site.data.search_index.filename`, and without it the search box in the masthead has nothing to query
(fetches 404 silently rather than erroring the build):

```
python3 tools/build_search_index.py
```

Requires PyYAML and beautifulsoup4 (Python) plus a `bundle install`'d Ruby environment (it shells out to
`tools/render_markdown.rb` to render page bodies through the same kramdown Jekyll uses). Outputs
`assets/search/search-index.<hash>.sqlite` and `_data/search_index.yml` — both gitignored build artifacts,
regenerated on every run. Wired into CI in `.github/workflows/jekyll.yml` before the Jekyll build step. See
`.claude/search-plan.md` for the design/tuning history behind the search feature.

`build-all-docs.py` is a local, personal-use script (untracked, not part of the site or its build). It
concatenates all doc pages into a single `all-bblocks-docs.md` for the user's own convenience (e.g. pasting into
another tool). It has no bearing on the Jekyll site, CI, or published output — ignore it unless the user
specifically asks about it.

There is no test suite or linter configured for this repo.

## Architecture / content structure

- `_pages/`: all documentation content, organized into subfolders that map to top-level nav sections:
  `overview/` (concepts), `usecases/`, `build/` (quick start / local build / GitHub setup / contributing),
  `use/` (consuming published bblocks), `create/` (authoring bblocks — the largest section: metadata, schema,
  examples, validation, transforms, semantic uplift, imports, extension points, security, etc.).
- `_data/navigation.yml`: the single source of truth for sidebar structure and page order (`docs:` list of
  sections, each with `children` of `{title, url}`). A page's presence here — not its file location — determines
  whether/where it shows up in the site nav and in `all-bblocks-docs.md`.
- Every page under `_pages/` needs Jekyll frontmatter with at least `title`; `permalink` is used for pages
  referenced by a stable/short URL (e.g. `_pages/create/index.md` has `permalink: /create`). Internal links
  between docs pages use relative paths (e.g. `../build/local`, `imports`, `#anchor`).
- `_config.yml`: Jekyll config. Uses the **remote theme** `mmistakes/minimal-mistakes@4.24.0` (Minimal Mistakes),
  with `sidebar.nav: docs` applied globally via `defaults`, so every page automatically gets the `docs` nav
  from `_data/navigation.yml` in its sidebar.
- `design/`: standalone design notes (architecture, versioning, agent federation) — not part of the built site
  nav, kept as reference/working documents.
- `.github/workflows/jekyll.yml`: CI/CD — builds with Jekyll on push to `master` and deploys to GitHub Pages.
  No test job; a successful `jekyll build` is the only gate.

## Content conventions

- This site documents a companion ecosystem of tools/repos (e.g. `bblock-template`, the postprocessing tooling,
  bblocks registers created by others). When writing docs, prefer linking to those external repos/tools rather
  than duplicating their reference docs here.
- Docs frequently reference concrete file/property names from the bblocks framework itself (e.g.
  `bblocks-config.yaml`, `_sources/`, identifier prefixes) — keep terminology consistent with existing pages in
  `_pages/create/` when adding related content.
