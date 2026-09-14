# OGC Blocks, AI-readiness renditions, and agent knowledge formats

**Status:** design note. Non-normative, exploratory. Records observed parallels, a framing
for interpreting recurring questions, and open questions. Makes no commitment to any of
the renditions sketched below, and does not imply that any of them are planned.

**Purpose:** to give a consistent answer to the question "how does OGC Blocks relate to
OKF / knowledge graphs / agent tooling", and to give anyone designing such a bridge a
shared vocabulary and a list of the decisions that would need making.

---

## 1. Framing: what the Blocks approach actually is

The most common misreading of OGC Blocks treats it as a JSON toolchain. It is more
usefully described as **dependency management and continuous test for specification
components**, with:

- stable, globally unique, resolvable identifiers
- declared relations between components — dependency, profiling, extension points,
  register-level imports
- versioning and lifecycle state
- machine-checkable conformance, run continuously, with published reports
- derived artefacts built automatically from authored sources

JSON Schema + JSON-LD + SHACL is the instantiation that is furthest developed, and a
genuinely powerful one, because that triple gives structure, meaning and constraint over
the same component. But nothing in the list above is specific to it. The same machinery
applies to RDF and OWL artefacts, to UML or SysML models, to XSD, to protocol schemas —
to any artefact family where components have dependencies, versions and testable
conformance, and where the cost of an unmanaged specification estate is felt.

This framing matters for everything that follows, because it locates "AI readiness" as
**a layer of value over an existing substrate**, not a change of direction.

---

## 2. Terminology

- **OKF — Open Knowledge Format.** An open, vendor-neutral specification from Google
  Cloud for packaging knowledge as a directory of Markdown files with YAML frontmatter,
  cross-linked into a graph that agents traverse. v0.1 is deliberately minimal: the only
  required frontmatter field is `type`; `title`, `description`, `resource`, `tags` and
  `timestamp` are recommended. `index.md` and `log.md` are reserved filenames providing
  progressive disclosure and chronological change history. v0.2 (2026) adds provenance,
  trust, lifecycle and attestation, backward-compatibly. A producer/consumer ecosystem
  exists across several languages, including deterministic generators that build bundles
  from repositories, database schemas and docs sites without an LLM.
- **LOKF — Linked Open Knowledge Format.** A semantic profile of OKF defined in LinkML,
  binding concepts, fields and relations to schema.org, DCAT and PROV-O, and generating a
  JSON-LD context, JSON Schema, SHACL shapes and an OWL ontology from that single source.
  Adds typed relations in place of OKF's untyped Markdown links.
- **Graphify** (Graphify-Labs). Turns a codebase, with its docs, SQL schemas, configs and
  PDFs, into a queryable property graph. Deterministic tree-sitter parsing for code, LLM
  only for unstructured material, each edge tagged as read directly or resolved. Ships an
  MCP server so an agent traverses the graph instead of reading files. Not a vector index.

Two disambiguations worth making whenever these questions arise: **OKG** is a different
and ambiguous acronym and should not be read as OKF; **Graphiti** (Zep) is an unrelated
temporal knowledge-graph library for agent memory built by LLM extraction.

---

## 3. The shared premise, and where each party pre-compiles

All of these rest on the same observation: structure that has already been declared
should be read, not statistically re-inferred. They differ in what is declared, when, and
by whom.

| | Declares | When | Technology scope |
|---|---|---|---|
| Graphify | Relations recoverable by parsing source | Post-implementation | Code, DDL, manifests |
| OKF | Concept boundaries, navigation order, links, provenance | Documentation time | Markdown bundles |
| OGC Blocks | Identity, dependency, constraint, semantics, conformance | Pre-implementation, cross-organisation | Format-agnostic by design |

The working hypothesis — that standardising design patterns is a form of pre-compilation
— holds for all three, provided the object of compilation is kept distinct. OKF
pre-compiles **navigation**: explicit links and index files replace similarity search
over an undifferentiated corpus. Graphify pre-compiles **code structure**. Blocks
pre-compile **meaning, constraint and lineage**, once, in a form that many consumers
share.

The last of these is the only one whose value scales with adoption across organisations
rather than within a single repository or bundle. That is the distinctive claim, and it
is independent of serialisation.

---

## 4. The normativity axis

The sharpest contrast with OKF is not architectural but in enforcement stance, and both
positions are deliberate.

