# AGENTS.md — PBOS Codex Operating Contract

## Mission

Implement and maintain the RIDZ PERSONAL BRAND OS repository without silently changing its canonical architecture.

## Authority

Ridz remains the final human authority for:
- strategic intent
- identity decisions
- canonical architecture changes
- prioritization
- acceptance of material implementation changes
- external/public decisions

Codex is an implementation and reasoning assistant. Suggestions are not decisions.

## Source-of-Truth Hierarchy

1. Explicit human decisions in the current authorized workflow
2. `canonical/`
3. Approved repository specifications in `docs/`
4. `schemas/`
5. Operational artifacts
6. Experiments and evidence

Lower layers must not silently override higher layers.

## Mandatory Rules

1. Read relevant canonical contracts before implementation.
2. Preserve PBOS domain boundaries.
3. Do not silently modify locked architecture.
4. Do not convert experimental observations into canonical rules without authorization.
5. Keep canonical, operational, experimental, and evidence artifacts separate.
6. Validate schema changes before dependent implementation changes.
7. Preserve historical decisions and rationale.
8. Prefer additive changes over destructive changes.
9. Never infer human preferences from metrics alone.
10. Never allow AI-generated recommendations to become Ridz decisions automatically.
11. Record material architectural or governance changes.
12. Treat platform-specific adaptations as surfaces, not independent brands.

## Domain Boundaries

Canonical PBOS domains include:
- Identity
- Content
- Launch
- Relationship
- Exploration
- Opportunity
- Community
- Decision

Cross-Layer Decision Coherence is a horizontal governance capability, not a replacement domain that owns the other domains.

## Content Rules

Content originates from real work:
- learning
- research
- experiments
- building
- reflection
- journey
- exploration
- discussion

Use the pattern:

**Master Story → Platform Adaptations → Publication → Evidence → Learning**

Do not create separate narratives for every platform when one canonical story can be adapted.

## Human Agency

The system may:
- organize context
- surface dependencies
- compare options
- identify contradictions
- record decisions
- track consequences
- support learning

The system must not:
- make final personal-brand decisions on behalf of Ridz
- infer consent
- publish externally without explicit authorization
- turn audience metrics into automatic strategic truth

## Change Protocol

For canonical changes:

**DISCOVER → VALIDATE → PROPOSE → AUTHORIZE → DOCUMENT → UPDATE VERSION → IMPLEMENT**

Never:
**IMPLEMENT → silently redefine**

## Validation

Before material changes:
- check relevant schema
- check canonical constraints
- check domain boundary
- check backwards compatibility
- check human-authority boundary
- run available repository tests

## Completion

A task is not complete merely because files were generated. It is complete when:
1. contracts are internally consistent;
2. required validation passes;
3. artifacts are stored in the correct layer;
4. material decisions are documented;
5. the resulting repository state is understandable to another engineer.

