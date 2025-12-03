# Casey Crane Hire GitHub Repo Blueprints

This plan outlines ready-to-import repository structures for two key projects: `caseybot-ai` and `caseycranehire-marketing`. Each blueprint follows Casey's safety-first brand voice (yellow/white/black), Australian standards (CICA, Worksafe Victoria, AS2550), and automation-focused workflows.

## caseybot-ai

AI assistant and automation engine for lift planning, compliance, and quoting.

### Directory Structure
```
caseybot-ai/
├── README.md
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                  # Lint, tests, security scan
│   │   ├── deploy-docs.yml         # Publish docs to GitHub Pages
│   │   └── content_scheduler.yml   # Weekly knowledge refresh from /data
│   └── CONTRIBUTING.md
├── ai/
│   ├── caseybot_planner.py         # Generates lift plans from structured job inputs
│   ├── load_calc.py                # Material weight calculator (concrete, steel, glass)
│   ├── quote_gen.py                # Pricing estimator by radius/tonnage
│   ├── compliance_checker.py       # Validates plans against CICA & Worksafe guidelines
│   └── prompts/
│       └── prompt-library.md       # Prompt templates for job intake & safety checks
├── data/
│   ├── materials.csv               # Density values and safety factors
│   ├── crane_specs.csv             # Fleet capacities, radii, and counterweights
│   └── templates/
│       ├── lift_plan_template.md
│       └── swms_checklist.md
├── docs/
│   ├── lift_study_template.md      # AS2550-compliant template
│   ├── JSA_checklist.md
│   ├── maintenance_log.md
│   └── pdf/
│       └── LiftStudy_<Client>_<Date>.pdf (generated)
├── reports/
│   └── generator.py                # ReportLab PDF generation
├── scripts/
│   ├── sync_gdrive_logs.py         # Google Sheets -> JSON -> Markdown reports
│   └── refresh_keywords.py         # Daily SEO keyword refresh
├── tests/
│   └── test_load_calc.py
└── requirements.txt
```

### Automation & Integrations
- **GitHub Actions**: CI for lint/tests, scheduled content refresh, and docs deployment.
- **APIs**: Google Business, Canva, YouTube, Xero, FreeCAD macro hooks.
- **Outputs**: Markdown docs, ReportLab PDFs (`LiftStudy_<Client>_<Date>.pdf`), JSON job logs.
- **Secrets**: All credentials stored in GitHub Secrets; no plaintext tokens committed.

### Notes for Contributors
- Follow Australian safety standards in prompts, calculations, and PDFs.
- Maintain versioned data for fleet specs and safety checklists.
- Keep try/except out of import blocks; prefer explicit error handling.

## caseycranehire-marketing

Marketing automation hub for Casey’s social, blog, and SEO content.

### Directory Structure
```
caseycranehire-marketing/
├── README.md
├── .github/
│   ├── workflows/
│   │   ├── auto_social_scheduler.yml   # Weekly Facebook/Instagram push
│   │   ├── seo_refresh.yml            # Daily keyword refresh jobs
│   │   └── blog_publish.yml           # Publish Markdown blogs to CMS/WordPress
│   └── CONTRIBUTING.md
├── ai-marketing/
│   ├── prompt-library.md              # SEO, captions, AI visual prompts
│   ├── 30day-calendar.csv             # Auto-generated content calendar
│   └── content_scheduler.yml          # Workflow config for weekly content
├── content/
│   ├── blogs/
│   │   └── How_Casey_Cranes_Outperforms.md
│   ├── social/
│   │   ├── instagram/
│   │   └── facebook/
│   └── seo/
│       ├── keyword_sets.csv
│       └── backlink_targets.csv
├── analytics/
│   ├── performance_dashboard.md
│   └── gmb_report_template.md
├── scripts/
│   ├── generate_calendar.py
│   ├── post_to_social.py
│   └── refresh_keywords.py
└── templates/
    ├── landing_page.html
    └── email_newsletter.md
```

### Automation & Integrations
- **GitHub Actions**: Auto-publish blogs, daily SEO refresh, and weekly social pushes.
- **APIs**: Google Business, Canva, YouTube, Instagram/Facebook, Xero for cost tracking.
- **Content Governance**: Store imagery references in `images/` with alt text; keep brand colors yellow/white/black.
- **Safety & Compliance**: Ensure posts referencing lifts mention adherence to CICA and Worksafe Victoria standards.

### Notes for Contributors
- Maintain 30-day calendar freshness; regenerate monthly.
- Use Australian spelling and tone; keep messaging authentic and safety-led.
- Version control all campaign assets (CSV/Markdown) to track performance over time.
