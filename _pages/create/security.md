---
title: Security
permalink: /create/security
---

Publishing an OGC Blocks register is not just publishing data. Building a register can execute code — your own,
or code pulled in from a register you import — and every register you import extends what you're implicitly asking
consumers to trust. This page covers what to put in your `SECURITY.md`, what running transforms and plugins actually
means for security, and what to check before trusting a register you didn't build.

## `SECURITY.md`

Every register repository should carry a `SECURITY.md` alongside its `README.md` and `LICENSE`. At minimum, it
should state:

- **where to report a suspected security issue** — a monitored email address or a private reporting channel (e.g.
  [GitHub private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)), not a public issue tracker;
- **what's in scope** — this repository's own sources (`transforms.yaml`, `plugins.transforms`/`plugins.validators`
  declarations, CI/CD workflows, `bblocks-config.yaml`); most maintainers cannot vouch for imported registers, so
  say so explicitly rather than leaving it implied;
- **what a report should include** — the affected block identifier, the specific transform/plugin/import
  declaration if relevant, and whether the issue could propagate to registers that import this one.

[`bblock-template`](https://github.com/opengeospatial/bblock-template) does not yet ship a `SECURITY.md` — that
support is in progress and, once available, the tooling will create and keep one up to date for you automatically
(choosing the right variant depending on whether your repository lives under an OGC-controlled organization or not).
Until then, write one by hand; the structure above is the one the automated version will use, so nothing you write
now needs to be redone later.

## Code execution surface

A register with no code of its own can still execute code when it's built, from three sources:

- **`transforms.yaml`** — inline `python`, `node`, `jq`, `xslt`, SPARQL, SHACL-AF, or `semantic-uplift` logic, run
  automatically against matching example snippets during postprocessing (see [Transforms](transforms));
- **transform and validator plugins**, declared under `plugins.transforms` / `plugins.validators` in
  `bblocks-config.yaml` and installed via `pip`, which accepts any specifier `pip install` understands — including
  `git+https://...` URLs, i.e. code from anywhere the declaration points to;
- **cross-block `get_transformer` / `getTransformer` calls**, which can invoke a transform defined in a *different*
  block — including one reached through an import.

This means a register that declares no transforms of its own is not automatically free of executable content: it
may have inherited some through an import (see [Imports and trust](#imports-and-trust) below).

**How and when this code runs depends on the environment:**

- **In CI**, the postprocessor runs unattended. Declared transforms and plugins execute automatically with whatever
  access the CI job has — secrets, network, and write access to the publishing target. A slow or resource-heavy
  transform also inflates CI run time and cost.
- **Running locally**, the tooling asks for explicit confirmation before installing a plugin or executing Python or
  Node transform code. Don't script around this confirmation — it's the one point where a human actually looks at
  what's about to run.

Per-plugin virtualenv isolation prevents dependency conflicts between plugins and the postprocessor. It is **not** a
security boundary — a plugin runs with whatever access the process running it has, regardless of which virtualenv
it's in.

**Recommendations:**

- Review any new or changed `transforms.yaml` entry, and any new plugin declaration, with the same rigor as
  application code committed to the repository — because it is.
- Before adding or updating a `pip`/`git+https` plugin reference, check who maintains that source and when it was
  last reviewed.
- Never commit SPARQL push or other CI credentials (`sparql.push` in `bblocks-config.yaml`) to version control —
  use repository or organization secrets, and scope who can read them.
- Avoid broadening CI/CD workflow permissions beyond what postprocessing and publishing actually require.

## Imports and trust

`bblocks-config.yaml`'s `imports` list (see [Setting up imports](imports)) can reference any register URL, OGC or
not. Once imported, that register's `bblocks://` schema references, JSON-LD context, and SHACL shapes are all
inherited automatically — and any block in your repository can invoke a transform defined in it.

A few properties make an import's real footprint easy to underestimate:

- **Imports are transitive.** Importing one register also pulls in whatever *that* register imports, recursively.
  Your actual dependency set is a transitive closure, not the list you wrote down in `imports`.
- **Silence is still an import.** If `imports` is omitted from `bblocks-config.yaml`, the main OGC register is
  imported by default, along with everything it imports. There's no such thing as importing nothing by accident —
  if you want that, declare `imports: []` explicitly.
- **Imports aren't pinned.** Entries resolve by URL at build time, with no version, commit, or digest pinning and
  no lockfile. The same `bblocks-config.yaml` rebuilt tomorrow may pull in different content from the same URL.

Because of this, review an import the same way you'd review a new dependency in any other project: check who
maintains it and whether it's still active before adding it, and periodically re-check imports you already have —
not just when you add them.

## Checking a register before you trust it

You don't have to take a register's word for what it does. Its published `register.json` and related output make
several things checkable without reading its source repository at all:

- **which transform and validator plugins it declares**, including the exact `pip` specifier each was installed
  from;
- **the code each block's declared transforms would run**, published alongside the blocks themselves;
- **its import edges**, and by resolving those recursively, its full transitive closure;
- **the license** applying to the register and to each block, via the `license` object in `bblocks-config.yaml` or
  a block's own `bblock.json` (see [Building Block metadata](metadata#links-and-references)).

The [OGC Blocks meta-register catalog](http://defs-dev.opengis.net/bblocks-meta-register) — and its MCP server, for
tools that support it — indexes this across every register it knows about, so you can look up a register's declared
plugins, imports, and license without cloning it.

What none of this tells you: whether any of that content was actually *reviewed*, by whom, or when, and whether an
import's target has changed since you last checked it built the same way. That's still on you to track — a
register's published metadata tells you what it does, not whether anyone can vouch for it.
