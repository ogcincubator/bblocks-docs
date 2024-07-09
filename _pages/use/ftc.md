---
title: Feature Type Catalogs
permalink: /use/ftc
---

The concept of a "Feature Type Catalog" (FTC) has been widely accepted as a concept, however interoperable implementations have been slow to emerge.

This may be because FTCs in practice need to be technically aligned with the underlying infrastructure publishing Features as data, and this in turn has two distinct aspects: persistence (how features are stored) and transfer (how they are exposed). Both of these aspects tend to be technology dependent, and hence expression of Feature Types is often tied to one or other of such aspects.

Building Blocks provide a new opportunity to publish Feature Types in a technology agnostic way, using multiple schemas mapped to common semantic models, supported by examples and validation.

Effectively this means the design pattern of a schema mapped to a Class with a Frame (a set of properties). Building Blocks can handle abstract 