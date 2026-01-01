# Copilot Instructions for Casey Cranes Video Catalog

## Project Overview
This is a video catalog management system for Casey Crane Hire, a crane rental company specializing in Grove all-terrain cranes. The repository organizes, tracks, and manages video marketing content across multiple platforms (Instagram, Facebook, YouTube, Google Ads).

**Key Purpose**: Catalog and document video content without storing the actual video files (due to size limitations).

## Repository Structure
- `metadata/` - Video metadata in JSON format (CCH-XXX.json)
- `schemas/` - JSON schemas for data validation
- `scripts/` - Python automation tools for catalog management
- `docs/` - Current marketing guides and strategies
- `archive/` - Historical/old versions of documents
- `templates/` - Templates for video documentation
- `content/` - Marketing content
- `images/` - Image assets
- `VIDEO_CATALOG.md` - Master catalog of all videos in markdown format

## Technology Stack
- **Primary Language**: Python 3
- **Data Format**: JSON for structured metadata
- **Documentation**: Markdown
- **Validation**: JSON Schema

## Equipment Context
Casey Crane Hire operates Grove all-terrain cranes:
- GMK5170 (170-tonne)
- GMK5150 (150-tonne)
- GMK4080 (80-tonne)
- GMK3060 (60-tonne)
- GMK5250 (250-tonne)

**Branding Standards**: White booms/cabs, yellow headboards, Casey Crane Hire logo prominently displayed.

## Coding Standards and Conventions

### Python
- Use Python 3 syntax
- Follow PEP 8 style guidelines
- Include docstrings for functions and classes
- Use type hints where applicable (as seen in `catalog_manager.py`)
- Prefer `pathlib.Path` over `os.path` for file operations
- Use descriptive variable names

### File Naming
- Video metadata: `CCH-XXX.json` (where XXX is a 3+ digit sequential ID)
- Pattern: `CCH-` prefix followed by zero-padded numbers
- All JSON files should follow the schema in `schemas/video-metadata-schema.json`

### JSON Structure
- Always validate against the schema before committing
- Keep metadata up-to-date with current video status
- Use ISO 8601 format for dates and timestamps
- Include all required fields as defined in the schema

### Documentation
- Use markdown for all documentation
- Keep README files in each directory to explain contents
- Update `VIDEO_CATALOG.md` when adding new videos
- Archive old versions instead of deleting (move to `archive/`)

## Automation Scripts

### Main Tool: `scripts/catalog_manager.py`
Available commands:
- `python scripts/catalog_manager.py list` - List all videos
- `python scripts/catalog_manager.py stats` - Show statistics
- `python scripts/catalog_manager.py report` - Generate full report
- `python scripts/catalog_manager.py check` - Check completeness and validation

**Always use these scripts** for catalog operations rather than manual manipulation.

## Best Practices

### DO:
- Run validation checks before committing changes
- Use the automation scripts for catalog operations
- Keep JSON metadata and markdown catalog synchronized
- Archive old versions instead of deleting
- Follow the existing schema structure strictly
- Update performance metrics regularly
- Include proper attribution and source URLs for videos

### DON'T:
- Edit files in the `archive/` directory (they're historical)
- Delete old versions (archive them instead)
- Ignore validation errors from the schema
- Store actual video files in the repository (link to external platforms)
- Modify the video ID pattern (CCH-XXX format)
- Skip schema validation when creating new video entries

## Video Management Workflow

### Adding a New Video:
1. Determine the next sequential ID (e.g., if CCH-001 exists, use CCH-002)
2. Create JSON file in `metadata/` using the schema
3. Add entry to `VIDEO_CATALOG.md`
4. Run `python scripts/catalog_manager.py check` to validate
5. Commit changes

### Updating Video Information:
1. Edit the corresponding JSON file in `metadata/`
2. Update the performance metrics section
3. Validate changes with the check command
4. Update `VIDEO_CATALOG.md` if needed

## Common Patterns

### JSON Metadata Structure:
```json
{
  "id": "CCH-001",
  "title": "Video Title",
  "description": "Description",
  "status": "published|cataloged|archived|in_production",
  "platforms": [
    {
      "name": "youtube|instagram|facebook|tiktok|google_ads|website",
      "published": true|false,
      "url": "https://...",
      "publishDate": "2025-12-20"
    }
  ],
  "performance": {
    "views": 0,
    "likes": 0,
    "shares": 0,
    "comments": 0,
    "engagement_rate": 0.0,
    "lastUpdated": "2025-12-20T10:00:00Z"
  }
}
```

## Testing and Validation
- Always run `python scripts/catalog_manager.py check` before committing
- Ensure JSON files are valid and conform to the schema
- Test script changes with sample data first
- Verify markdown formatting in documentation updates

## Dependencies
- Python 3.x (no external packages required for basic operations)
- Standard library modules: json, os, pathlib, datetime, argparse

## Business Context
- **Competitor awareness**: Track positioning against Membreys Cranes, P&D Rigging, MCG Cranes, and others
- **Marketing focus**: Social media content, Google Ads, equipment showcases
- **Target platforms**: Instagram, Facebook, YouTube, Google Drive

## Repository Maintainer
Benjamin Ashdown - Casey Crane Hire

## Special Notes
- Videos are hosted externally (YouTube, Instagram, Facebook, Google Drive)
- This repository is a catalog system, not a video storage system
- Focus on metadata accuracy and completeness
- Regular weekly reviews of performance metrics are expected
- Keep branding standards consistent across all video documentation
