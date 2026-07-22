# Job Search Automation — Dylan Michael

## Goal (current phase)
1. **Survival track:** Find any decent job very close to 11110 68 Ave NW, Edmonton (Southgate / 68 Ave / Calgary Trail). Cafe, retail, warehouse, food service OK. Pay floor soft for this track.
2. **Career track:** Keep drafting marketing / SEO / AI roles ≥ CAD $60k (Edmonton or remote).
3. Once employed locally, shift focus to better career roles.

## Autonomy settings (user-approved 2026-07-22)
| Setting | Value |
|---------|--------|
| Schedule | Open / frequent (recommend daily 08:00 America/Edmonton) |
| Scope | Both local basic + career |
| Auto-draft | **Yes — no ask** for: (a) local roles within ~15 min of 11110 68 Ave NW, or (b) career High/Good fit ≥60 |
| Notify | PR updates on branch `cursor/dylan-michael-profile-setup-7ff7` (or current working branch) |
| Auto-submit | **Desired** — see limits below |

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

1. Open https://cursor.com/automations  
2. New automation → **Scheduled** → daily (or every 12 hours)  
3. Repository: this `ai-job-search` repo  
4. Tools: git write, PR update, LinkedIn/web search as available  
5. Paste the prompt below  

### Automation prompt (copy/paste)

```
You are Dylan Michael's job-search agent. Profile is in CLAUDE.md and .claude/skills/job-application-assistant/.

PHASE: Survival + career dual track.
Home: 11110 68 Ave NW, Edmonton, AB (prioritize Southgate, 68 Ave, Calgary Trail, Empire Park / Lendrum).

EVERY RUN:
1. Load job_scraper/seen_jobs.json and job_search_tracker.csv. Skip already-seen URLs.
2. Search NEW jobs (last 7–14 days):
   A) LOCAL BASIC near home: warehouse, barista, cafe, cashier, retail, dishwasher, crew, stock, unloader, sales associate — Southgate / 68 Ave / Calgary Trail first.
   B) CAREER: SEO, digital marketing, AI marketing/automation, marketing account manager — Edmonton or remote Canada, prefer ≥ CAD $60k.
3. For each NEW job:
   - LOCAL: if within ~15 min of 11110 68 Ave NW OR clearly Southgate/68 Ave/Calgary Trail → AUTO-DRAFT (no questions). Use cv/main_local_edmonton.tex pattern; 1-page PDF; blurb in APPLICATIONS_LOCAL.md.
   - CAREER: if overall fit ≥ 60 (Good/High) → AUTO-DRAFT (no questions). Full CV+cover via /apply rules; update APPLICATIONS_READY.md.
   - Else: log in seen_jobs as skipped/low; do not draft.
4. Compile PDFs (lualatex/xelatex). Keep personal outputs even if gitignored.
5. Update job_search_tracker.csv status ready_to_submit.
6. Commit + push to the working branch. Update the open PR description with a dated "New drafts this run" table (company, role, link, files).
7. Do NOT invent metrics. Do NOT fabricate experience. Use Audi Southgate, 2 Lumin clients, 20h/week Claude savings, Google AI Professional Certificate as factual.

SUBMIT ATTEMPTS:
- If a public apply email exists, draft and send application email with PDF attached only if outbound email is configured; otherwise add mailto: line to checklist.
- Do not claim LinkedIn/Indeed/Starbucks form submit succeeded unless a browser MCP with an authenticated session actually completed submit.
- Never store or ask for passwords in the PR.

End with a short PR summary: N new local drafts, M new career drafts, links to checklists.
```

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
