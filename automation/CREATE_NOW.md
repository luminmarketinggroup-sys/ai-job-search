# Create the automation — do this once (2 minutes)

**DONE — live:** https://cursor.com/automations/e3c97a08-8569-11f1-a7d1-d6b4613131ce  
Name: `daily job search` · Enabled: yes · Owner: Lumin Group

Keep Path B (GitHub Actions) **disabled** unless you intentionally want a second scheduler.

---

## Path A — Cursor Automations UI (preferred)

1. Open **https://cursor.com/automations/new** (logged in as luminmarketinggroup@gmail.com / Lumin Group)
2. Set fields:

| Field | Value |
|-------|--------|
| Name | `Dylan daily job search` |
| Trigger | **Scheduled** → every day → `0 14 * * *` (14:00 UTC ≈ 8am Edmonton MST) or every 12 hours |
| Repository | `luminmarketinggroup-sys/ai-job-search` |
| Branch | `cursor/dylan-michael-profile-setup-7ff7` |
| Tools | Git write / PR update enabled; memories optional |
| Prompt | Paste entire contents of `automation/daily-job-search-prompt.md` |

3. **Save** and leave it **Enabled**
4. Reply here with the automation URL (or UUID from the URL) so we can verify with `get-automation`

Desktop shortcut: in a local Agent chat on this repo, run `/automate` and say:  
“Daily dual-track job search for Dylan — use `automation/daily-job-search-prompt.md`, schedule daily 14:00 UTC, repo ai-job-search on branch cursor/dylan-michael-profile-setup-7ff7, update PR #1.”

---

## Path B — GitHub Actions cron (already in repo)

If you prefer not to use Automations UI:

1. Create API key: https://cursor.com/dashboard → **API Keys**
2. GitHub → `ai-job-search` → Settings → Secrets and variables → Actions → New secret  
   Name: `CURSOR_API_KEY`  
   Value: the key
3. Actions → **Daily job search** → Enable workflow / Run workflow once to test

Workflow file: `.github/workflows/daily-job-search.yml`
