---
title: Viewer tab plugins
permalink: /create/tab-plugins
---

[View plugins](/create/view-plugins) add a custom visualization for one example snippet or one
transform output. **Tab plugins** are a separate, parallel mechanism: they add a whole new
top-level tab to a bblock's detail page, driven by the full bblock (and its register) rather than
a single piece of content — useful for anything that doesn't fit "one visualization for one
example," such as a custom summary panel, a report generated from a build plugin's output, or a
view over the bblock's metadata itself.

A tab plugin is a small client-side ES module the viewer loads at runtime (via a browser-native
`import()`), just like a view plugin, and decides for itself — given the whole bblock — whether it
applies. If it matches, the viewer adds an extra tab after all the built-in ones (About, Examples,
Data structure, JSON Schema, ...), rendering the plugin's own content full-page.

## Adding a tab plugin to a register

Declare one or more plugins under `viewer.tab-plugins` in `bblocks-config.yaml` — the same shape as
`view-plugins`, just a sibling key:

```yaml
viewer:
  tab-plugins:
    - url: https://example.org/my-plugin/dist/index.js
      export: MyTabPlugin   # optional; a single name, an array of names, or omitted for the default export
      weight: 100            # optional; higher sorts earlier among tab plugins
```

* `url` — the plugin's ES module, fetched at runtime via `import()`. Must be served with
  permissive CORS (GitHub Pages does this by default).
* `export` — which export(s) of the module to use as plugin classes. Omit it (or set it to
  `null`/`""`/`[]`) to use the module's default export; set it to an array to pull in several
  plugin classes from the same file/bundle. A single bundle can mix view-plugin and tab-plugin
  classes, declared separately under `view-plugins`/`tab-plugins`.
* `weight` — controls ordering relative to other *tab* plugins (higher sorts earlier). Tab plugins
  always render after every built-in tab, regardless of weight.

This is written through to `register.json` (as `viewer.tabPlugins`, camelCased) and read by the
viewer at runtime — no postprocessing step touches the plugin code itself, so a register only ever
needs to point at where the plugin is hosted.

Tab plugins pair naturally with a [build plugin](/create/build-plugins) that adds a new
field/document to a bblock's `json-full` output — the build plugin emits the data, the tab plugin
renders it — but the two aren't coupled at the mechanism level. A tab plugin's `matches()` can key
off anything in the bblock or register, not just a specific field a build plugin added.

## Writing a tab plugin

Start from the same [bblocks-view-plugin-starter](https://github.com/ogcincubator/bblocks-view-plugin-starter)
template repo used for view plugins — it includes two worked tab-plugin examples (a plain-JS "Used
by" reverse-dependency tab, and a TS+Vue "Register info" tab) alongside the view-plugin ones. See
that repo's README, "Tab plugins" section, for the full walkthrough; the interface is summarized
here.

### Plugin interface

```ts
class MyTabPlugin {
  // Route `section` slug and tab key — required for a stable link across rebuilds (recoverable
  // if missing: the host synthesizes one from tabLabel, but declare it explicitly).
  static tabId = 'my-tab';
  // v-tab display text — required, no placeholder fallback if omitted (the plugin is skipped).
  static tabLabel = 'My Tab';
  // Icon (MDI name) — optional, falls back to a generic default.
  static icon = 'mdi-puzzle-outline';
  // Ordering among other matched tab plugins for the same bblock — optional, default 0.
  static weight = 0;
  // Whether the instance + rendered DOM persist across same-bblock tab switches (default true) or
  // are torn down/rebuilt every time the tab is left/reactivated (false) — set false only for
  // something holding a live connection/poller that shouldn't run in the background.
  static cacheable = true;

  // context: the full bblock and register objects, plus a small document-fetching facade — see
  // below. Unlike a view plugin, there's no per-candidate constructor argument: a tab plugin's
  // decision is over the whole bblock, not one example/transform-output representation of it.
  constructor(context) {
    this.context = context;
  }

  // Whole-context predicate deciding whether this plugin contributes a tab for this bblock — not
  // bound to checking a single field. May be async. Default true if unimplemented.
  async matches() { return true; }

  // el: an empty container for the *entire* tab body (not a small chrome-wrapped box like a view
  // plugin gets) — no fullscreen-toggle chrome is provided. May be async.
  render(el) { /* mount here */ }

  // Optional teardown — called when the tab/bblock unmounts (see `cacheable` above).
  destroy(el) {}
}
```

The `context` object passed to the constructor:

```ts
interface TabPluginContext {
  bblock: object;                 // the full, already-fetched bblock (json-full shape)
  register: object | null;        // the full, already-constructed register object
  viewerConfig: object | null;    // the viewer's resolved runtime config
  depResolver?: DependencyResolver; // optional shared-dependency cache, same as view plugins
  fetchDocument(bblock, property): Promise<unknown>;
  fetchDocumentByUrl(bblock, url, options?): Promise<unknown>;
  getBBlock(itemIdentifier): Promise<object | undefined>;
  getBBlocks(includeRemote?): Promise<Record<string, object>>;
}
```

`fetchDocument`/`fetchDocumentByUrl`/`getBBlock`/`getBBlocks` are the same helpers regular viewer
components use to fetch a bblock's own documents or look up other bblocks — handy if a tab plugin
wants to check or render something beyond what's already inline in `context.bblock`.

Bundle any third-party dependency (including a UI framework, if you want one — `render(el)` is a
plain DOM-element handoff, so `createApp(...).mount(el)`/React's `createRoot(el).render(...)` work
the same way a view plugin could mount Three.js into its box) into your own plugin module rather
than assuming the host provides it. See [View plugins](/create/view-plugins#writing-a-view-plugin)
and the starter template's README for the shared guidance (lazy-loading heavy dependencies,
`context.depResolver`, CSS injection) that applies identically here.

### Trying it out

Same as for view plugins: build the plugin, serve `dist/` from any static host with permissive
CORS, and point `bblocks-config.yaml` at it as shown above. See
[View plugins → Trying it out](/create/view-plugins#trying-it-out) for the full walkthrough
(jsDelivr hosting via the starter template, local testing tips, and why the devtools console
matters for anything an async error in your own plugin code wouldn't otherwise surface).

See a tab plugin working live on the
[tab-plugin-demo bblock](https://ogcincubator.github.io/bblocks-examples/bblock/ogc.bbr.examples.plugins.tab-plugin-demo)
in the `bblocks-examples` register.

### Trust model

Same as view plugins: a register only ever loads the tab plugins it declares itself — plugins from
imported registers are never consulted. Declaring a plugin's URL is equivalent to embedding a
`<script>` on a page you control: no sandboxing is applied, so only point at code you trust.
