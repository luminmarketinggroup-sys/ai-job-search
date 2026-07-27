#!/usr/bin/env python3
"""Send Lillian Schule Zech portal packets and mailto applications via Resend.

Portal employers -> email packet to schulezechlillian@gmail.com with links + PDFs.
Mailto employers -> email employer with Reply-To Lillian, BCC Lillian.

Env:
  RESEND_API_KEY   required
  RESEND_FROM      default: Lillian Schule Zech <dylan@luminmarketinggroup.com>
  RESEND_REPLY_TO  default: schulezechlillian@gmail.com
"""

from __future__ import annotations

import argparse
import base64
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKETS = ROOT / "candidates" / "lillian" / "email_packets"
SEND = ROOT / "scripts" / "send_application_email.py"

LILLIAN = "schulezechlillian@gmail.com"

PORTALS = {
    "general_bank": {
        "subject": "Ready to apply: General Bank CSR I — resume + cover letter attached",
        "body": PACKETS / "portal_general_bank.txt",
        "attach": [
            ROOT / "candidates/lillian/cv/main_general_bank.pdf",
            ROOT / "candidates/lillian/cover_letters/cover_general_bank_csr_i.pdf",
        ],
    },
    "dynacare": {
        "subject": "Ready to apply: Dynacare Call Attendant (Remote) — resume + cover letter attached",
        "body": PACKETS / "portal_dynacare.txt",
        "attach": [
            ROOT / "candidates/lillian/cv/main_dynacare.pdf",
            ROOT / "candidates/lillian/cover_letters/cover_dynacare_call_attendant.pdf",
        ],
    },
    "atco": {
        "subject": "Ready to apply: ATCO Gas Customer Care Rep (Temp) — resume + cover letter attached",
        "body": PACKETS / "portal_atco.txt",
        "attach": [
            ROOT / "candidates/lillian/cv/main_atco.pdf",
            ROOT / "candidates/lillian/cover_letters/cover_atco_customer_care_representative.pdf",
        ],
    },
    "alberta_blue_cross": {
        "subject": "Ready to apply: Alberta Blue Cross Claims Coordinator — resume + cover letter attached",
        "body": PACKETS / "portal_alberta_blue_cross.txt",
        "attach": [
            ROOT / "candidates/lillian/cv/main_alberta_blue_cross.pdf",
            ROOT / "candidates/lillian/cover_letters/cover_alberta_blue_cross_claims_coordinator.pdf",
        ],
    },
    "jobber": {
        "subject": "Ready to apply: Jobber Product Support Specialist — resume + cover letter attached",
        "body": PACKETS / "portal_jobber.txt",
        "attach": [
            ROOT / "candidates/lillian/cv/main_jobber.pdf",
            ROOT / "candidates/lillian/cover_letters/cover_jobber_product_support_specialist.pdf",
        ],
    },
    "royal_glenora": {
        "subject": "Ready to apply: Royal Glenora Front Desk Member Services — resume + cover letter attached",
        "body": PACKETS / "portal_royal_glenora.txt",
        "attach": [
            ROOT / "candidates/lillian/cv/main_royal_glenora.pdf",
            ROOT / "candidates/lillian/cover_letters/cover_royal_glenora_front_desk_member_services.pdf",
        ],
    },
    "ama_roadside": {
        "subject": "Ready to apply: AMA Roadside Member Service Rep (WFH) — resume + cover letter attached",
        "body": PACKETS / "portal_ama_roadside.txt",
        "attach": [
            ROOT / "candidates/lillian/cv/main_ama_roadside.pdf",
            ROOT / "candidates/lillian/cover_letters/cover_ama_member_service_representative_roadside.pdf",
        ],
    },
    "ama_retail": {
        "subject": "Ready to apply: AMA Retail Support Agent (St. Albert + Edmonton) — resume + cover letter attached",
        "body": PACKETS / "portal_ama_retail.txt",
        "attach": [
            ROOT / "candidates/lillian/cv/main_ama_retail.pdf",
            ROOT / "candidates/lillian/cover_letters/cover_ama_retail_support_agent.pdf",
        ],
    },
}

MAILTOS = {
    "peace_hills": {
        "to": "sclawson@phgic.com",
        "subject": "Claims Advisor – Property application — Lillian Schule Zech (Edmonton)",
        "body": PACKETS / "mailto_peace_hills_employer.txt",
        "attach": [
            ROOT / "candidates/lillian/cv/main_peace_hills.pdf",
            ROOT / "candidates/lillian/cover_letters/cover_peace_hills_claims_advisor_property.pdf",
        ],
        "lillian_copy_body": PACKETS / "mailto_peace_hills_lillian_copy.txt",
        "lillian_copy_subject": "Copy: Peace Hills Claims Advisor email application prepared for you",
    },
    "trans_global": {
        "to": "careers@thebrick.com",
        "subject": "Creditor Insurance Claims Representative application — Lillian Schule Zech (Edmonton)",
        "body": PACKETS / "mailto_trans_global_employer.txt",
        "attach": [
            ROOT / "candidates/lillian/cv/main_trans_global.pdf",
            ROOT / "candidates/lillian/cover_letters/cover_trans_global_creditor_claims_representative.pdf",
        ],
        "lillian_copy_body": None,
        "lillian_copy_subject": None,
    },
}


def run_send(to: str, subject: str, body: Path, attach: list[Path], dry_run: bool) -> int:
    env = os.environ.copy()
    env.setdefault(
        "RESEND_FROM",
        "Lillian Schule Zech <dylan@luminmarketinggroup.com>",
    )
    env.setdefault("RESEND_REPLY_TO", LILLIAN)
    # Always BCC Lillian so she has a sent copy for employer mailtos
    if to.lower() != LILLIAN.lower():
        env["RESEND_BCC"] = LILLIAN
    cmd = [
        sys.executable,
        str(SEND),
        "--to",
        to,
        "--subject",
        subject,
        "--body-file",
        str(body),
    ]
    for path in attach:
        cmd.extend(["--attach", str(path)])
    if dry_run:
        cmd.append("--dry-run")
    print("\n===", subject, "===")
    return subprocess.call(cmd, cwd=str(ROOT), env=env)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--only",
        help="Comma-separated keys from portals/mailtos (e.g. general_bank,peace_hills)",
    )
    parser.add_argument(
        "--portals-only",
        action="store_true",
        help="Only email portal packets to Lillian",
    )
    parser.add_argument(
        "--mailtos-only",
        action="store_true",
        help="Only send employer mailto applications",
    )
    args = parser.parse_args()

    only = {x.strip() for x in args.only.split(",")} if args.only else None
    failures = 0

    if not args.mailtos_only:
        for key, item in PORTALS.items():
            if only and key not in only:
                continue
            code = run_send(
                LILLIAN,
                item["subject"],
                item["body"],
                item["attach"],
                args.dry_run,
            )
            failures += 0 if code == 0 else 1

    if not args.portals_only:
        for key, item in MAILTOS.items():
            if only and key not in only:
                continue
            code = run_send(
                item["to"],
                item["subject"],
                item["body"],
                item["attach"],
                args.dry_run,
            )
            failures += 0 if code == 0 else 1
            # Optional heads-up copy to Lillian for Peace Hills
            if item.get("lillian_copy_body") and (not only or key in only):
                code2 = run_send(
                    LILLIAN,
                    item["lillian_copy_subject"],
                    item["lillian_copy_body"],
                    item["attach"],
                    args.dry_run,
                )
                failures += 0 if code2 == 0 else 1

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
