#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "docs/implementation/PBOS_REPOSITORY_CODEX_IMPLEMENTATION_SPECIFICATION_v0.1.md",
    "docs/governance/CHANGE_PROTOCOL.md",
    "docs/governance/LOCKED_ARCHITECTURE.md",
    "docs/governance/CANONICAL_PROVENANCE_MANIFEST.yaml",
    "canonical/identity/identity.yaml",
    "canonical/architecture/domain-boundaries.yaml",
    "canonical/governance/human-authority.yaml",
    "canonical/content/content-principles.md",
    "schemas/identity/account.schema.json",
    "schemas/content/content-item.schema.json",
    "schemas/story/master-story.schema.json",
    "schemas/platform/platform-adaptation.schema.json",
    "schemas/publication/publication.schema.json",
    "schemas/relationship/relationship.schema.json",
    "schemas/exploration/exploration-item.schema.json",
    "schemas/opportunity/opportunity.schema.json",
    "schemas/community/community-item.schema.json",
    "schemas/decision/decision.schema.json",
    "schemas/evidence/evidence.schema.json",
]

def fail(message):
    print("FAIL:", message)
    sys.exit(1)

for rel in REQUIRED_FILES:
    if not (ROOT / rel).is_file():
        fail("missing required file: " + rel)

identity = (ROOT / "canonical/identity/identity.yaml").read_text()
for marker in [
    'public_brand: "Ridz Builds"',
    'core_identity: "AI Builder in Progress"',
    'primary_tagline: "Learning AI by Building."',
    'community_invitation: "Build With Ridz"',
]:
    if marker not in identity:
        fail("canonical identity marker missing: " + marker)

boundaries = (ROOT / "canonical/architecture/domain-boundaries.yaml").read_text()
for marker in [
    "identity:", "content:", "launch:", "relationship:",
    "exploration:", "opportunity:", "community:", "decision:"
]:
    if marker not in boundaries:
        fail("domain boundary missing: " + marker)

if 'type: "horizontal_governance_capability"' not in boundaries:
    fail("cross-layer capability is not explicitly horizontal")

authority = (ROOT / "canonical/governance/human-authority.yaml").read_text()
for marker in [
    'owner: "Ridz"',
    "final personal-brand decisions",
    "unauthorized external publication",
]:
    if marker not in authority:
        fail("human authority marker missing: " + marker)

agents = (ROOT / "AGENTS.md").read_text()
for marker in [
    "Ridz remains the final human authority",
    "Do not silently modify locked architecture",
    "DISCOVER → VALIDATE → PROPOSE → AUTHORIZE → DOCUMENT → UPDATE VERSION → IMPLEMENT",
]:
    if marker not in agents:
        fail("AGENTS governance marker missing: " + marker)

schemas = list((ROOT / "schemas").rglob("*.schema.json"))
if len(schemas) < 11:
    fail("expected at least 11 schemas, found " + str(len(schemas)))

for path in schemas:
    try:
        json.loads(path.read_text())
    except Exception as exc:
        fail("invalid JSON schema: " + str(path) + ": " + str(exc))

print("PASS: required repository contracts")
print("PASS: canonical identity")
print("PASS: domain boundaries")
print("PASS: human authority")
print("PASS: Codex governance")
print("PASS: provenance manifest")
print("PASS: " + str(len(schemas)) + " JSON schemas parse successfully")
print("PBOS_REPOSITORY_V0_1_VALIDATION=PASS")
