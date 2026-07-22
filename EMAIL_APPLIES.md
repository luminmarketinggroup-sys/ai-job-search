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
| 6 | StackAdapt | careers@stackadapt.com | `96d42b43-cbd2-4171-b706-f580c07e14a4` | **submitted** (also finish Greenhouse if you can) |
| 7 | Pacesetter Homes | info@yourpacesetter.com | `003dc722-b14f-45e5-9743-1c58fadc5176` | **submitted** (also finish ADP/Career Centre if you can) |
| 8 | Morguard | hrassist@morguard.com | `7b60362f-85c4-4923-8a5a-960355ad14a5` | **submitted** (also finish Teamtailor portal if you can) |
| 9 | Riva International | careers@rivaengine.com | `2ce95f74-4d01-435b-ab50-f6ca9bfd9d72` | **submitted** (address unverified; Greenhouse CAPTCHA blocked) |
| 10 | Riva International | info@rivaengine.com | `6d1c9e2b-dbd9-4616-966d-0442b7283808` | **submitted** (address unverified; Greenhouse CAPTCHA blocked) |

From: `dylan@luminmarketinggroup.com` · Reply-To/Bcc: `dylanschule@live.ca`

**Still portal-only (cloud cannot complete CAPTCHA):** AMA Member Rewards (`careers.ama.ab.ca`), plus official Greenhouse/Teamtailor/ADP forms for Riva/StackAdapt/Morguard/Pacesetter if email is not enough.

## Send more later

```bash
python3 scripts/send_ready_emails.py --dry-run
python3 scripts/send_application_email.py --to … --subject … --body … --attach …
```

Key lives in gitignored `.env` only — never commit it.
