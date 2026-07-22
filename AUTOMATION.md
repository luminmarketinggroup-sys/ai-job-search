# Job Search Automation — Dylan Michael

## Goal (current phase)
1. **Survival track:** Find any decent job very close to 11110 68 Ave NW, Edmonton (Southgate / 68 Ave / Calgary Trail). Cafe, retail, warehouse, food service OK. Pay floor soft for this track.
2. **Career track:** Keep drafting marketing / SEO / AI roles ≥ CAD $60k (Edmonton or remote).
3. Once employed locally, shift focus to better career roles.

## Autonomy settings (user-approved 2026-07-22 — LOCKED)
| Setting | Value |
|---------|--------|
| Schedule | **Open** (recommend daily 08:00 America/Edmonton until Cursor Automation is created) |
| Scope | **Both** — nearby decent survival jobs first, then career ≥$60k |
| Goal now | Any decent job very close to 11110 68 Ave NW; upgrade career once employed |
| Auto-draft | **Yes — no ask** for: (a) local roles within ~15 min of home / Southgate / 68 Ave / Calgary Trail, or (b) career High/Good fit ≥60 |
| Notify | **PR updates** on branch `cursor/dylan-michael-profile-setup-7ff7` |
| Auto-submit | **Requested without human** — cloud cannot complete most portal forms; see limits. Email-apply roles may be sent when outbound mail exists. |

## What Cursor Cloud can do unattended
- Scrape LinkedIn/web for new jobs
- Score fit (local proximity OR career framework)
- Auto-draft CV + cover/blurb
- Commit + push + update PR body / `APPLICATIONS_*.md` + `job_search_tracker.csv`

## Auto-submit reality check
Most employers (Starbucks, Indeed Easy Apply, LinkedIn Easy Apply, mall retailers) require a logged-in browser session and CAPTCHA. **Cloud agents cannot reliably auto-submit those forms.**

Workable submit paths:
1. **Email apply** — agent can send where a public apply email exists (human inbox may still need confirmation).
2. **Cursor Desktop + browser MCP** — you stay logged into Indeed/LinkedIn/Starbucks; agent fills forms on your machine (still fails on CAPTCHA/2FA).
3. **Human 5-minute batch** — agent prepares everything; you click Submit from `APPLICATIONS_LOCAL.md` / `APPLICATIONS_READY.md`.

Until Desktop browser automation is wired, treat “auto-submit” as: **auto-draft + PR notify + checklist ready for one-tap submit.**

---

## Create the Cursor Automation

**Status:** Cloud agents cannot create Automations in the Cursor UI (no Create API; `/automate` is Desktop-only).  
**Do this once:** follow `automation/CREATE_NOW.md` (Path A UI or Path B GitHub Actions).

Canonical prompt file (copy/paste source of truth):  
`automation/daily-job-search-prompt.md`

In-repo scheduled trigger (Path B):  
`.github/workflows/daily-job-search.yml` — needs secret `CURSOR_API_KEY`.

---

## Desktop path for closer-to-auto-submit (optional next step)

On your laptop (Cursor Desktop):
1. Install a browser MCP / enable browser tool  
2. Log into Indeed, LinkedIn, Starbucks careers, etc. in that browser  
3. Ask the agent: “Submit all ready_to_submit rows in APPLICATIONS_LOCAL.md using my logged-in browser”  
4. Approve CAPTCHAs when they appear  

This is the only practical way to approach “auto submit without human” for form-based employers.

---

## Priority order when drafting
1. Same street / Southgate / Calgary Trail basic jobs  
2. Other nearby Edmonton basic jobs  
3. Career High fits ≥ $60k  
4. Career Good fits  
