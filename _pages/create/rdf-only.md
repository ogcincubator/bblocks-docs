---
title: RDF-only Building Blocks
permalink: /create/rdf-only
---
Building Blocks can be defined that use RDF only. An RDF building block can:

1. Define RDF (TTL) examples how to use the Semantic model
2. Apply SHACL Shapes to [validate examples](validation#shacl-validation)
3. [Perform transforms](transforms) and validate results

Test cases and examples as either TTL or JSONLD will undergo syntax and SHACL validation.

`examples.yaml` can have embedded TTL - eg.

```
- title: Example of SOSA ObservationCollection
  comment:
    This class is a target for the SOSA v 1.1 update. 

  snippets:
    - language: turtle
      code: |-
        @prefix sosa: <http://www.w3.org/ns/sosa/> .
        @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
        @prefix eg: <http://example.org/my-feature/> .
        @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

        eg:c1 a sosa:ObservationCollection ;
          sosa:hasMember eg:pop1999, eg:pop2000 ;
          sosa:observedProperty <http://dbpedia.org/ontology/population> ;
        .

```

## Ontology

A building block can declare an ontology document — an RDF file that defines the classes, properties, and
relationships that the building block's data model is based on.

The `ontology` property in `bblock.json` accepts a file path (relative to the building block directory) or a URL:

```json
{
  "ontology": "ontology.ttl"
}
```

If `ontology` is not set, the postprocessor will automatically look for `ontology.ttl` or `ontology.owl` in the
building block directory and use the first one found.

The resolved ontology is published as part of the build output and included in the building block's register entry.

## Semantic annotations

Two metadata properties allow a building block to be linked to RDF concepts and classes:

### `concept`

`concept` is an array of URIs for the RDF concept(s) that this building block represents
(mapped to `skos:closeMatch` in the register).

```json
{
  "concept": [
    "https://www.w3.org/ns/sosa/Observation"
  ]
}
```

### `rdfType`

`rdfType` is an array of URIs for the RDF class(es) that instances of this building block conform to
(mapped to `rdfs:subClassOf` in the register). Use this when you want to declare that instances of the
building block belong to a particular RDF class.

```json
{
  "rdfType": [
    "https://www.w3.org/ns/sosa/Observation"
  ]
}
```