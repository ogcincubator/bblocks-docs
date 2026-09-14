# AI Readiness

Working note. Scope is anchored by the reviewed use case outline at
[usecases/ai-readiness](https://ogcincubator.github.io/bblocks-docs/usecases/ai-readiness) — this note
becomes the deeper dive into design principles and mechanisms it points to.

Two things from the reviewed use case shape how this note should be written:

- **AI readiness is framed as efficiency**, not just correctness — improved processing time,
  token/model cost, human validation effort and energy consumed, plus the effort needed to identify
  and frame where AI can usefully be applied at all. Candidate mechanisms below should be justified
  against one or more of these, not just "this would help an agent."
- **The use case is also an on-ramp.** It's explicitly intended to introduce Building Blocks to people
  arriving with an AI-readiness requirement or interest, not only to describe internal design intent.
  That means mechanisms in this note should stay explainable to that audience — motivated from the
  factor list, not from Building Blocks internals outward.

## Relationship to other design notes

- [agent-federation.md](agent-federation.md) already lays out the enterprise viewpoint: AI agents as
  likely primary consumers of interoperability resources, the actors involved, and the trust/cost
  framing. This note is the narrower, mechanism-level companion: given that framing, what actually
  makes a Building Block (or a register of them) usable by an agent.
- [schema-vocabulary-bindings.md](schema-vocabulary-bindings.md) covers the semantic-binding
  mechanisms (JSON-LD, SHACL, codelists) behind the use case's "explicit, disambiguated semantics"
  factor — meaning has to be machine-checkable before an agent can be expected to get it right.
- [metadata-tiers.md](metadata-tiers.md) — possible home for "AI readiness" as a declared tier/property.
  Still open per the use case's considerations: it may just be the natural consequence of doing
  existing FAIR/semantic-uplift work well, rather than something to name and track separately.

## Related practices: Graphify and Open Knowledge Foundation

See [blocks-and-knowledge-graphs.md](blocks-and-knowledge-graphs.md) for the fuller design note this
section summarises — full terminology, a table of what each approach pre-compiles and when, the
normativity trade-off between OKF and Blocks, and candidate view/bridge shapes. What follows here is
the short version relevant to AI readiness.

### Graphify

Graphify (and similar code-assistant tooling) pre-compiles a source repository into a
structured representation — call graphs, symbol indices, dependency maps — specifically so an LLM
doesn't have to reconstruct that structure from raw source on every query.

OGC Building Blocks already
does the structurally analogous thing for standards: decomposing a standard into small, identified,
independently-validatable units instead of one monolithic document.

### OKF

**OKF — Open Knowledge Format.** An open, vendor-neutral specification from Google Cloud for packaging
knowledge as a directory of Markdown files with YAML frontmatter, cross-linked into a graph that an
agent traverses instead of running similarity search over an undifferentiated corpus. v0.1 is
deliberately minimal: the only required frontmatter field is `type`; `title`, `description`,
`resource`, `tags` and `timestamp` are recommended, and `index.md`/`log.md` are reserved filenames
providing progressive disclosure and a chronological change history. v0.2 (2026) adds provenance,
trust, lifecycle and attestation, backward-compatibly. A producer/consumer ecosystem already exists,
including deterministic generators that build OKF bundles from repositories, database schemas and
docs sites without an LLM. **LOKF** (Linked Open Knowledge Format) is a semantic profile of OKF,
defined in LinkML, that binds it to schema.org, DCAT and PROV-O and generates a JSON-LD context, JSON
Schema, SHACL shapes and an OWL ontology from that single source — structurally close to what a Block
already carries, just derived in the opposite direction (one schema → four artefacts, versus Blocks
composing those four from separately authored sources with inheritance and profiling).

Where this matters for AI readiness: OKF trades enforcement for near-zero adoption friction — it's
permissive by design, so a consumer must not reject a bundle for unknown types, unknown keys or broken
links — while Blocks trade authoring effort for validated, interoperable meaning. A Blocks-to-OKF
projection is one of several candidate view/bridge shapes discussed in
[blocks-and-knowledge-graphs.md §10](blocks-and-knowledge-graphs.md#10-candidate-view-and-bridge-shapes),
not a design commitment.

## Candidate mechanisms

Loosely ordered against the use case's "AI readiness factors" list; each should eventually be
justified against the efficiency framing above (processing time / token-model cost / human validation
effort / energy) rather than taken on faith.

- **Retrieval-oriented artifacts via a pluggable construction layer.** The use case's considerations
  lean toward this over a hardcoded design: rather than the register committing to one technology for
  chunking/embedding, expose a pluggable artefact-construction layer so different retrieval strategies
  (RAG index, fine-tuning corpus, agent tool schema) can be generated from the same source blocks
  without the register needing to pick a winner. Needs a concrete design — where this layer sits
  relative to bblocks-postprocess, what the plugin interface looks like.
- **Chunking/sizing of blocks relative to context windows.** Is there a natural "AI-friendly"
  granularity, and does it conflict with good schema design for humans? Ties directly to the
  human-vs-AI-legibility tension noted above.
- **Verification loop for agent-generated content.** Use the same pass/fail example suites and SHACL
  shapes that check human-authored examples to check agent output — an agent proposes data, the
  existing test machinery validates it, closing the loop the use case calls out as "verified, not just
  plausible."
- **Provenance/trust signalling.** How would an agent (or a human reviewing an agent's work) tell a
  block's semantics are authoritative vs. draft vs. a third-party profile? Relevant to the trust
  framing in [agent-federation.md](agent-federation.md).
- **Structural consistency as an auditable QC check.** If predictable structure across blocks is what
  lets an agent generalise from one block to another, that consistency could be checked automatically
  at register-build time rather than only aspired to.
- **A minimal "AI-ready" checklist, if one exists.** The use case leaves open whether this varies too
  much by consumer to be worth defining. Worth a short spike: try to write the checklist against the
  factor list and see whether it actually converges or fragments by consumer type.

## Status

Scoped against the reviewed use case. Next step is to pick one candidate mechanism (the pluggable
artefact-construction layer looks like the most concrete starting point, since the use case already
leans toward it) and take it to an actual design.
