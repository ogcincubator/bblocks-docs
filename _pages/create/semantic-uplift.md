---
title: Semantic uplift
permalink: /create/semantic-uplift
redirect_from:
  - /create/json-ld-context
---

The Building block design allows for "semantic annotation" through the use of a **context** document that
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
- using the property `x-jsonld-context` in the _schema.(yaml/json) for the building block - e.g.
  `x-jsonld-context: ../../../sosa-ssn.jsonld`

The JSON LD context:

1. Maps JSON elements to URIs (which can be URIs of a richer semantic model)
2. Allows validation of complex logical constraints using SHACL Shapes to [validate examples](validation)
3. [Perform transforms](transforms) to any other RDF model and validate results

## Modularity support

JSON-LD contexts need to be aware of the underlying JSON schema - and in many applications schemas are compplex with  nested sub-schemas. Examples of this are metadata schemas such as STAC, but even the basic GeoJSON Feature model is surprisingly hard to model in a consistent fashion.

The Building Blocks design allows automatic combination of contexts based on the schema re-use patterns.  As schema complexity grows through re-use of standard components the benefits of the Building Blocks approach rapidly evolves from an efficiency into a critical enabler. 

_Its probable that the lack of JSON-LD support for existing metadata is due to this challenge.  This capability is not  only faster and better - but making semantic interoperability practically achievable for the first time._

## Context design

If contexts are being combined, then a number of possibilities emerge, but need careful design and testing.

One such possibility is the conversion of tokens into URIs depending on where these are encountered in a schemas. 

This can be achieved through several mechanisms. 

_TBD: document local contexts and use of @base mappings - and link to examples of different patterns_

## Additional semantic uplift steps

Sometimes, using JSON-LD is not enough to convert a JSON document into RDF, so additional steps may be required. This is
a common occurrence, for example, when defining JSON-LD contexts for already-existing or legacy JSON schemas, which are
hard or even impossible to adapt to better fit a given semantic data model.

Semantic uplift pre- and/or post-processing (i.e., before and/or after applying the building block's JSON-LD context)
can be defined in a `semantic-uplift.yaml` file in the building block directory, with the following format:

```yaml
additionalSteps:
  - type: jq                            # Type of transform
    code: |                             # Code for this transform
      .a = .b + 1
  - type: sparql-construct
    ref: semantic-uplift/constr.sparql  # A ref (from the bblock directory) can be used instead
```

### Types of semantic uplift steps

The following types are supported and will be automatically processed when uplifting examples and test resources:

* Pre-processing (on JSON document, before applying JSON-LD context)
  * `jq`: [JQ transform](https://jqlang.github.io/jq/manual/)
* Post-processing (on RDF graph, after applying JSON-LD context and parsing).
  * `shacl`: [SHACL AF](https://www.w3.org/TR/shacl-af/#rules) ruleset. The original graph plus the entailed triples
    (if any) will be returned.
  * `sparql-construct`: A [SPARQL CONSTRUCT](https://www.w3.org/TR/sparql11-query/#construct) query that will
    replace the graph obtained from the JSON-LD uplift.
  * `sparql-update`: A [SPARQL UPDATE](https://www.w3.org/TR/2013/REC-sparql11-update-20130321/) query that will
    be applied on the graph. The full resulting graph will be returned.

### Semantic uplift in run-time

If extra steps are required to map a schema to a model, then it becomes an implementation challenge to implement these steps. It is a work in progress to consider the reusability (FAIR) of transformations, and how these may be related to known profiles and allow software to automatically apply a small number of well-tested standard transformations.