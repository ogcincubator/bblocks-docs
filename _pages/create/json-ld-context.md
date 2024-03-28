---
title: Adding JSON-LD context (Semantic uplift)
permalink: /create/json-ld-context
---
The Building block design allows for "semantic annotation" through the use of a **_context_** document that
cross-references each schema element to a URI, using the JSON-LD syntax. The end result is still a valid JSON schema,
but may also be parsed as flexible RDF graphs if desired.

This provides multiple significant improvements over non-annotated schemas:

1. differentiates between the same and different meanings for common element names used in different places
2. can be used to link to a semantic model further describing each element
3. allows use of advanced, standardised validation of instance data
4. allows automated annotation of schemas themselves for tools able ot exploit additional information

The JSON schema for a building block is optionally linked to a conceptual model by using a root-level `x-jsonld-context`
property pointing to a JSON-LD context document (relative paths are ok). The Building Blocks Register can
then annotate every property inside the JSON schemas with their corresponding RDF predicate automatically.

Building Blocks defining JSON schemas can be annotated with JSON-LD contexts using either:
 - including a file (`context.jsonld`) in the building block directory (this can be overriden with a file path or URL
   using the `ldContext` property in `bblock.json`)
 - using the property `x-jsonld-context` in the _schema.(yaml/json) for the building block - e.g. `x-jsonld-context: ../../../sosa-ssn.jsonld`
 
The JSON LD context: 

1. Maps JSON elements to URIs (which can be URIs of a richer semantic model)
2. Allows validation of complex logical constraints using SHACL Rules to [validate examples](validation)
3. [Perform transforms](transforms) to any other RDF model and validate results

## Modularity support

JSON-LD contexts are very complex and hard to debug if the schema is at all complex.  

The Building Blocks design allows automatic combination of contexts based on the schema re-use patterns.

## Context design

_TBD: document local contexts and use of @base mappings. _ 