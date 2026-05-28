# Changelog

All notable changes to this project are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.0.0] — 2026

### Added
- `firewall/iptables-baseline.sh` — Linux host hardening ruleset (INPUT/FORWARD/OUTPUT default-deny)
- `firewall/nftables-perimeter.conf` — Stateful perimeter firewall, all chains hardened
- `segmentation/vlan-design.md` — VLAN architecture: LAN / DMZ / MGMT / GUEST / SERVER
- `segmentation/acl-policy.md` — Inter-VLAN ACL policy
- `segmentation/topology.md` — Network topology diagram
- `ids-ips/snort-local.rules` — Snort 3 detection rules (port scan, SQLi, reverse shells)
- `ids-ips/suricata-local.rules` — Suricata rules (C2, RDP brute force, DNS exfiltration)
- `isms/controls.md` — ISO 27001:2022 Annex A control mapping (A.8.16, A.8.20–A.8.23)
- `isms/risk-register.md` — Network risk register
- `threat-model/threat-model.md` — STRIDE threat model
- `threat-model/attack-paths.md` — 5 documented attack paths with mitigations
- `scripts/audit_open_ports.py` — Port audit tool
- `scripts/check_firewall_rules.py` — Firewall policy validator
- `scripts/generate_risk_report.py` — Risk register → Markdown report generator
- `tests/test_scripts.py` — pytest suite for all scripts
- GitHub Actions CI: pytest, firewall validation, ruff linting
