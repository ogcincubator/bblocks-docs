# Capability model for semantic resource publishing

## Prompt

Create a "capability maturity model" for publishing semantic resources that reflects the realities of a federated architecture.

Use the thinking here: https://www.ogc.org/blog-article/the-all-or-nothing-myth-of-interoperability/

Take into account the "Linked data" but recognise that the target is not publication of resources into a Linked Data framework, but readiness to re-use such resources in a transparent and non-fragile way.

The business context is "research" so take into account that the business goal capabilities for content looks something like this:

1. scientific method and responsibility - make sure details of research are adequately described
2. transparency - vocabularies and data are accessible in some form
2. reproduceability - vocabularies and data are accessible in standardised form that can easily be reused using original methods.
3. shared understanding - a community of practice, such as a joint project sess limited re-use (and hence review) of materials
4. contribution to a domain - published as a reusable resource in a domain specific context, such as a shared repository (ontoportal, agrovoc) etc without a specific authoritative status
5. standardised by a domain - published as a recommended resource by a domain community within a formal governance framework
6. recognised as a cross-domain standard (de jure or de facto)
7. adopted by operational agencies to deliver policy outcomes
8. international standard (potentially implicated in procurement requirements)

note this is a draft set of maturity options, and may be augmented or should be updated to use more commonly accepted terminology if identified.

The principles from the OBO foundry https://obofoundry.org/principles/fp-000-summary.html apply to this task, and should be cross-referenced or adopted as required - noting this maps to the middle tiers - neither the very simple publication case nor explicitly adressing the federation models required for re-use.

first identify the stages, then suggest a table of additional metadata elements needed to support each tier (if required).  Assume a formal metadata profile will be required for each capability stage, these may be "null profiles" that don't add additional content elements. Profiles may constrain the content values however, by requiring that the organisation managing a vocabulary meets a particular requirement.

A technical capabilities maturity model could also be derived along the lines of:

1. curation
2. standardisation of content
3. import/export of heterogenous sources
4. interoperability of access
5. federation on common technical platforms
6. federation of heterogenous platforms 
7. visualisation tools for clients
8. semantic alignment tools for client systems
9. federated AI agents

Note this technical model is not the goal here - but considering it may suggest metadata requirements supporting the business (i.e. reuse) goals - for example metadata to support clients downloading resources and retaining actionable provenance that allows downloaded resources to be updated from (or provide updates to) a source.

---

## 1. Framing

This document describes a model for progressive capability maturity for published vocabularies and semantic resources. It encompasses the starting state of Research Vocabularies Australia but considers also the potential value of these resources to clients, and how to classify them in order to optimise effort on standardisation and metadata. It addresses the goal of integration of research with operational roles, both in the re-use of resources provided explicitly to support operational roles, upon which further research is based, and the evolution of such resources from initial research context into acceptance and re-use by a community and finally into operational monitoring or delivery against policy goals.

It is tempting to consider the publication of semantic resources in the context of "Linked Data" 
Interoperability is not a binary achieved by full Linked Data publication; it is a gradient of progressively cheaper transaction costs, reached by standardising one component at a time (descriptive text → selective standardisation → machine-actionable structure → recursive/governance optimisation → shared economies of participation). This model applies that gradient to the *business* goal of research reuse rather than to the *technical* goal of Linked Data conformance. A resource can sit at a high business maturity tier (e.g. adopted by an operational agency) while remaining technically modest (e.g. CSV + a stable identifier scheme), provided governance and provenance are strong enough to make reuse non-fragile.

Two related, but non-identical, reference points are used for calibration rather than adopted wholesale:

- **FAIR** (Findable, Accessible, Interoperable, Reusable) — a widely recognised vocabulary for the same underlying concerns, used below as terminology, not as a gate.
- **5-star Linked Data** (Berners-Lee) — a technical proxy for tiers 2–4 below. Full 5-star achievement is neither necessary nor sufficient for the higher business tiers, which depend on governance, authority and community trust rather than serialisation format.

The **OBO Foundry principles** map to the middle of the business scale (tiers 3–6 below): they presuppose a resource is already accessible and structured, and stop short of describing cross-domain or operational-agency federation. That mapping is made explicit in §3.

## 2. Business capability maturity model


