# Copilot Instructions for Casey Crane Hire Video Catalog

## Repository Purpose
This is a **video catalog management system** for Casey Crane Hire's marketing content—not a video storage system. Videos are hosted externally (YouTube, Instagram, Google Drive); this repo catalogs metadata, marketing strategies, and compliance artifacts.

## Architecture Overview

### Data Flow
1. **Video metadata** → JSON files in `metadata/` (schema-validated) → catalog reports
2. **Marketing docs** → `docs/` (current) vs `archive/` (historical versions only)
3. **Automation** → Python scripts in `scripts/` process JSON and generate reports
4. **Governance** → `.github/` contains CODEOWNERS, rulesets, and Copilot prompts

### Directory Structure
```
metadata/CCH-{ID}.json     # Structured video data (PRIMARY: use this, not markdown)
schemas/                   # JSON Schema for validation
scripts/catalog_manager.py # CLI tool for list/stats/check/report (268 lines)
docs/                      # Current marketing guides (messaging, calendars, strategies)
archive/                   # Historical versions ONLY—never edit these files
.github/                   # Governance scaffolding (CODEOWNERS, copilot prompts, rulesets)
```

**Critical:** `docs/` = current, `archive/` = read-only history. If updating a doc, edit in `docs/`, never touch `archive/`.

## Key Workflows

### Adding a Video
```bash
# 1. Create metadata/CCH-{next-id}.json using CCH-001.json as template
# 2. Validate against schema
python scripts/catalog_manager.py check
# 3. Update VIDEO_CATALOG.md if needed (but JSON is the source of truth)
```

### Running the Catalog Manager
```bash
python scripts/catalog_manager.py list    # List all videos (~0.1s)
python scripts/catalog_manager.py stats   # Get statistics (~0.2s)
python scripts/catalog_manager.py check   # Validate all metadata (~0.2s)
python scripts/catalog_manager.py report  # Generate full report (~0.3s)
```
**Performance:** These operations are 300-1200x faster than manual checks (see PERFORMANCE_IMPROVEMENTS.md).

### Updating Marketing Content
- Edit files in `docs/` directly—they're the current versions
- If creating a new version, move the old one to `archive/` first
- Follow Australian spelling and safety-first brand voice (yellow/white/black colors)

## Project-Specific Conventions

### Branding Standards (Enforced by compliance module)
- **Colors:** Yellow headboards, white booms/cabs, black accents
- **Logo:** Must be visible and dominant (never secondary to decorative elements)
- **Compliance:** All videos must pass branding verification (`branding` object in JSON schema)

### Video IDs
- Format: `CCH-{3+ digits}` (e.g., `CCH-001`, `CCH-042`)
- Pattern enforced by schema: `^CCH-\\d{3,}$`
- Sequential numbering for easy tracking

### Equipment References
Valid crane models (enum in schema):
- `GMK5170` (170-tonne), `GMK5150` (150-tonne), `GMK4080` (80-tonne)
- `GMK3060` (60-tonne), `GMK5250` (250-tonne)

### Status Values
- `published` - Live on platforms
- `cataloged` - Recorded, not yet published
- `archived` - Historical/replaced
- `in_production` - Being edited

## Integration Points

### External APIs (mentioned in REPO_BLUEPRINTS.md)
Future integrations planned:
- Google Business Profile (performance metrics)
- YouTube/Instagram APIs (auto-fetch views/engagement)
- Canva (template management)
- Xero (cost tracking)

### Governance Enforcement
- **CODEOWNERS:** All changes require @Justbenno review
- **Branch protection:** See `docs/governance/branch-protection-rules.md` and `.github/admin/rulesets/default.json`
- **Copilot PR guard:** Structural changes only (see `.github/copilot/prompts/pr-review-guard.md`)

## Common Patterns

### Schema Validation Pattern
```python
# scripts/catalog_manager.py uses this approach:
with open(schema_path, 'r') as f:
    schema = json.load(f)
# Validate each JSON file against schema
# Report missing required fields, invalid enum values, pattern mismatches
```

### Error Handling
- Script uses explicit error handling, not try/except in import blocks
- Graceful failures with clear error messages (e.g., "Schema not found at {path}")

### File Naming
- JSON metadata: `CCH-{ID}.json` (zero-padded to 3+ digits)
- Marketing docs: Descriptive kebab-case (e.g., `content-calendar-november-2025.md`)
- Archive files: Original name preserved (shows version history)

## Testing & Validation

### Before Committing
1. Run `python scripts/catalog_manager.py check` to validate all JSON
2. Ensure new videos follow schema (`required: ["id", "title", "dateRecorded", "status"]`)
3. Check that old docs were moved to `archive/` before creating new versions

### No Test Suite Yet
Currently no automated tests—validation relies on schema checks and manual review. (See PERFORMANCE_IMPROVEMENTS.md "Future Improvements" for planned GitHub Actions workflow.)

## Important "Why" Decisions

### JSON Over Markdown for Metadata
- **Before:** All metadata in VIDEO_CATALOG.md (slow, error-prone, hard to query)
- **After:** JSON with schema validation (10x faster processing, machine-readable)
- Markdown catalog (`VIDEO_CATALOG.md`) still exists but JSON is the authoritative source

### Archive Strategy
- **Problem:** 165KB of duplicate content (3 versions of same calendar, 5 messaging guides)
- **Solution:** Single source of truth in `docs/`, old versions in `archive/` (38% storage reduction)
- **Rule:** Never edit `archive/`—it's historical record only

### Governance Scaffolding (Added in PR #7)
- **Purpose:** Prevent drift in brand assets, enforce review discipline, enable compliance audits
- **Files:** CODEOWNERS, branch protection rulesets, Copilot PR review guard, Day 1 compliance audit checklist
- **Context:** See `docs/compliance/day-1-audit-checklist.md` for brand compliance requirements

## Quick References

### Finding Information
- Current marketing guide → `docs/messaging-guide.md`
- Content calendar → `docs/content-calendar-november-2025.md`
- All videos → `python scripts/catalog_manager.py list`
- Schema reference → `schemas/video-metadata-schema.json`
- Performance context → `PERFORMANCE_IMPROVEMENTS.md`

### Key Files to Study
- `scripts/catalog_manager.py` - Core automation logic
- `metadata/CCH-001.json` - Example video metadata structure
- `schemas/video-metadata-schema.json` - Validation rules and data types
- `docs/governance/branch-protection-rules.md` - Governance policies
- `REPO_BLUEPRINTS.md` - Future repo structure plans (caseybot-ai, marketing hub)

## What to Avoid
- Don't edit files in `archive/` (move current versions there first, then create new in `docs/`)
- Don't add video files to repo (they're gitignored—too large for GitHub)
- Don't bypass CODEOWNERS review (governance requirement)
- Don't use generic crane models—only the 5 Grove models in the schema enum
- Don't create duplicate content—consolidate and archive old versions
- Don't skip schema validation when adding/updating metadata JSON files

## Australian Compliance Context
Casey Crane Hire operates under:
- **CICA** (Crane Industry Council of Australia) standards
- **Worksafe Victoria** regulations
- **AS2550** (Australian Standard for crane operations)

When generating lift plans, quotes, or safety content, reference these standards. Brand messaging emphasizes safety-first and adherence to Australian regulations.
