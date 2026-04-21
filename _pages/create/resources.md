---
title: External resources
permalink: /create/resources
---

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
