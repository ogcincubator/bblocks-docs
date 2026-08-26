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
4. Plugin validation (if validator plugins are configured — see [Validator plugins](#validator-plugins))

Outputs are written to `/build/tests/`. A summary report is produced at `/build/tests/report.html`, linked from the generated building block index.

Transform outputs can also be validated against building block profiles using the same validators —
see [Transforms — Output profile validation](/create/transforms#output-profile-validation).

### File types

Inside the `tests` directory, any file is eligible for validation. Built-in validators filter by extension:

- `*.ttl`: [Turtle](https://www.w3.org/TR/turtle/) RDF files validated against the SHACL shapes (see [SHACL Validation](#shacl-validation)).
- `*.jsonld`: JSON-LD files validated against the Building Block JSON Schema and then against the SHACL shapes.
- `*.json`: JSON files validated against the JSON Schema, then "semantically uplifted" by embedding the Building Block's `context.jsonld`, and finally validated against the SHACL shapes.

Validator plugins can claim any additional file type by declaring the MIME types or extensions they handle.
Files not claimed by any validator are silently skipped.

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
| `media-type` | no | Explicit MIME type for this resource. Useful when the file extension does not map to a standard type, or when a validator plugin requires a specific type |

Example:

```yaml
- ref: https://example.org/samples/my-feature.json
- ref: https://example.org/samples/invalid-feature.json
  require-fail: true
- ref: local-extra-test.json
  output-filename: extra-test-output.json
- ref: assets/my-geometry.wkt
  media-type: text/wkt
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

### Closure graph inheritance

A building block's closure graph used for SHACL validation is not just its own `shaclClosures`. It is assembled
from the whole `dependsOn`/`isProfileOf` chain (the same chain `shaclShapes` are inherited across), and includes,
for every building block in that chain (including itself):

* its declared `shaclClosures`;
* its `ontology`, if it has one (see [Metadata](metadata) and [RDF-only Building Blocks](rdf-only));
* any `resources` entry with `role: data` whose `format` is an RDF serialization (Turtle, RDF/XML, JSON-LD,
  N-Triples, N3, TriG) — see [External resources](resources). A `role: data` resource in a non-RDF format
  (e.g. CSV, NetCDF) is not affected; it is not parseable RDF and stays a published artifact only.

So a building block that depends on (or profiles) another one declaring an ontology or an RDF `role: data`
resource automatically has access to that data when its own SHACL shapes are validated, without needing to
redeclare it as `shaclClosures`.

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

## Validator plugins

The built-in validators cover JSON Schema, JSON-LD context, and SHACL. For any other file type or
validation logic — ZIP integrity, WKT geometry, XSD schema validation, custom business rules — you can
add **validator plugins** declared in `bblocks-config.yaml`.

```yaml
plugins:
  validators:
    - pip: git+https://github.com/example/my-bblocks-validator-plugin.git
      modules:
        - my_bblocks_validator_plugin
```

Each plugin entry installs one or more pip packages and scans the listed Python modules for validator
classes. A validator class is recognised by duck typing — it needs:

- `mime_types` and/or `file_extensions`: a list of strings declaring which files this class handles
- `validate(self, meta)`: a callable that accepts a metadata object and returns a list of entries or `None`

Each plugin runs in its own isolated virtualenv (created automatically under the postprocessing sandbox
at `.bblocks-sandbox/plugins/`), so dependency conflicts between plugins or between a plugin and the
postprocessor itself are not a concern.

`pip` accepts any specifier that `pip install` understands, including version constraints, GitHub URLs,
and local paths. It can be a string or a list when multiple packages are needed.

### The `meta` object

The `meta` argument passed to `validate()` is a simple namespace with the following attributes:

| Attribute | Type | Description |
|-----------|------|-------------|
| `input_path` | `str` | Absolute path to the file to validate |
| `mime_type` | `str` \| `None` | MIME type of the file (from the file extension or `media-type` in `tests.yaml`) |
| `display_filename` | `str` | Original filename, for use in error messages |
| `schema_ref` | `str` \| `None` | Schema ref from the test entry, or `None` |
| `context` | namespace | Building block context (see below) |

**`meta.context` attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `bblock_id` | `str` | Building block identifier |
| `bblock_name` | `str` \| `None` | Human-readable building block name |
| `register_base_url` | `str` \| `None` | Base URL of the register |
| `validation_resources` | `list` | Resources with `role: validation` from `bblock.json` — each is a dict with `ref` (cwd-relative path or URL), `format`, and optionally `conformsTo` |
| `bblock_metadata` | `dict` \| `None` | Full building block metadata snapshot (from `bblock.json`) |

### Return value and error handling

Return a list of entry dicts to report findings:

```python
[
    {"message": "File is valid", "is_error": False},
    {"message": "Checksum mismatch", "is_error": True},
]
```

Return `None` or `[]` to signal "nothing to report" (not an error — the validator simply did not apply
or found nothing to flag).

Raise any exception to signal an unexpected failure — the full traceback is captured and reported as an
error in the validation output.

Each entry dict supports an optional `payload` key for structured metadata:

```python
{"message": "Invalid geometry on line 3", "is_error": True, "payload": {"line": 3}}
```

Any output written to `stdout` or `stderr` during `validate()` (e.g. `print()` calls) is captured and
logged at `DEBUG` level. To see it, run the postprocessor with `--log-level DEBUG`.

### File matching

Validators self-filter: the plugin framework calls `validate()` only for files whose extension or MIME
type appears in `mime_types` or `file_extensions`. Files not matched by any validator are silently skipped.

`file_extensions` entries may include or omit the leading dot (`.zip` and `zip` are both accepted).

When a test resource has a non-standard extension, declare its type explicitly in `tests.yaml`:

```yaml
- ref: assets/my-geometry.wkt
  media-type: text/wkt
```

### Validator class attributes

| Attribute | Required | Description |
|-----------|----------|-------------|
| `mime_types` | at least one of these | List of MIME type strings this class handles |
| `file_extensions` | at least one of these | List of file extension strings (`.zip`, `.wkt`, …) |

### Using validation resources (XSD example)

Validator plugins can access bblock-level validation resources — files or URLs declared with
`role: validation` in `bblock.json`. This is how a plugin can be driven by per-bblock configuration
rather than hard-coding schemas inside the plugin.

Declare the resource in `bblock.json`:

```json
{
  "resources": [
    {
      "role": "validation",
      "ref": "assets/schema.xsd",
      "format": "application/xml",
      "conformsTo": "https://www.w3.org/2001/XMLSchema"
    }
  ]
}
```

Then read it in the plugin via `meta.context.validation_resources`:

```python
class XsdValidator:
    mime_types = ['application/xml', 'text/xml', 'application/gml+xml']
    file_extensions = ['.xml', '.gml']

    def validate(self, meta):
        resources = getattr(meta.context, 'validation_resources', None) or []
        xsd_specs = [
            r for r in resources
            if r.get('conformsTo') in {
                'https://www.w3.org/2001/XMLSchema',
                'http://www.w3.org/2001/XMLSchema',
            }
        ]
        if not xsd_specs:
            return None  # no XSD declared — nothing to do

        from lxml import etree
        doc = etree.parse(meta.input_path)
        entries = []
        for spec in xsd_specs:
            xsd = etree.XMLSchema(etree.parse(spec['ref']))
            if xsd.validate(doc):
                entries.append({'message': f"Valid against {spec['ref']}", 'is_error': False})
            else:
                for error in xsd.error_log:
                    entries.append({'message': error.message, 'is_error': True,
                                    'payload': {'line': error.line}})
        return entries
```

### Example plugin

The following skeleton shows the minimal structure for a validator that checks ZIP file integrity:

```python
# my_bblocks_validator_plugin/__init__.py
import zipfile


class ZipValidator:
    mime_types = ['application/zip', 'application/x-zip-compressed']
    file_extensions = ['.zip']

    def validate(self, meta):
        try:
            with zipfile.ZipFile(meta.input_path) as zf:
                bad_file = zf.testzip()
        except zipfile.BadZipFile as exc:
            return [{'message': f'Invalid ZIP file: {exc}', 'is_error': True}]

        if bad_file is not None:
            return [{'message': f'ZIP archive is corrupt (first bad entry: {bad_file})',
                     'is_error': True}]

        return [{'message': f'ZIP archive is valid ({meta.display_filename})',
                 'is_error': False}]
```

A real-world example with multiple validators (ZIP, WKT geometry, and XSD) is
[bblocks-sample-validator-plugins](https://github.com/ogcincubator/bblocks-sample-validator-plugins).

### Reports

Validation entries produced by plugins appear in a **Plugin** section of the HTML and text reports.
Each entry is attributed to its source class (`module.ClassName`) so it is easy to trace which plugin
flagged a given file.