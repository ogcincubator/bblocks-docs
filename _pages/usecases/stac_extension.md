---
title: STAC extensions
permalink: /usecases/stac_extensions
---

## Creating or updating a STAC extension

_(This is a work in progress and we explore even better ways to support STAC and Records extensions)_

STAC extensions are defined in a repository and provide a number of elements - they are in fact a "STAC Building Block" in that they can be combined with each other. ("Building" is the fundamental concept here!)

One problem is that extensions may have inconsistent schemas, reuse of schema elements and duplication. 

Using the OGC Building Blocks approach to define or annotate a STAC extension provides an additional layer of support for:

- validating examples work with other STAC schemas
- documenting the relationships between STAC schemas
- integration of STAC schemas and or conceptual model into other metadata models
- integration of other building blocks into STAC schemas

### Dependency modelling and reduction of duplication

Refactoring STAC schemas to reuse (rather than copy) sub-schemas for specific patterns makes it clear the common semantics and intended interoperability of these sub-schemas.

For example, this could have avoided the triplication of "raster" models from EO, raster and core 1.1 schemas that now makes extensions like STAC-MLM very verbose and complex.

### Documentation management

By linking a STAC sub-schema building block to an ontology (description of all the elements) using JSON-LD "semantic uplift" documentation can be generated automatically, and kept up to date.  This semantic documentation can be combined with other stac extensions to create rich documentation of how a community profile uses multiple STAC extensions.

