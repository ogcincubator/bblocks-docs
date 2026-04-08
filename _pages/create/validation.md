---
title: Validation
permalink: /create/validation
---

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