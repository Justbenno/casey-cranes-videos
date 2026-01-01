# Day 1 Compliance Officer Audit Checklist — First 5 Assets

Purpose: Execute a high-signal, high-risk audit across five assets with immediate evidence capture and remediation. Output a register with evidence links and deadlines (7-day remove / 30-day correct).

Dates:
- Start: 2026-01-01
- Remove by (7 days): 2026-01-08
- Correct by (30 days): 2026-01-31

Evidence storage (recommended):
- Directory: `docs/compliance/evidence/2026-01-01/` (update folder to match audit date for future runs)
- Naming: `{asset}-{page-or-context}-{view}.{png|pdf}`
  - Example: `website-footer-homepage.png`, `about-us-fullpage-top.png`, `quote-template-export.pdf`

## Asset 1 — Website: Footer (all pages)
Pass if: Logo remains dominant; doodle is small + secondary and only in approved footer position.  
Evidence: Screenshot footer on homepage + one service page.  
If fail: Remove doodle from footer or reduce until it’s clearly secondary.

Checklist:
- [ ] Homepage footer screenshot captured
- [ ] Service page footer screenshot captured
- [ ] Logo dominance verified
- [ ] Doodle small + secondary
- [ ] Doodle present only in footer (approved)

## Asset 2 — Website: About Us page
Pass if: Doodle appears once only (or not at all), and never competes with the logo.  
Evidence: Full-page screenshot (top + mid + bottom).  
If fail: Remove extra doodle instances; keep one supporting placement only.

Checklist:
- [ ] Top section screenshot captured
- [ ] Mid section screenshot captured
- [ ] Bottom section screenshot captured
- [ ] Doodle count ≤ 1
- [ ] No competition with logo

## Asset 3 — Quote template (current active version)
Pass if: Logo in header; doodle footer only, monochrome, visually small, and not near pricing/totals.  
Evidence: Export 1-page PDF + screenshot of the Canva/InDesign template showing locked footer element.  
If fail: Correct layout + lock master template + retire old versions.

Checklist:
- [ ] 1-page PDF export captured
- [ ] Template editor screenshot with locked footer element
- [ ] Header contains logo
- [ ] Doodle in footer only
- [ ] Doodle monochrome + visually small
- [ ] Doodle not near pricing/totals
- [ ] Old versions retired (if applicable)

## Asset 4 — SWMS / OH&S / Lift Study template (most used one)
Pass if: Zero doodle presence anywhere.  
Evidence: Screenshot header/footer of the template + first page export.  
If fail: Immediate removal of doodle and re-issue template.

Checklist:
- [ ] Header screenshot captured
- [ ] Footer screenshot captured
- [ ] First page export captured
- [ ] Verified zero doodle presence
- [ ] Template re-issued (if fail)

## Asset 5 — Google Business Profile: Cover image
Pass if: Logo is primary focal point; doodle (if present) is background-only; background is real site/crane photography (not stock).  
Evidence: Screenshot GBP cover as public sees it + source image file location.  
If fail: Replace cover with approved template and restrict future changes to Owner/Brand Manager approval.

Checklist:
- [ ] Public GBP cover screenshot captured
- [ ] Source image file location recorded
- [ ] Logo primary focal point
- [ ] Doodle background-only (if present)
- [ ] Background is real site/crane photography

## Register Output Instructions
Populate Airtable/Sheets with 5 rows:
- Columns: Asset, Location, Pass/Fail, Evidence Links, Owner, Deadline Remove, Deadline Correct, Status, Notes
- Deadlines: Remove by 2026-01-08; Correct by 2026-01-31
- Attach evidence links from `docs/compliance/evidence/2026-01-01/` or external storage
