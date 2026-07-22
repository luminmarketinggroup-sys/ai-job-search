# Email applies — Resend

**Identity**
- From: `Dylan Michael <dylan@luminmarketinggroup.com>` (Resend verified domain)
- Reply-To / personal: `dylanschule@live.ca` (replies land here)
- Setup: `automation/RESEND_SETUP.md`

**Cannot use `@live.ca` as From** — Resend only sends from domains you verify. Personal inbox is Reply-To (+ optional Bcc).

---

## Send now (after `RESEND_API_KEY` is in `.env`)

```bash
pip install resend python-dotenv
python3 scripts/send_ready_emails.py --dry-run
python3 scripts/send_ready_emails.py
```

| # | Company | To | Attachments |
|---|---------|-----|-------------|
| 1 | Connected Creative | hannah@connectedcreative.ca | `cv/main_connected_creative.pdf`, cover |
| 2 | Guardium Group | info@guardiumgroup.com | `cv/main_example.pdf`, cover |

Fallback (no API key): open `documents/applications/SEND_*.eml` and Send from Outlook.

---

## After you send / agent sends
Reply `submitted email Connected Creative` / `Guardium` so the tracker flips to submitted.
