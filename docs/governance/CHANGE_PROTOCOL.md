# PBOS Change Protocol

## Canonical Change Rule

PBOS locked architecture must not be changed implicitly through implementation.

## Required Sequence

1. Discover
2. Validate
3. Identify contradiction or gap
4. Propose change
5. Obtain explicit human authorization
6. Document decision
7. Version the canonical artifact
8. Implement
9. Validate again

## Artifact Classification

- canonical = approved source of truth
- operational = execution state
- experimental = hypothesis/test
- evidence = observed result

Evidence may trigger discovery but cannot silently become canonical policy.

## Repository Principle

Git history is implementation history. Canonical documents remain the readable source of truth.

