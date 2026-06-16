---
title: What is a Building Block?
permalink: /overview/whatis
---
An Building Block is a way of packaging a component of a **specification** that can be re-used in other specifications.

This packaging directly supports **reuse** (according to FAIR principles), following these [Design Principles](principles).

Note that one of the most common forms of re-use however is profiling a complete standard for application in a specific domain or jurisdiction. Buildings Blocks allow us to deal with complexity of real requirements by providing reusable implementation patterns and the tools to reuse them when combined and specialised.

This "symmetrical" model of combination works because Building Blocks "normalise" the packaging of different specification components into a common consistent model that supports reuse both by other specification developers, but human and AI agents needed to understand and validate compliance with these specifications.

For various reasons specifications have often made statements in text regarding how they relate to other specifications, and created implementation artefacts such as schemas that may not make these intentions explicit. OGC Building Blocks support **technology agnostic dependencies and relationships** - essentially forming the data management method for this apsect of OGC's knowledge graph (OGC RAINBOW).

The key focus is on quality control and trust. 
This is achieved through the ability to break complex problems into simpler parts, systematic documentation and testing with examples, and automated composition of these into the complex objects (comprehensive specifications) needed to support data exchange and analysis applications.  The ability to inherit validation rules makes the whole process quicker and more trustworthy, since subject experts can assess each part using examples.

The following diagram shows how Building Blocks form a value-added packaging option for such specification elements that can then be exploited as part of a comprehensive knowledge base to support discovery and re-use (FAIR principles).

[![Overview](https://lucid.app/publicSegments/view/266abfd3-ed51-43a8-a9b0-8e3251c28b54/image.png)](https://lucid.app/publicSegments/view/266abfd3-ed51-43a8-a9b0-8e3251c28b54/image.png)

Many OGC Standards contain reusable building blocks that can be used in other OGC Standards. The Standards themselves can also be structured with modular sets of requirements that collectively function as a reusable building block (see image bellow).

[![Usage](/assets/api-bblocks.png)](/assets/api-bblocks.png)

To facilitate the discovery of these building blocks by other Standards and applications, once they are identified their definition should be published in the [OGC Register](https://opengeospatial.github.io/bblocks/register/). Normative information about the OGC Standards building blocks can be found in the [Technical Committee Policies and Procedures](https://docs.ogc.org/pol/05-020r29/05-020r29.html#building-bloocks) 