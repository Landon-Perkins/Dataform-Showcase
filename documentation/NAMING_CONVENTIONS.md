# Naming Conventions

This repository uses a clear naming strategy to make lineage and responsibilities easy to understand at a glance.

## Naming principles

- source models are easy to recognize by their prefix and placement
- staging models communicate trust and standardization
- reporting models are clearly consumer-facing
- operational models are separated from core business logic

## Common prefixes

### Source models
- src- for source-level definitions
- raw source tables typically live under the source folders

### Staging models
- s_o_t- for source-of-truth and standardized staging logic
- names reflect the domain rather than the source system alone

### Reporting models
- p_bi- for Power BI or consumer-facing reporting models
- crm- or customer-related names for CRM-specific outputs

### Operational models
- asrt- for assertion models
- snapshot or snapshot-like naming conventions for historical tracking
- ad hoc or recovery naming for operational support logic

## Example pattern

- source product feed
- staging product source-of-truth table
- reporting product output for downstream use

This pattern is intentionally consistent across domains so reviewers can orient quickly.

## Column naming patterns

- use snake_case for column names
- use id for identifiers
- use date for time dimensions
- use is_ for boolean indicators
- keep names business-readable and not overly technical

## Why this matters

Good naming reduces ambiguity in interviews, code reviews, and stakeholder walkthroughs. It also makes the repository easier to maintain over time.
