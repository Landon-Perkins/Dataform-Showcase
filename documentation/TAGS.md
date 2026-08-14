# Tagging Guide

Tags are used to communicate domain ownership, refresh cadence, and the operational intent of each model. They are intentionally lightweight, but they make the repo much easier to navigate and explain.

## Common tag categories

### Domain tags
- crm_netsuite
- pos
- sell_in
- reporting
- demo_staging
- money_manager

### Refresh tags
- daily
- hourly
- 2 hour
- p_bi 1 hour
- p_bi daily

### Operational tags
- snapshot
- assertion
- manual_assertion

## Example usage

A reporting model may carry tags such as:
- reporting
- sell_in
- p_bi 1 hour

An operational model may carry:
- snapshot
- data_warehouse

## Why tags matter

Good tags help a reviewer understand:
- what the model does
- which domain it belongs to
- how often it is refreshed
- whether it is operational or business-facing

This kind of metadata is not just housekeeping. It is part of the maintainability story.
