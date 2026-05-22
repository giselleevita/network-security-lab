#!/usr/bin/env python3
"""
generate_risk_report.py
Parses the risk register and generates a prioritised Markdown report.
"""

import re
from pathlib import Path
from datetime import datetime

RISK_REGISTER_PATH = Path("isms/risk-register.md")
OUTPUT_PATH = Path("isms/risk-report-generated.md")

RISK_LEVELS = {
    "CRITICAL": (15, 20),
    "HIGH": (10, 14),
    "MEDIUM": (6, 9),
    "LOW": (1, 5),
}


def parse_risk_register(path: Path) -> list[dict]:
    """Parse the markdown risk register table into structured data."""
    content = path.read_text()
    risks = []
    table_pattern = re.compile(
        r"\|\s*(R-NET-\d+)\s*\|([^|]+)\|([^|]+)\|([^|]+)\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)[^|]*\|([^|]+)\|([^|]+)\|"
    )
    for match in table_pattern.finditer(content):
        risks.append({
            "id": match.group(1).strip(),
            "asset": match.group(2).strip(),
            "threat": match.group(3).strip(),
            "vulnerability": match.group(4).strip(),
            "likelihood": int(match.group(5)),
            "impact": int(match.group(6)),
            "score": int(match.group(7)),
            "treatment": match.group(8).strip(),
            "residual": match.group(9).strip(),
        })
    return sorted(risks, key=lambda r: r["score"], reverse=True)


def score_to_level(score: int) -> str:
    for level, (low, high) in RISK_LEVELS.items():
        if low <= score <= high:
            return level
    return "UNKNOWN"


def generate_report(risks: list[dict]) -> str:
    lines = [
        f"# Network Security Risk Report",
        f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n",
        "## Executive Summary\n",
        f"Total risks identified: **{len(risks)}**",
    ]
    for level in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
        count = sum(1 for r in risks if score_to_level(r["score"]) == level)
        if count:
            lines.append(f"- {level}: {count}")
    lines.append("\n## Prioritised Risk List\n")
    for r in risks:
        level = score_to_level(r["score"])
        lines.append(f"### {r['id']} — {r['threat']} ({level}, Score: {r['score']})")
        lines.append(f"- **Asset**: {r['asset']}")
        lines.append(f"- **Vulnerability**: {r['vulnerability']}")
        lines.append(f"- **Likelihood**: {r['likelihood']} | **Impact**: {r['impact']}")
        lines.append(f"- **Treatment**: {r['treatment']}")
        lines.append(f"- **Residual Risk**: {r['residual']}\n")
    return "\n".join(lines)


def main():
    print(f"[*] Parsing risk register from {RISK_REGISTER_PATH}...")
    risks = parse_risk_register(RISK_REGISTER_PATH)
    if not risks:
        print("[!] No risks parsed — check risk register format.")
        return
    report = generate_report(risks)
    OUTPUT_PATH.write_text(report)
    print(f"[+] Report generated: {OUTPUT_PATH} ({len(risks)} risks)")
    print(report[:500])


if __name__ == "__main__":
    main()
