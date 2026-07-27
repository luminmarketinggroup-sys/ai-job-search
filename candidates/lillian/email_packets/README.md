# Lillian — Email / Portal Packets

## Rule
- **Portal employers:** email a ready-to-upload packet to `schulezechlillian@gmail.com` with the portal link, role summary, resume PDF, and cover letter PDF.
- **Mailto employers:** send the application to the employer (Reply-To Lillian), and BCC Lillian.

## Send command

Requires `RESEND_API_KEY` in the environment (Cursor Cloud secret or `/workspace/.env`).

```bash
# Dry run
python3 scripts/send_lillian_portal_packets.py --dry-run

# Send all portal packets to Lillian
python3 scripts/send_lillian_portal_packets.py

# Send only selected companies
python3 scripts/send_lillian_portal_packets.py --only general_bank,dynacare,atco

# Peace Hills employer mailto (not a portal packet)
python3 scripts/send_lillian_portal_packets.py --peace-hills
```

## From / Reply-To
- From: `Lillian Schule Zech <dylan@luminmarketinggroup.com>` (verified domain)
- Reply-To for packets to Lillian: `schulezechlillian@gmail.com`
- Reply-To for employer mailto: `schulezechlillian@gmail.com`
