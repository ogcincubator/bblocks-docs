---
title: Building Block Types
permalink: /overview/types
---

Building Blocks are an **extensible framework** for specification development and re-use.  They are not run-time components for operational systems, but they can be used as part of the development, testing and documentation of such systems.

Building Blocks support different technologies and the combination or translation between them. Types are however best thought of as the implementation of different [patterns](#patterns), which may be used in combination if required.  


# Supported technologies

Because most people will arrive here with an understanding of one or more technologies, lets start with a few examples, before exploring the underlying behavioural types. 

Key technologies currently supported include:

- JSON schema fragments
- JSON schema with JSON-LD mappings to semantic definitions
- OpenAPI components
- RDF models
- transformations from XML, CSV, etc to validatable forms (JSON, RDF)
- rules (constraints on schemas or SHACL for RDF models)

Building Blocks allow different technologies to be integrated in some cases (such as JSON, JSON-LD and RDF) - and manage the complexities and subtleties of integration patterns.

In all cases, the Building Block annotations provide transparent dependency declarations and the opportunity to systematically test examples.

**Other technologies can be supported in future** - based on existence of mechanisms to combine components, validate examples, or specific needs to track dependencies.

# Patterns (Functional Types)

Building blocks are combined in a number of common implementing patterns:

## Aggregation/Composition

A schema or other model is constructed by aggregating a number of other building blocks. This may be a form of [specialisation](#specialisation) of a general container model, such as a GeoJSON Feature.

## Extension

A specification defines additional properties of another schema or model. (Note this is also a form of [profile](#profiling) since it constrains an "open to extension" option by defining what an extension must look like. )

## Specialisation

A model or schema is constrained by specialising an existing attribute with a more specific model, such as defining the type of features present in a FeatureCollection.

## Semantic annotation

Where a semantic binding mechanism is available (such as JSON-LD for JSON) a Building Block may exist purely to bind schema elements to definitions.

Note this pattern is especially important when one schema could be mapped to more than one ontology (definition set).

For example, a simple mapping for some discovery metadata might use schema.org - however for operations and understanding of the data a richer domain model will always be required. 

## Profiling

Profiling adds constraints to a model - for use in a particular context. Profiles may involve [specialisation](#specialisation) or [extension](#extension).  They may also add **rules** or **vocabulary bindings**.

## Vocabulary Bindings

Many applications define the allowable content of a data element using a controlled vocabulary. Such a vocabulary may be static, or may be a dynamic an extensive register that needs to be accessed via a service. 

_Note that the case of validation of content using services requires custom validators since no standard has been defined for this capability._

## Transformations

Building Blocks can include, or indeed just be defined around, transformations between specifications. This allows a specification to be tested and documented against its relationships to other specifications.

If those other specifications are also defined using the machine readable Building Block model, then validation is performed against the post-transformation target.

AI agents in particular can exploit this validation process automatically when creating or translating data or creating code.

## Testing examples

Building Blocks may be scoped simply to supply or test a set of examples for a given specification. This can be used to improve specification development processes, or document how a specification can be used in certain circumstances.

## Documenting validators

The plug-in transformer and validator capabilities of the Building Blocks framework means that it is possible to have a Building Block whose main job is to provide test cases, documentation and CI/CT for validation tools. 

Typically validators will be tied to specific profiles of standards, in order to simplify the number of cases each validator needs to be tested against.
