# Resend setup — Dylan Michael job applications

## Important constraint
Resend **cannot** send *From* `@live.ca` (Microsoft owns that domain).

Configured identity:
| Role | Address |
|------|---------|
| **From** (verified domain) | `Dylan Michael <dylan@luminmarketinggroup.com>` |
| **Reply-To** (personal inbox) | `dylanschule@live.ca` |
| **Bcc** (optional sent copy) | `dylanschule@live.ca` via `RESEND_BCC` |

Employers reply → lands in your Outlook/Live inbox.

---

## One-time Resend dashboard steps

1. Open https://resend.com/domains  
2. Add / verify **`luminmarketinggroup.com`** (DNS: SPF + DKIM as Resend shows)  
3. Open https://resend.com/api-keys → create key with **Sending access**  
4. Put the key where agents can read it (pick one):

### A) Local / this cloud VM (fastest for tonight)
Create `/workspace/.env` (gitignored):

```bash
RESEND_API_KEY=re_xxxxxxxx
RESEND_FROM=Dylan Michael <dylan@luminmarketinggroup.com>
RESEND_REPLY_TO=dylanschule@live.ca
RESEND_BCC=dylanschule@live.ca
```

### B) Cursor Cloud Agents secrets (for daily automation)
Cursor Dashboard → Cloud Agents → Environment / Secrets → add:
- `RESEND_API_KEY`
- optional: `RESEND_FROM`, `RESEND_REPLY_TO`, `RESEND_BCC`

If no Cloud Environment exists yet, create one for `ai-job-search` and attach secrets there so the daily automation can send.

---

## Send ready applications

```bash
pip install resend python-dotenv
python3 scripts/send_ready_emails.py --dry-run   # preview
python3 scripts/send_ready_emails.py             # send Connected Creative + Guardium
```

Single email:

```bash
python3 scripts/send_application_email.py \
  --to hannah@connectedcreative.ca \
  --subject "Marketing Manager application — Dylan Michael (Edmonton)" \
  --body-file /tmp/body.txt \
  --attach cv/main_connected_creative.pdf \
  --attach cover_letters/cover_connected_creative_marketing_manager.pdf
```

---

## After domain is verified
Reply in chat with: `Resend ready` (and confirm `dylan@luminmarketinggroup.com` is OK as From).  
Agent will send Connected Creative + Guardium immediately.
