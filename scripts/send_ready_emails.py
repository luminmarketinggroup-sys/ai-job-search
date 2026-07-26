#!/usr/bin/env python3
"""Send all ready email-apply jobs (Connected Creative + Guardium)."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEND = ROOT / "scripts" / "send_application_email.py"

JOBS = [
    {
        "name": "Connected Creative",
        "to": "hannah@connectedcreative.ca",
        "subject": "Marketing Manager application — Dylan Michael (Edmonton)",
        "body": """Hi Hannah,

Please find attached my resume and cover letter for the Marketing Manager role at Connected Creative.

I'm based in Edmonton and currently own marketing for 2 active client accounts at Lumin Marketing Group (SEO, paid media, social, email/CRM, web, and reporting). Happy to send work samples on request.

Thanks,
Dylan Michael
825-967-9337
dylanschule@live.ca
https://www.linkedin.com/in/dylan-michael-993a78392
""",
        "attach": [
            "cv/main_connected_creative.pdf",
            "cover_letters/cover_connected_creative_marketing_manager.pdf",
        ],
    },
    {
        "name": "Guardium Group",
        "to": "info@guardiumgroup.com",
        "subject": "Digital Marketing Specialist — Dylan Michael",
        "body": """Hi,

Please find attached my resume and cover letter for the Digital Marketing Specialist role.

Thanks,
Dylan Michael
825-967-9337
dylanschule@live.ca
https://www.linkedin.com/in/dylan-michael-993a78392
""",
        "attach": [
            "cv/main_example.pdf",
            "cover_letters/cover_guardium_digital_marketing_specialist.pdf",
        ],
    },
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--only",
        choices=["connected", "guardium", "all"],
        default="all",
    )
    args = parser.parse_args()

    selected = JOBS
    if args.only == "connected":
        selected = [JOBS[0]]
    elif args.only == "guardium":
        selected = [JOBS[1]]

    failed = 0
    for job in selected:
        print(f"\n=== {job['name']} ===")
        cmd = [
            sys.executable,
            str(SEND),
            "--to",
            job["to"],
            "--subject",
            job["subject"],
            "--body",
            job["body"],
        ]
        for a in job["attach"]:
            cmd.extend(["--attach", a])
        if args.dry_run:
            cmd.append("--dry-run")
        rc = subprocess.call(cmd, cwd=ROOT)
        if rc != 0:
            failed += 1
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
