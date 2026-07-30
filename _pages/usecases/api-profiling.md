---
title: Profiling an API
permalink: /usecases/api-profiling
---

[Profiling a standard](usecases#profiling-a-standard) is discussed in the abstract elsewhere in these
use cases. APIs are a special case worth walking through on their own: the base standard is described
by an OpenAPI document rather than a standalone JSON Schema, which changes how far Building Blocks can
automate the profiling for you.

This page walks through a concrete example: profiling [OGC API - Processes Part 1](https://docs.ogc.org/is/18-062/18-062.html)
to expose a single, fixed process (`buffer-geometry`) with a known set of inputs and outputs, instead
of the generic, dynamically-discoverable process catalog the base standard describes.

The finished example is published at
[`ogc.bbr.examples.ogcapi.processes.custom-api`](https://ogcincubator.github.io/bblocks-examples/bblock/ogc.bbr.examples.ogcapi.processes.custom-api)
in the [bblocks-examples](https://github.com/ogcincubator/bblocks-examples) register. This page explains
the reasoning behind its structure — for the schemas themselves, follow the links.

## The reasoning

1. **Start from the base API as a Building Block.** OGC API - Processes Part 1 is already published as
   `ogc.api.processes.v1.api`, an `api`-class block backed by an OpenAPI document. Profiling means
   reusing it wholesale and only touching the parts that are actually specific to your deployment.

2. **Identify what's generic and what's domain-specific.** Most of OGC API - Processes is generic
   machinery that any implementation reuses unchanged: the landing page, conformance, job list, job
   status, and error responses. The parts that are inherently domain-specific are the **process
   description** and the **shape of a process's inputs and outputs** — those are exactly the pieces
   this profile needs to fix in place.

3. **Check how the base block can be constrained.** Because the base is OpenAPI-backed rather than a
   plain JSON Schema, [extension points](../create/extension-points) on it are **declarative only** —
   the postprocessor records the mapping in the register for tooling and consumers, but it cannot
   compile a single merged OpenAPI document the way it can for schema-only blocks. This means the
   OpenAPI wiring itself has to be written by hand, and the extension point is added on top to make
   the relationship machine-readable.

4. **Model the domain-specific parts as their own schema blocks**, using ordinary composition
   (`allOf`/`$ref`), not anything specific to extension points:
   - A `buffer-geometry` **input description** and **output description**, each extending the base's
     generic per-input/output description schema with fixed titles, cardinalities, and a reference to
     the process's own input/output JSON Schema.
   - A `buffer-geometry` **process description**, composing the base `process` schema with those two
     blocks, so the process's own description is now fully specific rather than generic.

5. **Aggregate the process-specific blocks into collection schemas.** The base API's job-results and
   process-listing paths don't talk about *one* process — they talk about *the input/output description
   of whatever process is being described*. So `inputDescriptions`/`outputDescriptions` blocks are
   defined as thin `anyOf` wrappers around the process-specific descriptions. These collection blocks —
   not the process-specific ones directly — are what the base schema's extension slots get mapped to,
   so the profile stays open to adding more processes later without touching the extension point.

6. **Write the profile's own OpenAPI document**, reusing the base's generic paths by reference
   (`bblocks://ogc.api.processes.v1.paths.*`) and substituting the fixed, process-specific schemas
   wherever the base would otherwise have left the shape open (the process description path, the
   execute request body, the job results response).

7. **Declare the profile block itself**: `isProfileOf: ogc.api.processes.v1.api`, plus an
   `extensionPoints` entry mapping the base's generic `inputDescription`/`outputDescription` schema
   slots to the collection blocks from step 5. This is what makes the profiling relationship discoverable
   in the register, even though the actual substitution already happened by hand in the OpenAPI document.

## The blocks involved

| Block | Type | Role |
|---|---|---|
| [`ogc.api.processes.v1.api`](https://ogcincubator.github.io/bblocks-ogcapi-processes/bblock/ogc.api.processes.v1.api) | `api` (OpenAPI) | Base standard being profiled |
| [`ogc.bbr.examples.ogcapi.processes.custom-api`](https://ogcincubator.github.io/bblocks-examples/bblock/ogc.bbr.examples.ogcapi.processes.custom-api) | `api` (OpenAPI) | The profile: `isProfileOf` the base, declares the extension point, owns the profile's `openapi.yaml` |
| `ogc.bbr.examples.ogcapi.processes.schemas.inputDescriptions` / `.outputDescriptions` | `schema` | Collections (`anyOf`) of known process-specific descriptions — the actual extension point targets |
| `ogc.bbr.examples.ogcapi.processes.schemas.buffer-geometry.inputDescription` / `.outputDescription` | `schema` | Extend the base's generic per-input/output description for the `buffer-geometry` process specifically |
| `ogc.bbr.examples.ogcapi.processes.schemas.buffer-geometry.inputSchema` / `.outputSchema` | `schema` | The actual data shape of the process's inputs/outputs, referenced from the description blocks |
| `ogc.bbr.examples.ogcapi.processes.schemas.buffer-geometry.processDescription` | `schema` | Composes the base `process` schema with the two description blocks above |

## Why this shape, and not another

An alternative would have been to skip the collection blocks and map the extension point directly to
`buffer-geometry.inputDescription`/`.outputDescription`. That would work for a profile that only ever
exposes one process, but it hard-codes the process into the extension point mapping itself. Going through
an `anyOf` collection keeps the extension point stable — pointing at "the set of processes this API
exposes" — while new processes can be added by extending the collection, not by touching the profile's
metadata.

It's also worth noting the OpenAPI document does the real substitution work here: every `$ref` to a
fixed schema in `custom-api`'s `openapi.yaml` is what actually produces a valid, fully-specific API
description. The `extensionPoints` declaration doesn't change validation behavior for OpenAPI-backed
blocks — its value is making that hand-written substitution discoverable and queryable for anyone
consuming the register, the same way it would be for a schema-only block.

## See also

- [Extension points](../create/extension-points) — the mechanism used to declare the profiling
  relationship, including the OpenAPI-specific caveat
- [Imports and profiles](../overview/profiles) — the general `isProfileOf` relationship
- [Profiling a standard](usecases#profiling-a-standard) — the abstract use case this page makes concrete