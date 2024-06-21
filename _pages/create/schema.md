---
title: Defining a schema
permalink: /create/schema
---
Building Blocks can be defined to reuse existing JSON schemas in a more sophisticated way.

A re-used schema can be:

1. [profiled (by extension or constraints)](#profiling-json-schemas)
2. Mapped to a [semantic (RDF)](rdf-only) model allowing richer specification of constraints.
3. [Tested](validation) with examples and test cases.

## How to reuse

This is simply a matter of referencing the reused schema in the building block schema(.json|.yaml):

```json
{ 
   "$ref": "http://somestablelocation.org/schema.json"
}
```

## How to reuse a building block with its added components...

this is done in a two-step process:

1. in the `bblocks-config.yaml` file tell the processing where to find building block registers:
    
    ```yaml
    schema-mapping:
      default: https://opengeospatial.github.io/bblocks/annotated-schemas/
    
    imports:
      - default
      - https://opengeospatial.github.io/ogcapi-sosa/build/register.json
    ```
    
    The default is the OGC master register of building blocks.

2. use the `bblocks:://{id}` syntax as href in schema $ref elements. 

    This means your building block will inherit all json-ld contexts and SHACL rules from the referenced building block automatically and apply during [testing](create/validation).


# Profiling JSON Schemas

Profiling JSON schemas is a complex subject. This document is a placeholder for a description of best practices and support tooling.

## Why is this challenging?

The JSON Schema specification and tooling landscape is complex.  Versions of the OpenAPI Specification (OAS) use different versions of JSON-Schema and tool support varies.

In particular, reuse mechanisms such as $dynamicRef may not be available.

## Version-agnostic Building Blocks

The Building Block post-processing tooling automatically generates OAS 3.0 and OAS 3.1 compatible schemas. It is recommended to develop new building blocks using improved modularity and reuse support in modern schema versions, and allow the Building Block to create a "down-compiled version".

## OAS 3.0 Compatibility

OGC APIs are currently bound to OAS v3.0 which limits JSON schema patterns that can be supported.

The implication is that currently it is typical necessary to recreate complex structural hierarchies and compose into "allOf[]" structures in order to place constraints into a location.

e.g. to make the relatively simple constraints that a "SurveyObservationCollection" is a collection  "SurveyObservation" objects, and must declare that some schema for describing "SensorType" is used, a significant portion of the structure must be detailed.

```json

"SurveyVectorObsCollection": {
      "allOf": [
        {
          "$ref": "https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/features/observationCollection/schema.json"
        },
        {
          "properties": {
            "features": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/SurveyVectorObsFeature"
              }
            },
            "properties": {
              "properties": {
                "madeBySensor": {
                  "$ref": "#/$defs/SensorType"
                }
              },
              "required": [
                "madeBySensor"
              ]
            }
          }
        }
      ]
    }
  }
```

## Future options

A number of strategies are being considered to simplify this. At this stage alternative approaches:
- define a new constraint language that can be directly compiled from simple statements into the target schema constraint
- use the most compact form in more recent JSON schema - potentially requiring extension hooks in the base schemas - and compile to legacy forms with full structure replication
- work with JSON schema community to define new capabilities designed for easier profiling in a future version of JSON
- create a "wizard" tool to write constraints

All these have significant impact and effort implications.

Follow updates at [this issue](https://github.com/opengeospatial/bblock-template/issues/2)
