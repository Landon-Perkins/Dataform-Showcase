# SQL Style Guide

This guide captures the coding standards used across the repository. The goal is not to enforce dogma, but to make the code easier to review, extend, and explain.

## Naming conventions

- use uppercase SQL keywords
- use lowercase snake_case for table names and columns
- use descriptive model names that reflect the business domain
- prefer clear, business-readable aliases over cryptic shorthand
- keep names consistent across source, staging, and reporting layers

## Structural conventions

- prefer CTEs for logical steps
- keep one clear final SELECT from a final CTE
- separate raw logic from derived logic
- avoid deep nested subqueries when a small intermediate CTE improves clarity
- make the business decision visible in the SQL

## Business-logic conventions

- comment non-obvious logic
- document edge cases and exceptions
- preserve the reason behind a transformation in code comments
- prefer readable CASE logic over clever abstractions

## Dataform conventions

- include a meaningful description for each model
- use tags that capture both the domain and refresh cadence
- keep dependency assumptions explicit
- use assertions where uniqueness, nullability, or row conditions are important

## Quality expectations

- readable code should still be understandable to a reviewer who did not author it
- transformations should be easy to explain in plain English
- business definitions should remain consistent from source to reporting
- code should signal intent, not just produce output

## Why this matters

Strong SQL style is not just cosmetic. It reduces review time, increases maintainability, and makes the repo easier to present to hiring teams and stakeholders.
