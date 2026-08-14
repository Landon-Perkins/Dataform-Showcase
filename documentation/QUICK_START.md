# Quick Start Guide

This repository is designed to be easy to understand quickly. The goal is to make the business story and the technical structure visible without requiring a long briefing.

## What you are looking at

The project follows a three-layer model:

1. Source layer
   - raw or lightly shaped feeds
2. Staging layer
   - normalized, deduplicated, trusted intermediate data
3. Reporting layer
   - BI-ready or stakeholder-facing outputs

## The four primary domains

### Products
The product domain focuses on master data quality, product keys, and product hierarchy logic. It is a good example of how a staging layer resolves duplicates and business naming issues before a reporting layer consumes it.

### POS
The POS domain covers transaction-level sales activity and exception logic. This is a strong demonstration of operational data quality monitoring, product matching, and exception-driven analytics.

### Sell-in
The sell-in domain is centered on channel and vendor performance. It shows how sales activity is aligned to categories, vendors, and member contexts for downstream reporting.

### Customer
The customer domain demonstrates CRM and member-centric models. It is valuable for illustrating how customer-level logic is combined with subscription and service attributes.

## Recommended review order

If you want to quickly understand the repo, review these in order:

1. [README.md](../README.md)
2. [ARCHITECTURE.md](ARCHITECTURE.md)
3. [LINEAGE.md](LINEAGE.md)
4. one staging model
5. one reporting model

## Good files to inspect first

- [definitions/staging/source_of_truth/s_o_t-products.sqlx](../definitions/staging/source_of_truth/s_o_t-products.sqlx)
- [definitions/staging/source_of_truth/s_o_t-pos_incl_excep.sqlx](../definitions/staging/source_of_truth/s_o_t-pos_incl_excep.sqlx)
- [definitions/staging/source_of_truth/s_o_t-sell_in.sqlx](../definitions/staging/source_of_truth/s_o_t-sell_in.sqlx)
- [definitions/reporting/power_bi/p_bi-pos_incl_excep.sqlx](../definitions/reporting/power_bi/p_bi-pos_incl_excep.sqlx)
- [definitions/reporting/crm/p_bi-customer.sqlx](../definitions/reporting/crm/p_bi-customer.sqlx)

## What to look for

- how source logic is separated from reporting logic
- how business rules are documented inline
- how uniqueness and data quality checks are handled
- how naming and tags communicate domain intent

## Why this matters

This repo is meant to show that the author can reason in layers, build trusted intermediate data, and create outputs that are explainable to both technical and business stakeholders.
