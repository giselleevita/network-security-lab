#!/usr/bin/env python3
"""
check_firewall_rules.py
Validates that a firewall rule file conforms to expected security policy.
Checks for: default-deny, logging enabled, SSH rate limiting.
"""

import re
import sys
import argparse
from pathlib import Path

POLICY_CHECKS = [
    {
        "id": "FW-001",
        "name": "Default deny INPUT",
        "pattern": r"policy drop|\-P INPUT DROP",
        "required": True,
    },
    {
        "id": "FW-002",
        "name": "Default deny FORWARD",
        "pattern": r"\-P FORWARD DROP|chain forward.*policy drop",
        "required": True,
    },
    {
        "id": "FW-003",
        "name": "Drop logging enabled",
        "pattern": r"log prefix|log flags",
        "required": True,
    },
    {
        "id": "FW-004",
        "name": "SSH rate limiting",
        "pattern": r"limit rate|--limit|hitcount",
        "required": True,
    },
    {
        "id": "FW-005",
        "name": "Established/related accept",
        "pattern": r"established.*related|ct state established",
        "required": True,
    },
]


def check_rules(filepath: Path) -> list[dict]:
    content = filepath.read_text()
    findings = []
    for check in POLICY_CHECKS:
        matched = bool(re.search(check["pattern"], content, re.IGNORECASE | re.DOTALL))
        status = "PASS" if matched else ("FAIL" if check["required"] else "WARN")
        findings.append({**check, "status": status, "matched": matched})
    return findings


def main():
    parser = argparse.ArgumentParser(description="Firewall rule policy validator")
    parser.add_argument("file", help="Firewall config file to validate")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"[!] File not found: {path}")
        sys.exit(1)

    print(f"[*] Validating: {path.name}\n")
    findings = check_rules(path)

    passed = sum(1 for f in findings if f["status"] == "PASS")
    failed = sum(1 for f in findings if f["status"] == "FAIL")

    for f in findings:
        icon = "✅" if f["status"] == "PASS" else "❌"
        print(f"  {icon} [{f['id']}] {f['name']:40s} — {f['status']}")

    print(f"\n  {passed}/{len(findings)} checks passed.")
    if failed:
        print(f"  ⚠  {failed} policy violation(s) found — review firewall config.")
        sys.exit(1)
    else:
        print("  ✅ All required policy checks passed.")


if __name__ == "__main__":
    main()
