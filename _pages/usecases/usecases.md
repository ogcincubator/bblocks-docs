# Uses Cases for OGC Building Block Registers

## Writing a new standard

numerous SWGs and document Editors ask for a simple capability to search and determine if there is a requirements class somewhere in some OGC Standard that they can reuse. Then, if they find that requirements class, they do not have to copy all the content from one standard into another but instead use a reference (and unique identifier). Then at publication, the full content (including the conformance test classes and OpenAPI/YAML content for API standards) would be shown but not actually duplicated. This is the standards' developer use case.


## Quality control for a standard
### QC - schema compatibility
often standards are designed and state intended compatibility with other standards. In the case of validatable standards such as encoding schemas it is possible to define requirements to conform to multiple schemas, in whole or part. Building Blocks can define this as a composite schema that supports testing, whilst retaining the original standard schemas for use in run-time applications.

### QC - example correctness
testing examples against specifications.  Building Blocks allow for more sophisticated error reporting than most standard developer tools - and layering of additional diagnostics as required. For example SHACL validation that reports which nodes in an example are being tested provides high quality design-time diagnostics, even if this may not be practical for higher throughput run-time validation of data

### QC - testing rules
provision of both pass and fail cases for all or key rules in a standard tests these rules themselves.


## Publishing improved resources for using a standard
- adding more examples
- adding machine readable validation and guidance tools
- providing examples of combination with related standards
- demonstrating interoperability with available tooling
- defining translations and data integration tools for other standards - such as adaptors, migrations etc.

## Profiling a standard

## Designing reusable infrastructure

Clear documentation and conformance testing capabilities allow infrastructure such as hosting platforms to define the interoperability requirements for applications to be developed in such platforms.  An example would be a Digital Twin of a complex environment, where the goal is to support evolution of capabilities through extensible data acquisition, processing, visualisation - and user interactions.  
Such infrastructures will typically require profiles of general standards, constrained to use information sources governed and accessible within the infrastructure - such as controlled vocabularies, and particular subsets of component and API functionality supporting discovery and re-use in consistent fashions.

## Applying OGC standards to an application

There are three sub-use cases depending on motivation.

### Interoperability of the application design solution with available tools 
Reduces cost, time, risk and documentation burden on application design.

### Interoperability of the application with other related applications

reuse of components accelerates design and reduces documentation and testing burdens.  A common documentation style reduces cost of interoperability when integrating different systems. Transparency of reuse of common components reduces the cost of identifying interoperability opportunities and where custom solutions will be required.  For a typical applicsation it is expected that most components will not be unique, and use of well described profiles can address application specific requirements rather than design and documentation of all aspects of component behaviour.

### Deployability of application in an infrastructure context

re-use of components defining interoperability capability of infrastructures and platforms can accelerate and guarantee fit-for-purpose design of applications operating in those contexts.

## Discovering relevant OGC standards

This is supported by the register function of OGC Building Blocks, and the expression as a Knowlege Graph.

The role of AI to assist users match needs to available standards is assumed to become more important. It is expected this will be facilitated by linking standards to each other and documentaton anout the use of these, such as Engineering Reports, Guidance, Case Studies and scientific papers.
