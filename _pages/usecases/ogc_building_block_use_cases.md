
# Use Cases for OGC Building Block Registers

## Conventions

The word "specification" is used in many cases - because the target may be less formal than a published standard, but the mechanics of design and testing can and should be similar.  Specifications may become candidate standards in due course, so if the specification development process is powerful and easy enough this pathway is facilitated.

## Use Case 1: Reusing Requirements Classes While Writing a New Standard

- **Audience:** OGC Standard Working Groups (SWGs), Standard Editors  
- **Pre-conditions:**  
  - A new OGC standard is being written  
  - Building Block registry is available
  - Building Blocks reference the published Requirements Classes (the reusable text content) and make text available for discovery
  - A mechanism to include Building Blocks by reference is available in the standards documentation environment

- **Post-conditions:**  
  - References to reusable requirements classes are included  
  - Published documents render full content, identifying common content and new content
  - Content duplication and consistent rendering at publication time using automated publishing tooling.
  - Ready republishing of standard versions for proposal review and update

- **Notes**
  - Developing and testing a standard using a register of Building Blocks allows included and new content to be treated using the same toolkit
  - OGC uses a standards documentation environment ("Metanorma") based on Asciidoc templates
  - An extension to the Building Block Register tooling to generate a Metanorma template would be far more efficient than manual copy/paste approaches currently required.
  - Annotations of requirements could be built into Building Blocks - e.g. as JSON schema annotation elements
  - Editing tools could be created to support capturing requirements during standards development and testing, leading to full automation of the normative components of standards writing.

**Scenario:**  
An editor uses the Building Block Register to reference the one of the optional conformance classes from the GeoPose API (such as YawPitchRoll model) and include this in a new model - for example describing a scene viewpoint in a 3D landscape.  This new model is published at the "press of a button" into a formal standard format with validated examples and clear transparency and validation of its conformance and interoperability with the GeoPose standard.

## Use Case 2: Schema Compatibility for Quality Control

- **Audience:** Standards Developers, Quality Control Engineers  
- **Pre-conditions:**  
  - Encoding or schema-based standard is being authored  
  - Component and compatability target schemas are available
- **Post-conditions:**  
  - Composite schemas support compatibility assertions and conformance testing
  - A Building Block for the stricter validation scenario is available for reuse in other contexts, such as STAC extensions.
  - Improved testing and resulting standard quality
  - Building Blocks and derived knowledge bases have human and machine readable traceability of the design intent of the standard.

**Notes**
  It is also possible to check backwards compatibility of published versions using this approach.

**Scenario:**  
The OGC API Records schema is being developed and declares (in text) an intent to be compatible with the STAC metadata record schema. Using Building Blocks, a composite schema is created requiring conformance to both Records and STAC schemas, and valid STAC examples tested against this combined schema. (This is a real scenario - in practice using this approach a number of inconsistencies were identified and rapidly resolved resulting in a better, more consistent Records standard draft prior to release.) This validates the integration without changing the originals, ensuring runtime and design-time compatibility.

## Use Case 3: Example Validation for Specification QA

- **Audience:** Standards Developers, Tool Vendors  
- **Pre-conditions:**  
  - Examples exist in the standard  
  - Schemas or other validatable descriptions (such as SHACL rules) are available to match the standard requirements  
- **Post-conditions:**  
  - Examples pass semantic and structural validation 
  - Detailed diagnostics are provided to confirm correct operation of the tests 

**Scenario:**
Examples in the specification (a standard or application design specification) are managed in discrete files that can be processed and referenced.  These may be published in-line with normative and descriptive text in a specification. 

## Use Case 4: Rule Testing with Pass/Fail Cases

- **Audience:** Conformance Test Developers, SWGs  
- **Pre-conditions:**  
  - Standard contains testable rules  
  - Framework for capturing positive and negative cases exists  
- **Post-conditions:**  
  - Rules have validated pass/fail cases in test suite  

**Notes**
Complex and subtle rules can be very hard to understand - having confidence in executable versions of these through transparent testing of multiple cases is essential to establishing trust, a vital aspect of Reuse (as per FAIR)

**Scenario:**  
Complex rules - such as the inter-relationships between properties that must be present in Observations and ObservationCollections (ISO 19158, OMS, SOSA) are hard to manually assess for correctness.  Provision of failure test cases ensure that such rules work as intended.



## Use Case 5: Publishing Enhanced Standard Resources

- **Audience:** SWGs, Educators, Tool Vendors  
- **Pre-conditions:**  
  - Standard has been published  
  - There is interest in enriching the standard’s adoption and clarity  
