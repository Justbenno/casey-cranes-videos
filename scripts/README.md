# Scripts Directory

Automation scripts for managing the Casey Crane Hire video catalog efficiently.

## Available Scripts

### stream_with_log.py

An interactive script for chatting with OpenAI's GPT models with automatic logging.

**Requirements**: Python 3.8+, `openai` package

**Setup**:
```bash
# Install the OpenAI package
pip install openai

# Edit the script and replace "your-api-key-here" with your actual OpenAI API key
# Or set the OPENAI_API_KEY environment variable
```

**Usage**:
```bash
python stream_with_log.py
```

**Features**:
- Prompts you to enter a question for the AI model
- Streams the response in real-time to your terminal
- Automatically saves the full conversation to a timestamped file in the `responses/` directory
- Each response is saved as `response_YYYY-MM-DD_HH-MM-SS.txt`

**Note**: The `responses/` directory is automatically created and excluded from git commits (see `.gitignore`).

### catalog_manager.py

A comprehensive Python tool for managing the video catalog.

**Requirements**: Python 3.8+

**Usage**:
```bash
# List all videos in the catalog
python catalog_manager.py list

# Show statistics about the catalog
python catalog_manager.py stats

# Generate a full markdown report
python catalog_manager.py report

# Check all videos for completeness and validation
python catalog_manager.py check
```

**Features**:
- Lists all videos with their status
- Validates video metadata against required fields
- Generates statistics (by status, type, platform, etc.)
- Identifies incomplete videos (missing branding, equipment info, etc.)
- Produces human-readable reports

## Future Scripts

Additional scripts can be added here for:
- Automated video uploads to platforms
- Performance metrics tracking
- Content calendar management
- Social media post scheduling

---

*Last Updated: December 20, 2025*
