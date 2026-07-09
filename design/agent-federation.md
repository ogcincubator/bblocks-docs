# AI Enabled Federation of Interoperability Resources

This document uses the ISO RM-ODP architectural viewpoints to separate concerns to simplify complex, inter-related issues 

## Enterprise viewpoint

### Emerging Architectural Context

Note - it is possible some coherent model will emerge from some group that addresses all these concerns.

It is increasingly obvious that AI agents will emerge as the primary tools for discovery and utilisation of interoperability resources.

The underlying logic is that LLMs, whilst powerful are limited by several factors:

- ability to access trusted context
- ability for humans to review quality of results for complex scenarios
- fundamental limits on complexity of problem vs complexity of training
- cost of accessing context (tokens)

Some of these can be mitigated by approaches such as RAG, and more granular agentic AI, where agents perform specific auditable actions.

The level of ambition to connect and exploit multiple information resources to create more sophisticated and timely results will just keep increasing as more power is available in infrastructure.

at time of writing, AI agents and machine access have just eclipsed human originated transactions in the wider Internet. This is likely to accelerate.

The underlying business context is one of **trust** - this applies to applications from research, to establishing reliable information supply chains, to answering specific questions.

Trust can be improved by including multiple verification cycles - and more context, at which point the **cost** becomes more limiting.

The only way to scale access to reliable context is to be able to integrate context from different sources, rather than trying to gather all content in one place.  Specialised agents may use local resources, but these will perform specific roles in a wider ecosystem.

To understand the full enterprise requirements it is necessary to understand the nature of information flows, and the actors involved.

### Actors (Stakeholders)

Actors can be categorised in two ways: via governance domains and behaviour.

Governance Domains:

- International technical standards - e.g. ISO, W3C, OGC, IETF
- International domain specific standards and data providers- GBIF, HL7 (health), CODATA/CDIF, etc
- Regional policy and shared infrastructure - e.g. EU Data Spaces, Copernicus
- National official infrastructure
- National research infrastructure
- Local operational infrastructure (e.g. state governments)
- Community of practice and networks (e.g. TERN)
- Joint project environments
- Local project context

Behavioural:

- End users
- Data product generation
- Data integration pathway deployers
- Data integration pathway designers
- Data integration infrastructure host processes
- Data integration infrastructure host designers
- Data access service providers
- Data archival roles
- Data producer
- Project and Scientific documentation

Note: Consider a RACI matrix view of actors and governance domains compared to information types.


## Information

Certain types of information are implication in managing complexity of context.  These represent trusted pathways to easily verifiable results.

- Controlled vocabularies with definitions
- Schemas (structure)
- Data models (relationships)
- Descriptions of data, with reference to how vocabularies, schemas and data models interact
- Descriptions of data access mechanisms
- Definitions of relationships
  - model-model
  - schema-model
  - term-term (crosswalk)
  - schema-schema (including syntax such as XML->JSON)\
- Published documentation

Whilst LLMs are good at predicting these, the amount of context needed to do it, and the discoverability of that context at run time means that both cost and quality issues escalate. 

What is required is a model showing how different agents (AI or human) interaction with such resources for a given exploitation (application) architecture and the role of infrastructure services in supporting this information.


### Use Case: AI agent supported calculation of an indicator

In this case, an indicator such as a Sustainable Development Goal is described by an organisation (such as a UN body) , and referenced as a requirement by a jurisdiction (such as a local government).

To calculate the indicator a set of data must be identified, this may be a mixture of data held globally, regionally, nationally or locally.  At each of these jurisdictional tiers data may be held in domain-specific infrastructures.

The tools to combine these datasets to calculate the indicator may be distributed across multiple tiers - typically there is a high level model for the indicator, and a series of information manipulation processes to convert available data into the forms needed.  This pattern applies to scientific workflows, monitoring and even general queries. With the advent of powerful AI agents accessing data the cost of ad-hoc queries will plummet, and the number will grow - it will be feasible to rapidly assess the potential of different data sources to solve problems, and to explore correlations and other questions that could be answered. 