| | OKF v0.1/0.2 | OGC Blocks |
|---|---|---|
| Required declarations | One field (`type`) | Identifier and metadata, plus what the block class requires |
| Vocabulary | `type` values not centrally registered | Identifiers globally unique, register-scoped, resolvable |
| Relations | Untyped Markdown links | Typed: dependency, profile, extension point, register import |
| Validation | Permissive by design — a consumer must not reject a bundle for unknown types, unknown keys, broken links or missing indexes | Schema validation, SHACL, declared tests, published reports |
| Lifecycle | `timestamp`, `log.md`; v0.2 adds provenance and trust | `status`, `maturity`, `version`, addition and change timestamps |
| Failure mode | Under-specification: two producers express the same relation incompatibly | Adoption cost: conformance requires real authoring effort |

Neither is a defect. OKF buys near-zero adoption friction and turns a pile of documents
into a graph. Blocks buy interoperability of meaning and pay in authoring discipline.
Questions of the form "should Blocks be more like OKF", or the reverse, are usually
really about which cost the asker prefers to bear.

**LOKF is the convergence already visible from the other side.** It generates a JSON-LD
context, JSON Schema, SHACL shapes and an OWL ontology from one LinkML definition — an
artefact set structurally close to what a Block carries. The difference is direction of
travel: LOKF derives all four from a single schema, Blocks compose them from separately
authored sources with inheritance and profiling across a register.

---

## 5. AI readiness as a layer, not a pivot

If the substrate is dependency-managed, continuously tested specification components,
then "AI readiness" is the observation that a new class of consumer has appeared which
wants those components in a different rendition: navigable, progressively disclosable,
retrievable without parsing a schema language, and annotated with enough provenance for
an agent to know what it is trusting.

That is an additional output class over existing authored sources. It does not require
changing what a Block *is*, and it should not be allowed to.

The corollary is that the interesting architectural question is not "should Blocks
produce OKF bundles" or "should registers emit property graphs". It is **where such
renditions live and how cheaply they can be replaced.**

---

## 6. Core versus view

A workable separation:

**Core** — anything whose loss loses information:
identity, versioning, declared dependency and profile relations, authored schemas,
contexts, shapes, examples, tests, validation results, build provenance.

**View** — anything regenerable from the core:
human-readable documentation, the hosted viewer, RDF renditions and triplestore push,
flattened property tables, an OKF bundle, a property-graph projection, an agent-facing
MCP surface, a retrieval index.

The test is simple: if it can be rebuilt from core artefacts, it is a view. If losing it
loses something nobody else holds, it is core and belongs under validation and version
control.

The register already has the relevant extension machinery in embryo. Transforms are
declared per block with input and output media types, are discoverable from the register
so clients need not reimplement them, and are exercised against example snippets during
the build — with the transform library, not the sample output, treated as the primary
artefact. Transform and validator plugins are declared in register configuration and
recognised by duck typing, without a base class. The planned extension of plugins into
the artefact builders generalises the same pattern from data conversion to derived
views.

If view generation sits there, then an OKF rendition, a property-graph projection, or
whatever succeeds them are **plugins with declared outputs**, discoverable from the
register in the same way transforms already are — and, importantly, removable without
consequence when they stop being the right shape.

---

## 7. Volatility is the design constraint

Practice in this area is changing faster than specification cycles. OKF moved from v0.1
to a v0.2 with a trust, provenance and attestation layer within months, and a surrounding
ecosystem of generators, MCP servers, editor plugins, language implementations and a
semantic profile appeared around it in the same period. Code-graph tooling is moving at a
similar rate, and the retrieval-versus-traversal question is unsettled.

The reasonable response is not to pick a winner. It is to ensure that:

- the core carries enough declared structure that **any** such view is cheap to generate
- views are versioned and labelled with what they are lossy about
- the register records which views it currently emits, rather than the specification
  promising any particular one
- no view acquires authority, because views will be retired

A view that is expensive to produce or awkward to remove will outlive its usefulness.

---

## 8. What already exists in graph form

Worth stating plainly, because questions here often assume otherwise:

- **Instance data** already has a canonical graph projection. The assembled JSON-LD
  context plus semantic uplift is a declarative, deterministic JSON-to-RDF transform,
  with SHACL for constraint checking on the result.
