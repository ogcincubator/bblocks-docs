---
title: Building Block relationships
permalink: /overview/relationships
---

Several types of relationships can be declared when defining Building Blocks.

## <a name="type-dependsOn"></a>Generic dependency (`dependsOn`)

This relationship implies that a building block depends on another, in a generic manner.

This is the default type of relationship that exists, for example, when the schema of a building
block is referenced from another. 

This type of dependency uses the `dependsOn` property in the building blocks register and metadata files.

## <a name="type-profileOf"></a>Profiling (`profileOf`)

Profiling signals that a building block does not merely reference or reuse another, but that it _extends_ it,
that is, it inherits its main structure and provides additional metadata properties, constraints, examples, etc.

This type of dependency is declared using `profileOf` in `bblock.json`.

## Extension points

When defining [extension points](../create/extension-points.md), three new types of relationships are involved.

### <a name="type-extends"></a>Extends

This relationship links a building block with the another that is used as an extension base, and for 
which extension points are defined. It is a special case of the `profileOf` property.

### <a name="type-extensionTarget"></a>Extension target

This relationship links a building block to another that is used to augment or constraint references to an
[extension source](#type-extensionSource).

### <a name="type-extensionSource"></a>Extension source

This type of relationship binds an [extension target](#type-extensionTarget) with the original building
block referenced by the [extension base](#type-extends).