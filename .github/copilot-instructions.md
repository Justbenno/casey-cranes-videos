# Casey Crane Hire Video Catalog - Copilot Instructions

## Project Overview

This repository is a comprehensive catalog and documentation system for Casey Crane Hire's video marketing content. It serves as a centralized system for organizing, tracking, and managing all video content including marketing videos for social media (Instagram, Facebook, Meta), Google Ads video content, equipment showcase videos, project documentation videos, and training/safety videos.

**Important**: This repository does NOT store actual video files (due to GitHub file size limitations). Instead, it catalogs videos stored on YouTube, Instagram, Facebook, Google Drive, and other cloud storage platforms.

## Purpose and Business Context

Casey Crane Hire is a crane hire company featuring **Grove all-terrain cranes** with specific branding requirements. This catalog helps track competitive positioning against competitors like Membreys Cranes and Transport, P&D Rigging, MCG Cranes, JYC, Metcalf, Gravity Rigging, Paramount Cranes, Sventec Cranes, Browns Cranes, Mackay United, KTB Cranes, Cranetec, Komp Cranes, Cardinias Cranes, and Crane Tec.

## Technology Stack

- **Primary Language**: Python 3
- **Data Formats**: JSON (for metadata), Markdown (for documentation)
- **Schemas**: JSON Schema (draft-07) for validation
- **Version Control**: Git/GitHub
- **Automation**: Python scripts for catalog management

## Repository Structure

```
casey-cranes-videos/
├── metadata/           # Video metadata files (JSON format following schema)
├── schemas/            # JSON schemas for data validation
├── scripts/            # Python automation scripts for catalog management
├── templates/          # Templates for video documentation
├── docs/               # Marketing guides and strategies
├── content/            # Marketing content
├── images/             # Image assets
├── archive/            # Historical/old versions of documents
└── .github/            # GitHub configuration, workflows, and Copilot instructions
```

## Coding Standards

### Python

- Use Python 3.x syntax
- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
  - Example: `def function(param: str) -> dict[str, Any]:` (Python 3.9+)
  - Or with imports: `from typing import Dict` then `def function(param: str) -> Dict[str, Any]:`
- Use descriptive variable names in snake_case
- Include docstrings for classes and functions
- Use `pathlib.Path` for file path operations instead of `os.path`
- Handle errors explicitly with try/except blocks
  - Avoid: `try: import module except: pass` (silently ignores errors)
  - Prefer: `try: import module except ImportError as e: logger.warning(f"Optional module not available: {e}")`

### JSON

- Follow the JSON Schema defined in `schemas/video-metadata-schema.json`
- Use 2-space indentation for JSON files
- Ensure all required fields are present: `id`, `title`, `dateRecorded`, `status`
- Video IDs must follow pattern: `CCH-` followed by 3 or more digits (e.g., `CCH-001`, `CCH-002`, `CCH-100`)
- Date formats must be ISO 8601: `YYYY-MM-DD`
- Duration format: `MM:SS` or `HH:MM:SS`

### Markdown

