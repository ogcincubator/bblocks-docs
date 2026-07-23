---
title: Viewer view plugins
permalink: /create/view-plugins
---

The [Building Blocks Viewer](/create/postprocessing#building-blocks-viewer) renders a few
content-based visualizations out of the box — a map view for GeoJSON, a 3D view, and a web view for
HTML/XML content. **View plugins** let a register add its own custom visualizations for example
snippets or transform outputs, without that code living inside the viewer itself.

A view plugin is a small client-side ES module the viewer loads at runtime (via a browser-native
`import()`) and matches against the content of an example snippet or transform output. If it
matches, the viewer adds an extra tab that renders the plugin's own view alongside the built-in
code/schema tabs.

## Adding a view plugin to a register

Declare one or more plugins under `viewer.view-plugins` in `bblocks-config.yaml`:

```yaml
viewer:
  view-plugins:
    - url: https://example.org/my-plugin/dist/index.js
      export: MyPlugin   # optional; a single name, an array of names, or omitted for the default export
      weight: 100         # optional; higher sorts earlier among plugin tabs
```

* `url` — the plugin's ES module, fetched at runtime via `import()`. Must be served with
  permissive CORS (GitHub Pages does this by default).
* `export` — which export(s) of the module to use as plugin classes. Omit it (or set it to
  `null`/`""`/`[]`) to use the module's default export; set it to an array to pull in several
  plugin classes from the same file/bundle.
* `weight` — controls tab ordering relative to other view plugins (higher sorts earlier). The
  viewer's own built-in views (map/3D/web) always sort first regardless of `weight`.

This is written through to `register.json` (as `viewer.viewPlugins`, camelCased) and read by the
viewer at runtime — no postprocessing step touches the plugin code itself, so a register only ever
needs to point at where the plugin is hosted.

### Out-of-the-box plugins

The viewer's built-in map, 3D, and web views are themselves ordinary view plugins, published as
[bblocks-viewer-base-plugins](https://github.com/ogcincubator/bblocks-viewer-base-plugins):

* **Map view** (`GeoJsonMapPlugin`) — renders GeoJSON `Feature`/`FeatureCollection` content on a
  Leaflet map, with semantically-enriched popups for JSON-LD-aware content.
* **3D view** (`ThreeDPlugin`) — renders GeoJSON with Z coordinates, or CityJSON-like topologies, as
  an interactive 3D scene (orbit controls, grid/wireframe/edges/vertices toggles).
* **Web view** (`WebViewPlugin`) — points a sandboxed iframe at HTML content served from an
  absolute URL.

These ship with the viewer automatically, so a register doesn't need to declare them. The package is
also usable as a self-hosted plugin bundle in its own right — for example, if you want one of these
same visualizations available for a custom media type it doesn't match by default — and is a good
real-world reference for writing your own plugin, beyond the starter template's examples.

## Writing a view plugin

Start from the [bblocks-view-plugin-starter](https://github.com/ogcincubator/bblocks-view-plugin-starter)
template repo — click "Use this template" on GitHub, or clone it:

```shell
git clone https://github.com/ogcincubator/bblocks-view-plugin-starter my-plugin
cd my-plugin
npm install
```

It contains a minimal plugin skeleton (in both TypeScript and JavaScript — pick one, delete the
other), two complete worked examples (a JSON tree view and a CSV table view), and a build setup
producing a single deployable `dist/index.js`.

### Plugin interface

A plugin module exports one or more classes (default export, or named exports referenced by
`export` in `bblocks-config.yaml`). Each class:

```ts
class MyPlugin {
  // MIME types this plugin might handle, checked against each candidate's resolved MIME type
  // before the class is instantiated. Supports wildcards ('text/*', '*/*'). Required.
  static supportedTypes = ['application/geo+json'];

  // Tab label and icon (MDI name, e.g. 'mdi-map') — optional, both fall back to a generic default.
  static viewName = 'Map';
  static icon = 'mdi-map';

  // candidates: one entry per available representation of the same content — one per example
  // snippet language, or a single-element array for a transform output. Each candidate is
  // { type, content, url, label }; a plugin picks whichever one(s) it actually wants.
  //
  // context: { bblock, viewerConfig } — host information beyond the candidates themselves.
  // Always supplied; using it is what's optional.
  constructor(candidates, context = {}) {
    this.candidates = candidates;
  }

  // Optional content-based filter for when the type filter alone isn't precise enough. Only
  // called for candidates whose content resolved. Return false to withdraw the match — omit
  // this method to always match once the type filter passes.
  matches() { return true; }

  // el: an empty <div> the plugin owns, sized to the viewer's plugin-tab chrome (small box with a
  // fullscreen toggle). May be async.
  render(el) { /* mount your view here */ }

  // Optional teardown when the tab/component unmounts.
  destroy(el) {}
}
```

A candidate has the shape:

```ts
interface ViewPluginCandidate {
  type: string | null;     // resolved MIME type, e.g. 'application/geo+json'
  content: string | null;  // resolved text, or null if not (yet) available
  url: string | null;      // the URL this content came from, if any
  label: string;           // human-readable label (snippet language, or transform id)
}
```

Bundle any third-party dependency your plugin needs into its own module — a plugin is a
self-contained embeddable widget, not code that shares the host viewer's runtime. Import heavy
dependencies lazily inside `render()` so they're only downloaded once the plugin actually renders,
not just because it was checked for a match.

If your plugin needs its own CSS, inject it at runtime via a `<style>` tag rather than relying on a
`<link>` in the host page — see the starter template's README for the exact pattern (a static, not
dynamic, `?raw` CSS import).

The starter's README covers the full contract, build/bundling notes, the CSS-injection pattern, and
a FAQ (local testing, error handling, shipping multiple plugins from one bundle) in more detail than
reproduced here.

### Trying it out

Build the plugin (`npm run build`), serve `dist/` from any static host with permissive CORS
(GitHub Pages works out of the box), and point a register's `bblocks-config.yaml` at it as shown
above. For local testing, the simplest setup is same-origin: serve the plugin file from the same
static server as the register/build directory you're previewing in the
[local viewer](/create/postprocessing#building-blocks-viewer).

### Trust model

A register only ever loads the view plugins it declares itself — plugins from imported registers
are never consulted. Declaring a plugin's URL is equivalent to embedding a `<script>` on a page you
control: no sandboxing is applied, so only point at code you trust.
