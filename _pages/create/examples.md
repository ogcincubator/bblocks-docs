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

## Targeting specific sub-schemas

Sometimes it is helpful to target a specific subschema with an example of just that part of a model.  This allows simplified views of a complex application schema to be collated in a single location.

This is achieved with the `schema-ref` key:

```
`- title: Targetting a subschema
    snippets:
      - language: json
        schema-ref: "#/$defs/Activity"
        ref: "myfile.json"
```

the schema-ref can be in the form:

- relative to bblock schema
- an absolute HTTP url
- a bblocks:// identifier
- relative the file structure (..\)

It is recommended to use `$defs` or `$anchor` in schemas to identify units that logically can be referenced externally, independent of the internal schema structure, which could be modified for various reasons in future versions.

Note this validation may be done against the individual building block - but this is not necessarily convenient if this is managed in a separate register.  

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
