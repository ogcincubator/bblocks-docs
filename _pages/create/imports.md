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

## Local imports

Sometimes, a remote repository may not be available publicly (e.g., for security reasons). In that case,
repository-URL-to-local-path mappings can be added inside an `imports-mappings` object in a
`bblocks-config-local.yml` file:

```yaml
imports-local:
  'https://example.com/bbr/build/register.json': '/imports/ogc/bblock-prov-schema'
  'https://example.com/relative/register.json': '../../ogc/bblock-prov-schema'
```

When running using the docker container these additional repository copies need to be made available by adding additional `volumes` to the container:
```yaml
 -v "$(pwd)/../../ogc/bblock-prov-schema:/imports/ogc/bblock-prov-schema"
```

Similarly to URL repositories, `build/register.json` and `register.json` will also be checked for a valid
register file.