| Tier | Name | Source draft label | Description | Interoperability-spectrum analogue |
|---|---|---|---|---|
| 1 | **Documented** | scientific method and responsibility | Research method, data, and vocabularies are described in enough detail to be scientifically accountable. No commitment to public access yet. | Pre-Step 1 (internal record only) |
| 2 | **Transparent** | transparency | Vocabularies/data are accessible in *some* human-readable form (report, spreadsheet, web page). Satisfies openness norms; not yet machine-actionable. | Step 1 — descriptive text |
| 3 | **Reproducible** | reproduceability | Published in a standardised, machine-readable structure (e.g. RDF/OWL/SKOS/CSV-W) sufficient that a third party can re-run the original method and get the same result. | Steps 2–3 — incremental standardisation → actionable machine-readable standards |
| 4 | **Community-shared** | shared understanding | A defined community of practice (e.g. a joint project) shares semantics and reuses/reviews each other's resources. Reuse is real but bounded; review substitutes for formal governance. | Step 4 (partial) — recursive optimisation within a bounded group |
| 5 | **Domain-contributed** | contribution to a domain | Deposited in a shared domain repository (OntoPortal, AGROVOC, etc.) as a candidate reusable resource, discoverable beyond the originating community, but without authoritative status. | Step 4 — governance/process standardisation begins |
| 6 | **Domain-standardised** | standardised by a domain | Recommended/endorsed within a formal domain governance framework: maintenance lifecycle, versioning commitments, and an accountable locus of authority. | Step 5 — economies of participation within a domain |
| 7 | **Cross-domain standard** | recognised as a cross-domain standard | Adopted across multiple domains, de facto (independent widespread adoption) or de jure (ratified by a cross-domain body such as OGC, W3C, ISO/TC 211). | Step 5, extended across domains |
| 8 | **Operationally adopted** | adopted by operational agencies | Embedded in operational/regulatory infrastructure delivering policy outcomes; carries SLA-grade stability and change-management obligations. | Step 5 — network effects at institutional scale |
| 9 | **Internationally standardised** | international standard | Formal international standard status, potentially referenced in procurement or regulatory requirements; the resource itself becomes a compliance object. | Step 5 — maximal economies of participation |

## 3. Cross-reference: OBO Foundry principles by tier

The OBO Foundry principles (numbered per the summary page; note the source lists jump from 13 to 16 and 19–20, which is preserved here) become binding progressively across tiers 3–6.  This reflects the simplification of OBOFoundry around a centralised repository of resources that have achieved some maturity.

| OBO principle | First mandatory at tier | Notes |
|---|---|---|
| 1. Open | 3 (Reproducible) | Open availability is a precondition for machine reuse, not just transparency. |
| 2. Common Format | 3 (Reproducible) | Formal language/concrete syntax = the "standardised form" that defines this tier. |
| 3. URI/Identifier Space | 3 (Reproducible) | Stable, dereferenceable identifiers needed before reuse can be automated. |
| 6. Textual Definitions | 3–4 | Starts as good practice at Reproducible, expected by Community-shared. |
| 7. Relations (reuse existing) | 5 (Domain-contributed) | Interoperating with other domain resources presumes shared relation vocabularies. |
| 4. Versioning | 4 (Community-shared) | A community reusing a resource needs to track which version it reused. |
| 8. Documentation | 4 (Community-shared) | Supports review within the community of practice. |
| 9. Documented Plurality of Users | 5 (Domain-contributed) | Repository deposit implies (or aims at) users beyond the originating project. |
| 10. Commitment to Collaboration | 4–5 | Underpins both community sharing and domain contribution. |
| 5. Scope | 5 (Domain-contributed) | A repository entry needs a declared scope to be findable/comparable against peers. |
| 12. Naming Conventions | 5 (Domain-contributed) | Repository-level naming clashes only become a concern once deposited alongside peers. |
| 11. Locus of Authority | 6 (Domain-standardised) | Formal governance requires a named accountable party, not just a contact. |
| 13. Notification of Changes | 6 (Domain-standardised) | Becomes a governance obligation, not a courtesy. |
| 16. Maintenance | 6 (Domain-standardised) | Formal maintenance commitment is what separates a standard from a contribution. |
| 19. Term Stability | 6 (Domain-standardised) | Required once a resource is a recommended dependency for others. |
| 20. Responsiveness | 6 (Domain-standardised) | Formalised community-input channel, matching governance-framework expectations. |

