---
title: Postprocessing overview
permalink: /create/postprocessing
---

Building Blocks sources are post-processed using a workflow package maintained by the OGC. You may modify this if needed to perform additional actions - however this is subject to continual improvement as new types of building blocks are supported and improvements in available tools are made.



![OGC Building Blocks processing](https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/master/process.png)

### Output testing

The outputs can be generated locally by running the following:

```shell
# Process building blocks
docker run --pull=always --rm --workdir /workspace -v "$(pwd):/workspace" \
  ghcr.io/opengeospatial/bblocks-postprocess  --clean true --base-url http://localhost:9090/register/
```

**Notes**:

* Docker must be installed locally for the above commands to run
* The syntax for `-v "$(pwd):/workspace"` may vary depending on your operating system
* Output files will be created under `build-local` (not tracked by git by default)
* The value for `--base-url` will be used to generate the public URLs (schemas, documentation, etc.). In this case,
  we use the local `http://localhost:9090/register/` URL to make the output **compatible with the
  viewer** when running locally (see below). If omitted, the value will be autodetected from the repository
  metadata.

#### Building Blocks Viewer

You can also preview what the output will look like inside the Building Blocks Viewer application:

```shell
docker run --rm --pull=always -v "$(pwd):/register" -p 9090:9090 ghcr.io/ogcincubator/bblocks-viewer
```

**Notes**:

* Make sure to [compile the register](#output-testing) before running the viewer (or delete `build-local`
  altogether to view the current build inside `build`).  
* Docker must be installed locally for the above commands to run
* The syntax for `-v "$(pwd):/register"` may vary depending on your operating system
* `-p 9090:9090` will publish the Viewer on port 9090 on your machine