- **Post-conditions:**  
  - Enhanced examples, validation tools, and integration guides are discoverable  

**Scenario:**  
The OGC API - Features standard is extended with additional examples, demonstrations of RDF mappings to semantic models to document feature types, SHACL rules, symbology rules, controlled vocabulary usage in particular circumstances and code to handle these patterns — all linked via the Building Block registry but published independently of the core document. 

Augmented guidance can be published at any time without republishing standards and creating more demanding review of impacts.

## Use Case 6: Profiling a Standard

- **Audience:** Profile Designers, Platform Architects  
- **Pre-conditions:**  
  - A 'parent' standard is available
  - Optionally additional standards to be incorporated are available as Building Blocks
  - Domain-specific constraints or extensions are understood
- **Post-conditions:**
  - One or more valid and documented profiles are published
  - Examples and cross-transformation tests to related standards are tested and included as guidance
  - Relationships between profiles and 

**Notes**
 - whilst not strictly necessary, the base and incorporated component standards can be "wrapped" as Building Blocks to improve visibility of dependencies - and to factor our validation rules common the base standard to avoid replicating these in multiple profiles.
 - 
**Scenario:**  
A national agency in Europe publishes metadata standards restricted to their data policies and vocabularies, as a profile of ```GeoDCAT```, and a matching profile of ```OGG API Records``` to provide an implementation option. This profile is intended to be compatible with both regional standards (DCAT-AP - the DCAT Application Profile for European Portals) and domain specific standards - for example metadata for Machine Learning Training sets. 

A series of profiles is discovered to help compartmentalise different requirements for different circumstances into multiple simple profiles rather than a single complex profile with many rules about different content requirements. The Building Blocks make this easy to "refactor" requirements and track dependencies and commonalities across these different needs.

The new and coherent set of profiles is published into their national standards documentation environment, but discoverable to a wider audience via the Building Block registry and supports cross-agency reuse and adaptation by other jurisdictions.

## Use Case 7: Designing Reusable Infrastructure

- **Audience:** Digital Twin Developers, Platform Providers  
- **Pre-conditions:**  
  - An infrastructure supporting resource re-use is being developed
- **Post-conditions:**  
  - Infrastructure exposes API/data interfaces that align with known standards
  - API and data standards are published as one or more Building Block Registers
  - Documented standards are incorporated in any addition infrastructure documentation systems as required
  - Applications can plug in with minimal change  

**Scenario:**  
A smart city’s digital twin reuses profiles of CityGML and OGC API - Tiles. Platform components document their interoperability requirements using registered Building Blocks, allowing external apps to integrate smoothly.

## Use Case 8: Applying Standards in Application Design

- **Audience:** Application Developers, System Integrators  
- **Pre-conditions:**  
  - Application design is underway  
  - Interest in OGC-compliant components exists  
- **Post-conditions:**  
  - Interoperable, standards-based application is developed

**Notes**
Reusing proven patterns reduces design and documentation costs, risks and improves capabilities to handle scenarios understood by the standards developers but not necessarily well anticipated during early design stages.

**Sub-Scenarios:**  

### A. Interoperability with Tools  
A tool (e.g. software library or application) can validate outputs simply by adding examples to a local copy or extended application profile of a Building Block.  The enhanced validation and reporting capabilities reduce development and testing time, support regression testing for changes and versions in both code and standard, and provide transparent quality assurance record for development processes. 

### B. Application-to-Application Interoperability  
Two application components share information according to an agreed and documented specification. Building Blocks support transparent testing of each the outputs, but also allow refinement to handle profiles for different circumstances. 

### C. Deployability in Infrastructure  

A key design requirement may be to be able to deploy an application within a specific environment. This may have three aspects requiring detailed specifications, and commonality between these specification aspects can be handled using Building Blocks:
 1. Understanding data sources (and outputs of other components) during application design
2.  Documenting application outputs for reuse
3. Registering and categorising deployed applications according to infrastructure cataloguig requirements for management or discovery.

## Use Case 9: Discovering Relevant OGC Standards

- **Audience:** New Users, AI Assistants, Developers, Researchers  
- **Pre-conditions:**  
  - A user has a specific problem or interest  
  - The Building Block knowledge graph and register are available  
- **Post-conditions:**  
  - Relevant standards and implementation guides are suggested  

**Scenario:**  
A researcher wants to publish water quality data. An AI assistant queries the Building Block knowledge graph and suggests a profile of OGC SensorThings API, provides sample datasets, and links to a related case study.