OBO principles have no direct analogue at tiers 1–2 (pre-publication) or tiers 7–9 (cross-domain/operational/international),  those tiers are covered instead by the metadata/governance constraints in §4 and the technical federation stages in §5.

## 4. Metadata profile requirements by tier

Per the prompt, every tier requires a formal metadata profile, but a profile may be a **null profile** — adding no new elements, only constraining the values or governance of elements already present. "Constraint" below means an organisational/governance requirement on the publisher, not new descriptive content.

| Tier | New metadata elements | Constraint on publisher/organisation |
|---|---|---|
| 1 Documented | Title, description/abstract, author(s)/responsible party, creation date, method description | None |
| 2 Transparent | Access URL/landing page, licence or terms of access, format/media type, contact point | Publisher must be identifiable (name + contact) |
| 3 Reproducible | Serialisation format, namespace/URI pattern, version identifier + history link, machine-readable licence | Format must conform to a named open standard; identifiers must be dereferenceable |
| 4 Community-shared | Community/project identifier, review status, known-reusers list, change-notification channel | Responsible party reachable by the community; review process documented (informally) |
| 5 Domain-contributed | Scope statement, definition-coverage indicator, relation-reuse declaration, repository/deposit identifier | Naming conforms to repository conventions |
| 6 Domain-standardised | Governance-body identifier, endorsement/recommendation date, maintenance-policy reference, deprecation/succession policy | Publisher must be a recognised governance entity; documented deprecation policy required |
| 7 Cross-domain standard | Mappings/cross-references to other domain standards, adoption-registry entries, conformance test-suite reference | Ratified or recognised by more than one independent governance body (or demonstrated wide de facto adoption) |
| 8 Operationally adopted | SLA/service-level metadata, operational point of contact, policy-instrument reference, change-notice-period commitment | Operating organisation must be a mandated government/operational agency; availability commitments required |
| 9 Internationally standardised | Formal standard identifier (e.g. ISO number), procurement-reference clause, certification-scheme reference | Ratified by an accredited international standards body (ISO, IEC, W3C Recommendation, OGC Standard) |

## 5. Technical capability axis (secondary)

Retained from the source draft as an orthogonal axis: it describes *how* federation is achieved technically, not the business readiness the model above tracks. It's useful only insofar as it surfaces metadata needed for durable reuse — in particular, **actionable provenance**: metadata letting a client that has downloaded a resource detect upstream changes and push/pull updates, rather than holding a silently-decaying copy.

| Stage | Metadata implication for reuse                                                                                     |
|---|--------------------------------------------------------------------------------------------------------------------|
| 1. Curation | Provenance of curation decisions (who, when, why changed)                                                          |
| 2. Standardisation of content | Conformance/version identifiers referenceable by consumers                                                         |
| 3. Import/export of heterogeneous sources | Source-system identifier, extraction timestamp, transform/mapping reference                                        |
| 4. Interoperability of access | Stable access protocol/endpoint metadata (e.g. content negotiation, API descriptors)                               |
| 5. Federation on common technical platforms | Shared identifier resolution scheme across nodes                                                                   |
| 6. Federation of heterogeneous platforms | Cross-platform identifier/version reconciliation. schema and classification mappings. API adaptors where relevant. |
| 7. Visualisation tools for clients | Reusable libraries, embdeddable widgets,                                                                           |
| 8. Semantic alignment tools for client systems | Mapping/alignment metadata (e.g. SKOS mapping relations, confidence scores)                                        |
| 9. Federated AI agents | Machine-actionable capability/consent metadata (what an agent may read, cache, or write back)                      |

Tiers 3 and 6 are the load-bearing ones for the "download and stay in sync" scenario the prompt calls out: they are what let a consumer retain a *reference* to the source (not just a copy) and negotiate updates in either direction.

## 6. Open questions / next steps

- Consider the explicit inclusion of federated search and AI assistants.
- Confirm whether "Community-shared" (4) and "Domain-contributed" (5) should collapse into one tier for some domains, or whether the distinction (bounded project vs. open repository) is doing useful work.
- Decide whether FAIR terminology should replace the tier names outright, or remain an annotation as here.
- The technical axis (§5) needs its own maturity criteria per stage if it is ever promoted from "orthogonal note" to a tracked capability.
