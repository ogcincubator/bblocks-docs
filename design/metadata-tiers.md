# Tiered Metadata Model for Data and Model Reuse

An analysis of the "system context" for provision of metadata and supporting semantic assets to support the effective reuse of data and analytical capabilities. 

This document examines how functional and governance tiers may be considered and integrated into a heterogeneous but coherent "metadata ecosystem" model supported by interoperability standards.

This document uses the ISO RM-ODP architectural viewpoints to separate concerns to simplify complex, inter-related issues 

## Background

Metadata is not a "one size fits all" proposition. Nor is it neatly managed in a single place when "systems of systems" necessary to address the complexities of our natural and social environments, or activities happening at scale.

"Metadata" is a term that has different connotations for different system paradigms.  In domains dominated by human observation of phenomena, such as photographic or other scenes, biodiversity in the form of species occurrence, cultural heritage and health consultation this is contextual metadata captured manually or automatically at a fine-grained level of transactions.  In Earth Observation and spatio-temporal models of phenomena distribution this normally involves a processing chain where various models are chained to relate observable phenomena to a domain specific phenomenon of interest, such as converting spectral bands to vegetation models, or detecting statistical trends in large datasets of fine-grained observations and transactions.

With many systems and communities facing these needs over a long period of time a number of key patterns can re readily identified:

- There have been many developments of "metadata schema" attempting to standardise metadata models for specific domains
- These schemas are "of a time" reflecting dominant technology paradigms in the community
- All such schemas need augmentation with rules regarding the content
- Controlled vocabularies are widely used, but usually can only cover part of (i.e. a limited set of elements) of the metadata schema
- Common core and flexible extensions to vocabularies are a common but not ubiquitous pattern
- Metadata schema flexibility is variable and often ideosyncratic to the implementing flexibility
- To date no universally accepted, and perhaps no valid, solution for metadata profiling including vocabulary content rules and validation has been identified.
- To date no universally accepted, and perhaps no valid, solution for federated management of metadata using different technologies and profiles has been identified.

The evidence base for these assertions includes a range of communities where solutions, if they exist, would be expected to be common knowledge, or at least actively discussed. These communities include:

- CODATA/CDIF
- OGC
- ISO TC211
- W3C
- GEO (Group on Earth Observations)
- buildingSmart
- obofoundry
- RDA (Research Data Alliance)
- Ontoportal Federation
- EU Data Portal
- ESA EarthCode
- national Spatial Data Infrastructures
- national Data access portals
- ARDC (Australian Research Data Commons)
- International Data Spaces Consortium
- {{ TBD: identify others }}



## Enterprise viewpoint



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


## Information Viewpoint

Certain types of information are implicated in managing complexity of context.  These represent trusted pathways to easily verifiable results.

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

Each metadata environment present in the different governance tiers and implementing systems will have a subset of these, using a range of approaches with a variable amound of standardisation.

An initial challenge is to collect and compare different approaches and identify where challenges for each actor suggest standardisation activities have greatest value. 

It will not be possible to impose a common solution on all players for all aspects, however it may be possible to propagate common solutions via well known technologies by making them support the relationships between different solutions. 

**Example: SDG 15.3.1 (Land Degradation Neutrality) computed for an Australian LGA**

A local government must report progress against SDG 15.3.1, "proportion of land that is degraded over total land area," as defined by UNCCD/UNSD. The global abstract model decomposes this into three sub-indicators — land cover change, land productivity dynamics, and soil organic carbon stock change — each with its own reference methodology.

An agent tasked with computing the indicator for the LGA would need to:

