# Lillian — Curated apply packets (2026-07-27)

Status legend: **portal_packet** = email Lillian with files + portal link · **mailto** = email employer (BCC Lillian)

| # | Company | Role | Channel | Status | Portal / Email | Resume | Cover |
|---|---------|------|---------|--------|----------------|--------|-------|
| 1 | General Bank of Canada | CSR I | portal | emailed | https://www.generalbank.ca/careers/ | `cv/main_general_bank.pdf` | `cover_letters/cover_general_bank_csr_i.pdf` |
| 2 | Dynacare / CannAmm | Call Attendant (Remote) | portal | emailed | https://jobs.jobvite.com/dynacare/job/oI9oAfwz | `cv/main_dynacare.pdf` | `cover_letters/cover_dynacare_call_attendant.pdf` |
| 3 | ATCO Gas | Customer Care Rep (Temp) | portal | emailed | https://careers.atco.com/ | `cv/main_atco.pdf` | `cover_letters/cover_atco_customer_care_representative.pdf` |
| 4 | Alberta Blue Cross | Claims Coordinator | portal | emailed | https://careers.ab.bluecross.ca | `cv/main_alberta_blue_cross.pdf` | `cover_letters/cover_alberta_blue_cross_claims_coordinator.pdf` |
| 5 | Peace Hills Insurance | Claims Advisor – Property | mailto | submitted | sclawson@phgic.com | `cv/main_peace_hills.pdf` | `cover_letters/cover_peace_hills_claims_advisor_property.pdf` |
| 6 | Trans Global / The Brick | Creditor Insurance Claims Rep | mailto | submitted | careers@thebrick.com | `cv/main_trans_global.pdf` | `cover_letters/cover_trans_global_creditor_claims_representative.pdf` |
| 7 | Jobber | Product Support Specialist (Future Opportunities) | portal | emailed | https://jobs.ashbyhq.com/jobber/17b641db-0e40-418e-a53d-ffce4fee2a31/application | `cv/main_jobber.pdf` | `cover_letters/cover_jobber_product_support_specialist.pdf` |
| 8 | Royal Glenora Club | Front Desk Member Services (Part-Time) | portal | emailed | https://royalglenoraclub.easyapply.co/job/front-desk-member-services-representative-part-time | `cv/main_royal_glenora.pdf` | `cover_letters/cover_royal_glenora_front_desk_member_services.pdf` |
| 9 | AMA | MSR Roadside Assistance (WFH) | portal | emailed | https://albertamotorassociation.wd3.myworkdayjobs.com/en-US/AMA/job/CA-AB-Edmonton-South/Member-Service-Representative--Roadside-Assistance--Work-from-Home-_JR102609-1 | `cv/main_ama_roadside.pdf` | `cover_letters/cover_ama_member_service_representative_roadside.pdf` |
| 10 | AMA | Retail Support Agent (St. Albert 6-mo + Edmonton priority) | portal | emailed | St. Albert + Edmonton Workday links in `email_packets/portal_ama_retail.txt` | `cv/main_ama_retail.pdf` | `cover_letters/cover_ama_retail_support_agent.pdf` |

## Batch 2 notes (Jobber + Royal Glenora)
- [x] Contact details are Lillian only
- [x] Sales quotas and kitchen detail de-emphasized
- [x] CV 2 pages / cover letter 1 page (compiled + visual check)
- [x] ATS text layer: email/phone literal; no cid garbage
- [x] Portal packets under `email_packets/portal_jobber.txt` and `portal_royal_glenora.txt`
- [x] Resend send for Jobber + Royal Glenora portal packets

## Watched / skipped this search
- Jobber CSR (closed) → used Product Support Specialist evergreen instead
- Jobber Retention Specialist → more consultative; skip for now
- Litco Law Client Solutions Receptionist → Lever 404
- Intact Customer Accounts (Edmonton) → careers URL 404 at verify; recheck later
- BITTS Receptionist → not on bitts.ca/jobs (only Exam Proctor)
- FloForm CSR/Estimator → sales/estimating heavy
- Dermapure Receptionist → 2 years + French requirement
- Ellement Member Service Administrator → Workable showed 0 openings at verify
- ATB / Servus → sales-heavy (already skipped)

## Batch 3 notes (AMA)
- [x] Roadside WFH MSR: training Aug 31 2026; evenings/weekends; min 16 hrs/wk
- [x] Retail Support: St. Albert 6-month + Edmonton priority list (same packet)
- [x] Contact details Lillian only; CV 2 pages / cover 1 page
- [x] Portal packets emailed to Lillian

## Send
```bash
python3 scripts/send_lillian_portal_packets.py --dry-run
python3 scripts/send_lillian_portal_packets.py --only ama_roadside,ama_retail --portals-only
python3 scripts/send_lillian_portal_packets.py              # all
```
