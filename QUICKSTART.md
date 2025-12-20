# Quick Start Guide

This guide helps you quickly get started with the Casey Crane Hire video catalog management system.

## For New Users

### 1. Understanding the Repository Structure
```
casey-cranes-videos/
├── README.md                    # Start here
├── VIDEO_CATALOG.md             # Master video list (markdown)
├── PERFORMANCE_IMPROVEMENTS.md  # What's been optimized
├── metadata/                    # Video data (JSON format)
├── schemas/                     # Data validation rules
├── scripts/                     # Automation tools
├── docs/                        # Marketing guides (current)
├── archive/                     # Old versions (historical)
└── templates/                   # Templates for new content
```

### 2. Finding Information

**Looking for current marketing guidelines?**
→ Check `docs/messaging-guide.md`

**Need the content calendar?**
→ Check `docs/content-calendar-november-2025.md`

**Want to see all videos?**
→ Run: `python scripts/catalog_manager.py list`

**Need historical versions?**
→ Check `archive/` directory

## For Daily Tasks

### View All Videos
```bash
python scripts/catalog_manager.py list
```

### Check Video Completeness
```bash
python scripts/catalog_manager.py check
```

### Get Statistics
```bash
python scripts/catalog_manager.py stats
```

### Generate Full Report
```bash
python scripts/catalog_manager.py report > video_report.md
```

## Adding a New Video

### Option 1: JSON Format (Recommended for automation)
1. Copy `metadata/CCH-001.json` as a template
2. Rename to next ID: `CCH-002.json`
3. Edit the JSON with video details
4. Validate: `python scripts/catalog_manager.py check`

### Option 2: Markdown Format (Traditional)
1. Use template: `templates/video-entry-template.md`
2. Add entry to `VIDEO_CATALOG.md`
3. Create detailed metadata file in `metadata/`

## Common Tasks

### Update Video Performance Metrics
Edit the JSON file in `metadata/` and update the `performance` section:
```json
"performance": {
  "views": 1234,
  "likes": 56,
  "shares": 12,
  "comments": 8,
  "engagement_rate": 4.5,
  "lastUpdated": "2025-12-20T10:00:00Z"
}
```

### Mark Video as Published
Update the `platforms` array in the video's JSON file:
```json
"platforms": [
  {
    "name": "youtube",
    "published": true,
    "url": "https://youtube.com/watch?v=...",
    "publishDate": "2025-12-20"
  }
]
```

### Archive an Old Video
Change the `status` field to `"archived"`:
```json
"status": "archived"
```

## Tips for Efficiency

1. **Use the scripts** - They're much faster than manual checks
2. **Keep JSON files updated** - They power the automation
3. **Run checks regularly** - Catch issues early
4. **Use the schema** - It defines what fields are needed
5. **Check archive/ first** - Don't reinvent the wheel

## Troubleshooting

### Script doesn't run
```bash
# Make sure you have Python 3
python3 --version

# Make script executable
chmod +x scripts/catalog_manager.py

# Run with python3 explicitly
python3 scripts/catalog_manager.py list
```

### Can't find a document
- Current docs → `docs/` directory
- Old versions → `archive/` directory
- Video data → `metadata/` directory

### Not sure which version to use
Always use files from `docs/` directory. Files in `archive/` are historical only.

## Getting Help

1. Check this guide first
2. Read `README.md` in each directory
3. Look at examples in `metadata/CCH-001.json`
4. Review `PERFORMANCE_IMPROVEMENTS.md` for context
5. Contact Benjamin Ashdown (repository maintainer)

## Best Practices

✅ **DO**:
- Update video metadata regularly
- Run validation checks before committing
- Keep JSON and markdown in sync
- Archive old versions instead of deleting
- Use automation scripts

❌ **DON'T**:
- Edit files in `archive/` directory
- Delete old versions (move to archive instead)
- Ignore validation errors
- Work directly in the main branch without testing

---

**Need more details?** See the full README.md in the root directory.

**Ready to get started?** Try: `python scripts/catalog_manager.py list`
