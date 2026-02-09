# Architecture for maximising impact of OGC

## Business

Goals:

- increase the visible impact of OGC standards to solve problems
- increase the value of participation as OGC members

Assumptions

- The business context is not static
- AI is likely to raise expectations that information can be more efficiently accessed
- IPT demands increase as AI exploitation becomes more prevalent
- A significant refocus of direction may require process and policy evolution, and clear gains must be established.


Questions

- how to engage new members without key contributers feeling sidelined or threatened?
- what are the measurable improvements the market seeks or would recognise
- Do we analyse and build then show - or sell a concept and try to guess the application 

## Information

There is no expectation that OGC can or should maintain a monopoly on any content. 

There are cases (like schema.org) where large organisations publish information in a form that has some value to users, and provides significant value to the organisation.
These information sources **are not designed to support other peoples business problems** - for example will never allow AI assisted integration of environmental data to identify risks or trends.

Current (typical) situation:

- No **accepted** interoperable model of Feature Types (or federated catalogues) 
- No **common** model of n-dimensional data semantics (what do dimensions mean) - except for spectral bands in STAC, for which 3 alternative models provided (!)
- No systematic provenance for data outputs
- Heterogeneous semi-structured (at best)  documentation for data and processing
- Ad hoc approaches to data quality
- Explosion in capability to derive new data from ML - and potentially AI orchestrated - processing without skills, tools or governance

The opportunity is providing several extra pieces of information on top of "basic APIs":

- unambiguous identification of information elements (mapped to URIs)
- linked to richer semantic descriptions
- links to knowledge graphs holding additional information and relationships
- clear dependencies and identification of common patterns across a range of APIS

These opportunities have known technical solutions but require:

- acceptance and re-use of high fidelity reusable components
- policy and procedure support to avoid proliferation of 

One key issue to note is that standardised information models with sufficient capability to solve non-trivial problems have a medium level of complexity. 
Development of software libraries to exploit them reduces the cognitive burden and risk for participants.

Registers of:

- Feature Types
- Implementation support for Features types (libraries, transformers, validators)
- Registers of profiles
- Controlled vocabularies (must be federated - goal is to push OGC resources into third-party vocabularies)

 
## Computational

APIs define boundaries of computational elements.

- profiling of APIs ubiquitous but currently ad-hoc
- binding API + data model + vocabularies + organisational access a bare minimum **always needed** - **not currently tool supported**

Questions

- what is the real friction in an end to end system
- what are the engineering limitations (performance by better design rather that brute for scaling)

- 

## Engineering

- How to stop OGC being hit in run-time - its should be point of truth, not a run-time dependency
- in the run time environment needed to solve problems, which transactions have most value ( cost * frequency)
- Cost as data
- cost as time
- cost of reliability
- cost of establishing reuse - evaluation, negotiation


## Technology

The technical viewpoint is relatively straightforward - impact via open source libraries, but potential for members to develop interoperable solutions with added value.

The wrinkle is version compatibility 

- version agnostic solutions
- version translation/profiles?

