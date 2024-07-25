---
title: Design Principles
permalink: /overview/principles
---

The OGC Building Block framework addresses the gap between the FAIR principles and traditional approaches to designing and publishing interoperability specifications.

The focus is on **Reusability**, as the point at which value is achieved for both specification creators and specification consumers.

Resuability of common components enhances specification development speed and quality.

Identification of commonalities reduces effort for consumers to understand and exploit specifications.

A range of specific design goals addressed by the OGC Building Blocks are discussed below.

## Abstraction Neutrality
Specifications may apply to different levels of abstraction - i.e. conceptual vs. physical. 
The design principles described here apply to all levels of abstraction.  In particular it must be possible to describe and navigate (Findability) the relationships between specifications at different levels of abstraction.

## Technology Neutrality
Specifications may be tied to a specific technology (e.g. JSON schema), which may be appropriate to a given level of abstraction. The core principles of Building Blocks are independent of the specification technology used.

That said, higher levels of support may be provided for key technologies. A particular focus is on the emerging generation of JSON based APIs and data formats and the challenges of semantic interoperability. Building Blocks may be defined for ontologies, UML models, XML schemas, database schemas or any other technology. 

## Transparency of Dependencies and Commonality
Explicit dependencies between Building Blocks support Findability and understanding (Re-use), and in some cases can directly support interoperability at run-time.  

Many specification languages or target technologies are poor at exposing such dependencies, particularly between different levels of abstraction using different specification languages. Building Blocks allow a **common canonical expression of specification relationships**.  These relationships can be published as a Knowledge Graph, 

## Federation

Building Blocks must support re-use of components across different governance domains. This is supported by [Transparency](#transparency-of-dependencies-and-commonality).

Managing distributed development and evolution cycles is supported by [Regression Testing](#testing.)

## Profiling

Building Blocks should be simple to specialise.

See [Profiles](profiles.md)

## Testing

Testing is automated, and functions in at least four modes:

1) Basic syntax checking of components and descriptions
2) Unit tests of example implementations for individual components, including positive and negative tests
3) Integration testing, including inheritance of tests from dependencies
4) Regression testing to ensure continual compliance with dependent components.











