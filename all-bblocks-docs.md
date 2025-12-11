
# Filename: ./index.markdown
---
title: OGC Specification Building Blocks
permalink: /
---

<img src="assets/bblocks-qr.png" alt="QR Code" style="float:right; width: 200px; max-width: 33%"/>
This is the documentation for the OGC Building Blocks framework, a **specification component** packaging approach supporting:

- improved documentation of dependencies between specifications
- improved re-use of common elements across specifications
- validation of examples, test cases
- unit testing of validation
- semantic annotation
- validation of rules and constraints (using semantic annotations)
- testing of transformations and alignments to other specifications
- management of registers and Knowledge Graph views of ecosystems of specifications.

To provide suggestions for improvement on this documentation or ask questions please lodge issues [here](https://github.com/ogcincubator/bblocks-docs/issues) or submit pull requests.


## Overwhelmed?

<img src="assets/explorer_cave.png"  style="float:right; width: 200px; max-width: 33%"/>

It's natural to be overwhelmed by a new framework that addresses many complex aspects of a problem, in a new way. Powerful machines are scary.

However the Building Blocks can be explored incrementally, based on your starting knowledge and problems you wish to solve.

Explore these example [Use Cases](/usecases/usecases) or go straight to the [Tutorials](https://ogcincubator.github.io/bblocks-tutorial/) - which break these capabilities down step by step.

Building Blocks give you the tools to explore new territory, and improve your understanding and re-use of standards when solving your own problems.

<img src="assets/explorer_kit.png"  style="float:right; width: 200px; max-width: 33%"/>

## Overview 

Building Blocks  support the **FAIR principles** for **specifications** - with every specification being a component that can be
re-used. For more discussion see [Design Principles](overview/principles)

Building Blocks can be used to **add documentation** to existing specification components, or to **design** and 
**assemble** reusable specification components cost-effectively using a test-driven approach. 

Building Blocks are *technology-agnostic* - i.e. may be various [types](overview/types) - however an emphasis is
support for JSON schemas for use in OGC API definitions, with semantic annotation using JSON-LD.

Building Blocks can be organised into [registers](overview/registers) for convenience, each repository creating a local
register that can be integrated with other application domain registers.

Published OGC API specifications are, or will be, described in
the [register of OGC Specification Building blocks](https://opengeospatial.github.io/bblocks/register/). The framework
can be used for development of specifications or publication of specifications in your own application domain. The
framework supports transparent **federation of Building Block registers.**

The framework supports testing of examples, and validation using rules inherited from other Building Blocks that are
re-used (by aggregation or profiling) to create compatible specifications for specific applications.

For more details consider using the [Tutorials](https://ogcincubator.github.io/bblocks-tutorial/) - a step-wise introduction to various features and configuration details for Building Blocks.


# Filename: ./build/contribution.md
---
title: Build - Contributing
permalink: /build/contribution
---

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
[create-clean-pr.sh](https://gist.githubusercontent.com/avillar/acb3e22d36ddf1ddbf8ff5c1aa64616f/raw/a0046485a48bc1ced94b8d2c6605d32df0f3c3eb/create-clean-pr.sh)

The script is run locally on the directory of the forked register, and it requires that the upstream repository
(i.e., the original Building Blocks register) is
[added as a remote](https://docs.github.com/en/get-started/git-basics/about-remote-repositories#creating-remote-repositories).
By default, the `fork-parent` remote name will be used, but it can be configured to something different (e.g., `upstream`).

The script will create a new branch with a random name, clean any changes done to the `build/` directory and anything in it, 
push the branch to your fork of the register, and provide you with a URL to create the Pull Request directly.

It relies on the [`git-filter-repo`](https://github.com/newren/git-filter-repo) Python script, so you must have a working
Python environment for it to work. If `git-filter-repo` is already installed on your system, the script will use it,
and otherwise will download a copy to a temporary directory (which will be deleted once it is done).
# Filename: ./build/github.md
---
title: Quick Start - Github Automation
permalink: /build/github
---

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
# Filename: ./build/local.md
---
title: Quick Start - Tutorials
permalink: /build/local
---


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

# Filename: ./build/tutorial.md
---
title: Quick Start - local build
permalink: /build/tutorial
---


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
# Filename: ./create/documentation.md
---
title: Adding documentation
permalink: /create/documentation
---

Human-readable documentation can be added inside a `description.md` Markdown file in the Building Block directory.
Relative links and images can be included in this file, and they will be resolved to full URLs when the building 
block is processed. 

# Assets
Any relative URL included in the description of the building block and in the markdown content of the
examples will be converted into a full URL relative to the source location (i.e., that of `bblock.json`).-

Assets (e.g., images) can be placed in the `assets/` directory for later use in documentation pages,
by using references to `assets/filename.ext`.

For example, a `sample.png` image in that directory can be included in the description
Markdown code of a building block like this:

```markdown
![This is a sample image](assets/sample.png)
```
# Filename: ./create/examples.md
---
title: Creating examples
permalink: /create/examples
---

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

# Filename: ./create/imports.md
---
title: Setting up imports
permalink: /create/imports
---
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

# Filename: ./create/index.md
---
title: How to create Building Blocks
permalink: /create
---
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
# Filename: ./create/metadata.md
---
title: Building Block metadata
permalink: /create/metadata
---
Building block metadata provides context information about the item in the building blocks register. It is based on [ISO 19135](https://www.iso.org/standard/54721.html), the standard for item registration of geographic information, from which it extracted its six mandatory items (flagged with *). The ISO schema is extended with other properties (in green), which account for things such as the visual representation in the register, item validation or relation with other building blocks.

[![building block](../assets/bblock.png)](../assets/bblock.png)

# Filename: ./create/postprocessing.md
---
title: Postprocessing overview
permalink: /create/postprocessing
---

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
# Filename: ./create/rdf-only.md
---
title: RDF-only Building Blocks
permalink: /create/rdf-only
---
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

# Filename: ./create/schema.md
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

# Filename: ./create/semantic-uplift.md
---
title: Semantic uplift
permalink: /create/semantic-uplift
redirect_from:
  - /create/json-ld-context
---

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

JSON-LD contexts are very complex and hard to debug if the schema is at all complex.

The Building Blocks design allows automatic combination of contexts based on the schema re-use patterns.

## Context design

_TBD: document local contexts and use of @base mappings. _

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

# Filename: ./create/structure.md
---
title: Building Block structure
permalink: /create/structure
---

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
# Filename: ./create/transforms.md
---
title: Transforms
permalink: /create/transforms
---

Transformations may be required for several reasons:

1. To test the ability of a building block to model information from a particular source (that does not conform to the building block specification).

Accordingly, different types of transformations may be required:

1. Encoding translations (e.g. XML -> JSON)
2. Schema transformations
3. Semantic transformations (entailments, equivalent terms)
4. Content transformations (terminology)

**Note that the Building Blocks viewer application is still being developed to show all types of transformation in appropriate places.**

## Transformation tools

Building Blocks are technology agnostic, however rich support exists for JSON Schema and JSON-LD/RDF:

- SHACL (AF- advances features) SPARQL rules are powerful for schema, semantic and content transformation rules.
- JQ may be used for pure JSON transformations

Custom code may be used for transformation and validation. (details TBD) 

## Examples

A key example is the mismatch between the GeoJSON geometry model and the GeoSPARQL geometry model. This
requires the transformation of both structure and vocabulary to convert GeoJSON to valid GeoSPARQL - see this [example](https://ogcincubator.github.io/bblocks-examples/bblock/ogc.bbr.examples.feature.geosparqlFeature)

The transformation specification is here:

https://github.com/ogcincubator/bblocks-examples/blob/master/_sources/feature/geosparqlFeature/bblock.json#L17

## Technical Documentation

TBD
# Filename: ./create/validation.md
---
title: Validation
permalink: /create/validation
---

Building Blocks have powerful automated testing capabilities using the built-in GitHub actions.

These can be supplemented with additional custom validation and transformation processes as required.

## Examples

Examples defined in the `examples.yaml` (inline or by file reference) get validated and included in generated documentation.

Test cases defines in the `tests/` subdirectory of each building block get validated. Additional or external tests
can be added in `tests.yaml` as a list of objects with a `ref` property pointing to the test resource's location,
and optionally defining the `output-filename` and/or `require-fail` properties (for more information, see the 
example `tests.yaml` file provided in the template and 
[the JSON Schema for `tests.yaml`](https://github.com/opengeospatial/bblocks-postprocess/blob/master/ogc/bblocks/schemas/tests.schema.yaml){:target="_blank"}.

In each case, the `/build/tests/` directory contains a set of validation outputs.

Validation includes the following steps:

1. JSON schema validation (if JSON schema supplied)
2. JSON-LD uplift (if JSON and context supplied) ( `{testcase}.jsonld` and `{testcase}.ttl` generated)
3. SHACL validation (if SHACL shapes defined)

A summary report is produced at `/build/tests/report.html`.

This is linked from the generated building block index.

## Test resources

The `tests` directory contains test resources that can be used for performing validation tasks. There are two
types of validations:

- JSON schema
- RDF / [SHACL](https://www.w3.org/TR/shacl/), if a top-level (i.e., same directory as `bblock.json`).

Inside the `tests` directory, 3 types of files will be processed:

- `*.ttl`: [Turtle](https://www.w3.org/TR/turtle/) RDF files that will be validated against the SHACL shapes.
    - SHACL shapes are loaded from the `shaclShapes` property inside `bblock.json`. If a `shapes.shacl` file is found
      in the Building Block directory it will be used by default. **SHACL files must be serialized as Turtle**.
- `*.jsonld`: JSON-LD files that will be first validated against the Building Block JSON Schema
  and then against the SHACL shapes.
- `*.json`: JSON files that will be first validated against the JSON Schema, then "semantically uplifted"
  by embedding the Building Block's `context.jsonld`, and finally validated against the SHACL shapes.

If the filename for a test resource ends in `-fail` (e.g., `missing-id-fail.json`), validation will only pass
if the test fails (JSON SCHEMA, SHACL shapes, etc.); this allows writing negative test cases.

[Examples](#examples) in JSON and JSON-LD format will also be uplifted and validated. 

## SHACL Validation

SHACL shapes can be defined in a ```shapes.shacl``` file or any other files or URLs in the `bblocks.json`:

```
 "shaclShapes": [
    "vocabs-shacl.ttl"
  ]
  "shaclClosures": [
    "../../vocabularies/terms.ttl",
```

`shaclClosures` refers to additional files with RDF data required to perform validation - such as checking the types of related objects.

this is particularly useful for relatively small, static vocabularies (e.g. "codelists") that form part of the specification realised by the building block

## Tools

In addition to built-in testing capabilities the following online tools can be helpful in developing and debugging different layers of the design:

* [JSON Schema validator](https://www.jsonschemavalidator.net/){:target="_blank"}
* [JSON-LD Playground](https://json-ld.org/playground/){:target="_blank"}
* [SHACL Validator](https://shacl-play.sparna.fr/play/validate){:target="_blank"}

Hint - to use the JSON Schema validator with a published schema you can create a wrapper such as 

```json
{
  "$ref": "https://my.org/schema.json?version"
}
```

(updating `version` forces the validator to pick up any changes in the published schema.)
# Filename: ./overview/openscience.md
# The Role of OGC Building Blocks in Advancing Open Science

(work in progress - do not link)

## Overview

Science requires reproducability.

This requires detailed documentation of many aspects of the methodology and execution, as well as the inputs and results. Such documentation becomes extremely complex to create and interpret - but this is greatly facilitated by standardised structures and contents. Open Science increasingly aims for machine-readability (as far as possible) of these descriptions to support validation and reuse of the underlying science through repeatable **workflows**.

Scientific workflows are increasingly complex, encompassing not only data but also APIs, metadata structures, vocabularies, and methodological descriptions. Reusability, transparency, and interoperability across these components are essential for ensuring research processes align with the FAIR (Findable, Accessible, Interoperable, Reusable) principles. The OGC Building Blocks methodology offers a structured, component-based approach to standardization, validation, and discovery that directly supports these goals. This white paper explores its strategic relevance for open science.

## 1. The Challenge of Specification Fragmentation

Many interoperability specifications—especially those used in the geospatial and environmental sciences—include rich and varied components such as schemas, ontologies, and APIs. However, these components are often embedded in natural language documents, obscuring machine-readable relationships and dependencies. This lack of transparency hinders reuse and makes validation difficult.

For example, during the Nov 2024 Metadata CodeSprint ([citesprint2024]), challenges were observed in reconciling metadata standards like ISO 19115, DCAT, STAC, and GeoDCAT. Without a modular structure, aligning or profiling such standards across different domains requires manual interpretation and ad hoc tooling.

## 2. Building Blocks: A Methodology for Specification Modularity

The OGC Building Block methodology provides a systematic approach for:

- Packaging atomic components of specifications (schemas, requirements, examples, tests, transformations).
- Documenting relationships between components, including inheritance, profiling, or conformance constraints.
- Validating and testing examples and implementations in a CI/CT environment.
- Publishing metadata-rich representations of these components as Linked Data in a Knowledge Graph.

This approach supports the use of mapping scripts and profiling files, as illustrated in prior work on JSON-LD context file splitting and namespace separation ([jsonldsplit]).

## 3. Enabling Interoperability in Scientific Workflows

Scientific workflows commonly involve combinations of metadata standards, data exchange formats, and processing algorithms. The Building Block methodology enhances these workflows in several key ways:

- **Profiling and Composition**: Researchers can construct domain-specific profiles by assembling relevant building blocks from multiple standards.
- **Mapping and Transformation**: Explicit mappings (e.g., GeoDCAT to ISO 19115) can be authored, registered, and validated as first-class artefacts.
- **Lifecycle Integration**: Tools and datasets can reference specific building blocks, embedding interoperability validation directly into the workflow lifecycle.

This was evident in the application of profile-based JSON schema generation and modular schema production by namespace ([schemasplit]).

## 4. Supporting FAIR and Reproducible Science

The Building Block methodology aligns with and supports the FAIR principles:

- **Findability**: Building blocks are published in a standardized form with metadata suitable for indexing in registries and knowledge graphs.
- **Accessibility**: Blocks are retrievable as standalone artefacts, with versioning and licensing clearly documented.
- **Interoperability**: Semantic mappings, conformance relationships, and transformation tools can be directly expressed and tested.
- **Reusability**: Blocks can be referenced, composed, and refined without duplicating entire specifications.


Tools developed for dynamic JSON schema generation and mapping-based validation workflows ([schemagen]), as well as integration with provenance frameworks ([iaprovenance]), demonstrate practical implementation of these goals.



## 5. Strategic Recommendations

To promote open science through better standards infrastructure, the following actions are recommended:

- Adopt building block principles when designing scientific data standards and workflows.
- Encourage standards bodies to modularize specifications using the OGC Building Blocks model.
- Develop tooling to register and discover building blocks, enabling automated integration into scientific platforms.
- Engage research communities in the validation and curation of reusable components.

## Conclusion

The OGC Building Block methodology offers a practical, future-proof path to composable, transparent, and validated specifications. Its application in the scientific domain can significantly lower the cost of interoperability, increase reuse of data and services, and help ensure that science is not only open—but also robustly machine-actionable.

## References


# Filename: ./overview/principles.md
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












# Filename: ./overview/profiles.md
---
title: Profiles
permalink: /overview/profiles
---

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









# Filename: ./overview/qr.md
---
title: QR code for OGC Specification Building Blocks
permalink: /overview/qr
---
Find documents online at https://ogcincubator.github.io/bblocks-docs/

![](../assets/bblocks-qr.png)


# Filename: ./overview/registers.md
---
title: Building Block Registers
permalink: /overview/registers
---

OGC BuildingBlocks are published as registers (collections), with each repository defining a sub-register that can be aggregated.

Aggregated registers will all have their own governance regimes, which SHOULD be clearly defined as documentation describing scope and rules for inclusion.

Key examples include:

- [OGC Specification Building Blocks](https://opengeospatial.github.io/bblocks/register/) - Building Blocks defined by OGC specifications. (_may include common utility patterns common to multiple specifications_)
- [OGC Incubator Building Blocks](https://ogcincubator.github.io/bblocks/) - Building Blocks needed by multiple application domains. (_not yet formally transferred to an appropriate SWG_)
- [Examples](https://ogcincubator.github.io/bblocks-examples/) - Examples of different types and usage patterns. (_these are NOT intended as reuse except in examples and tutorials_)
- [Tutorial](https://ogcincubator.github.io/bblocks-tutorial/) - a step-wise introduction to various features and configuration details for Building Blocks.

![OGC Building Block Register Ecosystem](https://lucid.app/publicSegments/view/9d075f82-8611-4f32-83eb-994143669cc8/image.png)
# Filename: ./overview/types.md
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



# Filename: ./overview/whatis.md
---
title: What is a Building Block?
permalink: /overview/whatis
---
An Building Block is a way of packaging a component of a **specification** that can be re-used in other specifications.

This packaging directly supports **reuse** (according to FAIR principles), following these [Design Principles](overview/principles).

For various reasons specifications have often made statements in text regarding how they relate to other specifications, and created implementation artefacts such as schemas that may not make these intentions explicit. OGC Building Blocks support **technology agnostic dependency and rtelationshops** - essentially forming the data management method for this apsect of OGC's knowledge graph (OGC RAINBOW).

The key focus is on automated quality control, via inheritable testing on a simple aspect-by-aspect basis for standards as they are composed from common specification elements into comprehensive specifications to support data exchange and analysis applications/  

The following diagram shows how Building Blocks form a value-added packaging option for such specification elements that can then be exploited as part of a comprehensive knowledge base to support discovery and re-use (FAIR principles).

![Overview](https://lucid.app/publicSegments/view/266abfd3-ed51-43a8-a9b0-8e3251c28b54/image.png)

Many OGC Standards contain reusable building blocks that can be used in other OGC Standards. The Standards themselves can also be structured with modular sets of requirements that collectively function as a reusable building block (see image bellow).

[![Usage](/assets/api-bblocks.png)](/assets/api-bblocks.png)

To facilitate the discovery of these building blocks by other Standards and applications, once they are identified their definition should be published in the [OGC Register](https://opengeospatial.github.io/bblocks/register/). Normative information about the OGC Standards building blocks can be found in the [Technical Committee Policies and Procedures](https://docs.ogc.org/pol/05-020r29/05-020r29.html#building-bloocks) 
# Filename: ./usecases/ogc_building_block_use_cases.md

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
  - Schemas or other validatable descriptions (such as SHACL shapes) are available to match the standard requirements  
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
The OGC API - Features standard is extended with additional examples, demonstrations of RDF mappings to semantic models to document feature types, SHACL shapes, symbology rules, controlled vocabulary usage in particular circumstances and code to handle these patterns — all linked via the Building Block registry but published independently of the core document. 

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

# Filename: ./usecases/stac_extension.md
---
title: STAC extensions
permalink: /usecases/stac_extension
---

## Creating or updating a STAC extension

_(This is a work in progress and we explore even better ways to support STAC and Records extensions)_

STAC extensions are defined in a repository and provide a number of elements - they are in fact a "STAC Building Block" in that they can be combined with each other. ("Building" is the fundamental concept here!)

One problem is that extensions may have inconsistent schemas, reuse of schema elements and duplication. 

Using the OGC Building Blocks approach to define or annotate a STAC extension provides an additional layer of support for:

- validating examples work with other STAC schemas
- documenting the relationships between STAC schemas
- integration of STAC schemas and or conceptual model into other metadata models
- integration of other building blocks into STAC schemas

### Dependency modelling and reduction of duplication

Refactoring STAC schemas to reuse (rather than copy) sub-schemas for specific patterns makes it clear the common semantics and intended interoperability of these sub-schemas.

For example, this could have avoided the triplication of "raster" models from EO, raster and core 1.1 schemas that now makes extensions like STAC-MLM very verbose and complex.

### Documentation management

By linking a STAC sub-schema building block to an ontology (description of all the elements) using JSON-LD "semantic uplift" documentation can be generated automatically, and kept up to date.  This semantic documentation can be combined with other stac extensions to create rich documentation of how a community profile uses multiple STAC extensions.


# Filename: ./usecases/usecases.md
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

# Filename: ./use/finding.md
---
title: Finding Building Blocks
permalink: /use/finding
---


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
# Filename: ./use/ftc.md
---
title: Feature Type Catalogs
permalink: /use/ftc
---

Building Blocks solve a key limitation of traditional specifications using mixtures of documentation styles and locations - by normalising the documentation for a wide range of specification types it allows for increased **Access** in practice - since all the reusable components can be reliably found via the underlying Linked Data and Register models.

The concept of a "Feature Type Catalog" (FTC) has been widely accepted as a concept, however interoperable implementations have been slow to emerge.

This may be because FTCs in practice need to be technically aligned with the underlying infrastructure publishing Features as data, and this in turn has two distinct aspects: persistence (how features are stored) and transfer (how they are exposed). Both of these aspects tend to be technology dependent, and hence expression of Feature Types is often tied to one or other of such aspects.

Building Blocks provide a new opportunity to publish Feature Types in a technology agnostic way, using multiple schemas mapped to common semantic models, supported by examples and validation.

Effectively this means the design pattern of a schema mapped to a Class with a Frame (a set of properties). Building Blocks can handle abstract or conceptual models, or technology specific physical implementation schemas, and crucially and uniquely the **relationships between concepts and implementation options**.

# Filename: ./use/linked-data.md
---
title: Linked Data / JSON-LD Context
permalink: /use/linked-data
---

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


# Filename: ./use/reusing-schemas.md
---
title: Reusing schemas
permalink: /use/reusing-schemas
---

Building Blocks can be reused in several ways:

- if creating a JSON schema based BuildingBlock then use the $ref: bblocks://{block id} to make a JSON schema reference to any building block in the import list [see imports](../create/imports)
- for other [types of Building Blocks](../overview/types) declare as an entry in the dependsOn element of a `block.json` metadata file
- cut and paste "ready to use" forms from the `build/` directory of any building block repository into a some other form of application (not a reusable Building Block itself)
- directly reference the artefacts in the `build` directory using the URL pattern specified in the building block
  description (noting this may be affected by changes if a building block is moved from one register to another - bblocks:// references will still work if imports approach is used.)
