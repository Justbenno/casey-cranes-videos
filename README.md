# Casey Cranes Video Catalog

This repository serves as a comprehensive catalog and documentation system for Casey Crane Hire's video marketing content.

## Purpose

This repository helps organize, track, and manage all video content for Casey Crane Hire, including:

- Marketing videos for social media (Instagram, Facebook, Meta)
- Google Ads video content
- Equipment showcase videos
- Project documentation videos
- Training and safety videos

## Repository Structure

```
casey-cranes-videos/
├── README.md                 # This file
├── VIDEO_CATALOG.md          # Master catalog of all videos
├── metadata/                 # Video metadata files (JSON format)
├── schemas/                  # JSON schemas for data validation
├── scripts/                  # Automation scripts for catalog management
├── templates/                # Templates for video documentation
├── docs/                     # Marketing guides and strategies
├── archive/                  # Historical/old versions of documents
├── content/                  # Marketing content
└── images/                   # Image assets
```

## Equipment Featured

All videos feature Casey Crane Hire's fleet of **Grove all-terrain cranes**:

- **GMK5170** - 170-tonne capacity
- **GMK5150** - 150-tonne capacity  
- **GMK4080** - 80-tonne capacity
- **GMK3060** - 60-tonne capacity
- **GMK5250** - 250-tonne capacity

### Branding Standards

All equipment in videos must display:
- **White booms and cabs**
- **Yellow headboards**
- **Casey Crane Hire logo prominently displayed**

## Video Storage

**Note**: This repository does NOT store actual video files (due to GitHub file size limitations). Instead, it catalogs videos stored on:

- YouTube
- Instagram
- Facebook
- Google Drive
- Other cloud storage platforms

Each video entry includes links to where the actual video file is hosted.

## Competitor Awareness

This catalog helps track our competitive position against:

Membreys Cranes and Transport, P&D Rigging, MCG Cranes, JYC, Metcalf, Gravity Rigging, Paramount Cranes, Sventec Cranes, Browns Cranes, Mackay United, KTB Cranes, Cranetec, Komp Cranes, Cardinias Cranes, Crane Tec

## Usage

### Managing Videos

#### Adding a New Video
1. Create a new JSON file in `metadata/` using the next sequential ID (e.g., `CCH-002.json`)
2. Follow the schema defined in `schemas/video-metadata-schema.json`
3. Add an entry to `VIDEO_CATALOG.md`
4. Or use the template in `templates/video-entry-template.md` for markdown format

#### Updating Video Information
- Edit the corresponding JSON file in `metadata/`
- Update the entry in the catalog if needed

#### Automation Scripts
Use the Python script for easier management:
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

### Weekly Reviews
Review and update video performance metrics weekly using the automation scripts.

## Maintained By

Benjamin Ashdown  
Casey Crane Hire

---

*Last Updated: October 26, 2025*

