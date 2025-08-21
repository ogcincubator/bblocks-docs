---
title: Linked Data / JSON-LD Context
permalink: /use/linked-data
---

# Linked Data 

The key characteristic of Linked Data is that elements of data can be linked to more resources.

The main aspects of this are:

1. Schema elements and data contents can be **unambiguously** identified - allowing all sorts of downstream operations to be performed with confidence.
2. Elements of schemas can be linked to explanations and documentation
3. Data values can be linked to controlled vocabularies with definitions
4. Data values can be links to other data objects

The key enabler for Linked Data is the use of RDF - and this can be done with "native RDF" - but the focus on the Building Blocks is "semantic uplift" of JSON.

This can be done with JSON-LD. Whilst it has its limitations JSON-LD is a commonly used standard that provides an enabler.

The challenges with JSON-LD lie in its mirroring of underlying JSON schema structures - it doesnt support significant structure reorganisation, and its complex to build JSON-LD contexts that mirror complex schemas.

The OGC Building Blocks **solve this** by allowing unit-testing of simple JSON-LD contexts for sub-schemas, and compilation of reliable context documents for schemas that re-use these sub-schemas.
(Note this is currently the only Open Source tooling known to support this, and was developed in consultation with JSON schema design leads.)

For more information refer the [Use Cases](/usecases/usecases) and 

