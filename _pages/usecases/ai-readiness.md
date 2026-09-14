---
title: AI Readiness of Interoperability Resources
permalink: /usecases/ai-readiness
---

_This is a first outline of the use case, for review and refinement. Once agreed, it will anchor a
deeper dive into design principles and mechanisms in the [design notes](https://github.com/ogcincubator/bblocks-docs/blob/master/design/ai-readiness.md)._

## The use case

Standards, schemas and vocabularies are increasingly discovered, interpreted and acted on by AI
agents (LLMs, RAG pipelines, agentic tools) rather than solely by humans reading documentation. This
is already touched on under [Discovering relevant OGC standards](usecases#discovering-relevant-ogc-standards),
where the register's Knowledge Graph is identified as a discovery aid. **AI readiness is broader than
discovery**: it is about whether a standard's artifacts are structured so that an agent can correctly
*interpret* them, *act* on them, and have that action *verified*, at a cost (in tokens, time, risk)
that is actually affordable.

<div class="notice notice--info" markdown="1">
#### An analogous move: Graphify

Tools such as Graphify pre-compile a code repository into a structured
representation specifically to make it more tractable for LLMs to navigate and reason about, rather
than relying on the LLM to parse raw source on demand. OGC Building Blocks already does something
structurally similar for standards — decomposing them into small, identified, machine-validatable
units. It's a useful point of resemblance, not the focus of this use case; the concerns below apply
whether or not the comparison holds up. See [design/ai-readiness.md](https://github.com/ogcincubator/bblocks-docs/blob/master/design/ai-readiness.md)
for where the analogy breaks down.
</div>

## Who this is for

- **Standards editors / SWGs** who want their standard to be reliably discoverable and usable by AI
  tooling, not just human implementers.
- **Downstream implementers** using LLM agents or copilots to build conformant applications, and who
  need the agent's output to be checkable against something authoritative.
- **Infrastructure and platform operators** who want agents to validate, generate, or transform data
  against known-good constraints, with auditable results.
- **Register/tooling maintainers** (bblocks-postprocess, the meta-register, semantic uplift tooling)
  who decide what artifacts a Building Block produces and in what form.

## What "AI readiness" means

AI readiness means increased efficiency - improved processing time, token and model cost, human validation, energy consumed - and also in the effort required to identify and frame the use of AI to improve utilisation of information.

## AI readiness factors

- **Stable, resolvable identifiers.** `bblocks://` references and register URIs give an agent something
  durable to cite and re-fetch, instead of re-deriving meaning from free text each time.
- **Explicit, disambiguated semantics.** JSON-LD context and SHACL shapes turn "what does this field
  mean" from a prose question into a queryable, machine-checkable fact (see
  [semantic uplift](../create/semantic-uplift)).
- **Bounded, composable units.** Small, well-scoped blocks are easier to retrieve, fit in a context
  window, and reason about individually than one large, monolithic standard document.
- **Verifiable output, not just plausible output.** JSON Schema/SHACL validation and example test suites
  let an agent's generated content be checked mechanically, rather than trusted on the strength of the
  model producing it.
- **Grounding examples, including negative ones.** Pass *and* fail examples (already a QC practice —
  see [QC - testing rules](usecases#qc---testing-rules)) give an agent concrete signal about the
  boundary of correctness, not just descriptions of it.
- **Documentation generated from the same source as the machine artifacts.** If human-facing docs and
  machine-facing schemas can drift apart, an agent trained or grounded on one will mislead about the
  other.
- **Predictable, consistent structure across blocks.** An agent that has learned to work with one
  Building Block should be able to generalise to another without bespoke handling.

## Related material

- [Discovering relevant OGC standards](usecases#discovering-relevant-ogc-standards) — the existing
  use case section this one extends, moving from *finding* the right standard to *correctly using* it.
- [design/agent-federation.md](https://github.com/ogcincubator/bblocks-docs/blob/master/design/agent-federation.md) —
frames AI agents as likely primary consumers of interoperability resources, and lays out the
  enterprise viewpoint (actors, trust, cost of context) this use case draws on.
- [design/schema-vocabulary-bindings.md](https://github.com/ogcincubator/bblocks-docs/blob/master/design/schema-vocabulary-bindings.md) —
  the semantic-binding mechanisms that make schemas machine-interpretable in the first place.

## Considerations (instructions for interpretation)

- "AI readiness" is the natural consequence of doing the FAIR/semantic-uplift work well, but the
  implications are broad enough that it may be worth naming and tracking as its own property (e.g. a
  metadata tier) rather than leaving it implicit — still open, not decided.
- What would we actually measure or test to call a Building Block "AI-ready"? Is there a minimal
  checklist, or does it vary too much by consumer (RAG index vs. agentic tool vs. fine-tuning corpus)?
- The register could expose retrieval-oriented artifacts directly (e.g. chunked/embedded
  representations) - this may be done with a pluggable artefact construction layer rather than a hardcoded design for specific technologies?
- This Use Case and associated design perspectives are intended to introduce the Building Blocks from the perspective of a requirement or familiarity with AI readiness.

## See also

- [Improving and Augmenting Standards](usecases) — the parent use-case index
- [Semantic uplift](../create/semantic-uplift)
- [Extension points](../create/extension-points)
