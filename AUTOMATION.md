# Job Search Automation — Dylan Michael

## Goal (current phase)
1. **Survival track:** Nearby warehouse / back-of-house / non-mall jobs near 11110 68 Ave NW (68 Ave industrial, Calgary Trail corridor). Pay floor soft.
2. **Career track:** Marketing / SEO / AI roles ≥ CAD $60k (Edmonton or remote).
3. Once employed locally, shift focus to better career roles.

## Hard skip (user 2026-07-22)
**Do not draft or prioritize public-facing jobs at Southgate Centre** — mall retail, sales associate, barista/cafe inside Southgate, food counter at Southgate, store educator / team leader at Southgate. Already-drafted Southgate public-facing rows stay in the archive but are out of the active submit batch.

## Autonomy settings (user-approved 2026-07-22 — LOCKED; Southgate PF excluded)
| Setting | Value |
|---------|--------|
| Schedule | **Open** / daily automation live |
| Scope | **Both** — nearby warehouse/back-of-house first, then career ≥$60k |
| Goal now | Decent nearby non-Southgate-public-facing job; upgrade career once employed |
| Auto-draft | **Yes — no ask** for: (a) local warehouse/BOH within ~15 min of home / 68 Ave / Calgary Trail (not Southgate public-facing), or (b) career High/Good fit ≥60 |
| Notify | **PR updates** on branch `cursor/dylan-michael-profile-setup-7ff7` |
| Auto-submit | Email via Resend when possible; portals still need human/Desktop browser |

## What Cursor Cloud can do unattended
- Scrape LinkedIn/web for new jobs
- Score fit (local proximity OR career framework)
- Auto-draft CV + cover/blurb
- Commit + push + update PR body / `APPLICATIONS_*.md` + `job_search_tracker.csv`

## Auto-submit reality check
Most employers (Starbucks, Indeed Easy Apply, LinkedIn Easy Apply, mall retailers) require a logged-in browser session and CAPTCHA. **Cloud agents cannot reliably auto-submit those forms.**

Workable submit paths:
1. **Email apply via Resend** — see `automation/RESEND_SETUP.md`. From `dylan@luminmarketinggroup.com`, Reply-To `dylanschule@live.ca`. Run `python3 scripts/send_ready_emails.py` when `RESEND_API_KEY` is set.
2. **Cursor Desktop + browser MCP** — you stay logged into Indeed/LinkedIn/Starbucks; agent fills forms on your machine (still fails on CAPTCHA/2FA).
3. **Human 5-minute batch** — portal forms from `SUBMIT_BATCH.md` / `APPLICATIONS_LOCAL.md`.

Until portals are browser-automated: **email roles auto-send via Resend; portals stay checklist.**

---

## Create the Cursor Automation

**Status: LIVE** (verified 2026-07-22)

| Field | Value |
|-------|--------|
| Name | daily job search |
| ID | `e3c97a08-8569-11f1-a7d1-d6b4613131ce` |
| Enabled | yes |
| Dashboard | https://cursor.com/automations/e3c97a08-8569-11f1-a7d1-d6b4613131ce |
| Owner | Lumin Group (`luminmarketinggroup@gmail.com`) |

Canonical prompt file: `automation/daily-job-search-prompt.md`  
Optional backup cron (Path B): `.github/workflows/daily-job-search.yml` — only if you also want GitHub Actions; disable one scheduler to avoid duplicate runs.

---

## Professional submit rule (LOCKED)

Follow what each employer requires:
1. **Portal / ATS first** when that is the listed apply path (BambooHR, Northstar, Sephora careers, Greenhouse, LinkedIn Easy Apply).
2. **Do not** use Contact Us forms when the employer says applications must go through Careers (e.g. Waste Logic).
3. **Email / Resend** only when the posting lists a mailto or recruiter email as an apply method.
4. Never claim portal submit succeeded without a confirmation screen.

Canonical field answers + PDF map: `PROFESSIONAL_PORTAL_APPLY.md`

## Desktop path for portal submits (required for CAPTCHA / login)

On your laptop (Cursor Desktop):
1. Install a browser MCP / enable browser tool  
2. Log into LinkedIn, Sephora, Princess Auto Northstar, BambooHR, etc. in that browser  
3. Ask: “Submit the packs in PROFESSIONAL_PORTAL_APPLY.md using my logged-in browser. I will approve CAPTCHAs.”  
4. Approve CAPTCHAs when they appear; agent uploads the curated CV/cover PDFs  

This is the professional path for form-based employers. Cloud VMs alone cannot complete reCAPTCHA or LinkedIn sessions reliably.

---

## Priority order when drafting
1. 68 Ave / Calgary Trail warehouse, dock, package handler, unloader, stock (non-mall)  
2. Other nearby Edmonton warehouse / BOH  
3. Career High fits ≥ $60k  
4. Career Good fits  
5. **Never:** Southgate Centre public-facing retail/food/cafe
