# Lillian — Curated apply packets (2026-07-27)

Status legend: **portal_packet** = email Lillian with files + portal link · **mailto** = email employer (BCC Lillian)

| # | Company | Role | Channel | Status | Portal / Email | Resume | Cover |
|---|---------|------|---------|--------|----------------|--------|-------|
| 1 | General Bank of Canada | CSR I | portal | curated | https://www.generalbank.ca/careers/ | `cv/main_general_bank.pdf` | `cover_letters/cover_general_bank_csr_i.pdf` |
| 2 | Dynacare / CannAmm | Call Attendant (Remote) | portal | curated | https://jobs.jobvite.com/dynacare/job/oI9oAfwz | `cv/main_dynacare.pdf` | `cover_letters/cover_dynacare_call_attendant.pdf` |
| 3 | ATCO Gas | Customer Care Rep (Temp) | portal | curated | https://careers.atco.com/ | `cv/main_atco.pdf` | `cover_letters/cover_atco_customer_care_representative.pdf` |
| 4 | Alberta Blue Cross | Claims Coordinator | portal | curated | https://careers.ab.bluecross.ca | `cv/main_alberta_blue_cross.pdf` | `cover_letters/cover_alberta_blue_cross_claims_coordinator.pdf` |
| 5 | Peace Hills Insurance | Claims Advisor – Property | mailto | curated | sclawson@phgic.com | `cv/main_peace_hills.pdf` | `cover_letters/cover_peace_hills_claims_advisor_property.pdf` |
| 6 | Trans Global / The Brick | Creditor Insurance Claims Rep | mailto | curated | careers@thebrick.com | `cv/main_trans_global.pdf` | `cover_letters/cover_trans_global_creditor_claims_representative.pdf` |

## Curation checklist (all six)
- [x] Contact details are Lillian only (phone/email/CIPR)
- [x] Sales quotas and kitchen detail de-emphasized
- [x] CV 2 pages / cover letter 1 page (compiled)
- [x] Portal/mailto path identified
- [x] Email body written under `email_packets/`
- [x] Resend send completed (2026-07-27): 4 portal packets to Lillian; Peace Hills + Trans Global mailed to employers (BCC Lillian)

## Send
```bash
python3 scripts/send_lillian_portal_packets.py --dry-run
python3 scripts/send_lillian_portal_packets.py              # all
python3 scripts/send_lillian_portal_packets.py --portals-only
python3 scripts/send_lillian_portal_packets.py --mailtos-only
```

Packet zips (for manual forward if email blocked): see `/opt/cursor/artifacts/lillian-apply-packets/`.
