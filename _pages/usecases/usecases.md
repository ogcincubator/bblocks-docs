---
title: Uses Cases for OGC Building Block Registers
permalink: /usecases/usecases
---

## Writing a new standard

SWGs and document Editors need a simple capability to search and determine if there is a _requirements class_ somewhere in some OGC Standard that they can reuse. Then, if they find that requirements class,  the can use a reference (and unique identifier).   Then at publication, the full content (including the conformance test classes and OpenAPI/YAML content for API standards) would be shown but not actually duplicated. This is the standards' developer use case.

Note that this is not something that is consistently done, or easy to do in the normal course of standards development:

- the technology of the standard may not support re-use by reference
- for various reasons many standards use a copy/paste/edit approach to re-use of schemas (e.g. STAC extensions)
- reusable resources may not have stable URI references, particularly during development and testing - but instead URL for idiosyncratic or temporary locations


## Quality control for a standard

### QC - schema compatibility

Often standards are designed and state intended compatibility with other standards. In the case of validatable standards such as encoding schemas it is possible to define requirements to conform to multiple schemas, in whole or part. Building Blocks can define this as a composite schema that supports testing, whilst retaining the original standard schemas for use in run-time applications.

### QC - example correctness

Testing examples against specifications.  Building Blocks allow for more sophisticated error reporting than most standard developer tools - and layering of additional diagnostics as required. For example SHACL validation that reports which nodes in an example are being tested provides high quality design-time diagnostics, even if this may not be practical for higher throughput run-time validation of data

### QC - testing rules

Rules are powerful aids in supporting use of standards. Often these are "buried" deep in descriptions of requirements. BuildingBlocks allow these to be re-used.

Re-use of complex rules has many advantages - it saves a lot of effort for downstream users of standards to interpret and fashion such rules, using expressions they may not be familiar with.

But such rules need to be trustworthy! Rules themselves should be tested - and this is done by ensuring they actually fail on invalid content.

Provision of both pass and fail cases for all or key rules in a standard tests these rules themselves.


## Publishing improved resources for using a standard
- adding more examples
- adding machine readable validation and guidance tools
- providing examples of combination with related standards
- demonstrating interoperability with available tooling
- defining translations and data integration tools for other standards - such as adaptors, migrations etc.

## Profiling a standard

Why start from scratch if you need a solution? But what if the available standards do not quite cover your specific needs, or need disciple to use consistently in your domain?

Profiles can extend a standard by:
 
- defining additional elements
- constraining use of existing elements (making mandatory, or forcing use of references)
- adding logical rules (e.g. combinations of properties which need to be present)
- defining content rules, such as use of controlled vocabularies

All of these can be done as testable machine readable constraints for JSON-LD enabled JSON schemas - other technologies and profiling concerns can always be implemented with text descriptions.

Profiles of standards are in practice nearly always required.  Due to lack of canonical profiling mechanisms, such profiles have often been long and detailed descriptive documents.

BuildingBlocks allow profiles to be described in a way that inherits any rules from re-used standards.  Such profiles only need to describe the specific **additional** constraints - and they can often be described in **machine readable** forms. 

The use of [semantic uplift](/create/semantic-uplift) is especially valuable to allow machine readable semantic rules to be created by experts and re-used by specialised profiles, and specialised profiles to unambigously create a validation capability. 


## Designing reusable infrastructure

Clear documentation and conformance testing capabilities allow infrastructure such as hosting platforms to define the interoperability requirements for applications to be developed in such platforms.  An example would be a Digital Twin of a complex environment, where the goal is to support evolution of capabilities through extensible data acquisition, processing, visualisation - and user interactions.  
Such infrastructures will typically require profiles of general standards, constrained to use information sources governed and accessible within the infrastructure - such as controlled vocabularies, and particular subsets of component and API functionality supporting discovery and re-use in consistent fashions.

## Applying OGC standards to an application

There are three sub-use cases depending on motivation.

### Interoperability of the application design solution with available tools 
Reduces cost, time, risk and documentation burden on application design.

### Interoperability of the application with other related applications

Reuse of components accelerates design and reduces documentation and testing burdens.  A common documentation style reduces cost of interoperability when integrating different systems. Transparency of reuse of common components reduces the cost of identifying interoperability opportunities and where custom solutions will be required.  For a typical application it is expected that most components will not be unique, and use of well described profiles can address application specific requirements rather than design and documentation of all aspects of component behaviour.

### Deployability of an application in an infrastructure context

Re-use of components defining interoperability capability of infrastructures and platforms can accelerate and guarantee fit-for-purpose design of applications operating in those contexts.

Infrastructures can define base profiles of standards needed for all applications. 

Applications can design by extending or cross-check using **infrastructure specific profiles of standards** as Building Block dependencies.

## Discovering relevant OGC standards

This is supported by the register function of OGC Building Blocks, and the expression as a Knowledge Graph.

The role of AI to assist users match needs to available standards is assumed to become more important. It is expected this will be facilitated by linking standards to each other and documentation about the use of standards, such as Engineering Reports, Guidance, Case Studies and scientific papers.
