# OGC Building Blocks — Versioning Scheme

## Introduction

OGC Building Blocks (bblocks) are reusable data components combining JSON Schema, JSON-LD contexts, SHACL rules, examples, and documentation. They are published in registers and referenced by other bblocks, applications, and data specifications.

This document describes a versioning scheme for bblocks that allows registers to host multiple versions of the same block simultaneously and allows consumers to declare which version they depend on. It is designed to be fully backward-compatible with the existing unversioned layout.

---

## Rationale

Building Blocks currently carry a `version` metadata attribute in `bblock.json`, but this is informational only. There is no mechanism to:

- publish multiple versions of the same block side-by-side in a single register
- reference a specific version of a block from a schema or context
- guarantee that a consumer always gets a compatible version of a dependency, even as the block evolves

Without versioning, any change to a block potentially affects all consumers silently. This is manageable while the ecosystem is small, but becomes a stability risk as adoption grows and blocks are reused across organisations.

The goal of this scheme is to give definers control over what they publish and when, and to give consumers predictable, stable references — while keeping the barrier to entry low for registers that do not yet need versioning.

---

## Concepts

### Versioned vs. unversioned blocks

A block is either **unversioned** (the existing layout: a single `bblock.json` representing the current state) or **versioned** (multiple `@`-prefixed subdirectories, each representing a discrete published version). A block cannot be both at the same time.

Unversioned blocks continue to work exactly as today. Versioning is opt-in.

### What a version is

A version is a snapshot of a block's artifacts — its schema, JSON-LD context, examples, transforms, and metadata — at a point in time. Versions are named using a `major[.minor[.patch]]` format (e.g., `1`, `1.2`, `1.2.3`). Definers choose the level of granularity that fits their release cadence.

### Referencing versions

Consumers reference a specific version of a block using the `bblocks://` URI scheme:

```
bblocks://ogc.geo.features.feature          ← unversioned (always latest)
bblocks://ogc.geo.features.feature/1        ← latest within 1.x.x
bblocks://ogc.geo.features.feature/1.2      ← latest within 1.2.x
bblocks://ogc.geo.features.feature/1.2.3    ← exact version
```

A less specific version reference (e.g., `/1`) resolves to the latest available version within that range. An unversioned reference always resolves to the latest, regardless of what versioned directories exist.

---

## Architecture

### Directory layout

Versioned block content lives in `@`-prefixed subdirectories inside the block's source directory. When versioned subdirectories are present, no `bblock.json` may exist at the same level — a block is either fully versioned or fully unversioned.

```
_sources/
  a/
    b/
      c/
        @1/
          bblock.json
          schema.yaml
          context.jsonld
        @1.2/
          bblock.json
          schema.yaml          ← updated schema
          # no context.jsonld — @1.2/bblock.json references ../@1/context.jsonld
        @2/
          bblock.json
          schema.yaml
          context.jsonld
```

Artifacts that do not change between versions do not need to be duplicated. A versioned `bblock.json` can reference files from sibling version directories using relative paths (e.g., `"ldContext": "../@1/context.jsonld"`). These are direct file references.

### `register.json` structure

Each block entry in `register.json` gains a `versions` map. The top-level entry continues to represent the **synthesised latest** (the highest available version), for backward compatibility with existing tooling. The latest version is also included as an entry in `versions` under its own key, so that new tooling has a single, consistent lookup method for all available versions.

```json
{
  "identifier": "ogc.geo.features.feature",
  "version": "2.1.4",
  "schema": "...",
  "context": "...",
  "versions": {
    "1":     { "schema": "...", "context": "...", "sourceFiles": "...", "..." },
    "1.2":   { "..." },
    "2":     { "..." },
    "2.1.4": { "..." }    ← same data as the top-level entry, kept in sync by the postprocessor
  }
}
```

The top-level `version` attribute identifies which `versions` key is current. Old tooling reads the top-level entry and gets the latest unchanged. New tooling reads `versions` for resolution and gets a complete, consistent picture of all available versions including latest — with no need for special-casing.

Unversioned blocks emit no `versions` map.

### Version naming and granularity

| Directory | Covers |
|-----------|--------|
| `@1` | All of `1.x.x` |
| `@1.2` | All of `1.2.x` |
| `@1.2.3` | Exactly `1.2.3` |

Definers choose the granularity that reflects the semantic contract they intend to maintain:

- **Major only** (`@1`, `@2`) — suitable where only breaking-change boundaries matter
- **Major.minor** (`@1.1`, `@1.2`) — stable core with backward-compatible additions
- **Major.minor.patch** (`@1.2.3`, `@1.2.4`) — production-grade, reproducible outputs needed

Granularity does not need to be consistent across versions of the same block — `@1` and `@2.1.4` can coexist.

---

## Impact on Stakeholders

### Building Block definers

Versioning is opt-in. An existing unversioned block requires no changes.

To adopt versioning:

1. Create a `@<version>/` subdirectory (e.g., `@1/`) inside the block's source directory.
2. Move **all** existing artifacts into the subdirectory: `bblock.json`, `schema.yaml`, `context.jsonld`, `examples.yaml`, `transforms.yaml`, and any other files. Most of these are auto-detected by the postprocessor when they are present in the same directory as `bblock.json`, so they must travel with it.
3. For subsequent versions, only files that actually change need to be added to the new version directory; unchanged artifacts can be referenced by relative path from the new `bblock.json`.

