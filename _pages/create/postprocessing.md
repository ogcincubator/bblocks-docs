---
title: Postprocessing overview
permalink: /create/postprocessing
---

Building Blocks sources are post-processed using a workflow package maintained by the OGC. You may modify this if needed to perform additional actions - however this is subject to continual improvement as new types of building blocks are supported and improvements in available tools are made.



[![OGC Building Blocks processing](https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/master/process.png)](https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/master/process.png)

### Output testing

The outputs can be generated locally by running the following:

```shell
# Process building blocks
docker run -it --pull=always --rm --workdir /workspace -v "$(pwd):/workspace" \
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
* By default the viewer shows only local building blocks. To also show imported ones, set
  [`viewer.show-imported-depth`](/create/structure#additional-register-metadata-properties) in `bblocks-config.yaml`.
* A register can add custom visualizations for examples/transform outputs via
  [view plugins](/create/view-plugins), or a whole new top-level bblock detail tab via
  [tab plugins](/create/tab-plugins).

### Using the development build

The postprocessor's `develop` branch and Docker image carry work that hasn't shipped in a stable
`v1.*.*` release yet. Register maintainers who want to try an upcoming feature — or who are asked
to help test one before it's released — can opt into it explicitly, per run or per workflow.

<div class="notice notice--warning" markdown="1">
`develop` is the absolute bleeding edge: unlike the release-tagged image (the untagged/`latest`/`v1`
image used by default), `@develop`/`:develop` is a moving pointer, not a fixed version — it can pick
up new, experimental, potentially breaking behavior on every run, with no compatibility guarantee
and no notice. Use it to test something specific, then switch back — don't leave a real register
pinned to it.
</div>

**Locally**, every register scaffolded from the template already has a `build-devel.sh` script
alongside `build.sh`/`view.sh` — run it instead of `build.sh` to build against the `develop` image:

```shell
./build-devel.sh
```

Any extra arguments are passed straight through to the postprocessor, so it composes with the usual
[flags](/create/postprocessing#output-testing) for finer-grained iteration, e.g.:

```shell
./build-devel.sh --filter ogc.my.namespace.myblock --steps annotate,jsonld,tests
```

**In CI**, point your `.github/workflows/process-bblocks.yml` caller at `@develop` instead of `@master`:

```yaml
jobs:
  validate-and-process:
    uses: opengeospatial/bblocks-postprocess/.github/workflows/validate-and-process.yml@develop
    secrets:
      sparql_username: ${{ secrets.sparql_username }}
      sparql_password: ${{ secrets.sparql_password }}
```

No other change is needed — on `develop`, `validate-and-process.yml` resolves against develop's own
postprocessing action and Docker image automatically. The same applies to a PR-check caller workflow
(`.github/workflows/pr-check.yml`, if your register has one): pin it at `@develop` the same way to
test upcoming PR-validation behavior too.

To pin an *exact* image instead of following `develop`'s moving tip — e.g. to reproduce a bug report
against the precise image it was seen on, including a specific past `v1.*.*` release — pass `image_tag`
to `validate-and-process.yml` (or `full`/`postprocess` directly) without changing which ref you're using:

```yaml
    with:
      image_tag: v1.0.20   # any tag actually pushed to ghcr.io/opengeospatial/bblocks-postprocess
```
