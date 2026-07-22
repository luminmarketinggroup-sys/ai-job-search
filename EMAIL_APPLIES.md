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
| 11 | LAG Auto Group | hiring@lagauto.ca | `14e431e7-b07d-4c8b-b592-d2ff7de870d6` | **submitted** |
| 12 | LawDepot | career@lawdepot.ca | `28c53902-f03c-42f2-8d47-78e6c6afdb39` | **submitted** (also careers.lawdepot.com) |
| 13 | Durabuilt Windows & Doors | hr@durabuiltwindows.com | `a7c31d3a-4541-405e-803f-90d352bbc1b2` | **submitted** (also JazzHR if available) |
| 14 | CREATIVE Agency | hello@acreativeagency.ca | `5b2c5cdd-9235-4189-95a9-34fc0f795777` | **submitted** (also finish web form if you can) |
| 15 | Randstad / client | chloe.naccache@randstad.ca | `e3f026a5-97ed-4586-8b43-d369751f259e` | **submitted** (recruiter email from JD) |
| 16 | Executrade (client) | iryna.chubynska@executrade.com | `8b7141d3-7540-4bbb-a3e8-51cec17bf277` | **submitted** (Marketing Generalist #86537) |
| 17 | Ayr Digital | careers@ayr.agency | `a4fdb2a8-81e4-407b-a102-6791d34532ce` | **submitted** (SEO Specialist) |
| 18 | Ayr Digital | careers@ayr.agency | `ce14179d-8b5b-40f0-ba54-488705a928a9` | **submitted** (Digital Marketing Manager) |
| 19 | Ayr Digital | careers@ayr.agency | `d77a9c2f-d0a5-4104-97cb-30740d917a57` | **submitted** (Paid Media Specialist) |
| 20 | Searchlight Digital | tedi@searchlightmarketing.ca | `287259bf-45a4-4e7b-847a-7535f5866432` | **submitted** (SEO & Google Ads Specialist; $40–50/hr) |
| 21 | Dentist Finder | kathan@dentistfinder.ai | `5fd86092-3c05-4575-8e72-e77adf7ff594` | **submitted** (SEO/GEO Specialist; remote Canada) |
| 22 | Home Painters Toronto | Brian@HomePaintersToronto.com | `08a97bfa-ef0b-452e-ad99-82c2d6032037` | **submitted** (Digital Marketing Specialist; remote) |
| 23 | BIS Safety Software | careers@bistraining.ca | `b274b335-52da-4a0b-ac2e-f22fa804b430` | **submitted** (Marketing Manager; also finish careers portal) |
| 24 | Recruitment Partners | careers@rpinc.ca | `57ab0830-dc4b-42a1-b027-51498d972e44` | **submitted** (Marketing Manager client role) |
| 25 | StackAdapt | careers@stackadapt.com | `369f0f23-f5d6-49ae-94c1-2f13be039df2` | **submitted** (Growth Marketing Manager, Integrated Campaigns) |

From: `dylan@luminmarketinggroup.com` · Reply-To/Bcc: `dylanschule@live.ca`

**Still portal-only (cloud cannot complete CAPTCHA):** AMA Member Rewards (`careers.ama.ab.ca`), Keysight, Elevation Capital (Rippling), AutoCanada careers, plus optional Greenhouse/Teamtailor/ADP/Jotform/CREATIVE form follow-ups if email is not enough. Warehouse Priority A needs Desktop browser.

## Pending email (Resend not configured this run — 2026-07-22 daily)

| # | Company | To | Role | Attachments | Status |
|---|---------|-----|------|-------------|--------|
| P1 | Goose Digital | renata@goosedigital.com | Account Lead, Digital Solutions | `cv/main_goose_digital.pdf` + `cover_letters/cover_goose_digital_account_lead.pdf` | **mailto ready** — send when `RESEND_API_KEY` set |
| P2 | Goose Digital | renata@goosedigital.com | Demand Generation Specialist | `cv/main_goose_digital.pdf` + `cover_letters/cover_goose_digital_demand_generation.pdf` | **mailto ready** — send when `RESEND_API_KEY` set |

## Send more later

```bash
python3 scripts/send_ready_emails.py --dry-run
python3 scripts/send_application_email.py --to … --subject … --body … --attach …
```

Key lives in gitignored `.env` only — never commit it.