- **The register catalogue** is already published as RDF. `register.json` carries
  self-links to `bblocks.jsonld` and `bblocks.ttl`, and the postprocessor can push
  register RDF, and ontologies, to a triplestore over the Graph Store Protocol, recording
  a `sparqlEndpoint` in the register. Dependency, profile, extension-point, import,
  status and version metadata are therefore already queryable as a graph.

So a register is a **producer** of graph structure, not a corpus to be extracted from.
Running register sources through a generic document or LLM extraction pass converts
typed, versioned, asserted relations into flatter inferred ones — a fidelity loss.

---

## 9. Where the approaches genuinely do not overlap

- Code graphs index **implementations**; Blocks describe **specifications**. Neither side
  carries an edge between a code symbol, table or endpoint and the Block it realises.
  Conformance exists as a validation-time check, not a navigable relation.
- OKF bundles are read by a **broad and growing set of agent tooling** that does not
  parse JSON Schema, JSON-LD or SPARQL. Register content currently reaches such tools
  only as HTML documentation or raw JSON.

---

## 10. Candidate view and bridge shapes

Options with trade-offs. No recommendation intended; each is a candidate for the view
layer described in §6, not for the core.

1. **Register-to-OKF projection.** One concept document per block, `type` from
   `itemClass`, links carrying dependency and profile relations, generated indexes, log
   from change timestamps. Reaches the OKF consumer ecosystem cheaply. Lossy: untyped
   links cannot distinguish dependency from profiling without a convention, and a
   permissive consumer enforces nothing.
2. **Blocks as an OKF `type` vocabulary.** OKF leaves `type` values unregistered; block
   identifiers are exactly the resolvable values that gap invites. Costs nothing, since
   unknown types must already be tolerated, and guarantees nothing either.
3. **LOKF rather than bare OKF** where typed relations and RDF fidelity matter — the
   mapping is then between two generated artefact sets rather than between a graph and a
   document pile.
4. **Identifier alignment in code graphs.** Block identifiers as node identifiers on the
   implementation side, making the specification-to-implementation join available to
   anything reading both. Minimal; disturbs neither lifecycle.
5. **Conformance annotation in source.** Code-side markers declaring which Block a
   construct implements. Highest fidelity, because the claim is made by whoever knows it;
   highest authoring cost.
6. **Agent-facing surface over the register itself** — an MCP or skill rendition of
   catalogue navigation. The most directly "AI ready" option, and the one whose
   conventions are least settled.

---

## 11. Standing considerations

- **Direction of authority.** A register is authoritative; any derived bundle or graph is
  a rendition. If a derived artefact becomes the thing people edit, normative and
  navigable copies diverge silently — and a permissive consumer contract guarantees
  nothing will signal it.
- **Overlapping lifecycle vocabularies.** OKF v0.2 provenance and trust, and register
  `status` and `maturity`, describe adjacent but non-identical things. Map explicitly, or
  carry both without merging.
- **Do not merge storage.** Per-repository code graphs rebuild on commit; OKF bundles are
  authored alongside their subject; registers publish for cross-organisation interchange.
  Aligning identifiers is cheap; unifying stores commits all three to a lifecycle none of
  them wants.
- **Preserve the closed/open world boundary.** Schemas and SHACL are constraints over
  bounded input; RDF is open-world; Markdown links are neither. Flatten all three and
  "required property", "observed property" and "someone linked these" become
  indistinguishable.
- **Provenance is the hard part,** not transport. Any merged view must carry whether a
  relation was published, parsed, inferred or merely linked, and by whom.

---

## 12. Open questions

- Which consumers would an OKF rendition reach that HTML documentation, JSON and RDF do
  not? Is that audience large enough to justify a maintained view?
- What convention would carry relation type through untyped Markdown links — or is that
  better handled by targeting LOKF?
- How should block `status`, `maturity` and version transitions map onto OKF v0.2 trust
  and lifecycle signals, if at all?
- What identifies a conformance relation reliably — annotation in code, schema reference,
  runtime introspection, or a combination?
- How far do the dependency-management and CI/CT principles carry into non-JSON artefact
  families in practice, and what does a UML or RDF-native block register need that the
  current tooling does not provide?
- What is the minimum the artefact-builder plugin interface must expose for view plugins
  to be genuinely cheap to add and to retire?
