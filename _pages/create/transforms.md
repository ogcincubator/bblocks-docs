---
title: Transforms
permalink: /create/transforms
---

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
| `bblock_name` | `str \| None` | Human-readable name |
| `bblock_version` | `str \| None` | Version string |
| `bblock_tags` | `list` | Tags declared in `bblock.json` |
| `bblock_files_path` | `str` | Absolute path to the building block source directory |
| `bblock_annotated_path` | `str` | Absolute path to the annotated output directory |
| `bblock_metadata` | `dict` | Full building block metadata snapshot at transform time |

| `source_schema_path` | `str \| None` | Relative path to the source schema file, or URL if declared as a remote reference |
| `annotated_schema_path` | `str \| None` | Relative path to the annotated schema, if generated |
| `jsonld_context_path` | `str \| None` | Relative path to the generated JSON-LD context, if present |
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
| `base_url` | `str \| None` | Base URL for generated output |
| `github_base_url` | `str \| None` | GitHub repository base URL (e.g. `https://github.com/org/repo/`) |
| `git_repository` | `str \| None` | Git remote URL |
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
