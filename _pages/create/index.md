---
title: How to create Building Blocks
permalink: /create
---
Building Blocks can be reused in several ways:

- if creating a JSON schema based BuildingBlock then use the $ref: bblocks://{block id} to make a JSON schema reference to any building block in the import list [see imports](/create/imports)
- for ther Building Blocks declare as an entry in the dependsOn element of a `block.json` metadata file
- cut and paste "ready to use" forms from the `build/` directory of any building block repository into a some other form of application (not a reusable Building Block itself)
- directly reference the artefacts in the `build` directory using the URL pattern specified in the building block
  description (noting this may be affected by changes if a building block is moved from one register to another - bblocks:// references will still work if imports approach is used.)

## Quick how-to create

1. Navigate to the [bblock-template](https://github.com/opengeospatial/bblock-template) repository.
2. Click on "Use this template" on GitHub (do not fork this repository, or you will have to manually enable the
   workflows).
3. Set the `identifier-prefix` provided by OGC in `bblocks-config.yaml`:
   * The first component of the prefix should represent the entity defining or maintaining this building block
     collection. If this is an OGC-related project, you may use `ogc.` here.
   * The rest of the prefix components should be chosen according to the nature of the collection. For example, if
     this repository only contained schemas for *OGC API X* version 1.x,
     a possible prefix could be `ogc.apis.api-x.v1.schemas.`.
   * Bear in mind that the path of the building blocks inside `_sources` will be used in their identifiers (see below).
   * **Identifiers should be as stable as possible**, even when under development. This makes it easier to promote
     building blocks to production (i.e., being adopted by the OGC as official), and avoids having to manually/update
     references (in dependency declarations, schemas, etc.).
4. Set a `name` for the repository inside `bblocks-config.yaml`.
5. Configure any necessary [imports](imports) inside `bblocks-config.yaml`.
6. Set the [additional register metadata properties](#additional-register-metadata-properties) in `bblocks-config.yaml`.
7. For each new building block, replace or create a copy of the `mySchema` or `myFeature` inside `_sources`.
   Note: **the path to and name of the new directory will be part of the building block identifier**.
8. Update the [building block's files](structure).
   1. [Add documentation](documentation) to your Building Block.
   2. See [defining a schema](schema) for information how test an existing schema.
   3. See [adding JSON-LD context](json-ld-context) for information how to "uplift" a schema - linking to a model using JSON-LD.
   4. See [validation](validation) for information how to define powerful constraints for schemas and semantic models.
   5. See [transforms](transforms) for information how to define and test transformations.
9. Replace the README.md file with documentation about the new building block(s).
10. Enable GitHub pages in the repository settings, setting "Source" (under "Build and deployment")
    to "GitHub Actions".

## Additional register metadata properties

The following additional properties can be set inside `bblocks-config.yml`:

* `name`: A (short) string with the name of the register.
* `abstract`: A short text to serve as an introduction to the register or building blocks collection. 
  Markdown can be used here.
* `description`: A longer text with a description of the register or collection. Markdown can be used here.