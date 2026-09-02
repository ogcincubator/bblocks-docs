---
title: Setting up imports
permalink: /create/imports
---
Any building blocks repository can import any other repository, so that references by id to building blocks
(e.g. inside schemas, in `bblock.json`, etc.) belonging to the imported repositories can be automatically resolved.

Repository imports can be defined as an array of URLs to the output `register.json` of other repositories inside
`bblocks-config.yaml`:

* If `imports` is missing from `bblocks-config.yaml`, the
  [main OGC Building Blocks repository](http://blocks.ogc.org/register.html) will be imported by default.
* `default` can be used instead of a URL to refer to the
  [main OGC Building Blocks repository](http://blocks.ogc.org/register.html). 
* If `imports` is an empty array, no repositories will be imported.

For example, the following will import two repositories, one of them being the main OGC Building Blocks repository:

```yaml
name: Repository with imports
imports:
  - default
  - https://example.com/bbr/build/register.json
```

*Note*: If the URL ends with `build/register.json` or `register.json`, you may omit the last part. For example,
when `https://example.com/bbr` is provided as an import, these URLs will be tried:

  * `https://example.com/bbr` 
  * `https://example.com/bbr/build/register.json`
  * `https://example.com/bbr/register.json`

The first URL to return a valid `register.json` will be used. 

## Import aliases

Instead of a full `register.json` URL, an import can also be written as an `@org/register` alias,
resolved against a Building Blocks meta-registry:

```yaml
imports:
  - "@ogc/main"        # equivalent to "default"
  - "@acme/my-bblocks"
```

This avoids hardcoding raw URLs, which can break if a repository moves host or is renamed. Aliases
are resolved at build time by looking them up in the meta-registry's index; if a register can't be
found there, or a previously-cached resolution turns out to be stale (the target has moved and the
index hasn't caught up yet), the postprocessor refreshes the index and retries once before failing.

The `"default"` marker itself is also resolved this way when a meta-registry is available, so it
stays correct even if the main OGC Building Blocks repository ever moves -- falling back to a local,
hardcoded URL if the meta-registry can't be reached, so a missing/`default` import never hard-fails.
An explicit `@org/register` alias, on the other hand, has no such fallback: if it can't be resolved,
the build fails.

By default, aliases resolve against the postprocessor's built-in meta-registry. This can be
overridden -- e.g. to point at a private/internal meta-registry -- with a `meta-registry` key in
`bblocks-config.yaml`:

```yaml
meta-registry: https://example.com/my-meta-registry/index.json
```

Set `meta-registry: null` to disable alias resolution entirely (any `@org/register` import will
then fail immediately, since there is nowhere to resolve it).

## Local URL mappings (for testing)

Sometimes, a remote repository may not be available publicly (e.g., for security reasons). In that case,
URL-to-local-path mappings can be added inside an `url-mappings` object in a
`bblocks-config-local.yml` file, like so:

```yaml
url-mappings:
  'https://example.com/bbr/': '/imports/ogc/bblock-prov-schema'
  'https://example.com/relative/': '../../ogc/bblock-prov-schema'
```

This will redirect all requests to `https://example.com/bbr/...` to the `/imports/ogc/bblock-prov-schema/...` path,
and `https://example.com/relative/...` to `../../ogc/bblock-prov-schema/...`; for example, 
`https://example.com/bbr/path/to/file.txt` will correspond to `/imports/ogc/bblock-prov-schema/path/to/file.txt`.

When running the bblocks-postprocess Docker container, these additional repository copies need to be made 
available to it as mounted [volumes](https://docs.docker.com/engine/storage/volumes/#options-for---volume):

```yaml
 -v "$(pwd)/../../ogc/bblock-prov-schema:/imports/ogc/bblock-prov-schema"
```

If you are using `build.sh` as suggested in [Local Build](../create/local), you can automate the volumes that
will be mounted in the `docker` command by creating a `.volumes` file in which each line will represent a
`<local path>:<container mount path>` pair. For example:

```
/absolute/path/to/mount:/mount/absolute
../relative/path:/mount/relative
```

When you run `build.sh`, the `.volumes` file will be parsed and the volumes will be mounted.
