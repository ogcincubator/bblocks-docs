---
title: Building Block relationships
permalink: /overview/relationships
---

Several types of relationships can be declared between Building Blocks. All of them are declared in
`bblock.json` and published in the register's `register.json`.

| Relationship | Declared on | Meaning | Is also a dependency |
|---|---|---|---|
| [`dependsOn`](#type-dependsOn) | any block | Generic dependency | — |
| [`isProfileOf`](#type-isProfileOf) | the profile | Specializes (extends) another block | Yes |
| [`isDescribedBy`](#type-isDescribedBy) | the schema | Is described by a model block | Yes |
| [`hasFormat`](#type-hasFormat) | each sibling | Same content in an alternate format | No |
| [Extension points](#extension-points) | the extending block | Substitutes referenced blocks | Yes |

## <a name="type-dependsOn"></a>Generic dependency (`dependsOn`)

This relationship implies that a building block depends on another, in a generic manner.

This is the default type of relationship that exists, for example, when the schema of a building
block is referenced from another.

`dependsOn` always lists the complete set of direct dependencies of a building block. The postprocessor
fills it in from three sources:

- every block referenced via a `bblocks://` `$ref` in the schema;
- every block named in `isProfileOf` or `isDescribedBy`;
- the blocks you list in `dependsOn` by hand.

So you only need to declare `dependsOn` explicitly for dependencies that none of the above reveals
(e.g. a transform-time or narrative-only prerequisite).

## <a name="type-isProfileOf"></a>Profiling (`isProfileOf`)

Profiling signals that a building block does not merely reference or reuse another, but that it _extends_ it,
that is, it inherits its main structure and provides additional metadata properties, constraints, examples, etc.

This type of dependency is declared using `isProfileOf` in `bblock.json`, with a single identifier or a list.

## <a name="type-isDescribedBy"></a>Described by (`isDescribedBy`)

This relationship links a building block (typically a schema) to the model block that describes it: for example,
the conceptual model or ontology that the schema is an encoding of.

It is declared on the schema block, using `isDescribedBy` in `bblock.json` with a single identifier or a list,
and points at the model block. The model block needs no changes; the inverse ("describes") is computed by tools
from the schemas that point at it.

```json
{
  "isDescribedBy": ["ogc.bbr.examples.linkeddata.forest-ontology"]
}
```

The same model can be described by many schemas: each of them declares `isDescribedBy` towards the same model
block, so the model block becomes the place where all its representations are listed. In RDF output,
the relationship is expressed with the IANA [`describedby`](http://www.iana.org/assignments/relation/describedby)
link relation.

## <a name="type-hasFormat"></a>Alternate formats (`hasFormat`)

This relationship links building blocks that represent the same content in different formats (for example, a
JSON and an XML encoding of the same model). The blocks are siblings: unlike profiling, neither is a
specialization of the other, and neither depends on the other.

It is declared using `hasFormat` in `bblock.json`, as a list of building block identifiers. The relationship is
symmetric, but it is not inferred from the other side: declare it on every sibling you want to link.
In RDF output it is expressed with `dct:hasFormat`.

## <a name="type-precedence"></a>Several relationships between the same two blocks

Since `isProfileOf` and `isDescribedBy` are also dependencies, a pair of blocks can appear under several
relationships at once in `register.json` (for example, under both `isDescribedBy` and `dependsOn`). Tools that
display relationships, such as the Building Blocks viewer, show only the most specific one:
`isDescribedBy`, then `isProfileOf`, then `dependsOn`.

## Extension points

When defining [extension points](../create/extension-points), three new types of relationships are involved.

### <a name="type-extends"></a>Extends

This relationship links a building block with another that is used as an extension base, and for 
which extension points are defined. It is a special case of the `isProfileOf` property.

### <a name="type-extensionTarget"></a>Extension target

This relationship links a building block to another that is used to augment or constraint references to an
[extension source](#type-extensionSource).

### <a name="type-extensionSource"></a>Extension source

This type of relationship binds an [extension target](#type-extensionTarget) with the original building
block referenced by the [extension base](#type-extends).