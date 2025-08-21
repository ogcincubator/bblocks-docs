---
title: OGC Specification Building Blocks
permalink: /
---

<img src="assets/bblocks-qr.png" alt="QR Code" style="float:right; width: 200px; max-width: 33%"/>
This is the documentation for the OGC Building Blocks framework, a **specification component** packaging approach supporting:

- improved documentation of dependencies between specifications
- improved re-use of common elements across specifications
- validation of examples, test cases
- unit testing of validation
- semantic annotation
- validation of rules and constraints (using semantic annotations)
- testing of transformations and alignments to other specifications
- management of registers and Knowledge Graph views of ecosystems of specifications.

To provide suggestions for improvement on this documentation or ask questions please lodge issues [here](https://github.com/ogcincubator/bblocks-docs/issues) or submit pull requests.


## Overwhelmed?

<img src="assets/explorer_cave.png"  style="float:right; width: 200px; max-width: 33%"/>

It's natural to be overwhelmed by a new framework that addresses many complex aspects of a problem, in a new way. Powerful machines are scary.

However the Building Blocks can be explored incrementally, based on your starting knowledge and problems you wish to solve.

Explore these example [Use Cases](/usecases/usecases) or go straight to the [Tutorials](https://ogcincubator.github.io/bblocks-tutorial/) - which break these capabilities down step by step.

Building Blocks give you the tools to explore new territory, and improve your understanding and re-use of standards when solving your own problems.

<img src="assets/explorer_kit.png"  style="float:right; width: 200px; max-width: 33%"/>

## Overview 

This supports the FAIR principles for **specifications** - with every specification being a component that can be
re-used. For more discussion see [Design Principles](overview/principles)

Building Blocks can be used to **add documentation** to existing specification components, or to **design** and 
**assemble** reusable specification components cost-effectively using a test-driven approach. 

Building Blocks are *technology-agnostic* - i.e. may be various [types](overview/types) - however an emphasis is
support for semantically annotated JSON schemas for use in OGC API definitions.

Building Blocks can be organised into [registers](overview/registers) for convenience, each repository creating a local
register that can be integrated with other application domain registers.

Published OGC API specifications are, or will be, described in
the [register of OGC Specification Building blocks](https://opengeospatial.github.io/bblocks/register/). The framework
can be used for development of specifications or publication of specifications in your own application domain. The
framework supports transparent **federation of Building Block registers.**

The framework supports testing of examples, and validation using rules inherited from other Building Blocks that are
re-used (by aggregation or profiling) to create compatible specifications for specific applications.

For more details consider using the [Tutorials](https://ogcincubator.github.io/bblocks-tutorial/) - a step-wise introduction to various features and configuration details for Building Blocks.

