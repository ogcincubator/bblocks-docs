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
[the updated JSON schema for `examples.yaml`](https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/master/ogc/bblocks/examples-schema.yaml)
for more information.

The `examples.yaml` file in `my-building-block` can be used as a template.