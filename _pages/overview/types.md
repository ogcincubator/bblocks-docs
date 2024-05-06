---
title: Building Block Types
permalink: /overview/types
---

Building Blocks may have different types, and implement different [patterns](#patterns), which may be used in combination if required.  

# Types (technology)

Key types include:

- JSON schema fragments
- JSON schema with JSON-LD mappings to semantic definitions
- OpenAPI components
- RDF models
- transformations from XML, CSV, etc to validatable forms (JSON, RDF)
- rules (constraints on other schemas or RDF models)

In all cases, the Building Block annotations provide transparent dependency declarations and the opportunity to systematically test example.

# Patterns

Building blocks are combined in a number of common implementing patterns:

## Aggregation/Composition

A schema or other model is constructed by aggregating a number of other building blocks. This may be a form of [specialisation](#specialisation) of a general container model, such as a GeoJSON Feature.

## Extension

A specification defines additional properties of another schema or model. (Note this is also a form of [profile](#profiling) since it constrains an "open to extension" option by defining what an extension must look like. )

## Specialisation

A model or schema is constrained by specialising an existing attribute with a more specific model, such as defining the type of features present in a FeatureCollection.

## Profiling

Profiling adds constraints to a model - for use in a particular context. Profiles may involve [specialisation](#specialisation) or [extension](#extension).  They may also add **rules** or **vocabulary bindings**.

## Vocabulary Bindings

Many applications define the allowable content of a data element using a controlled vocabulary. Such a vocabulary may be static, or may be a dynamic an extensive register that needs to be accessed via a service. 

_Note that the case of validation of content using services requires custom validators since no standard has been defined for this capability._


