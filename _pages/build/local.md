---
title: Quick Start - local build
permalink: /build/local
---

<div class="notice notice--info" markdown="1">
#### Windows setup

The commands on this page (and elsewhere in this "Quick Start" section) are written for a POSIX shell — `build.sh`,
`view.sh`, and the raw `docker run` commands below all assume bash-style syntax (e.g. `$(pwd)`). There is currently
no `.bat`/PowerShell equivalent, so on Windows you should run them from
[Git Bash](https://git-scm.com/downloads/win) (bundled with Git for Windows) or, for the smoothest experience,
[WSL](https://learn.microsoft.com/en-us/windows/wsl/install) with Docker Desktop's WSL 2 integration enabled.
</div>

## Quick how-to build locally

1. Install Docker.
2. Check out any valid Building Block implementation (e.g. [bblocks-examples](https://ogcincubator.github.io/bblocks-examples/)).
3. `cd` into the checked-out directory.
4. Run `build.sh` if present.
   - This runs the current build scripts and compiles the Building Blocks locally.
   - If not present, run the command directly (see [Postprocessing overview](../create/postprocessing) for more
     details and options):
   ```shell
   # Process building blocks
   docker run -it --pull=always --rm --workdir /workspace -v "$(pwd):/workspace" \
     ghcr.io/opengeospatial/bblocks-postprocess --clean true --base-url http://localhost:9090/register/
   ```
5. Run `view.sh` to preview the local build.
   - If not present, run:
   ```shell
   docker run --rm --pull=always -v "$(pwd):/register" -p 9090:9090 ghcr.io/ogcincubator/bblocks-viewer
   ```

You can now experiment with the source material, or proceed to [create your own building blocks](../create).

The output of the commands above is written to `build-local`, which is not tracked by git, so it will never
interfere with commits or Pull Requests.

If instead you want to update an existing register and submit your changes upstream, work on a
[fork of the repository](../build/contribution) rather than a plain local checkout. Forks have their own
concerns — most notably merge conflicts caused by the `build/` directory that the automated postprocessing
workflow commits on every push — covered in [Contributing updates to Building Blocks](../build/contribution).

## Postprocessing a subset of Building Blocks

Add `--filter {id}` to the Docker build command, where `{id}` is a Building Block identifier such as
`ogc.bbr.examples.feature.externalSchema`, to limit processing to a single Building Block.