Note: work is required to model the potential transactional load for different interaction paradigms, and to constantly monitor how these evolve with both agent power, agent accessibility and user expectations.

**Example: SDG 15.3.1 (Land Degradation Neutrality) computed for an Australian LGA**

A local government must report progress against SDG 15.3.1, "proportion of land that is degraded over total land area," as defined by UNCCD/UNSD. The global abstract model decomposes this into three sub-indicators — land cover change, land productivity dynamics, and soil organic carbon stock change — each with its own reference methodology.

An agent tasked with computing the indicator for the LGA would need to:

1. **Discover global baseline data via GEO catalogs.** Query the GEOSS Portal / GEO Knowledge Hub for global land cover (e.g. Copernicus Global Land Cover) and productivity time series that establish the baseline period required by the UNCCD methodology.
2. **Use OGC resources to learn access and structure.** Resolve the dataset's OGC API - Records entry to find its OGC API - Coverages or OGC API - EDR endpoint, and consult the relevant OGC SOSA/SSN Building Block to interpret in-situ soil observation payloads as `sosa:Observation` instances with correctly typed `sosa:hasResult` and `sosa:observedProperty`.
3. **Find domain-specific national data via TERN.** Query TERN's (Terrestrial Ecosystem Research Network) catalog for plot-based soil organic carbon and vegetation cover observations within the LGA — data too fine-grained to exist in any global catalog.
4. **Relate local data to the indicator via vocabularies and crosswalks.** Use TERN's controlled vocabulary services (and ARDC crosswalk registries) to map local land cover class codes and soil sampling methods to the IPCC/FAO LCCS classes and UNCCD-recognised SOC methods the global model expects.
5. **Run the local-to-global workflow.** Apply the UNCCD Good Practice Guidance calculation — implemented as a discrete, auditable workflow step — to convert TERN's plot observations plus the GEO baseline into a gridded degradation layer, then aggregate to the LGA boundary to produce the reported indicator value.

This chains a global abstract model (UNCCD/UNSD indicator definition) with jurisdiction-specific infrastructure (TERN), OGC-mediated discovery/access, and vocabulary crosswalks — each step independently auditable by a human reviewer, consistent with the trust argument in the Business section above.

## Computational

This architectural perspective needs to identify the types of computational nodes in an end-to-end application exploiting interoperability resources.  Dynamic discovery of integration opportunities and mechanisms needs to be matched with capability to deploy, test, refine and promote integration pathways in more persistent capabilities.

MCP servers with a range of "tools" is a near term way of creating scalable solutions, however the re-use of interoperability resources in these environments is not yet fully developed, and it is expected that rapid development is possible in this field.

Semantically explicit API and data description metadata is not widely available, and the governance mechanisms needed to standardise solutions are unclear.  These are concerns being addressed by the OGC, as a natural custodian for standards description spatio-temporal dimensions of data, representing the vast majority of data describing aspects of the "real world".  Some specialised application domains such as genetics and biochemistry will be able to use specialised simplifications with limited types of computational agents, however the general problem is one of describing both general and specific behaviours. 

## Engineering

It is assumed that interoperability resources are intended to support establishment of viable interactions between other components of an information system, and as such are not intended to be accessed dynamically in a high transactional load.

Conversely, its extremely important they can be found and applied effectively (i.e. FAIR) to both support data reuse and processing and to minimise the proliferation of incompatible data and systems. 

Security and access throttling mechanisms will be required. 

Federation of agents, from development and research context into infrastructure nodes managed by the end user community can mitigate load and access management requirements.

Interoperability resources are not data intensive, so many options emerge around, for example, proxying content to make it available in specific environments

## Technology

Managing cost means federation of agents - so that load is distributed across different nodes, and high demand applications can assume responsibility for appropriate access levels.

This implies a standardised mechanism to share content and behaviour across systems. Approaches like the Model Context Protocol may address some of these issues, however the gateway tiers that manage access will also require federation capabilities.

Commercial LLMs and AI tools will co-exist with open source and sovereign capabilities, so attention to interoperability and hand off between powerful tools solving problems once and cheaper tools providing visibility of these solutions may be the best option.