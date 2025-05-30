---
title: Quick Start - Tutorials
permalink: /build/local
---


## Quick how-to build locally

1. Install docker 
2. Check out any valid Building Block implementation (e.g. [bblocks-examples](https://ogcincubator.github.io/bblocks-examples/))
3. cd to the new directory
4. run `build.sh` or `build.bat` if present
   - this will access the current build scripts and compile the building block locally
   - if not present run the command 
 ```shell
# Process building blocks
docker run --pull=always --rm --workdir /workspace -v "$(pwd):/workspace" \
  ghcr.io/opengeospatial/bblocks-postprocess  --clean true --base-url http://localhost:9090/register/
```
5. run the view.sh or view.bat to preview the local build
 - if not present run 
 ```shell
docker run --rm --pull=always -v "$(pwd):/register" -p 9090:9090 ghcr.io/ogcincubator/bblocks-viewer
```
You can now experiment with the source material - or proceed to [create your own building blocks](../create).

(create a fork if you want to update the the repository so you can submit pull requests. The local build outputs will be ignored automatically on updates.)

## Postprocessing a subset of building blocks

Adding `--filter {id}` to the docker build command,  where {id} is a Building Block id such as `ogc.bbr.examples.feature.externalSchema` will limit processing to a single BBlock
