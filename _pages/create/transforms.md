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

## Unknown transform types

Declaring a transform with a type not listed above is valid — it will be included in the building block register for
other tools or systems that support it, and simply skipped during postprocessing.
