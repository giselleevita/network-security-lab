#!/usr/bin/env python3
"""
audit_open_ports.py
Scans a target host for open ports and flags unexpected services.
ISO 27001 A.8.20 — Network security audit support tool.

Usage:
    python scripts/audit_open_ports.py --target 192.168.1.1
    python scripts/audit_open_ports.py --target 192.168.1.1 --ports 1-1024
"""

import argparse
import socket
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

ALLOWED_PORTS = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    53: "DNS",
    25: "SMTP",
    993: "IMAPS",
}


def scan_port(host: str, port: int, timeout: float = 0.5) -> dict:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            service = ALLOWED_PORTS.get(port, "UNKNOWN")
            expected = port in ALLOWED_PORTS
            return {"port": port, "state": "open", "service": service, "expected": expected}
    except (socket.timeout, ConnectionRefusedError, OSError):
        return {"port": port, "state": "closed", "service": None, "expected": None}


def parse_port_range(port_str: str) -> list[int]:
    if "-" in port_str:
        start, end = port_str.split("-")
        return list(range(int(start), int(end) + 1))
    return [int(p) for p in port_str.split(",")]


def audit(target: str, ports: list[int]) -> dict:
    results = {"target": target, "timestamp": datetime.utcnow().isoformat(), "open_ports": [], "unexpected_ports": []}

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(scan_port, target, p): p for p in ports}
        for future in as_completed(futures):
            result = future.result()
            if result["state"] == "open":
                results["open_ports"].append(result)
                if not result["expected"]:
                    results["unexpected_ports"].append(result)

    results["open_ports"].sort(key=lambda x: x["port"])
    results["unexpected_ports"].sort(key=lambda x: x["port"])
    return results


def main():
    parser = argparse.ArgumentParser(description="Open port auditor")
    parser.add_argument("--target", required=True, help="Target IP or hostname")
    parser.add_argument("--ports", default="1-1024", help="Port range, e.g. 1-1024 or 22,80,443")
    parser.add_argument("--output", help="Output JSON file path (optional)")
    args = parser.parse_args()

    ports = parse_port_range(args.ports)
    print(f"[*] Scanning {args.target} ({len(ports)} ports)...")
    results = audit(args.target, ports)

    print(f"\n[+] Open ports ({len(results['open_ports'])})")
    for p in results["open_ports"]:
        flag = "⚠ UNEXPECTED" if not p["expected"] else "✓"
        print(f"    {flag:15s} {p['port']:5d}/tcp  {p['service']}")

    if results["unexpected_ports"]:
        print(f"\n[!] {len(results['unexpected_ports'])} unexpected port(s) found — investigate immediately.")
    else:
        print("\n[+] All open ports are within expected policy.")

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\n[+] Results saved to {args.output}")

    return results


if __name__ == "__main__":
    main()
