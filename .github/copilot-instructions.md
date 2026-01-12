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
- Use type hints for function parameters and return values (e.g., `def function(param: str) -> Dict[str, Any]:`)
- Use descriptive variable names in snake_case
- Include docstrings for classes and functions
- Use `pathlib.Path` for file path operations instead of `os.path`
- Handle errors explicitly with try/except blocks (avoid bare try/except in import blocks)

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
- Markdown documentation: Use UPPER_CASE with hyphens for existing docs (e.g., `VIDEO-MARKETING-STRATEGY.md`) or kebab-case for new documents
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
