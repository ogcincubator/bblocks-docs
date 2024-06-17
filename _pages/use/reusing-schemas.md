---
title: Reusing schemas
permalink: /use/reusing-schemas
---

Building Blocks can be reused in several ways:

- if creating a JSON schema based BuildingBlock then use the $ref: bblocks://{block id} to make a JSON schema reference to any building block in the import list [see imports](/create/imports)
- for other [types of Building Blocks](/overview/types) declare as an entry in the dependsOn element of a `block.json` metadata file
- cut and paste "ready to use" forms from the `build/` directory of any building block repository into a some other form of application (not a reusable Building Block itself)
- directly reference the artefacts in the `build` directory using the URL pattern specified in the building block
  description (noting this may be affected by changes if a building block is moved from one register to another - bblocks:// references will still work if imports approach is used.)
