---
title: Building Block structure
permalink: /create/structure
---

The following image summarizes the general usage of a building block:

[![Usage](/bblocks-docs/assets/usage.png)](/bblocks-docs/assets/usage.png)

## Building Block sources

The `_sources` directory will contain the sources for the building blocks inside this repository.

- `bblock.json`: Contains the metadata for the building block. Please refer to this
  [JSON schema](https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/master/ogc/bblocks/metadata-schema.yaml)
  for more information.
- `description.md`: Human-readable, Markdown document with the description of this building block.
  See [Adding documentation](documentation) for more information.
- `examples.yaml`: A list of examples for this building block. See [Examples](examples).
- `schema.json`: JSON schema for this building block, if any. See [JSON schema](schema).
    - `schema.yaml`, in YAML format, is also accepted (and even preferred).
- `assets/`: Documentation assets (e.g. images) directory. See [Assets](#assets) below.
- `tests/`: Test resources. See [Validation](#validation-and-tests).

Building Block identifiers are automatically generated in the form:

```
<identifier-prefix><bb-path>
```

where:

- `identifier-prefix` is read from `bblocks-config.yaml`. This will initially be a placeholder value,
  but should have an official value eventually (see [How-to](#how-to)).
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

## Ready to use components

The `build/` directory will contain the **_reusable assets_** for implementing this building block.

*Sources* minimise redundant information and preserve original forms of inputs, such as externally published
schemas, etc. This allows these to be updated safely, and also allows for alternative forms of original source
material to be used whilst preserving uniformity of the reusable assets.

**The `build` directory should never be edited**. Moreover, applications should only use (copy or reference) resources
from this directory.