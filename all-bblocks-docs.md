<!-- source: _pages/overview/whatis.md -->

# What is a Building Block?

An Building Block is a way of packaging a component of a **specification** that can be re-used in other specifications.

This packaging directly supports **reuse** (according to FAIR principles), following these [Design Principles](overview/principles).

For various reasons specifications have often made statements in text regarding how they relate to other specifications, and created implementation artefacts such as schemas that may not make these intentions explicit. OGC Building Blocks support **technology agnostic dependency and rtelationshops** - essentially forming the data management method for this apsect of OGC's knowledge graph (OGC RAINBOW).

The key focus is on automated quality control, via inheritable testing on a simple aspect-by-aspect basis for standards as they are composed from common specification elements into comprehensive specifications to support data exchange and analysis applications/  

The following diagram shows how Building Blocks form a value-added packaging option for such specification elements that can then be exploited as part of a comprehensive knowledge base to support discovery and re-use (FAIR principles).

![Overview](https://lucid.app/publicSegments/view/266abfd3-ed51-43a8-a9b0-8e3251c28b54/image.png)

Many OGC Standards contain reusable building blocks that can be used in other OGC Standards. The Standards themselves can also be structured with modular sets of requirements that collectively function as a reusable building block (see image bellow).

[![Usage](/assets/api-bblocks.png)](/assets/api-bblocks.png)

To facilitate the discovery of these building blocks by other Standards and applications, once they are identified their definition should be published in the [OGC Register](https://opengeospatial.github.io/bblocks/register/). Normative information about the OGC Standards building blocks can be found in the [Technical Committee Policies and Procedures](https://docs.ogc.org/pol/05-020r29/05-020r29.html#building-bloocks) 

---

<!-- source: _pages/overview/principles.md -->

# Design Principles

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













---

<!-- source: _pages/overview/registers.md -->

# Building Block Registers

OGC BuildingBlocks are published as registers (collections), with each repository defining a sub-register that can be aggregated.

Aggregated registers will all have their own governance regimes, which SHOULD be clearly defined as documentation describing scope and rules for inclusion.

Key examples include:

- [OGC Specification Building Blocks](https://opengeospatial.github.io/bblocks/register/) - Building Blocks defined by OGC specifications. (_may include common utility patterns common to multiple specifications_)
- [OGC Incubator Building Blocks](https://ogcincubator.github.io/bblocks/) - Building Blocks needed by multiple application domains. (_not yet formally transferred to an appropriate SWG_)
- [Examples](https://ogcincubator.github.io/bblocks-examples/) - Examples of different types and usage patterns. (_these are NOT intended as reuse except in examples and tutorials_)
- [Tutorial](https://ogcincubator.github.io/bblocks-tutorial/) - a step-wise introduction to various features and configuration details for Building Blocks.

![OGC Building Block Register Ecosystem](https://lucid.app/publicSegments/view/9d075f82-8611-4f32-83eb-994143669cc8/image.png)

---

<!-- source: _pages/overview/profiles.md -->

# Profiles

BuildingBlocks support two usage modes:
- composition
- profiling

This document described profiling mechanisms.

**Profiles** allow all the underlying details of base standards to be automatically included in testing and validation - this _encapsulates_ the underlying complexity of base specifications.
 
This dramatically **simplifies** profiles in terms of both development and usage, and ensures **consistency** and conformance of profiles with base specifications.

In particular, if base specifications use the OGC BuildingBlocks then profiles can _leverage_ all the effort in design, testing and validation capabilities.

Thus profiles also use the same structures, so they can be profiled in turn.

## What is a profile?

A profile defines a set of constraints on a base specification. Implementations of profiles conform to the base specification.

Because many technologies like JSON and RDF are permissive (by default) about additional information being present, definition of an *extension* is effectively defining a *constraint* on how additional information should be represented.

## Profiles of profiles... 

Profiles can be designed as separate re-usable sets of constraints that can be reused - for example a time-series of water-quality monitoring observations could be specified as a profile of both a time-series profile of Observations and a water-quality profile for the results of such observations.
In turn the time-series profile could defined as data structure using GeoJSON, or Coverage JSON.  The water-quality content requirements could be described using constraints independent of the data structure.

## Profiles for infrastructure compatibility

Profiles can be layered to meet different needs. The typical usage is for applications that are compatible with shared infrastructures, where applications may be designed to interact with other applications, but the supporting infrastructures for these applications may also be designed to interoperate with other infrastructures.

Underlying standards allow reusable software and libraries to be used at all levels.

This can be visualised as a layered model of typical profiles, identifying the types of constraints typically present at each layer. 

![Profile layers](profiles.png)


## What forms of constraints are possible?

The **OGC BuildingBlock** model supports a range of possible constraint approaches.  The goal is to make such constraints **_machine-readable_** to the extent possible.

Constraints SHOULD be defined in a form that allows for **_validation_** of test cases and examples.

Built-in support is provided for automatic validation of the following forms:
- project metadata (description)
- well-formed example encoding (JSON, TTL)
- JSON schema (for JSON examples) for **structure**
- SHACL (Shapes Constraint Language for RDF) for **content** and **logical consistency**

In addition [custom validators](../create/validation) can be added to the validation workflow. 

Using a JSON-LD context "semantic uplift" of JSON to RDF supports use of SHACL and other forms of validators to 

## Testing

Test cases should be provided for each component part of a specification.  This requires a minimal conformant **base example** that the specific test case can be added to.

(Note consideration is being given to making such a baseline example resuable by reference instead of duplication, and potentially derived automatically from declared schema)

Testing should start by validating the **base example** passes all declared constraints, then for each profile constraint:
- identifying a set of valid cases that should conform to the constraint, testing each aspect
- creating a copy of the base under the **/tests/** folder with a name indicating which constraint and case is being tested - e.g. **my-building-block/tests/mything-property-b-number.json**
- adding the specific example to the example
- creating one or more failure tests with **-fail** file name endings - e.g. **my-building-block/tests/mything-property-b-number-fail.json**










---

<!-- source: _pages/overview/types.md -->

# Building Block Types

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




---

<!-- source: _pages/overview/relationships.md -->

# Building Block relationships

Several types of relationships can be declared when defining Building Blocks.

## <a name="type-dependsOn"></a>Generic dependency (`dependsOn`)

This relationship implies that a building block depends on another, in a generic manner.

This is the default type of relationship that exists, for example, when the schema of a building
block is referenced from another. 

This type of dependency uses the `dependsOn` property in the building blocks register and metadata files.

## <a name="type-profileOf"></a>Profiling (`profileOf`)

Profiling signals that a building block does not merely reference or reuse another, but that it _extends_ it,
that is, it inherits its main structure and provides additional metadata properties, constraints, examples, etc.

This type of dependency is declared using `profileOf` in `bblock.json`.

## Extension points

When defining [extension points](../create/extension-points.md), three new types of relationships are involved.

### <a name="type-extends"></a>Extends

This relationship links a building block with the another that is used as an extension base, and for 
which extension points are defined. It is a special case of the `profileOf` property.

### <a name="type-extensionTarget"></a>Extension target

This relationship links a building block to another that is used to augment or constraint references to an
[extension source](#type-extensionSource).

### <a name="type-extensionSource"></a>Extension source

This type of relationship binds an [extension target](#type-extensionTarget) with the original building
block referenced by the [extension base](#type-extends).

---

<!-- source: _pages/usecases/usecases.md -->

# Uses Cases for OGC Building Block Registers

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

Rules are powerful aids in supporting use of standards. Often these are "buried" deep in descriptions of requirements. Building Blocks allow these to be re-used.

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


---

<!-- source: _pages/usecases/stac_extension.md -->

# STAC extensions

## Creating or updating a STAC extension

_(This is a work in progress and we will explore even better ways to support STAC and Records extensions)_


### STAC extension mechanisms

STAC extensions are defined in a repository and provide a number of elements - they are in fact a "STAC Building Block" in that they can be combined with each other. ("Building" is the fundamental concept here!)

The current approach to defining a STAC extension](https://stac-extensions.github.io/) currently is based on a git repository template, then editing a full copy of the STAC item and/or collection schemas.

This approach has several issues that could be improved:

- interdependencies are not visible
- recommended combinations are not named, and visibility of design intent limited to free text and examples.
- extensions may have inconsistent schemas, reuse of schema elements and duplication.
- version dependence is not well handled
- duplications exist without a deprecation mechanism
- a lot of JSON schema syntax is required to achieve very simple things
- the actual extension is buried deep in a complex schema
- there is no formal [governance of the extension mechanism](https://stac-extensions.github.io/) as a register
- key prefixes are recommended to avoid clashes - but no register of these exist - nor are they synced to other prefix mechanisms such as namespaces for CURIEs


### Building Blocks for STAC

most of the limitations discussed above could be avoided by using a formal register of Building Blocks with a simplified profiling mechanism - with auto-generation of STAC schemas for a suite of supported versions.

Using the OGC Building Blocks approach to define or annotate a STAC extension provides an additional layer of support for:

- AI-ready semantic annotation of the meaning of elements.
- validating examples work with other STAC schemas
- documenting the relationships between STAC schemas
- integration of STAC schemas and or conceptual model into other metadata models
- integration of other building blocks into STAC schemas


### Dependency modelling and reduction of duplication

Refactoring STAC schemas to reuse (rather than copy) sub-schemas for specific patterns makes it clear the common semantics and intended interoperability of these sub-schemas.

For example, this could have avoided the triplication of "raster" models from EO, raster and core 1.1 schemas that now makes extensions like [STAC-MLM](https://ogcincubator.github.io/bblocks-stac/bblock/ogc.contrib.stac.extensions.mlm) very verbose and complex.

### Documentation management

By linking a STAC sub-schema building block to an ontology (description of all the elements) using JSON-LD "semantic uplift" documentation can be generated automatically, and kept up to date.  This semantic documentation can be combined with other stac extensions to create rich documentation of how a community profile uses multiple STAC extensions.



---

<!-- source: _pages/usecases/functions.md -->

# Specifying functions

## Creating a function specification

_(This is a work in progress in consultation with the GeoSPARQL WG)_

### Goals:

- Document a function in some language
- Provide examples of execution
- Provide a test suite
- Provide a range of implementation resources

### Implementation resources

possible implementation resources include:

- formal mathematical expression
- implementation in one or more programming languages
- references to libraries
- test suites.

### Building Blocks support

- make all implementation resources visible by role and language
- provide extension point to execute function on examples during validation
- provide in-line or linked online playgrounds


---

<!-- source: _pages/build/local.md -->

# Quick Start - Tutorials

## Quick how-to build locally

1. Install docker 
2. Check out any valid Building Block implementation (e.g. [bblocks-examples](https://ogcincubator.github.io/bblocks-examples/))
3. cd to the new directory
4. run `build.sh` or `build.bat` if present
   - this will access the current build scripts and compile the building block locally
   - if not present run the command 
 ```shell
# Process building blocks
docker run --pull=always --rm --workdir /workspace -v "$(pwd):/workspace" \
  ghcr.io/opengeospatial/bblocks-postprocess  --clean true --base-url http://localhost:9090/register/
```
5. run the view.sh or view.bat to preview the local build
 - if not present run 
 ```shell
docker run --rm --pull=always -v "$(pwd):/register" -p 9090:9090 ghcr.io/ogcincubator/bblocks-viewer
```
You can now experiment with the source material - or proceed to [create your own building blocks](../create).

(create a fork if you want to update the the repository so you can submit pull requests. The local build outputs will be ignored automatically on updates.)

## Postprocessing a subset of building blocks

Adding `--filter {id}` to the docker build command,  where {id} is a Building Block id such as `ogc.bbr.examples.feature.externalSchema` will limit processing to a single BBlock


---

<!-- source: _pages/build/github.md -->

# Quick Start - Github Automation

# Configuring Github automations for CI/CT build

New and forked Github repositories need configuration to allow automated building. 

1. Fork the template or another repository to a git organisation you have admin access for.
1. In settings set "pages build" to "Github actions"
![](pages.png)
2. Run the "validate and postprocess" action 
![](run.png)
3. Link the generated output pages to the repo overview by selecting "show" 
![](link.png)

You can now navigate between repository sources and the published Building Blocks:

![From Repo to docs](to_register.png)

![From Docs to Repo](to_repo.png)

---

<!-- source: _pages/build/tutorial.md -->

# Quick Start - local build

# Building Blocks Tutorials

A range of tutorials will provide step by step introduction to the features of OGC Building Blocks.

Please raise an [issue](https://github.com/ogcincubator/bblocks-docs/issues) for new tutorial requests

## Tutorials

### [Core](https://ogcincubator.github.io/bblocks-tutorial/)

This steps through the core features of the OGC Building Blocks framework with an emphasis on OGC API ready, semantically enabled JSON schemas.


## Planned tutorials

### Governance

A description of various governance patterns and an introduction to OGC Policies and Procedures in relation to Building Blocks.

### Building interoperable metadata profiles (STAC, Records, 19115, DCAT etc)

This will focus on metadata design and the various extension and profiling mechanisms for metadata standards relevant to the OGC mission.

Transformations and testing will be a key aspect due to the variations schemas and encoding technologies in use.

### Data transformations

Transformations will be a constant challenge, and a wide range of transformation languages and tools may be needed - this tutorial will show options and how to extend the framework to include your own transformation tools.

### Semantic Model Publishing

Publishing semantic (RDF, OWL, SHACL) etc models is difficult due to limitations of existing tools. This tutorial will demonstrate how to factor semantic models into FAIR building blocks and make the model itself FAIR.

### UML models

UML models are notoriously difficult to manage in a modular fashion - this tutorial will focus on FAIR UML models - composition and testing.

---

<!-- source: _pages/build/contribution.md -->

# Build - Contributing

# Contributing updates to Building Blocks

One way to contribute to an already existing Building Blocks register is to
[fork it on GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo),
apply your own changes to your copy of the register and, when ready, create a
[Pull Request (PR)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
so that they can be included in the upstream register.

Creating a fork allows you to work on the `master`/`main` branch, which triggers the Building Blocks [postprocessing
workflows](../create/postprocessing), so you can preview your version of the register on its own GitHub pages. However,
by default GitHub disables workflows on forked repositories, so you need to manually enable them on the "Actions" tab
of your forked repository.

![Screenshot showing how to enable workflows in GitHub forks](github-fork-workflows-enable.png)

## Merge conflicts

The main downside of working with forks is that the Building Blocks postprocessing workflow generates artifacts
inside the `build/` directory of the repository, which can result in 
[merge conflicts](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github)
when the Pull Request is created, making the process more difficult.

To work around this, the following bash script can be used to create a "clean" branch excluding all changes in the 
`build/` directory, which can then be used to create the Pull Request from (instead of the `master`/`main` one):
[create-clean-pr.sh](https://gist.githubusercontent.com/avillar/acb3e22d36ddf1ddbf8ff5c1aa64616f/raw/create-clean-pr.sh)

The script is run locally on the directory of the forked register, and it requires that the upstream repository
(i.e., the original Building Blocks register) is
[added as a remote](https://docs.github.com/en/get-started/git-basics/about-remote-repositories#creating-remote-repositories).
By default, the `fork-parent` remote name will be used, but it can be configured to something different (e.g., `upstream`).

The script will create a new branch with a random name, clean any changes done to the `build/` directory and anything in it, 
push the branch to your fork of the register, and provide you with a URL to create the Pull Request directly.

It relies on the [`git-filter-repo`](https://github.com/newren/git-filter-repo) Python script, so you must have a working
Python environment for it to work. If `git-filter-repo` is already installed on your system, the script will use it,
and otherwise will download a copy to a temporary directory (which will be deleted once it is done).

## Fork-specific configuration overrides

When working on a fork, you may want to change some settings in `bblocks-config.yaml` — for example, to use a different
identifier prefix or a different set of imports — without those changes being included in the Pull Request.

You can do this by creating a `bblocks-config-override.yml` (or `.yaml`) file at the root of your repository. Any
top-level key present in this file will override the corresponding value from `bblocks-config.yaml`. For example:

```yaml
# bblocks-config-override.yml
identifier-prefix: my-fork.
imports:
  - https://www.example.com/overriden-import-1
  - https://www.example.com/overriden-import-2
```

The `create-clean-pr.sh` script automatically excludes `bblocks-config-override.yml/yaml` from the clean PR branch,
so these fork-specific settings will never appear in Pull Requests to the upstream register.

---

<!-- source: _pages/use/finding.md -->

# Finding Building Blocks

Whilst components described as Building Blocks may be referenced by individual specifications, due to evolution of the specification publication process over time this is not consistent in terms of identification or disposition of published artefacts. Such components may be published as discrete resources, or bundled in larger packages. They may or may not be in consistent machine-readable forms. This leads to many challenges for discovery of such components.  General text search options may assist, but will be subject to limited ability to precisely recall only relevant components.

The OGC Building Block Framework provides three improved approaches for discovery:

1. [Registers](../overview/registers)
1. [RAINBOW (OGC Knowledge Graph)]() 
1. Transparent Dependencies 


# Well-known Building Blocks registers

## OGC Specifications

- [OGC Specification Building Blocks](https://opengeospatial.github.io/bblocks/register/) - Building Blocks defined by OGC specifications. (_may include common utility patterns common to multiple specifications_)

## OGC Specifications (in development)

- [OGC API - SOSA](https://opengeospatial.github.io/ogcapi-sosa/) - Implementation of the [OMS/ISO 19156 standard](http://www.opengis.net/def/docs/20-082r4) using the [SOSA ontology](https://www.w3.org/TR/vocab-ssn/).
- [OGC API Records - GeoDCAT](https://ogcincubator.github.io/geodcat-ogcapi-records/) - Implementation of GeoDCAT using OGC API Records

## Incubator

- [OGC Incubator Building Blocks](https://ogcincubator.github.io/bblocks/) - Building Blocks needed by multiple application domains. (_not yet formally transferred to an appropriate SWG_)

## Projects

- [ILIAD Digital Twin of the Ocean - OGC API Profiles](https://ogcincubator.github.io/iliad-apis-features/)

---

<!-- source: _pages/use/ftc.md -->

# Feature Type Catalogs

Building Blocks solve a key limitation of traditional specifications using mixtures of documentation styles and locations - by normalising the documentation for a wide range of specification types it allows for increased **Access** in practice - since all the reusable components can be reliably found via the underlying Linked Data and Register models.

The concept of a "Feature Type Catalog" (FTC) has been widely accepted as a concept, however interoperable implementations have been slow to emerge.

This may be because FTCs in practice need to be technically aligned with the underlying infrastructure publishing Features as data, and this in turn has two distinct aspects: persistence (how features are stored) and transfer (how they are exposed). Both of these aspects tend to be technology dependent, and hence expression of Feature Types is often tied to one or other of such aspects.

Building Blocks provide a new opportunity to publish Feature Types in a technology agnostic way, using multiple schemas mapped to common semantic models, supported by examples and validation.

Effectively this means the design pattern of a schema mapped to a Class with a Frame (a set of properties). Building Blocks can handle abstract or conceptual models, or technology specific physical implementation schemas, and crucially and uniquely the **relationships between concepts and implementation options**.


---

<!-- source: _pages/use/linked-data.md -->

# Linked Data / JSON-LD Context

# Linked Data 

The key characteristic of Linked Data is that elements of data can be linked to more resources.

The main aspects of this are:

1. Schema elements and data contents can be **unambiguously** identified - allowing all sorts of downstream operations to be performed with confidence.
2. Elements of schemas can be linked to explanations and documentation
3. Data values can be linked to controlled vocabularies with definitions
4. Data values can be links to other data objects

The key enabler for Linked Data is the use of RDF - and this can be done with "native RDF" - but the focus on the Building Blocks is "semantic uplift" of JSON.

This can be done with JSON-LD. Whilst it has its limitations JSON-LD is a commonly used standard that provides an enabler.

The challenges with JSON-LD lie in its mirroring of underlying JSON schema structures - it doesnt support significant structure reorganisation, and its complex to build JSON-LD contexts that mirror complex schemas.

The OGC Building Blocks **solve this** by allowing unit-testing of simple JSON-LD contexts for sub-schemas, and compilation of reliable context documents for schemas that re-use these sub-schemas.
(Note this is currently the only Open Source tooling known to support this, and was developed in consultation with JSON schema design leads.)

For more information refer the [Use Cases](/usecases/usecases) and 



---

<!-- source: _pages/use/reusing-schemas.md -->

# Reusing schemas

Building Blocks can be reused in several ways:

- if creating a JSON schema based BuildingBlock then use the $ref: bblocks://{block id} to make a JSON schema reference to any building block in the import list [see imports](../create/imports)
- for other [types of Building Blocks](../overview/types) declare as an entry in the dependsOn element of a `block.json` metadata file
- cut and paste "ready to use" forms from the `build/` directory of any building block repository into a some other form of application (not a reusable Building Block itself)
- directly reference the artefacts in the `build` directory using the URL pattern specified in the building block
  description (noting this may be affected by changes if a building block is moved from one register to another - bblocks:// references will still work if imports approach is used.)


---

<!-- source: _pages/create/index.md -->

# How to create Building Blocks

## starting point options:

1. Create from scratch using a template - see below
2. Fork an existing repository to update or add new building blocks, and generate a Pull Request to submit to the register owner
2. Copy any building block repository and edit `bblocks-config.yaml` and the `_sources/*` to create a new register

In all cases follow the [local build process](../build/local) to test before committing to an online repository.

## Quick how-to create

1. Navigate to the [bblock-template](https://github.com/opengeospatial/bblock-template) repository.
2. Click on "Use this template" on GitHub (do not fork this repository, or you will have to manually enable the
   workflows).
3. Set the `identifier-prefix` provided by OGC in `bblocks-config.yaml`:
   * The first component of the prefix should represent the entity defining or maintaining this building block
     collection. If this is an OGC-related project, you may use `ogc.` here.
   * The rest of the prefix components should be chosen according to the nature of the collection. For example, if
     this repository only contained schemas for *OGC API X* version 1.x,
     a possible prefix could be `ogc.apis.api-x.v1.schemas.`.
   * Bear in mind that the path of the building blocks inside `_sources` will be used in their identifiers (see below).
   * **Identifiers should be as stable as possible**, even when under development. This makes it easier to promote
     building blocks to production (i.e., being adopted by the OGC as official), and avoids having to manually/update
     references (in dependency declarations, schemas, etc.).
4. Set a `name` for the repository inside `bblocks-config.yaml`.
5. Configure any necessary [imports](imports) inside `bblocks-config.yaml`.
6. Set the [additional register metadata properties](#additional-register-metadata-properties) in `bblocks-config.yaml`.
7. For each new building block, replace or create a copy of the `mySchema` or `myFeature` inside `_sources`.
   Note: **the path to and name of the new directory will be part of the building block identifier**.
8. Update the [building block's files](structure).
   1. [Add documentation](documentation) to your Building Block.
   2. See [defining a schema](schema) for information how test an existing schema.
   3. See [adding JSON-LD context](json-ld-context) for information how to "uplift" a schema - linking to a model using JSON-LD.
   4. See [validation](validation) for information how to define powerful constraints for schemas and semantic models.
   5. See [transforms](transforms) for information how to define and test transformations.
9. Replace the README.md file with documentation about the new building block(s).
10. Enable GitHub pages in the repository settings, setting "Source" (under "Build and deployment")
    to "GitHub Actions".

## Additional register metadata properties

The following additional properties can be set inside `bblocks-config.yml`:

* `name`: A (short) string with the name of the register.
* `abstract`: A short text to serve as an introduction to the register or building blocks collection. 
  Markdown can be used here.
* `description`: A longer text with a description of the register or collection. Markdown can be used here.

---

<!-- source: _pages/create/imports.md -->

# Setting up imports

Any building blocks repository can import any other repository, so that references by id to building blocks
(e.g. inside schemas, in `bblock.json`, etc.) belonging to the imported repositories can be automatically resolved.

Repository imports can be defined as an array of URLs to the output `register.json` of other repositories inside
`bblocks-config.yaml`:

* If `imports` is missing from `bblocks-config.yaml`, the
  [main OGC Building Blocks repository](http://blocks.ogc.org/register.html) will be imported by default.
* `default` can be used instead of a URL to refer to the
  [main OGC Building Blocks repository](http://blocks.ogc.org/register.html). 
* If `imports` is an empty array, no repositories will be imported.

For example, the following will import two repositories, one of them being the main OGC Building Blocks repository:

```yaml
name: Repository with imports
imports:
  - default
  - https://example.com/bbr/build/register.json
```

*Note*: If the URL ends with `build/register.json` or `register.json`, you may omit the last part. For example,
when `https://example.com/bbr` is provided as an import, these URLs will be tried:

  * `https://example.com/bbr` 
  * `https://example.com/bbr/build/register.json`
  * `https://example.com/bbr/register.json`

The first URL to return a valid `register.json` will be used. 

## Local URL mappings (for testing)

Sometimes, a remote repository may not be available publicly (e.g., for security reasons). In that case,
URL-to-local-path mappings can be added inside an `url-mappings` object in a
`bblocks-config-local.yml` file, like so:

```yaml
url-mappings:
  'https://example.com/bbr/': '/imports/ogc/bblock-prov-schema'
  'https://example.com/relative/': '../../ogc/bblock-prov-schema'
```

This will redirect all requests to `https://example.com/bbr/...` to the `/imports/ogc/bblock-prov-schema/...` path,
and `https://example.com/relative/...` to `../../ogc/bblock-prov-schema/...`; for example, 
`https://example.com/bbr/path/to/file.txt` will correspond to `/imports/ogc/bblock-prov-schema/path/to/file.txt`.

When running the bblocks-postprocess Docker container, these additional repository copies need to be made 
available to it as mounted [volumes](https://docs.docker.com/engine/storage/volumes/#options-for---volume):

```yaml
 -v "$(pwd)/../../ogc/bblock-prov-schema:/imports/ogc/bblock-prov-schema"
```

If you are using `build.sh` as suggested in [Local Build](../create/local), you can automate the volumes that
will be mounted in the `docker` command by creating a `.volumes` file in which each line will represent a
`<local path>:<container mount path>` pair. For example:

```
/absolute/path/to/mount:/mount/absolute
../relative/path:/mount/relative
```

When you run `build.sh`, the `.volumes` file will be parsed and the volumes will be mounted.


---

<!-- source: _pages/create/structure.md -->

# Building Block structure

The following image summarizes the general usage of a building block:

[![Usage](../assets/usage.png)](../assets/usage.png)

## Building Block sources

The `_sources` directory will contain the sources for the building blocks inside this repository.

- `bblock.json`: Contains the metadata for the building block. Please refer to this
  [JSON schema](https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/master/ogc/bblocks/schemas/metadata.schema.yaml)
  for more information.
- `description.md`: Human-readable, Markdown document with the description of this building block.
  See [Adding documentation](documentation) for more information.
- `examples.yaml`: A list of examples for this building block. See [Examples](examples).
- `schema.json`: JSON schema for this building block, if any. See [JSON schema](schema).
    - `schema.yaml`, in YAML format, is also accepted (and even preferred).
- `assets/`: Documentation assets (e.g. images) directory. See [Assets](#assets) below.
- `tests/`: Test resources. See [Validation](#validation-and-tests).

Building Block identifiers are automatically generated in the form:

```
<identifier-prefix><bb-path>
```

where:

- `identifier-prefix` is read from `bblocks-config.yaml`. This will initially be a placeholder value,
  but should have an official value eventually (see [How-to](#how-to)).
- `bb-path` is the dot-separated path to the building block inside the repository.

For example, given a `r1.branch1.` identifier prefix and a `cat1/cat2/my-bb/bblock.json` metadata file,
the generated identifier would be `r1.branch1.cat1.cat2.my-bb`. This applies to the documentation
subdirectories as well, after removing the first element (e.g., Markdown documentation will be written to
`generateddocs/markdown/branch1/cat1/cat2/my-bb/index.md`).

### Grouping Building Blocks

Building blocks subdirectories can be grouped inside other directories, like so:

```
type1/
  bb1-1/
    bblock.json
  bb1-2/
    bblock.json
type2/
  subtype2-1/
    bb2-1-1/
        bblock.json
[...]
```

In that case, as noted above, `type1`, `type2` and `subtype2-1` will also be part of the building block identifiers.

## Additional register metadata properties

The following additional properties can be set inside `bblocks-config.yml`:

* `name`: A (short) string with the name of the register.
* `abstract`: A short text to serve as an introduction to the register or building blocks collection. 
  Markdown can be used here.
* `description`: A longer text with a description of the register or collection. Markdown can be used here.

## Ready to use components

The `build/` directory will contain the **_reusable assets_** for implementing this building block.

*Sources* minimise redundant information and preserve original forms of inputs, such as externally published
schemas, etc. This allows these to be updated safely, and also allows for alternative forms of original source
material to be used whilst preserving uniformity of the reusable assets.

**The `build` directory should never be edited**. Moreover, applications should only use (copy or reference) resources
from this directory.

---

<!-- source: _pages/create/postprocessing.md -->

# Postprocessing overview

Building Blocks sources are post-processed using a workflow package maintained by the OGC. You may modify this if needed to perform additional actions - however this is subject to continual improvement as new types of building blocks are supported and improvements in available tools are made.



![OGC Building Blocks processing](https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/master/process.png)

### Output testing

The outputs can be generated locally by running the following:

```shell
# Process building blocks
docker run --pull=always --rm --workdir /workspace -v "$(pwd):/workspace" \
  ghcr.io/opengeospatial/bblocks-postprocess  --clean true --base-url http://localhost:9090/register/
```

**Notes**:

* Docker must be installed locally for the above commands to run
* The syntax for `-v "$(pwd):/workspace"` may vary depending on your operating system
* Output files will be created under `build-local` (not tracked by git by default)
* The value for `--base-url` will be used to generate the public URLs (schemas, documentation, etc.). In this case,
  we use the local `http://localhost:9090/register/` URL to make the output **compatible with the
  viewer** when running locally (see below). If omitted, the value will be autodetected from the repository
  metadata.

#### Building Blocks Viewer

You can also preview what the output will look like inside the Building Blocks Viewer application:

```shell
docker run --rm --pull=always -v "$(pwd):/register" -p 9090:9090 ghcr.io/ogcincubator/bblocks-viewer
```

**Notes**:

* Make sure to [compile the register](#output-testing) before running the viewer (or delete `build-local`
  altogether to view the current build inside `build`).  
* Docker must be installed locally for the above commands to run
* The syntax for `-v "$(pwd):/register"` may vary depending on your operating system
* `-p 9090:9090` will publish the Viewer on port 9090 on your machine

---

<!-- source: _pages/create/metadata.md -->

# Building Block metadata

Building block metadata provides context information about the item in the building blocks register. It is based on [ISO 19135](https://www.iso.org/standard/54721.html), the standard for item registration of geographic information, from which it extracted its six mandatory items (flagged with *). The ISO schema is extended with other properties (in green), which account for things such as the visual representation in the register, item validation or relation with other building blocks.

[![building block](../assets/bblock.png)](../assets/bblock.png)

## Property reference

### Core (ISO 19135)

| Property | Required | Description                                                                                                                 |
|---|---|-----------------------------------------------------------------------------------------------------------------------------|
| `name` * | yes | User-friendly name for this Building Block.                                                                                 |
| `abstract` * | yes | Short description. Shown as a summary in the register.                                                                      |
| `status` * | yes | One of: `under-development`, `experimental`, `stable`, `superseded`, `retired`, `invalid`, `reserved`, `submitted`.         |
| `dateTimeAddition` * | yes | ISO 8601 date-time when this Building Block was added to the register (e.g. `2024-01-15T00:00:00Z`).                        |
| `itemClass` * | yes | Type of Building Block. See [Item classes](#item-classes).                                                                  |
| `version` * | yes | Version string (e.g. `0.1`, `1.0.0`).                                                                                       |
| `itemIdentifier` | auto | Unique identifier. Auto-generated from the register prefix and directory path — do not set manually.                        |
| `dateOfLastChange` | no | ISO 8601 date of the latest change (e.g. `2024-06-01`). Autodetected from git. Falls back to `dateTimeAddition` if omitted. |

### Item classes

| Value | Description |
|---|---|
| `schema` | JSON Schema object type / feature type |
| `datatype` | Simple JSON Schema data type |
| `path` | OpenAPI path |
| `parameter` | OpenAPI parameter |
| `header` | OpenAPI header |
| `cookie` | OpenAPI cookie |
| `response` | OpenAPI response object |
| `api` | Partial or full OpenAPI document |
| `model` | Ontology or data model |

### Links and references

| Property | Description |
|---|---|
| `sources` | Array of `{ title, link }` objects listing specifications, papers, or other documents this Building Block is based on. |
| `link` | Single URL to a website or external documentation page. |
| `links` | Array of `{ title, href, rel?, notes? }` link objects for richer link sets. |
| `tags` | Array of free-text strings for categorisation and search. |
| `group` | A short identifier to visually group related Building Blocks in the register. |
| `highlighted` | Boolean. Marks this Building Block as featured in the register's entry page. |

### Lifecycle and relationships

| Property | Description |
|---|---|
| `predecessor` | Identifier or URI of the Building Block that this one supersedes. |
| `successor` | Identifier or URI of the Building Block that supersedes this one. |
| `dependsOn` | Array of Building Block identifiers this one has a runtime dependency on (distinct from `isProfileOf`). |
| `seeAlso` | Array of related Building Block identifiers or URIs. |
| `isProfileOf` | Identifier(s) of the Building Block(s) this one is a profile of — i.e. a stricter, backward-compatible specialisation. See [Imports](imports). |

### Schema and API artifacts

| Property | Description |
|---|---|
| `schema` | URL for the JSON Schema of this Building Block (auto-derived when a `schema.yaml/json` file is present). |
| `openAPIDocument` | URL or path to an OpenAPI document backing this Building Block. |
| `ldContext` | URL to the JSON-LD `@context` document. Auto-derived when `context.jsonld` is present. See [Semantic uplift](semantic-uplift). |
| `extends` | Declares schema inheritance. See [Extension points](extension-points). |
| `extensionPoints` | Declares specialisations of referenced Building Blocks. See [Extension points](extension-points). |

### Validation

| Property | Description |
|---|---|
| `shaclShapes` | Array of SHACL files (paths or URLs) to use for RDF validation. `shapes.ttl` in the building block directory is picked up automatically. |
| `shaclClosures` | Array of RDF files or URLs merged into every test snippet as a SHACL closure. Useful for small, static vocabularies that must be present for validation to pass. See [Validation](validation#shacl-validation). |
| `requirementClasses` | Array of requirement class URIs (from a ModSpec specification) that can be used to validate this Building Block. |
| `conformanceClasses` | Array of conformance class URIs (from a ModSpec specification) that this Building Block refers to. |

### Semantic / RDF

| Property | Description |
|---|---|
| `ontology` | Path or URL to an RDF document containing the ontology for this Building Block. `ontology.ttl` or `ontology.owl` are auto-detected. See [RDF-only Building Blocks](rdf-only#ontology). |
| `concept` | Array of URIs for the RDF concept(s) this Building Block represents (`skos:closeMatch`). See [RDF-only Building Blocks](rdf-only#semantic-annotations). |
| `rdfType` | Array of URIs for the RDF class(es) that instances of this Building Block conform to (`rdfs:subClassOf`). See [RDF-only Building Blocks](rdf-only#semantic-annotations). |

### External resources

| Property | Description |
|---|---|
| `resources` | Array of external artifacts (data files, specifications, vocabularies…) associated with this Building Block. See [External resources](resources). |


---

<!-- source: _pages/create/documentation.md -->

# Adding documentation

Human-readable documentation can be added inside a `description.md` Markdown file in the Building Block directory.

Relative links and images `some/relative/link.ext` can be included in this file, and they will be resolved to full URLs of the source (_sources/...) when the building block is processed. 

To reference another building block in the UI however we need a relative link to the building block - this can be done using a `bblocks://my.prefix.my.bb` URL scheme - this will work on deployed pages as well as in the local viewer to support testing these links.

# Assets
Any relative **http** URL included in the description of the building block and in the markdown content of the
examples will be converted into a full URL relative to the source location (i.e., that of `bblock.json`).-

Assets (e.g., images) can be placed in the `assets/` directory for later use in documentation pages,
by using references to `assets/filename.ext`.

For example, a `sample.png` image in that directory can be included in the description
Markdown code of a building block like this:

```markdown
![This is a sample image](assets/sample.png)
```

---

<!-- source: _pages/create/schema.md -->

# Defining a schema

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

    This means your building block will inherit all json-ld contexts and SHACL shapes from the referenced building block automatically and apply during [testing](../create/validation).


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


---

<!-- source: _pages/create/semantic-uplift.md -->

# Semantic uplift

The Building block design allows for "semantic annotation" through the use of a **context** document that
cross-references each schema element to a URI, using the JSON-LD syntax. The end result is still a valid JSON schema,
but may also be parsed as flexible RDF graphs if desired.

This provides multiple significant improvements over non-annotated schemas:

1. differentiates between the same and different meanings for common element names used in different places
2. can be used to link to a semantic model further describing each element
3. allows use of advanced, standardised validation of instance data
4. allows automated annotation of schemas themselves for tools able ot exploit additional information

The JSON schema for a building block is optionally linked to a conceptual model by using a root-level `x-jsonld-context`
property pointing to a JSON-LD context document (relative paths are ok). The Building Blocks Register can
then annotate every property inside the JSON schemas with their corresponding RDF predicate automatically.

Building Blocks defining JSON schemas can be annotated with JSON-LD contexts using either:

- including a file (`context.jsonld`) in the building block directory (this can be overriden with a file path or URL
  using the `ldContext` property in `bblock.json`)
- using the property `x-jsonld-context` in the _schema.(yaml/json) for the building block - e.g.
  `x-jsonld-context: ../../../sosa-ssn.jsonld`

The JSON LD context:

1. Maps JSON elements to URIs (which can be URIs of a richer semantic model)
2. Allows validation of complex logical constraints using SHACL Shapes to [validate examples](validation)
3. [Perform transforms](transforms) to any other RDF model and validate results

## Modularity support

JSON-LD contexts need to be aware of the underlying JSON schema - and in many applications schemas are compplex with  nested sub-schemas. Examples of this are metadata schemas such as STAC, but even the basic GeoJSON Feature model is surprisingly hard to model in a consistent fashion.

The Building Blocks design allows automatic combination of contexts based on the schema re-use patterns.  As schema complexity grows through re-use of standard components the benefits of the Building Blocks approach rapidly evolves from an efficiency into a critical enabler. 

_Its probable that the lack of JSON-LD support for existing metadata is due to this challenge.  This capability is not  only faster and better - but making semantic interoperability practically achievable for the first time._

## Context design

If contexts are being combined, then a number of possibilities emerge, but need careful design and testing.

One such possibility is the conversion of tokens into URIs depending on where these are encountered in a schemas. 

This can be achieved through several mechanisms. 

_TBD: document local contexts and use of @base mappings - and link to examples of different patterns_

## Additional semantic uplift steps

Sometimes, using JSON-LD is not enough to convert a JSON document into RDF, so additional steps may be required. This is
a common occurrence, for example, when defining JSON-LD contexts for already-existing or legacy JSON schemas, which are
hard or even impossible to adapt to better fit a given semantic data model.

Semantic uplift pre- and/or post-processing (i.e., before and/or after applying the building block's JSON-LD context)
can be defined in a `semantic-uplift.yaml` file in the building block directory, with the following format:

```yaml
additionalSteps:
  - type: jq                            # Type of transform
    code: |                             # Code for this transform
      .a = .b + 1
  - type: sparql-construct
    ref: semantic-uplift/constr.sparql  # A ref (from the bblock directory) can be used instead
```

### Types of semantic uplift steps

The following types are supported and will be automatically processed when uplifting examples and test resources:

* Pre-processing (on JSON document, before applying JSON-LD context)
  * `jq`: [JQ transform](https://jqlang.github.io/jq/manual/)
* Post-processing (on RDF graph, after applying JSON-LD context and parsing).
  * `shacl`: [SHACL AF](https://www.w3.org/TR/shacl-af/#rules) ruleset. The original graph plus the entailed triples
    (if any) will be returned.
  * `sparql-construct`: A [SPARQL CONSTRUCT](https://www.w3.org/TR/sparql11-query/#construct) query that will
    replace the graph obtained from the JSON-LD uplift.
  * `sparql-update`: A [SPARQL UPDATE](https://www.w3.org/TR/2013/REC-sparql11-update-20130321/) query that will
    be applied on the graph. The full resulting graph will be returned.

### Semantic uplift in run-time

If extra steps are required to map a schema to a model, then it becomes an implementation challenge to implement these steps. It is a work in progress to consider the reusability (FAIR) of transformations, and how these may be related to known profiles and allow software to automatically apply a small number of well-tested standard transformations.

---

<!-- source: _pages/create/examples.md -->

# Creating examples

Examples help developers understand how they can integrate the building block into their applications. Code snippets in specific programming languages, are not only supported, but encouraged.

Each example consists of Markdown `content` and/or a list of `snippets`. `snippets`, in turn,
have a `language` (for highlighting, language tabs in Slate, etc.) and the `code` itself.

`content` accepts text in Markdown format. Any relative links or images will be resolved to full
URLs when the building block is published (see [Assets](#assets)).

Instead of the `code`, a `ref` with a filename relative to `examples.yaml` can be provided:

```yaml
examples:
  - title: My inline example
    content: Example with its code in the examples.yaml file
    snippets:
      - language: json
        code: '{ "a": 1 }'
  - title: My referenced example
    content: Example with its code pulled from a file
    snippets:
      - language: json
        ref: example1.json # in the same directory as examples.yaml
```

A `json-path` expression can be combined with `ref` to extract a specific value from the referenced
file instead of using its full contents. Both JSON and YAML files are supported. The first match of
the expression is used as the snippet code. If the file cannot be parsed or the expression matches
nothing, the snippet is skipped with a warning.

```yaml
examples:
  - title: My extracted example
    content: Only the "features" array from a GeoJSON file
    snippets:
      - language: json
        ref: example1.json
        json-path: $.features
```

Please refer to
[the updated JSON schema for `examples.yaml`](https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/master/ogc/bblocks/schemas/examples.schema.yaml)
for more information.

The `examples.yaml` file in `my-building-block` can be used as a template.

## Prefixes

Optionally, you can add a `prefixes` entry at the top level (alongside `examples:`) or inside a specific example,
with a dictionary of prefix-to-URI mappings, allowing you to omit those prefixes when used in JSON, JSON-LD and
Turtle examples, but that will be used when semantically uplifting the snippets:

```yaml
prefixes:
  # Default prefixes for all examples
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
examples:
  - title: Example with prefixes
    prefixes:
      ex: http://example.com/
    snippets:
      - language: turtle
        code: |
          ex:a rdfs:label "A" .
```


---

<!-- source: _pages/create/validation.md -->

# Validation

Building Blocks have powerful automated testing capabilities using the built-in GitHub actions.

## Examples

Examples defined in the `examples.yaml` (inline or by file reference) get validated and included in generated documentation.
Examples in JSON and JSON-LD format will also be semantically uplifted to RDF and validated.

## Test resources

Test resources can be provided in two ways:

- **Auto-detected**: files placed in the `tests/` subdirectory of each building block are automatically picked up.
- **Explicit**: additional or external test resources can be listed in a `tests.yaml` file (see below).

The following validation types are supported out of the box:

- JSON schema
- RDF / [SHACL](https://www.w3.org/TR/shacl/), if SHACL shapes are defined (e.g., in the same directory as `bblock.json`).

### Validation pipeline

Each test resource goes through the following steps:

1. JSON schema validation (if a JSON schema is supplied)
2. JSON-LD uplift (if JSON and a context are supplied) — produces `{testcase}.jsonld` and `{testcase}.ttl`
3. SHACL validation (if SHACL shapes are defined)

Outputs are written to `/build/tests/`. A summary report is produced at `/build/tests/report.html`, linked from the generated building block index.

Transform outputs can also be validated against building block profiles using the same validators —
see [Transforms — Output profile validation](/create/transforms#output-profile-validation).

### File types

Inside the `tests` directory, 3 types of files will be processed:

- `*.ttl`: [Turtle](https://www.w3.org/TR/turtle/) RDF files validated against the SHACL shapes (see [SHACL Validation](#shacl-validation)).
- `*.jsonld`: JSON-LD files validated against the Building Block JSON Schema and then against the SHACL shapes.
- `*.json`: JSON files validated against the JSON Schema, then "semantically uplifted" by embedding the Building Block's `context.jsonld`, and finally validated against the SHACL shapes.

### Negative test cases

If the filename for a test resource ends in `-fail` (e.g., `missing-id-fail.json`), validation will only pass
if the test fails (JSON Schema, SHACL shapes, etc.); this allows writing negative test cases.
The equivalent for `tests.yaml` entries is the `require-fail: true` property.

### tests.yaml

`tests.yaml` is useful when test resources already exist at a known URL — for example, sample data published
alongside a specification. Referencing them by URL avoids duplicating files in the repository and ensures
tests always run against the canonical source.

`tests.yaml` is a list of entries, each with the following properties:

| Property | Required | Description |
| --- | --- | --- |
| `ref` | yes | URL or local filename (relative to `tests.yaml`) of the test resource |
| `require-fail` | no | If `true`, validation passes only when the test fails (negative test case). Default: `false` |
| `output-filename` | no | Filename to use for the uplifted output files; defaults to the filename from `ref` |

Example:

```yaml
- ref: https://example.org/samples/my-feature.json
- ref: https://example.org/samples/invalid-feature.json
  require-fail: true
- ref: local-extra-test.json
  output-filename: extra-test-output.json
```

See also the example `tests.yaml` file provided in the template.

## SHACL Validation

SHACL shapes can be defined in a `shapes.shacl` file or via the `shaclShapes` property in `bblock.json`:

```json
{
  "shaclShapes": [
    "vocabs-shacl.ttl"
  ],
  "shaclClosures": [
    "../../vocabularies/terms.ttl"
  ]
}
```

`shaclClosures` refers to additional files with RDF data required to perform validation - such as checking the types of related objects.

This is particularly useful for relatively small, static vocabularies (e.g. "codelists") that form part of the specification realised by the building block

## Tools

In addition to built-in testing capabilities the following online tools can be helpful in developing and debugging different layers of the design:

* [JSON Schema validator](https://www.jsonschemavalidator.net/){:target="_blank"}
* [JSON-LD Playground](https://json-ld.org/playground/){:target="_blank"}
* [SHACL Validator](https://shacl-play.sparna.fr/play/validate){:target="_blank"}

{% capture notice-json-schema-tip %}
**Tip:** To use the JSON Schema validator with a published schema, create a wrapper such as:

```json
{
  "$ref": "https://my.org/schema.json?cb=1"
}
```

The `?cb=1` parameter is a cache-busting trick: changing its value (e.g. `?cb=2`) makes the validator
treat the URL as new and fetch a fresh copy, bypassing any cached version. The parameter name and value
are arbitrary — they have no special meaning.
{% endcapture %}
<div class="notice--info">{{ notice-json-schema-tip | markdownify }}</div>

---

<!-- source: _pages/create/transforms.md -->

# Transforms

A building block is a specification — it defines a data model that data can conform to. Transforms complement that by
defining a **reusable conversion library**: for data that conforms to this building block, here is how to convert it
into another format, encoding, or building block representation. Clients and tools can discover these transforms from
the building block register and use them as ready-made adapters without having to implement the conversion logic
themselves.

Typical conversions include encoding translations (e.g. XML to JSON), schema or structural transformations, semantic
uplift to RDF, and vocabulary or terminology mappings.

Transforms are declared in a `transforms.yaml` file in the building block directory. During postprocessing, example
snippets that match a transform's declared input media types are automatically run through it — this demonstrates the
transform works and gives clients a concrete preview of the output. The transform library itself, however, is the
primary artifact; the snippet outputs are illustrative.

## transforms.yaml structure

```yaml
transforms:
  - id: my-transform           # required; alphanumeric and dashes only
    description: What it does  # optional; Markdown accepted
    type: jq                   # required; see supported types below
    inputs:
      mediaTypes:
        - application/json     # media types this transform accepts
    outputs:
      mediaTypes:
        - application/json     # media types this transform produces
    code: |                    # inline code/script
      .foo = "bar"
```

The transform code can be declared inline with `code`, or referenced from a separate file with `ref`:

```yaml
  - id: my-transform
    type: jq
    ref: transforms/my-script.jq
```

Input and output media types can be given as plain strings (`application/json`) or as objects when a file extension is
needed for the output:

```yaml
    outputs:
      mediaTypes:
        - mimeType: text/csv
          defaultExtension: csv
```

Common short-form aliases such as `json`, `xml`, or `turtle` are also accepted and will be normalized to their canonical
MIME types.

---

## Supported transform types

### jq

Applies a [jq](https://jqlang.org) expression to JSON input.

- **Default inputs:** `application/json`
- **Default outputs:** `application/json`

```yaml
  - id: add-type
    type: jq
    code: |
      .type = "ex:MyFeature"
```

---

### sparql-construct

Runs a SPARQL CONSTRUCT query on RDF input, producing an RDF graph.

- **Default inputs:** `application/ld+json`, `text/turtle`
- **Default outputs:** `text/turtle`

```yaml
  - id: to-geosparql
    type: sparql-construct
    ref: transforms/to-geosparql.sparql
```

---

### sparql-update

Runs a SPARQL UPDATE statement on an RDF graph in-place.

- **Default inputs:** `application/ld+json`, `text/turtle`
- **Default outputs:** same as input

```yaml
  - id: remap-predicates
    type: sparql-update
    ref: transforms/remap.sparql
```

---

### shacl-af-rule

Applies [SHACL Advanced Features](https://www.w3.org/TR/shacl-af/) rules (SPARQL-based) to an RDF graph.

- **Default inputs:** `application/ld+json`, `text/turtle`
- **Default outputs:** `text/turtle`

```yaml
  - id: infer-types
    type: shacl-af-rule
    ref: transforms/infer-types.shacl.ttl
```

---

### xslt

Applies an XSLT stylesheet to XML input.

- **Default inputs:** `application/xml`
- **Default outputs:** `application/xml`

```yaml
  - id: normalise-xml
    type: xslt
    ref: transforms/normalise.xslt
```

---

### json-ld-frame

Applies a [JSON-LD frame](https://www.w3.org/TR/json-ld11-framing/) to JSON-LD or RDF input.

- **Default inputs:** `application/ld+json`, `text/turtle`
- **Default outputs:** `application/ld+json`

```yaml
  - id: frame-feature
    type: json-ld-frame
    ref: transforms/frame.jsonld
```

---

### semantic-uplift

Applies a semantic uplift mapping (as used by the OGC NA tools) to JSON input, producing RDF.

- **Default inputs:** `application/json`
- **Default outputs:** `text/turtle`

```yaml
  - id: uplift
    type: semantic-uplift
    ref: transforms/uplift.yaml
```

---

### python

Runs a Python code snippet. The snippet receives `input_data` (a string) and must assign its result to `output_data`.
A `transform_metadata` namespace is also available with the following attributes:

| Attribute | Description |
|-----------|-------------|
| `source_mime_type` | MIME type of the input snippet |
| `target_mime_type` | MIME type of the declared output |
| `metadata` | Extra metadata from the transform declaration (keys starting with `_` excluded) |
| `context` | [Transform context](#transform-context) namespace |

```yaml
  - id: uppercase-keys
    type: python
    inputs:
      mediaTypes: [ application/json ]
    outputs:
      mediaTypes: [ application/json ]
    code: |
      import json
      data = json.loads(input_data)
      output_data = json.dumps({k.upper(): v for k, v in data.items()}, indent=2)
```

**With dependencies:**

```yaml
  - id: to-csv
    type: python
    inputs:
      mediaTypes: [ application/json ]
    outputs:
      mediaTypes:
        - mimeType: text/csv
          defaultExtension: csv
    metadata:
      dependencies:
        pip: pandas>=1.5
        python: ">=3.10"   # optional; skipped if not met
    code: |
      import json, pandas as pd
      data = json.loads(input_data)
      output_data = pd.DataFrame(data if isinstance(data, list) else [data]).to_csv(index=False)
```

`pip` accepts any specifier that `pip install` understands, including GitHub URLs. If `python` is set to
a [PEP 440](https://peps.python.org/pep-0440/) version specifier, the transform is silently skipped when the runtime
does not meet the requirement.

The snippet can be adapted into a standalone script by reading from stdin and printing to stdout — `input_data` is just
a string variable, and `output_data` is whatever string you assign.

---

### node

Runs a Node.js code snippet. The snippet receives `inputData` (a string) and must assign its result to `outputData`.
A `transformMetadata` object is also available with the following properties:

| Property | Description |
|----------|-------------|
| `sourceMimeType` | MIME type of the input snippet |
| `targetMimeType` | MIME type of the declared output |
| `metadata` | Extra metadata from the transform declaration (keys starting with `_` excluded) |
| `context` | [Transform context](#transform-context) object (snake_case keys) |

```yaml
  - id: add-metadata
    type: node
    inputs:
      mediaTypes: [ application/json ]
    outputs:
      mediaTypes: [ application/json ]
    code: |
      const data = JSON.parse(inputData);
      data.generatedBy = 'my-transform';
      outputData = JSON.stringify(data, null, 2);
```

**With dependencies:**

```yaml
  - id: to-csv
    type: node
    inputs:
      mediaTypes: [ application/json ]
    outputs:
      mediaTypes:
        - mimeType: text/csv
          defaultExtension: csv
    metadata:
      dependencies:
        npm: json2csv
        node: ">=18"   # optional; skipped if not met
    code: |
      const { Parser } = require('json2csv');
      const rows = Array.isArray(inputData) ? inputData : [JSON.parse(inputData)];
      outputData = new Parser().parse(rows);
```

`npm` accepts any package name or specifier that `npm install` understands. If `node` is set to a semver range, the
transform is silently skipped when the runtime does not meet the requirement.

---

## Output profile validation

A transform's outputs can be validated against one or more building blocks by declaring them as
profiles. During postprocessing, every output file produced by the transform is validated against
each declared profile using the same validators that run on regular test resources (JSON Schema,
JSON-LD context, and SHACL).

Profiles are declared under `outputs.profiles` as a list of building block identifiers, using the
`bblocks://` URI scheme:

```yaml
transforms:
  - id: to-geojson-feature
    type: jq
    inputs:
      mediaTypes: [ application/json ]
    outputs:
      mediaTypes: [ application/geo+json ]
      profiles:
        - bblocks://ogc.geo.features.feature
```

Both locally-defined building blocks and imported building blocks from other registers are supported.

### What gets produced

For each declared profile, postprocessing creates a subdirectory named after the profile identifier
alongside the transform outputs and writes:

- A `.validation_{passed|failed}.txt` text report for each output file
- Semantic uplift side-outputs (`.jsonld`, `.ttl`) when the profile includes a JSON-LD context
- A consolidated `_report.json` covering all validated outputs for that profile

The per-snippet transform result in `register.json` gains a `profilesValidation` map keyed by
profile identifier:

```json
"profilesValidation": {
  "ogc.geo.features.feature": {
    "result": true,
    "report": "build/tests/my.bblock/transforms/ogc.geo.features.feature/_report.json",
    "upliftedFiles": {
      "jsonld": "build/tests/my.bblock/transforms/ogc.geo.features.feature/output.jsonld",
      "ttl":    "build/tests/my.bblock/transforms/ogc.geo.features.feature/output.ttl"
    }
  }
}
```

---

## Transform context

All executable transform types (Python, Node, and plugins) receive a **transform context** with metadata about
the building block, example, and postprocessing run. In Python snippets it is `transform_metadata.context`
(a `SimpleNamespace`); in Node snippets it is `transformMetadata.context` (a plain object); in plugins it is
`metadata.ctx` (a `SimpleNamespace`). All fields use snake_case.

**Building block:**

| Field | Type | Description |
|-------|------|-------------|
| `bblock_id` | `str` | Building block identifier |
| `bblock_name` | `str` \| `None` | Human-readable name |
| `bblock_version` | `str` \| `None` | Version string |
| `bblock_tags` | `list` | Tags declared in `bblock.json` |
| `bblock_files_path` | `str` | Absolute path to the building block source directory |
| `bblock_annotated_path` | `str` | Absolute path to the annotated output directory |
| `bblock_metadata` | `dict` | Full building block metadata snapshot at transform time |

| `source_schema_path` | `str` \| `None` | Relative path to the source schema file, or URL if declared as a remote reference |
| `annotated_schema_path` | `str` \| `None` | Relative path to the annotated schema, if generated |
| `jsonld_context_path` | `str` \| `None` | Relative path to the generated JSON-LD context, if present |
| `shacl_shapes_paths` | `list` | Relative paths or URLs of SHACL shapes (local files are relativized to CWD; remote references are preserved as URLs) |

**Example and snippet:**

| Field | Type | Description |
|-------|------|-------------|
| `example_index` | `int` | Zero-based index of the current example |
| `example` | `dict` | Full example object (title, prefixes, base-output-filename, etc.) — `snippets` excluded |
| `snippet_index` | `int` | Zero-based index of the current snippet within the example |
| `snippet` | `dict` | Full snippet object (language, url, ref, json-path, prefixes, etc.) — `code` excluded (use `input_data`) |

**Output:**

| Field | Type | Description |
|-------|------|-------------|
| `output_file` | `str` | Absolute path where this transform's output will be written |
| `output_dir` | `str` | Absolute path to the transform output directory for this building block |
| `working_dir` | `str` | Working directory at postprocessing time |

**Register and configuration:**

| Field | Type | Description |
|-------|------|-------------|
| `base_url` | `str` \| `None` | Base URL for generated output |
| `github_base_url` | `str` \| `None` | GitHub repository base URL (e.g. `https://github.com/org/repo/`) |
| `git_repository` | `str` \| `None` | Git remote URL |
| `id_prefix` | `str` | Building block identifier prefix from `bblocks-config.yaml` |
| `imported_register_urls` | `list` | Register import URLs from `bblocks-config.yaml` |
| `transform_plugins` | `list` | Active transform plugins |

Note: `bblock_metadata` reflects the state at transform time — fields populated after the transforms step
(such as `shaclShapes` URLs and `documentation`) will not be present yet.

---

## Unknown transform types

Declaring a transform with a type not listed above is valid — it will be included in the building block
register for other tools or systems that support it, and skipped during postprocessing unless a matching
[transform plugin](#transform-plugins) is declared.

---

## Transform plugins

You can add support for custom transform types by declaring **transform plugins** in a
`transform-plugins.yml` file at the root of your building blocks repository:

```yaml
plugins:
  - pip: git+https://github.com/example/my-bblocks-plugin.git
    modules:
      - my_bblocks_plugin
```

Each plugin entry installs one or more pip packages and scans the listed Python modules for transformer
classes. A transformer class is recognised by duck typing — it needs:

- `transform_types`: a non-empty list of type name strings
- `transform(metadata)`: a callable that accepts a metadata object and returns a string or bytes, or raises an exception on failure

Each plugin runs in its own isolated virtualenv (created automatically under the postprocessing sandbox),
so dependency conflicts between plugins, or between a plugin and the postprocessor itself, are not a
concern.

`pip` accepts any specifier that `pip install` understands, including version constraints, GitHub URLs,
and local paths. It can be a string or a list when multiple packages are needed.

The postprocessor automatically derives a human-facing URL from the `pip` specifier (PyPI page for
package names, repository URL for `git+https://` references). You can override this with an explicit
`url` field:

```yaml
plugins:
  - pip: git+https://github.com/example/my-bblocks-plugin.git
    url: https://github.com/example/my-bblocks-plugin
    modules:
      - my_bblocks_plugin
```

Plugin metadata (types, class names, pip reference, and URL) is included in `register.json` under
`transformPlugins`, allowing viewers and tooling to attribute each transform type to its plugin.

### The `metadata` object

The `metadata` argument passed to `transform()` is a plain namespace with the following attributes:

| Attribute | Type | Description |
|-----------|------|-------------|
| `type` | `str` | The transform type identifier (e.g. `jinja2`) |
| `transform_content` | `str` | The code or script declared in `transforms.yaml` (`code` or `ref`) |
| `input_data` | `str` | The example snippet text |
| `source_mime_type` | `str` | MIME type of the input snippet |
| `target_mime_type` | `str` | MIME type of the declared output |
| `metadata` | `dict` | Extra metadata from the transform declaration (keys starting with `_` excluded) |
| `sandbox_dir` | `None` | Always `None` in the plugin subprocess context |
| `ctx` | `SimpleNamespace` | [Transform context](#transform-context) |

### Return value and error handling

Return a `str` or `bytes` to produce output. Return `None` to produce no output (not an error).
Raise any exception to signal failure — the exception message becomes the transform's stderr output.

### Transformer class attributes

| Attribute | Required | Description |
|-----------|----------|-------------|
| `transform_types` | yes | List of type name strings this class handles |
| `default_inputs` | no | Default input media types (used when `inputs` is not declared in `transforms.yaml`) |
| `default_outputs` | no | Default output media types (used when `outputs` is not declared in `transforms.yaml`) |

### Example plugin

The following skeleton shows the minimal structure. `metadata.transform_content` carries the
user-supplied code or script from `transforms.yaml`, so the transform logic is data-driven rather
than hard-coded in the plugin.

```python
# my_bblocks_plugin/__init__.py
import json

class MyTransformer:
    transform_types = ['my-type']
    default_inputs = ['application/json']
    default_outputs = ['text/plain']

    def transform(self, metadata):
        data = json.loads(metadata.input_data)
        # metadata.transform_content holds the code/expression from transforms.yaml
        # return a string or bytes, or raise on error
        return str(data)
```

A real-world example is the
[bblocks-jinja2-transform-plugin](https://github.com/ogcincubator/bblocks-jinja2-transform-plugin),
which adds a `jinja2` transform type that renders Jinja2 templates against JSON input.


---

<!-- source: _pages/create/rdf-only.md -->

# RDF-only Building Blocks

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

---

<!-- source: _pages/create/resources.md -->

# External resources

The `resources` property in `bblock.json` attaches external artifacts to a building block — files or URLs that don't fit into a dedicated property such as `schema`, `ontology`, or `ldContext`. Each entry declares its role, location, and media type.

## Structure

Each entry in the `resources` array has the following fields:

| Field | Required | Description |
|---|---|---|
| `role` | yes | The relationship of this resource to the building block. See [Well-known roles](#well-known-roles). |
| `ref` | yes | File path (relative to the building block directory) or URL. |
| `format` | yes | MIME type, e.g. `text/turtle`, `application/json`. |
| `title` | no | Human-readable label for this resource. |
| `conformsTo` | no | URI of a profile or specification that this resource conforms to. |

## Well-known roles

The `role` field accepts any URI, but the following short names are also recognised:

| Role | Description |
|---|---|
| `constraints` | Normative constraints on the building block |
| `data` | RDF or other data associated with the building block |
| `example` | Example data or usage |
| `guidance` | Non-normative guidance |
| `mapping` | A mapping or crosswalk to another model |
| `schema` | A schema artifact |
| `specification` | A normative specification document |
| `validation` | Validation rules or shapes |
| `vocabulary` | A vocabulary, ontology, or codelist |

## Auto-discovery of `data.ttl`

If a `data.ttl` file is present in the building block directory and no `resources` entry with `role: data` pointing to it already exists, it is automatically added as a `data` resource with `format: text/turtle`.

## Example

```json
{
  "resources": [
    {
      "role": "data",
      "ref": "data.ttl",
      "format": "text/turtle",
      "title": "Background ontology data"
    },
    {
      "role": "specification",
      "ref": "https://example.org/my-spec.html",
      "format": "text/html",
      "title": "Governing specification"
    },
    {
      "role": "vocabulary",
      "ref": "vocab.ttl",
      "format": "text/turtle",
      "conformsTo": "https://www.w3.org/TR/skos-reference/",
      "title": "Domain vocabulary"
    }
  ]
}
```


---

<!-- source: _pages/create/extension-points.md -->

# Extension points

<div class="notice notice--danger" markdown="1">
#### Experimental feature
This feature is highly experimental and may not work correctly in all instances. Proceed at your own risk.
</div>

Extension points allow you to **specialize existing building blocks** by constraining or customizing their 
referenced components. This mechanism enables developers to create tailored versions of standard building 
blocks while maintaining compatibility with the original specifications.

An extension point consists of:
- A **base building block** that you want to extend.
- A set of **mappings** from referenced building blocks in the base (or its imports) to your custom building blocks.

<div class="notice notice--warning" markdown="1">
#### OpenAPI building blocks
For building blocks backed by an OpenAPI document rather than a standalone JSON Schema, extension points
are **declarative only** — they are recorded in the register for clients to interpret, but no compiled
schema document is produced.
</div>


This approach ensures that any references in the base schema (or **recursively in its imports**) to a
given building block are further constrained to conform to your specialized version.

For example: if a base `FeatureCollection` building block references a `Feature` building block, and you
need a collection that only accepts your specialized `MyFeature` type, you declare an extension mapping
`Feature → MyFeature`. The postprocessor then produces a compiled schema for your extension in which
every reference to `Feature` in the base — including references buried inside imported building blocks —
is constrained to also satisfy `MyFeature`. Consumers can validate against that single compiled schema
without needing to understand the extension relationship at all.

Extension points also preserve semantic mappings in building blocks and (unless explicitly disabled) inherit
SHACL validation shapes from both the base building block and the targets for the extensions.

![Sample extension diagram](../../assets/extensions/sample-extension-diagram.png)

## Why Use Extension Points?

- **Customization**: Adapt standard building blocks to your domain-specific requirements.
- **Consistency**: Maintain compatibility with OGC standards while introducing specialized semantics.
- **Reusability**: Avoid duplicating entire schemas; only override what you need.
- **Convenience**: The postprocessor compiles a single, self-contained schema document — no need to
  chain multiple schemas together at validation time.

## How It Works

When you declare an extension point:
1. You specify a **base building block**.
2. You provide a set of **from → to mappings**:
   - **fromBuildingBlock**: A building block referenced by the base.
   - **toBuildingBlock**: Your specialized version of that building block.

Any schema references to `fromBuildingBlock` in the base (or its imported building blocks)
will be constrained to also satisfy the schema of `toBuildingBlock`.

### Example Scenario
- **Base**: `FeatureCollection`
- **Referenced Block**: `Feature`
- **Custom Mapping**: `Feature → MyFeature`

Result:
- You create a custom `MyFeatureCollection` that contains elements valid as both `Feature` and `MyFeature`.

## Declaration Format
Extension points are declared in the **`bblock.json`** file using the following structure:

```json
{
  "...": "...",
  "extensionPoints": {
    "baseBuildingBlock": "ogc.ogc-utils.prov",
    "extensions": {
      "ogc.ogc-utils.prov-entity": "ogc.sandbox.extensions.featureExt"
    }
  }
}
```

* `baseBuildingBlock`: The identifier of the building block you are extending.
* `extensions`: A key-value map where:
    * Key: Identifier of the referenced building block in the base.
    * Value: Identifier of your specialized building block.

The example above ensures that wherever `prov-entity` appears in the base or its imports, 
it will be constrained to also satisfy `featureExt`. The generated JSON-LD context for the extension
will also include any mappings coming from `featureExt`.
