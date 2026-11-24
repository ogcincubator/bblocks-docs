---
title: Building Block structure
permalink: /create/structure
---

The following image summarizes the general usage of a building block:

[![Usage](../assets/usage.png)](../assets/usage.png)

## Building Block sources

The `_sources` directory will contain the sources for the building blocks inside this repository.

- `bblock.json`: Contains the metadata for the building block. Please refer to this
  [JSON schema](https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/refs/heads/master/ogc/bblocks/schemas/bblock.schema.yaml)
  for more information.
- `description.md`: Human-readable, Markdown document with the description of this building block.
  See [Adding documentation](documentation.md) for more information.
- `examples.yaml`: A list of examples for this building block. See [Examples](examples.md).
- `schema.json`: JSON schema for this building block, if any. See [JSON schema](schema.md).
    - `schema.yaml`, in YAML format, is also accepted (and even preferred).
- `assets/`: Documentation assets (e.g. images) directory. See [Assets](documentation.md#assets) below.
- `tests/`: Test resources. See [Validation](validation.md).

Building Block identifiers are automatically generated in the form:

```
<identifier-prefix><bb-path>
```

where:

- `identifier-prefix` is read from `bblocks-config.yaml`. This will initially be a placeholder value,
  but should have an official value eventually (see [How-to](index.md#quick-how-to-create)).
- `bb-path` is the dot-separated path to the building block inside the repository.

For example, given a `r1.branch1.` identifier prefix and a `cat1/cat2/my-bb/bblock.json` metadata file,
the generated identifier would be `r1.branch1.cat1.cat2.my-bb`. This applies to the documentation
subdirectories as well, after removing the first element (e.g., Markdown documentation will be written to
`generateddocs/markdown/branch1/cat1/cat2/my-bb/index.md`).

### Grouping Building Blocks

Building blocks subdirectories can be grouped inside other directories, like so:

```
type1/
  bb1-1/
    bblock.json
  bb1-2/
    bblock.json
type2/
  subtype2-1/
    bb2-1-1/
        bblock.json
[...]
```

In that case, as noted above, `type1`, `type2` and `subtype2-1` will also be part of the building block identifiers.

## Additional register metadata properties

The following additional properties can be set inside `bblocks-config.yml`:

* `name`: A (short) string with the name of the register.
* `abstract`: A short text to serve as an introduction to the register or building blocks collection. 
  Markdown can be used here.
* `description`: A longer text with a description of the register or collection. Markdown can be used here.
* `license`: `{ name?, url? }` object (at least one of the two is required) declaring the default license for
  the register and for every building block in it. A plain string (e.g. `"Apache-2.0"`) is also accepted as
  shorthand for `{ name: <string> }`. A building block can override this by declaring its own `license` in
  its `bblock.json` (see [Building Block metadata](metadata.md#links-and-references)). If `url` is omitted and
  a `LICENSE`, `LICENSE.md` or `LICENSE.txt` file exists at the repository root, its published URL is used
  automatically.
* `viewer`: Configuration for the [Building Blocks Viewer](postprocessing.md#building-blocks-viewer).
  * `show-imported-depth`: Controls which imported building blocks are shown in the viewer.
    * `0` (default): only local building blocks.
    * Positive integer (e.g. `1`, `2`): local building blocks plus imports up to that many levels deep.
    * Negative integer (e.g. `-1`): all imported building blocks, regardless of depth.

    This value is written to `register.json` and respected by the viewer both when deployed via GitHub Pages
    and when [run locally](postprocessing.md#building-blocks-viewer) against the register directly.
  * `view-plugins`: custom client-side visualizations for example snippets or transform outputs.
    See [Viewer view plugins](view-plugins.md).
  * `tab-plugins`: custom client-side tabs on a bblock's detail page, driven by the whole bblock
    rather than a single example/transform output. See [Viewer tab plugins](tab-plugins.md).

* `sparql`: Publishes the register's RDF output to a triplestore after each successful build (set to `false` or
  `null` to disable it, e.g. [on a fork](../build/contribution.md)).
  * `push`: [SPARQL Graph Store Protocol](https://www.w3.org/TR/sparql11-http-rdf-update/) endpoint to upload to.
    Setting it is what enables uploading; credentials are passed through the `sparql_username` and
    `sparql_password` workflow secrets.
  * `graph`: named graph for the register metadata (defaults to the register's base URL).
  * `query`: SPARQL query endpoint where the data will be available (informational, written to `register.json`).
  * `resources`: additional resources to upload apart from building block metadata.
    * `ontologies`: if `true`, each building block's `ontology` is uploaded to its own graph
      (`urn:ogc:bblocks/<id>/ontology`).
    * `data`: if `true`, the RDF [`data` resources](resources.md) of each building block (an RDF `format` such as
      `text/turtle` is required; non-RDF data is skipped) are merged and uploaded to a single graph per building
      block (`urn:ogc:bblocks/<id>/data`). Replacing or removing a resource is therefore picked up on the next
      build. Unlike ontologies, no profile entailment is applied, so this is suitable for instance data.

* `deploy`: How the built site is published (see [Publishing to a branch](../build/github.md#publishing-to-a-branch)).
  * `mode`: `artifact` (default) commits `build/` to the source branch and deploys it to GitHub Pages
    through GitHub Actions. `branch` publishes the site to a separate branch instead, leaving `build/` out of
    the source branch.
  * `branch`: name of the branch to publish to in `branch` mode (default: `gh-pages`).

## Ready to use components

The `build/` directory will contain the **_reusable assets_** for implementing this building block.

*Sources* minimize redundant information and preserve original forms of inputs, such as externally published
schemas, etc. This allows these to be updated safely, and also allows for alternative forms of original source
material to be used while preserving uniformity of the reusable assets.

**The `build` directory should never be edited**. Moreover, applications should only use (copy or reference) resources
from this directory.