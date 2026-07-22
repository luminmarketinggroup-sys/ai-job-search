# Email applies — Resend

**Identity**
- From: `Dylan Michael <dylan@luminmarketinggroup.com>` (Resend verified domain)
- Reply-To / personal: `dylanschule@live.ca` (replies land here)
- Setup: `automation/RESEND_SETUP.md`

**Cannot use `@live.ca` as From** — Resend only sends from domains you verify. Personal inbox is Reply-To (+ optional Bcc).

---

## Sent (2026-07-22)

| # | Company | To | Resend id | Status |
|---|---------|-----|-----------|--------|
| 1 | Connected Creative | hannah@connectedcreative.ca | `03fb2c51-f2f9-4716-8579-09b3a6a2f167` | **submitted** |
| 2 | Guardium Group | info@guardiumgroup.com | `912d371a-3252-43ab-be87-45a6149e6091` | **submitted** |
| 3 | KFC/Pizza Hut Southgate | hr.foodsservice@gmail.com | `ffcdb1a9-41a9-4906-92d2-e0a461b7f793` | **submitted** |
| 4 | KFC/Pizza Hut Southgate | jobs.southgatefoods@yahoo.com | `b372e6bb-95fd-4057-8e48-c119ddb779c1` | **submitted** |
| 5 | Adster Creative | info@adster.ca | `1a280859-70b8-4d8a-b11a-c4422c72399b` | **submitted** (also use Jotform if they ask) |

From: `dylan@luminmarketinggroup.com` · Reply-To/Bcc: `dylanschule@live.ca`

## Send more later

```bash
python3 scripts/send_ready_emails.py --dry-run
python3 scripts/send_application_email.py --to … --subject … --body … --attach …
```

Key lives in gitignored `.env` only — never commit it.
