---
title: Adding documentation
permalink: /create/documentation
---

Human-readable documentation can be added inside a `description.md` Markdown file in the Building Block directory.

Relative links and images `some/relative/link.ext` can be included in this file, and they will be resolved to full URLs of the source (_sources/...) when the building block is processed. 

To reference another building block in the UI however we need a relative link to the building block - this can be done using a `bblocks://my.prefix.my.bb` URL scheme - this will work on deployed pages as well as in the local viewer to support testing these links.

# Assets
Any relative **http** URL included in the description of the building block and in the markdown content of the
examples will be converted into a full URL relative to the source location (i.e., that of `bblock.json`).-

Assets (e.g., images) can be placed in the `assets/` directory for later use in documentation pages,
by using references to `assets/filename.ext`.

For example, a `sample.png` image in that directory can be included in the description
Markdown code of a building block like this:

```markdown
![This is a sample image](assets/sample.png)
```