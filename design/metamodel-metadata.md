# A meta-model for metadata

This addresses the "Information Viewpoint" for a generalised metadata capability.

It is intended to guide the design of infrastructure, tools and metadata standards for significant scale systems, regardless of system architecture (centralised, federated or distributed) [1] 

Defining "metadata" is notoriously contentious - this discussion takes a wide interpretation that encompasses every component and interaction in a "system of information systems". 

## FAIR

The FAIR principles provide a useful guidance for understanding the **types of metadata** required:

we will simply refer to the role of metadata using the initials of these principles, with the addition of "E=Evaluation"

### F=Findable: 

i.e. "Discovery metadata" - usually associated with catalogues and search functions

Discovery metadata is typically a large, generalised "omnibus" model mixing many aspects

Roles:
  discovery
  advertisement
    
Examples:
    - Schema.org
    - DublinCore
    - DarwinCore
    - DCAT
    - ISO19115
    - Z39-50

Discovery metadata schemas could generally be described as "simultaneously overspecified and underspecified" - they cannot be all things to all people. (Note - this generally applies to any complex schema that is not designed to be modular, extensible and profiled from its foundations. Since such schemas are usually about attaching metadata to raw values this is strongly relevant to note in general.)

### A=Accessible

**A** type metadata is usually in the form of **service catalogues** or components of **data set descriptions** such as DCAT DataDistributions.

i.e. it is usually attached to specific data resource descriptions to support the next step (**FA metadata**) - or provides a means to discover data available at an endpoint - often the means to harvest content into data catalogues.

Access methods may describe machine-accessible endpoints such as APIs.

Access metadata may be a simple reference to a standardised access method, or contain various levels of detail. 

Note that "standardised access methods" usually require a lot more information that just the "method signature" - since it is typical for an access service endpoint to support multiple methof signatures defined by different standards.

API metadata such as OpenAPI description documents allows software tools to build access clients semi-automatically - and increasingly AI agents will build rich capabilities - however the ability to use the data and services will depend on further types of metadata.

Thus there is a spectrum of choices re how much detail is bundled into Access metadata, and often depends on how familiar the user is with the exact nature of the data sources, including its semantics, structure and statistical distribution.

### I=Interoperable

There are two obvious aspects of this:

1. the interoperability of the description of the Access metadata (**IA metadata**)
2. the interoperability of the description of the data

the first is best handled on the basis of **profiles** describing how methods and data interact, which should be based on **data profiles**. 

Data profiles in turn have several obvious elements, each requiring interoperability of expression to support tooling for exploitation (and indeed more sophisticated discovery modes that simple text searches):

- data structure
- data dimensions
- data distribution (by dimension)
- data content (value ranges, including controlled vocabulary)
- data rules (combinations of data that need to be present)
- structure semantics (description of meaning of data structures = objects present)
- attribute semantics (what properties of objects mean)
- content semantics (best handled by controlled vocabularies, but ad-hoc value descriptions may be needed)
- data quality
- data history (provenance)

It is rare that all this metadata is ever present in a single place, but it is hard to consider a valid use of data where at the minimum some assumptions have not been made about each aspect.

The most common pattern observed is tooling handling the implicit semantics of data structures.  This in turn leads to the observation that data structures themselves have different roles and patterns, often used in conjunction with each other.

For example, from the [OGC Building Blocks overview of type:](https://ogcincubator.github.io/bblocks-docs/overview/types)

| Pattern | Description |
|---|---|
| **Aggregation / Composition** | A schema built by assembling other blocks (e.g. via `$ref`/`allOf`) |
| **Extension** | Adds properties to another schema or model (also a form of profiling) |
| **Specialisation** | Constrains an existing attribute with a more specific model (e.g. fixing a FeatureCollection's feature type) |
| **Semantic Annotation** | Binds schema elements to RDF definitions via JSON-LD — especially important when one schema could map to multiple ontologies |
| **Profiling** | Adds constraints for a particular context; may combine specialisation, extension, rules, or vocabulary bindings |
| **Vocabulary Bindings** | Constrains a value to a controlled vocabulary (static or dynamic/service-backed) |
| **Transformations** | Defines a reusable conversion between specifications; validated against the post-transform target |
| **Testing Examples** | Supplies or tests a set of examples for a given specification |
| **Documenting Validators** | Provides test cases, docs, and CI/CT for a validation tool — typically tied to specific profiles |
 
### R=Reusable

Reuse is a **business decision** and such a decision may rely on many factors.

The experience of **Access** and the cost-effectiveness achieved by the level of **Interoperability** will be a factor when there is discretion regarding reuse. When reuse is an imperative, poor metadata for these aspects leads to project cost and risk, and may determine reuse viability.

If F and A+I aspects are all "within tolerance" of available effort and motivation, then other aspects emerge.  This includes the aspects typically covered by the "Engineering Viewpoint" and "Technology Viewpoint".  Cost, risk and reliability may be limiting factors.

One aspect often conflated with the F or search function is around rights and restrictions. Models such as ODRL can be used to describe licences.  We can consider these re-use constraints that need to be surfaced as **FR metadata**.

It is however important to note however that increasingly automated agents are likely to have a role in the navigation of the complexities of reusability. This in turn leads to further constraints on the **AI** metadata to support **evaluation**

## Bringing it together

One key Use Case for integration of this metadata is **Transparency**.  Transparency is fundamental to science, management of state and financial rigour.

Transparency is also a foundation for **Trust** - which supports the end goal of **Reuse** and the efficiency and capability benefits that accrue.

Transparency is enabled by **Provenance**.  Provenance is assembled from the interactions of all systems in an information supply chain. Provenance is expensive or impossible to assemble if done _forensically_ after the fact - so a key goal of **Interoperability** is for **self-assembling provenance chains**.

Such chains however need to be explicit - and these become a driving Use Case for **Vocabulary Services** - persistent registers of objects and definitions that enable provenance chains to be exploited. 

## Summary

There are many components and types of metadata needed to support the implicit action agenda of the FAIR principles - and this deeper analysis suggests that FAIR + Evaluation is a viable meta-model for understanding the **role** of different metadata components.

Rigourous scientific workflows is a good test case for metadata requirements - since there is limited scope for simplifying assumptions where meaning is assumed by referencing strict regulation.  The patterns can easily be applied to any trusted information supply chain.  

Richer provenance metadata, enabled by the totality of this meta-model and a federated register implementation approach can be used to support efficient reuse of capabilities, including data, semantic resources, processing chains and the human expertise available to support information use.



  