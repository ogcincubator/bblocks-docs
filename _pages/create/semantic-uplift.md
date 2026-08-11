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

JSON-LD contexts need to be aware of the underlying JSON schema - and in many applications schemas are complex with nested sub-schemas. Examples of this are metadata schemas such as STAC, but even the basic GeoJSON Feature model is surprisingly hard to model in a consistent fashion.

The Building Blocks design allows automatic combination of contexts based on the schema re-use patterns: a building
block that has no `context.jsonld` (or `x-jsonld-context`) of its own can still resolve to a full, valid semantic
context, assembled from whichever of its dependencies (`dependsOn` / `isProfileOf`, walked transitively) do define
one. Dependencies without a context of their own are simply skipped over — they still contribute their JSON Schema,
just not any semantic mappings.

The diagram below is a real "Context sources" graph, traced by the [viewer](https://ogcincubator.github.io/bblocks-viewer)
for the [`Custom Result for Observation Feature`](https://ogcincubator.github.io/bblocks-viewer/#/bblock/ogc.bbr.examples.observation.vectorObservationFeature?register=https://ogcincubator.github.io/bblocks-examples/build/register.json)
building block, which defines no JSON-LD context of its own:

![Context sources graph for the Custom Result for Observation Feature building block, showing its assembled context traced back through Observation Result, JSON-FG Feature/Feature Collection - Lenient, GeoPose Basic-YPR, JSON Link, JSON-FG time member, Feature, Feature Collection and GeoJSON](../../assets/context-composition/context-composition-diagram.svg)

Its dependency chain runs several levels deep — through an intermediate `Observation Result` block, then through
customized `JSON-FG Feature`/`Feature Collection - Lenient` blocks, down to `GeoPose Basic-YPR`, `JSON Link`,
`JSON-FG time member`, `Feature`, `Feature Collection` and `GeoJSON` — yet the block itself just declares
`dependsOn`/schema references; every one of those ancestors' JSON-LD mappings is picked up and merged automatically.

As schema complexity grows through re-use of standard components, this stops being a convenience and becomes a
critical enabler: authors of a mid-level or leaf building block don't need to redeclare mappings already defined
by the blocks they build on, and every consumer gets a single, coherent context regardless of how many blocks were
combined to produce the schema.

### How the context actually gets assembled

The composition isn't a merge of pre-built `context.jsonld` files — it's driven off the schema itself, using
[`ogc-na-tools`](https://github.com/opengeospatial/ogc-na-tools), as part of the register build. Every building
block's schema is first annotated in place with its JSON-LD mappings (as `x-jsonld-*` properties, following any
`context.jsonld` it defines), then a second pass walks the compiled schema tree — through every `$ref`,
`allOf`/`anyOf`/`oneOf` — from the root down, collecting whatever mappings it finds along the way into one flat
`@context`. That walk happens for every building block, whether or not it defines a context of its own: a block
with no mappings just contributes none, but the ones its dependencies defined are still picked up wherever they
sit in the tree.

So the "assembly" is really schema traversal, which is why the graph the viewer draws for a block's dependencies
doubles as the map of where its context's mappings came from. Curious readers can dig into the
`ogc-na-tools` source for the details.

### Overriding an inherited binding

A block can redeclare a term its schema inherits from a block it references, and have its own mapping win over the
inherited one. Say a base building block's `context.jsonld` maps `note` to a generic SKOS predicate:

```json
{ "@context": { "note": "http://www.w3.org/2004/02/skos/core#note" } }
```

A block whose schema composes the base one via `allOf`/`$ref` (which is what `extends` in `bblock.json` sets up
for you) can narrow that mapping for its own copy of `note` just by giving its *own* `context.jsonld` a mapping
for the same property name:

```json
{ "@context": { "note": "http://www.w3.org/2004/02/skos/core#definition" } }
```

This works because annotation and assembly are two separate passes. Each block's schema is annotated from its own
context only, in isolation — the base block ends up with `note` already annotated as `skos:note`, and the
referencing block ends up with its own `note` already annotated as `skos:definition`, independently of one
another. Assembly is what brings the two together: it walks the referencing block's compiled schema — its own
properties plus, through `allOf`/`$ref`, the base schema's — and for a property mapped on both sides, the mapping
found in the *later* branch wins. Since `extends` (and any other `bblocks://` reference) always places the base
schema's `$ref` before the referencing block's own properties, the referencing block's mapping is what survives.

Because the override is resolved by branch order rather than by anything marking it as intentional, redeclaring a
term is enough to override it — there's no separate opt-in, and no warning if you didn't mean to. Reusing a
property name from a base schema in your own `context.jsonld` for an unrelated reason (or copy-pasting a mapping
from a sibling block "just in case") will silently override the inherited binding the same way a deliberate
specialisation would. If a property's meaning looks wrong in the assembled context, check whether every schema in
the `allOf`/`$ref` chain that mentions that property name is mapping it on purpose.

The override applies per JSON-LD keyword, not to the whole binding at once: if the base context also gives `note`
an `@type` and the child's context doesn't redeclare one, the base's `@type` is still inherited alongside the
child's overridden `@id`. Only the keywords the child's context actually redeclares are replaced.

This is a deliberate, reliable mechanism — useful for [profiling](../overview/profiles) a parent building block to
specialise an inherited term without forking its schema. It's unrelated to [extension points](extension-points),
which substitute one *referenced block* for another rather than override a *term mapping*.

A working, minimal example lives in the
[`bblocks-examples`](https://github.com/ogcincubator/bblocks-examples/tree/master/_sources/semantic-uplift/override-binding)
register: [`Override Binding - Base`](https://ogcincubator.github.io/bblocks-viewer/#/bblock/ogc.bbr.examples.semantic-uplift.override-binding.base?register=https://ogcincubator.github.io/bblocks-examples/build/register.json)
binds `note`/`label` to `skos:note`/`skos:prefLabel`, and
[`Override Binding - Child (Profile)`](https://ogcincubator.github.io/bblocks-viewer/#/bblock/ogc.bbr.examples.semantic-uplift.override-binding.child?register=https://ogcincubator.github.io/bblocks-examples/build/register.json)
profiles it, redeclaring `note` (partial override — only `@id`) and `label` (full override — `@id` and `@type`).

### Why not just reuse a general-purpose vocabulary like schema.org?

A general-purpose vocabulary has to cover every domain at once, so it ends up large, loosely defined, and only
loosely typed against any particular schema — good for broad discovery, but weak for validation and precise
tooling. A context assembled from Building Blocks is the opposite: each mapping is scoped to the exact schema it
annotates, tested against real examples (via [semantic uplift](#additional-semantic-uplift-steps) and
[SHACL validation](validation)), and versioned alongside the schema it describes. The resulting contexts are
small and stable enough to be identified and cached per building block, rather than re-fetched wholesale — which
matters as much for tooling and AI agents consuming these schemas as it does for the infrastructure serving them.

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