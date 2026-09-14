# Schema/Vocabulary bindings (cf Semantic Annotation)

This document describes the rationale, state of the art and options to consider for the specification of content with data structures.

The initial focus is on JSON and RDF - but this can be extrapolated to other technologies, such as NetCDf COAARD

## Overview

There is no standardised and widely implemented mechanism for mapping between schemas and semantic descriptions that addresses all needs. There are acitivities underway and sufficient commonality around motivation and approach to suggest that a common solution can be defined, or tooling to support combinations of solutions can be shared.

In particular these aspects have open challenges:

- structure vs. content - addressing implicit semantics of structure in the context of domain semantics
- controlled vocabulary binding - how to specify the range of a property 
- vocabulary services for term resolution - how allowable values may be determined by services if too large or dynamic for copies to be held or accessed.
- reuse and composition of common patterns
- identification of common patterns
- support in common code libraries

## JSON schema annotations

### OGC Building Blocks schema annotator

The OGC Building blocks uses aggregation of JSON-LD context

Pros: 
- can be applied to existing schemas without editing them
- Unit testing of individual mappings
- Composition
- SHACL can be used to bind vocabularies to schemas

Cons:
- limitations of JSON-LD for structures 
- limited generation of reports

Extension points:
- transformers to/from different languages
- pluggable 

### OGC Features Part 5 

Pros:
- supports a range of semantic annotations, including codelist bindings

Cons:
- requires schema to contain details
- no standards or tooling to expand
- 
### IETF JSON Schema

draft 3 (unreleased) has material on semantic annotatons.

Instructions: Follow this actvity

### JSON Sructure

https://json-structure.org/2026/08/06/semantic-annotations.html

### W3C Context Graphs Community Group

Unclear at this stage exactly how this activity will interact 

"A Context Graph treats this gap as a first-class, interoperable artifact: a structured representation of the contextual prerequisites required for valid interpretation, their dependencies, and their resolution status. The Community Group will formalize (1) a core data model for expressing contextual prerequisites and resolution state, (2) a minimal vocabulary for describing common categories of contextual mismatch, and (3) optional protocol guidance for structured clarification and safe stopping conditions when required context cannot be resolved. The goal is to enable independent systems to detect contextual misalignment, request missing prerequisites, and converge on a locally valid interpretation before downstream computation or decision-making proceeds.

Primary activities: This group will develop one or more specifications for representing Context Graphs, including: (1) a core data model for contextual prerequisites and their dependencies, (2) vocabularies for expressing resolution status and common categories of global–local contextual mismatch, and (3) optional protocol guidance for structured clarification and safe stopping conditions when required context cannot be resolved. The group will also produce use cases, requirements, test vectors, and best-practice guidance for implementers in knowledge management, enterprise decision workflows, and human–machine / human–AI systems."


https://www.w3.org/groups/cg/context-graph/