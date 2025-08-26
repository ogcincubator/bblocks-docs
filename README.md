# OGC Building Blocks documentation

OGC Building Blocks support the development, testing and publishing of machine-readable standards. They standardise the way dependencies are managed and support transparent and efficient reuse of components of standards, aggregation into new standards and profiling for specific applications.

This repository contains the sources for the
[OGC Location Building Blocks documentation](https://ogcincubator.github.io/bblocks-docs).

## For developers

This repository uses Jekyll to build the documentation. Please follow GitHub's documentation
on [using Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)
for more information.

For the truly impatient:

Build locally with:
`bundle exec jekyll serve`

Access the page on:
`http://127.0.0.1:4000/`

The [Minimal Mistakes Jekyll theme](https://mmistakes.github.io/minimal-mistakes/) is used for styling.

### Repository layout

* `_pages`: contains the different pages that make up the documentation.
* `_data`: additional files for layouts, configuration...
  * `navigation.yml`: navigation sidebar
* `assets`: contains images, css, js, etc.