For subsequent versions, only changed artifacts need new files; unchanged ones are referenced by relative path from the new `bblock.json`.

**Extension points** work with the versions explicitly declared in the extension point metadata. There is no automatic version alignment across parent and child blocks — if both are versioned and a new major version is released for each, the extension point metadata must be updated explicitly.

**Deprecation** is handled via the existing `status` metadata field in `bblock.json`. Versions with a status of `retired` or `superseded` are treated as deprecated: the postprocessor annotates the `register.json` entry accordingly and emits a warning. Deprecated versions continue to be served.

### Consumers / data modellers

Consumers referencing bblocks in schemas or contexts can continue using unversioned `bblocks://` URIs with no changes. To pin to a version, append the version to the URI:

```
bblocks://ogc.geo.features.feature/1.2
```

Version references are "compatible-with / at-least": `/1.2` means "the latest available within `1.2.x`", not exactly `1.2.0`. A reference resolves or it fails — there is no silent fallback to an older incompatible version.

### bblocks-viewer and other client tooling

The bblocks-viewer web application will need to be updated to support version-aware display:

- A version selector when a block has multiple available versions
- Versioned documentation URLs (e.g., `/blocks/ogc.geo.features.feature/1.2`)
- Clear indication of versions with `retired` or `superseded` status

Other clients that dereference `bblocks://` URIs must implement the version resolution algorithm described below.

---

## Implementation Details

### Version resolution algorithm

Given a version reference `r` and a `versions` map from `register.json`:

**Step 1 — Collect candidates.** A version entry `d` is compatible with `r` if:

- `d == r` (exact match), or
- `r` starts with `d.` — `d`'s scope covers `r` (e.g., r=`1.2.3`, d=`1.2`; r=`1.4`, d=`1`), or
- `d` starts with `r.` — `d` falls within `r`'s range (e.g., r=`1`, d=`1.2`)

Compatibility is strict: `@1.3` is **not** compatible with reference `1.4` — they share no prefix relationship. There is no silent fallback to the nearest lower version.

**Step 2 — Select best match.** Among compatible candidates: prefer the most specific (longest version string); among equally specific ones, prefer the numerically highest. Version components are compared **numerically** (`1.10 > 1.9`), not lexicographically.

**Step 3 — Fallback for unversioned blocks.** If no `versions` map exists, the block's top-level `version` metadata attribute is checked against `r` using the same compatibility rule. If compatible, the top-level entry is used. If not, resolution fails.

**Step 4 — Unversioned reference.** If `r` is absent, the top-level entry (synthesised latest) is always used.

#### Resolution examples

Given available versions `1`, `1.2`, `1.3`, `2`, `2.1.4`:

| Reference | Resolves to | Reason |
|-----------|-------------|--------|
| _(none)_ | latest (top-level) | Unversioned — always highest available |
| `1` | `1.3` | `1`, `1.2`, `1.3` all qualify; `1.3` is most specific and highest |
| `1.2` | `1.2` | Exact match |
| `1.2.5` | `1.2` | `1.2` covers `1.2.x`; `1` also compatible but less specific |
| `1.4` | error | `1.2` and `1.3` are not compatible with `1.4`; no `1` entry exists |
| `2` | `2.1.4` | Latest compatible `2.x` |
| `2.1` | `2.1.4` | Most specific compatible |
| `2.1.4` | `2.1.4` | Exact match |
| `3` | error | No compatible version found |

### Postprocessor changes

**Discovery.** The block discovery logic is extended to scan for `@*/bblock.json` patterns within each block's source directory. Each is treated as a distinct processing unit. The all-or-nothing rule is enforced at discovery time: a naked `bblock.json` alongside `@`-prefixed subdirectories is an error.

**Version metadata.** The `version` attribute in each versioned `bblock.json` is overridden by the postprocessor to match the directory name, in the same way `modified` is overridden from git history. Definers do not need to keep it in sync manually.

**Processing pipeline.** Each versioned block passes through the same pipeline as an unversioned one: schema annotation, `$ref` resolution, OAS 3.0 conversion, transforms, validation, and documentation generation. Versioned build artifacts are written under their respective output directories, mirroring the source layout:

- `build/annotated/a/b/c/@1.2/` — annotated schemas, contexts, and related artifacts
- `build/generated-docs/a/b/c/@1.2/` — generated documentation and JSON-full version
- `build/tests/a/b/c/@1.2/` — test outputs, validation report, and compiled and uplifted examples

**`register.json` generation.** After all blocks are processed, versioned entries are grouped by identifier, the `versions` map is populated, and the top-level entry is synthesised from the highest available version directory.


### `@`-prefixed directories and OS compatibility

`@` is not a reserved character on Linux, macOS, or Windows. Its use for scoped package directories in the npm ecosystem (`node_modules/@scope/package`) demonstrates reliable cross-platform support.

---

## Migration Path

| Scenario | Action required |
|----------|----------------|
| Existing unversioned register, no version pressure | None — continues to work as today |
| Existing unversioned register, consumers want version pinning | Add `@`-prefixed subdirectories; remove naked `bblock.json` from block root |
| New register | Recommended to adopt versioned layout from the start for any block intended for broad reuse |
| Consumer pinning an existing unversioned reference | Change `bblocks://a.b.c` to `bblocks://a.b.c/1.2` — no other changes needed |