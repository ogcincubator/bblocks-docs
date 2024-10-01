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
3. SHACL validation (if SHACL rules defined)

A summary report is produced at `/build/tests/report.html`.

This is linked from the generated building block index.

## Test resources

The `tests` directory contains test resources that can be used for performing validation tasks. There are two
types of validations:

- JSON schema
- RDF / [SHACL](https://www.w3.org/TR/shacl/), if a top-level (i.e., same directory as `bblock.json`).

Inside the `tests` directory, 3 types of files will be processed:

- `*.ttl`: [Turtle](https://www.w3.org/TR/turtle/) RDF files that will be validated against the SHACL rules.
    - SHACL rules are loaded from the `shaclRules` property inside `bblock.json`. If a `rules.shacl` file is found
      in the Building Block directory it will be used by default. **SHACL files must be serialized as Turtle**.
- `*.jsonld`: JSON-LD files that will be first validated against the Building Block JSON Schema
  and then against the SHACL rules.
- `*.json`: JSON files that will be first validated against the JSON Schema, then "semantically uplifted"
  by embedding the Building Block's `context.jsonld`, and finally validated against the SHACL rules.

If the filename for a test resource ends in `-fail` (e.g., `missing-id-fail.json`), validation will only pass
if the test fails (JSON SCHEMA, SHACL shapes, etc.); this allows writing negative test cases.

[Examples](#examples) in JSON and JSON-LD format will also be uplifted and validated. 

## SHACL Validation

SHACL rules can be defined in a ```rules.shacl``` file or any other files or URLs in the `bblocks.json`:

```
 "shaclRules": [
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