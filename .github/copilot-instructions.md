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
