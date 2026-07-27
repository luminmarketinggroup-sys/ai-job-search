#!/usr/bin/env python3
"""Send a job-application email via Resend with PDF attachments.

Resend can only send From a verified domain you control.
Personal inbox is attached as Reply-To (default: dylanschule@live.ca).

Env (from .env or process):
  RESEND_API_KEY   required
  RESEND_FROM      default: Dylan Michael <dylan@luminmarketinggroup.com>
  RESEND_REPLY_TO  default: dylanschule@live.ca
  RESEND_BCC       optional (e.g. your live.ca for a sent copy)

Usage:
  python3 scripts/send_application_email.py \\
    --to hannah@connectedcreative.ca \\
    --subject "Marketing Manager application — Dylan Michael (Edmonton)" \\
    --body-file /tmp/body.txt \\
    --attach cv/main_connected_creative.pdf \\
    --attach cover_letters/cover_connected_creative_marketing_manager.pdf
"""

from __future__ import annotations

import argparse
import base64
import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

import resend


ROOT = Path(__file__).resolve().parents[1]


def load_env() -> None:
    if load_dotenv:
        load_dotenv(ROOT / ".env")
    # also allow repo-root .env.local
    if load_dotenv:
        load_dotenv(ROOT / ".env.local", override=True)


def read_body(args: argparse.Namespace) -> str:
    if args.body_file:
        return Path(args.body_file).read_text(encoding="utf-8")
    if args.body:
        return args.body
    raise SystemExit("Provide --body or --body-file")


def main() -> int:
    parser = argparse.ArgumentParser(description="Send application email via Resend")
    parser.add_argument("--to", required=True, help="Recipient email")
    parser.add_argument("--subject", required=True)
    parser.add_argument("--body", help="Plain-text body")
    parser.add_argument("--body-file", help="Path to plain-text body file")
    parser.add_argument(
        "--attach",
        action="append",
        default=[],
        help="Attachment path (repeatable)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print payload summary without sending",
    )
    args = parser.parse_args()
    load_env()

    api_key = os.environ.get("RESEND_API_KEY", "").strip()
    from_addr = os.environ.get(
        "RESEND_FROM", "Dylan Michael <dylan@luminmarketinggroup.com>"
    ).strip()
    reply_to = os.environ.get("RESEND_REPLY_TO", "dylanschule@live.ca").strip()
    bcc = os.environ.get("RESEND_BCC", "").strip()

    body = read_body(args)
    attachments = []
    attach_names = []
    for rel in args.attach:
        path = Path(rel)
        if not path.is_absolute():
            path = ROOT / path
        if not path.exists():
            print(f"ERROR: missing attachment: {path}", file=sys.stderr)
            return 1
        attach_names.append(path.name)
        attachments.append(
            {
                "filename": path.name,
                "content": base64.b64encode(path.read_bytes()).decode("ascii"),
            }
        )

    print(f"From:     {from_addr}")
    print(f"Reply-To: {reply_to}")
    print(f"To:       {args.to}")
    if bcc:
        print(f"Bcc:      {bcc}")
    print(f"Subject:  {args.subject}")
    print(f"Attach:   {attach_names}")

    if args.dry_run:
        print("Dry run — not sent.")
        return 0

    if not api_key:
        print(
            "ERROR: RESEND_API_KEY is not set.\n"
            "Add it to .env (gitignored) or Cursor Cloud environment secrets.\n"
            "See automation/RESEND_SETUP.md",
            file=sys.stderr,
        )
        return 1

    params: dict = {
        "from": from_addr,
        "to": [args.to],
        "subject": args.subject,
        "text": body,
        "reply_to": reply_to,
    }
    if bcc:
        params["bcc"] = [bcc]
    if attachments:
        params["attachments"] = attachments

    resend.api_key = api_key
    result = resend.Emails.send(params)
    # SDK may return dict or object
    email_id = getattr(result, "id", None) or (result.get("id") if isinstance(result, dict) else result)
    print(f"Sent. Resend id: {email_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
