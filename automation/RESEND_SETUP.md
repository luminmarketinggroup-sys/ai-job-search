# Resend setup — dual candidate job applications

## Identities

| Candidate | From (verified domain) | Reply-To |
|-----------|------------------------|----------|
| Dylan | `Dylan Michael <dylan@luminmarketinggroup.com>` | `dylanschule@live.ca` |
| Lillian | `Lillian Schule Zech <dylan@luminmarketinggroup.com>` | `schulezechlillian@gmail.com` |

Resend cannot send *From* `@gmail.com` / `@live.ca`. Use the verified `luminmarketinggroup.com` domain and set Reply-To to the candidate’s personal inbox.

## One-time setup

1. https://resend.com/domains — verify `luminmarketinggroup.com`
2. https://resend.com/api-keys — create a Sending key
3. Add to Cursor Cloud Environment secrets for `luminmarketinggroup-sys/ai-job-search`:
   - `RESEND_API_KEY`
   - optional: `RESEND_FROM`, `RESEND_REPLY_TO`, `RESEND_BCC`
4. Or local `/workspace/.env` (gitignored):

```bash
RESEND_API_KEY=re_xxxxxxxx
RESEND_FROM=Lillian Schule Zech <dylan@luminmarketinggroup.com>
RESEND_REPLY_TO=schulezechlillian@gmail.com
```

Environment dashboard: https://cursor.com/dashboard/cloud-agents/environments/e/9c234b02-8653-11f1-a7d1-d6b4613131ce

## Lillian sends

```bash
python3 scripts/send_lillian_portal_packets.py --dry-run
python3 scripts/send_lillian_portal_packets.py
```

Portal packets go to `schulezechlillian@gmail.com`. Mailto apps go to the employer with BCC to Lillian.
