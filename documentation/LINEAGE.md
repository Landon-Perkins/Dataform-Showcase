# Lineage Overview

This repository demonstrates lineage in the most useful way for analytics engineering: the path from source to stage to reporting is visible and explainable.

## Core lineage pattern

The common flow is:

1. source tables ingest raw or lightly shaped records
2. staging models standardize, deduplicate, and align business logic
3. reporting models package curated outputs for BI and downstream analysis

## Showcase lineage examples

### Products
- source product data feeds the product staging layer
- product staging feeds rebate and product reporting outputs

### POS
- source POS and exception feeds feed the POS staging layer
- POS staging feeds the reporting model used for member sales and data-quality exceptions

### Sell-in
- source sell-in feeds feed the standardized sell-in staging layer
- sell-in staging feeds the reporting model used by BI consumers

### Customer
- customer staging models feed CRM and member-related reporting outputs

## Why lineage matters

Strong lineage is one of the clearest signs of mature analytics engineering. It shows that the author understands:
- data ownership
- transformation boundaries
- dependency management
- how to debug issues without guessing

## Operational lineage

The operational models in the repo follow the same idea. They are not disconnected helpers; they are part of the trust model for the system.

Examples:
- snapshots preserve historical context
- assertions verify assumptions and quality thresholds
- operational models support recovery and drift analysis

This makes the repo feel like a real data product rather than a collection of disconnected SQL files.
