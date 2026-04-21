---
title: Building Block metadata
permalink: /create/metadata
---
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
