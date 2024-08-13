---
title: Transforms
permalink: /create/transforms
---

Transformations may be required for several reasons:

1. To test the ability of a building block to model information from a particular source (that does not conform to the building block specification).

Accordingly, different types of transformations may be required:

1. Encoding translations (e.g. XML -> JSON)
2. Schema transformations
3. Semantic transformations (entailments, equivalent terms)
4. Content transformations (terminology)

**Note that the Building Blocks viewer application is still being developed to show all types of transformation in appropriate places.**

## Transformation tools

Building Blocks are technology agnostic, however rich support exists for JSON Schema and JSON-LD/RDF:

- SHACL (AF- advances features) SPARQL rules are powerful for schema, semantic and content transformation rules.
- JQ may be used for pure JSON transformations

Custom code may be used for transformation and validation. (details TBD) 

## Examples

A key example is the mismatch between the GeoJSON geometry model and the GeoSPARQL geometry model. This
requires the transformation of both structure and vocabulary to convert GeoJSON to valid GeoSPARQL - see this [example](https://ogcincubator.github.io/bblocks-examples/bblock/ogc.bbr.examples.feature.geosparqlFeature)

The transformation specification is here:

https://github.com/ogcincubator/bblocks-examples/blob/master/_sources/feature/geosparqlFeature/bblock.json#L17

## Technical Documentation

TBD