1. **Identify and access the required computational models** - this may be defined by the task, or may require discovery. Discovery could use different resources such as policy and best practice guidance, metadata for similar products with detailed provenance, catalogs of workflows, scientific papers. The computational model will determine the type of data required.
1. **Discover global baseline data via GEO catalogs.** Query the GEOSS Portal / GEO Knowledge Hub for global land cover (e.g. Copernicus Global Land Cover) and productivity time series that establish the baseline period required by the UNCCD methodology.
3. **Find domain-specific regional or national data.** Query TERN's (Australia's Terrestrial Ecosystem Research Network) catalog for plot-based soil organic carbon and vegetation cover observations within the LGA — data too fine-grained to exist in any global catalog. (or for example the EU Data Portal in a European context)
2**Use OGC resources to learn access and structure.** Resolve the dataset's OGC API - Records entry to find its OGC API - Coverages or OGC API - EDR endpoint, and consult the relevant OGC SOSA/SSN Building Block to interpret in-situ soil observation payloads as `sosa:Observation` instances with correctly typed `sosa:hasResult` and `sosa:observedProperty`.
4. **Relate local data to the indicator via vocabularies and crosswalks.** Use TERN's controlled vocabulary services (and ARDC crosswalk registries) to map local land cover class codes and soil sampling methods to the IPCC/FAO LCCS classes and UNCCD-recognised SOC methods the global model expects.
5. **Run the local-to-global workflow.** Apply the UNCCD Good Practice Guidance calculation — implemented as a discrete, auditable workflow step — to convert TERN's plot observations plus the GEO baseline into a gridded degradation layer, then aggregate to the LGA boundary to produce the reported indicator value.

This chains a global abstract model (UNCCD/UNSD indicator definition) with jurisdiction-specific infrastructure (TERN), OGC-mediated discovery/access, and vocabulary crosswalks — each step independently auditable by a human reviewer, consistent with the trust argument in the Business section above.

## Computational

The computational viewpoint can be loosely mapped to the FAIR principles, in that each of these principles require interaction with different types of metadata.

### Findable

Find actions depend on the user and the context they have.  In general it is preferable to "go where the users are" rather than try to create a new channel of engagement. For example, users accessing a data catalog to find data relevant to a need may engage via functional activities including targetted search, AI agent suggestion, browsing collections (where the collection organisation needs to be meaningful from the user's perspective), or by following relationships - such as finding a related data set and discovering data products derived from it, or vice versa.

Such data catalogs may exist in any "governance tier" of the ecosystem, and users may seek data based on local relevance ("what data available locally can be used to measure changes in vegetation cover over multiple years,  or analytical value, such as "how do other cities in Europe measure impact of climate change on vegetation cover". 

Each of the actors identified above can be analysed to identify how they address these different modes, the technologies currently used

### Accessible

For each data source there are accessibility issues, including availability, licence, cost, effort required (see interoperability).

In current paradigms often it is necessary to access data to determine metadata such as the data model used, controlled vocabulries used, spatial or temporal extent, resolution, quality.  

Accessibility needs to be correlated with engineering requirements regarding size, time, frequency of update, frequency of access etc.

### Interoperable

Interoperability can be used on many distinct aspects of the data flow transactions required. Use of standards reduces cost of interoperability. Where standard software libraries are embedded in application tools the ability to handle different aspects can be cost effectively shared. Service implementations supporting generic interaction models (APIs) need to be supported by transparent and clear models of the data and processing they support - this "binding" of API, data model and content rules is poorly standardised at present, however the emergence of semantically annotated schemas (c.f. OGC Building Blocks) allows for more explicit profiling of computational and data elements, and the binding relationships between specific data and generic API behaviours.

### Reusable




## Engineering

The general issue w.r.t. engineering in a tiered metadata system is that some resources have a greater relevance than others, and the more generalised layers could potentially be over-burdened, and act as a single point of failure.  This failure may be physical transaction limits, economic sustainability, governance continuity, malicious denial etc. 

Systems relying on external resources are also vulnerable to network failure, resources and enhanced security risks. 

Consequently, active caching and local, potentially off-line, resolution of shared resources needs to be designed into every level. Adoption of a common meta-model for sharing resources across governance and implementation tiers can reduce the burden of design and implementation of this capability.




## Technology

Any general approach needs to be technology neutral, since every stakeholder in this tiered paradigm will have its existing capabilities and there will be no general system evolution pathway that can or should be forced on them.

Furthermore, each participating capability will likely be optimised for the particular application domain, typically by simplifying certain aspects where very simple solutions are adequate and focusing on the areas where consensus within its community is feasible and adds value.

Requirements for open source implementations and sovereign capabilities will exist for some stakeholders, and will inevitably need to be considered in conjunction with commercial approaches that have developed massively scalable solutions. 

The impact of available tools in the hands of developers building information processing chains and exploiting the results cannot be underestimated - available tools support both constructive patterns and behavioural "antipatterns" that shift problems to other stakeholders.

Any metadata ecosystem needs to focus on the toolchain accessibility and ease of use to achieve effective re-use of the complex information required to genuinely support data reuse. 