- Use proper heading hierarchy (single # for title, ## for sections)
- Include blank lines between sections for readability
- Use bullet points for lists
- Include links to external resources where videos are hosted
- Follow existing documentation style in the repository

## Equipment and Branding Standards

### Casey Crane Hire Fleet

All videos must feature Casey Crane Hire's fleet of Grove all-terrain cranes:
- **GMK5170** - 170-tonne capacity
- **GMK5150** - 150-tonne capacity
- **GMK4080** - 80-tonne capacity
- **GMK3060** - 60-tonne capacity
- **GMK5250** - 250-tonne capacity

### Branding Requirements

All equipment in videos **must** display:
- **White booms and cabs**
- **Yellow headboards**
- **Casey Crane Hire logo prominently displayed**

When validating or documenting videos, always verify these branding elements using the `branding` object in metadata:
```json
"branding": {
  "whiteBoomsVerified": true,
  "yellowHeadboardsVerified": true,
  "logoVisible": true,
  "qualityCheckCompleted": true
}
```

## Video Categories

Use only these predefined video types in metadata:
- `marketing` - General marketing content
- `equipment_showcase` - Showcasing specific crane capabilities
- `project_documentation` - Documenting project work
- `training` - Training materials
- `safety` - Safety procedures and guidelines
- `social_media` - Content optimized for social platforms

## Automation Scripts Usage

### catalog_manager.py

The primary tool for managing the video catalog. Usage examples:

```bash
# List all videos
python scripts/catalog_manager.py list

# Show statistics
python scripts/catalog_manager.py stats

# Generate full report
python scripts/catalog_manager.py report

# Check completeness
python scripts/catalog_manager.py check
```

When working with the catalog, always use the automation script rather than manually editing multiple files.

## Adding New Videos

1. Create a new JSON file in `metadata/` using the next sequential ID (e.g., `CCH-002.json`)
2. Follow the schema defined in `schemas/video-metadata-schema.json`
3. Include all required fields: `id`, `title`, `dateRecorded`, `status`
4. Add platform-specific URLs where the video is published
5. Update `VIDEO_CATALOG.md` if needed
6. Use the template in `templates/video-entry-template.md` for markdown format

## File Naming Conventions

- Video metadata JSON files: `CCH-###.json` where ### is 3+ digits (e.g., `CCH-001.json`, `CCH-002.json`, `CCH-100.json`)
- Markdown documentation: The repository uses mixed naming conventions
  - Major/strategic docs: UPPER_CASE with hyphens or underscores (e.g., `VIDEO-MARKETING-STRATEGY.md`, `MARKETING_PACKAGE_SUMMARY.md`)
  - General docs: kebab-case (e.g., `competitor-analysis.md`, `blog-post-benefits.md`)
  - When creating new docs, match the pattern of similar existing documents
- Python scripts: Use snake_case (e.g., `catalog_manager.py`)
- Images: Descriptive names with hyphens (e.g., `gmk5170-white-boom.jpg`)

## Testing and Validation

- Always validate JSON files against the schema in `schemas/video-metadata-schema.json`
- Test Python scripts before committing changes
- Verify that metadata follows the required patterns (video IDs, dates, durations)
- Check that all required fields are present
- Ensure equipment names match the approved fleet list

## Documentation Requirements

- Update `VIDEO_CATALOG.md` when adding new videos
- Keep `README.md` current with any structural changes
- Document any new automation scripts in `scripts/README.md`
- Include clear examples and usage instructions
- Use Australian English spelling and conventions

## Weekly Maintenance

Review and update video performance metrics weekly using the automation scripts. Track:
- Views, likes, shares, comments
- Engagement rates
- Platform-specific performance
- Last updated timestamps

## Safety and Compliance

When documenting videos related to crane operations:
- Reference Australian standards (CICA, Worksafe Victoria, AS2550) where applicable
- Ensure safety-related content is accurate and compliant
- Maintain professional and safety-first messaging
- Follow industry best practices

## Restrictions

- **Never commit actual video files** to this repository (GitHub file size limitations)
- **Never commit secrets or credentials** - use GitHub Secrets for any API keys
- **Do not modify existing video IDs** - they are permanent identifiers
- **Do not remove or modify branding verification fields** without proper justification
- **Maintain backward compatibility** with existing metadata schema

## Governance and Structural Changes

For changes to repository scaffolding (`.github/**`, documentation, policies):
- Follow the PR review guard principles in `.github/copilot/prompts/pr-review-guard.md`
- Ensure changes are limited to structural/documentation files
- Link PRs to issues with clear rationale
- Maintain traceability and minimal surface area changes
- Escalate operational logic changes to @Justbenno

## Maintained By

Benjamin Ashdown (@Justbenno)  
Casey Crane Hire

## Additional Resources

- Video Marketing Strategy: `docs/VIDEO-MARKETING-STRATEGY.md`
- Competitor Analysis: `docs/competitor-analysis.md`
- Repository Blueprints: `REPO_BLUEPRINTS.md`
- Performance Improvements: `PERFORMANCE_IMPROVEMENTS.md`
# GitHub Copilot Instructions for Casey Cranes Video Catalog

## Repository Purpose

This repository is a **catalog and documentation system** for Casey Crane Hire's video marketing content. It does NOT store actual video files—only metadata, documentation, and management tools for videos hosted on YouTube, Instagram, Facebook, and other platforms.

## Key Repository Conventions

### 1. Repository Structure Philosophy

- `metadata/` - Video metadata in JSON format (source of truth for video data)
- `schemas/` - JSON schemas for validation
- `scripts/` - Python automation tools for catalog management
- `docs/` - Current marketing guides and strategies
- `archive/` - Historical versions (read-only, never edit)
- `templates/` - Templates for new content
- `content/` - Marketing content
- `images/` - Image assets

**Important**: Always keep `docs/` for current files and `archive/` for historical versions. Never edit files in `archive/`.

### 2. Technology Stack

- **Python 3** for automation scripts
- **JSON** for structured video metadata
- **Markdown** for documentation
- **JSON Schema** for data validation
- No build system, no dependencies beyond Python standard library

### 3. Video ID Conventions

- Format: `CCH-###` (e.g., `CCH-001`, `CCH-002`)
- Always use zero-padded 3+ digit numbers
- IDs must be sequential and unique
- Each video has both a JSON file (`CCH-###.json`) and optionally a detailed markdown file (`CCH-###-name.md`) in `metadata/`

### 4. Data Format Standards

#### JSON Metadata
- Follow `schemas/video-metadata-schema.json` strictly
- Required fields: `id`, `title`, `dateRecorded`, `status`
- Optional but commonly used fields: `description`, `duration`, `equipment`, `videoType`, `platforms`, `tags`, `technical`, `storage`, `performance`, `branding`, `notes`
- Date format: `YYYY-MM-DD` for dates (e.g., `2025-12-20`), ISO 8601 for date-time (e.g., `2025-12-20T10:00:00Z`)
- Status values: `published`, `cataloged`, `archived`, `in_production`
- Duration format: `MM:SS` or `HH:MM:SS`

#### Markdown Documentation
- Use clear headings and consistent structure
- Include links to actual video hosting platforms
- Follow existing template patterns in `templates/`

### 5. Crane Equipment Branding Standards

Casey Crane Hire's fleet consists of Grove all-terrain cranes:
- **GMK5170** (170-tonne)
- **GMK5150** (150-tonne)
- **GMK4080** (80-tonne)
- **GMK3060** (60-tonne)
- **GMK5250** (250-tonne)

**Visual Branding Requirements**:
- White booms and cabs
- Yellow headboards
- Casey Crane Hire logo prominently displayed

When documenting videos, always use exact crane model names and ensure branding standards are noted.

### 6. Automation Scripts

**Environment**: Python 3 (any 3.x version; tested with Python 3.12). No external dependencies — uses only the Python standard library. No `pip install` or virtual environment setup is needed.

**Important**: All scripts must be run from the **repository root** directory.

The primary tool is `scripts/catalog_manager.py`:
```bash
python scripts/catalog_manager.py list    # List all videos
python scripts/catalog_manager.py stats   # Show statistics
python scripts/catalog_manager.py report  # Generate full report
python scripts/catalog_manager.py check   # Validate metadata (use this to verify changes)
```

**Validation workflow** — always run after making changes to metadata:
```bash
python scripts/catalog_manager.py check
```
A clean run shows `Total Issues: 0`. Any issues are printed per-video.

**No CI/CD pipelines exist** in this repository (no `.github/workflows/`). Validation is entirely manual via the above command.

**When modifying scripts**:
- Maintain Python 3 compatibility
- Use only standard library (no external dependencies)
- Keep the command-line interface consistent
- Add validation and error handling
- Update script documentation in `scripts/README.md`

### 7. Video Catalog Management Best Practices

#### Adding New Videos
1. Create JSON file with next sequential ID in `metadata/`
2. Validate against schema
3. Update `VIDEO_CATALOG.md` if needed
4. Run `python scripts/catalog_manager.py check` to validate

#### Updating Videos
1. Edit the JSON file in `metadata/`
2. Update `lastModified` timestamp
3. Keep JSON and markdown descriptions in sync
4. Validate changes with automation script

#### Archiving Videos
- Change `status` field to `"archived"` in JSON
- Don't delete files; preserve history
- Move old documentation versions to `archive/` if creating new versions

### 8. Documentation Standards

- Use clear, concise language
- Include examples and code snippets where helpful
- Keep README files updated in each directory
- Document the "why" not just the "what"
- Prefer markdown tables for structured data presentation

### 9. Content and Marketing Guidelines

- Follow guidelines in `docs/messaging-guide.md` for content creation
- Respect competitive awareness (don't name competitors in video content)
- Maintain professional tone aligned with Casey Crane Hire brand
- Prioritize safety, reliability, and expertise in messaging

### 10. Git and Version Control

- Make small, focused commits
- Use descriptive commit messages
- Don't commit large binary files (videos, images over 1MB)
- Use `.gitignore` to exclude temporary files and build artifacts
- When in doubt, create a feature branch for experimentation

## Tasks Copilot Should Handle

✅ **Appropriate for Copilot**:
- Creating and updating video metadata JSON files
- Generating reports and statistics from catalog data
- Writing or updating documentation
- Creating templates for new content types
- Refactoring Python scripts for better maintainability
- Adding validation logic to ensure data quality
- Updating markdown catalogs and guides
- Creating GitHub issue/PR templates

❌ **Requires Human Review**:
- Changes to JSON schema definitions (affects all metadata)
- Modifications to core automation script logic
- Branding or marketing strategy decisions
- Competitive analysis and positioning
- Video content creation decisions
- Major structural repository changes

## Code Quality Expectations

- **Python**: Follow PEP 8 style guidelines, use type hints where beneficial
- **JSON**: Valid JSON syntax, follow schema, use consistent formatting (2-space indent)
- **Markdown**: Follow GitHub Flavored Markdown, use consistent heading levels
- **Testing**: Validate JSON against schema before committing
- **Documentation**: Keep inline comments minimal; let code be self-documenting

## Security and Privacy

- Never commit API keys, credentials, or secrets
- Don't include sensitive customer information in metadata
- Video URLs should be public-facing links only
- Respect copyright and licensing for all content

## Key Files Reference

| Path | Purpose |
|------|---------|
| `README.md` | Project overview and usage |
| `VIDEO_CATALOG.md` | Master catalog of all videos |
| `schemas/video-metadata-schema.json` | JSON schema for metadata validation |
| `scripts/catalog_manager.py` | Primary automation tool |
| `scripts/README.md` | Script usage documentation |
| `metadata/CCH-001.json` | Example video metadata file |
| `metadata/CCH-001-Cranepics.md` | Example detailed markdown entry |
| `templates/` | Templates for new content |
| `docs/` | Current marketing guides |
| `archive/` | Historical versions (read-only) |
| `.github/copilot-instructions.md` | This file |
| `.github/CODEOWNERS` | Code ownership rules |

## Contact

Repository maintained by Benjamin Ashdown (@Justbenno)
All structural changes require code owner approval per CODEOWNERS file.
