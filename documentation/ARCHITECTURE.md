# Architecture Overview

This repository follows a practical three-layer architecture common in mature analytics engineering teams: source, staging, and reporting. The pattern is intentionally simple to explain, but it is robust enough to support quality control, business logic, and downstream BI consumption.

## Architectural pattern

### 1. Sources
Source models represent raw or lightly managed tables from upstream systems. Their role is to preserve the original data footprint and establish clear lineage back to the originating system.

Examples in this repository include product, POS, sell-in, and customer feeds.

### 2. Staging
Staging models normalize, deduplicate, align keys, and add business logic that remains close to the source context. This is where the team resolves naming differences, standardizes categories, and creates trusted intermediate tables.

This layer is the backbone of the repository. It is where most of the reusable business logic lives and where data quality checks become visible.

### 3. Reporting
Reporting models package the outputs most useful to BI tools, stakeholder analysis, and operational review. These models are designed to be consumable and explainable downstream.

The reporting layer in this repo includes Power BI-oriented models and CRM-focused outputs.

## Dependency rule

The repository follows a simple and important principle: downstream models depend on upstream models, not on peer models or reporting-layer tables. This keeps lineage readable and reduces accidental coupling.

## Domain organization

The showcase focuses on four business areas:

- Products
- POS and member sales exceptions
- Sell-in
- Customer

These domains are intentionally narrow enough to be readable, but broad enough to demonstrate real modeling judgment, data quality thinking, and analytical depth.

## Operational layer

Beyond the core source-staging-reporting flow, the repo includes operational models for assertions, snapshots, and recovery scenarios. This is a key signal of senior-level work: the repo is not just producing reports, it is protecting data quality and operational trust.

Examples include:
- assertion models
- snapshot tables
- ad hoc recovery logic
- source validation checks

## Design principles

- keep the architecture explainable at a glance
- separate source logic from business-ready logic
- build trusted intermediate tables before reporting
- maintain clear lineage from raw data to consumer-facing output
- use assertions and operational checks as first-class components

## Why this type of structure matters

This architecture is easy to explain in a hiring conversation and easy to review in code. A reviewer can follow the flow from raw source to trusted staging to reporting output without needing a long briefing.

That readability is part of the showcase value.
