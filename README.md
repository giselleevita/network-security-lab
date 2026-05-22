# network-security-lab

> Practical network security hardening for SME infrastructure — firewall policy, network segmentation, IDS/IPS rules, and ISMS controls aligned to ISO 27001 Annex A.

[![CI](https://github.com/giselleevita/network-security-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/giselleevita/network-security-lab/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![ISO 27001](https://img.shields.io/badge/ISO%2027001-Annex%20A-blueviolet)](isms/controls.md)

---

## Overview

This lab simulates the security hardening of a typical SME network environment. It covers the full lifecycle from **threat modelling** → **network segmentation design** → **firewall policy** → **IDS/IPS deployment** → **ISMS control mapping**.

The architecture mirrors environments commonly found at IT security consultancies and their clients: a perimeter firewall, segmented internal zones, a DMZ for public-facing services, and monitoring infrastructure.

---

## Repository Structure

```
network-security-lab/
├── firewall/
│   ├── iptables-baseline.sh        # Linux host hardening ruleset
│   ├── nftables-perimeter.conf     # Perimeter firewall (stateful, all chains hardened)
│   └── README.md
├── segmentation/
│   ├── vlan-design.md              # VLAN architecture + DMZ design
│   ├── acl-policy.md               # Inter-VLAN ACL policy
│   └── topology.md                 # Network topology diagram
├── ids-ips/
│   ├── snort-local.rules           # Snort 3 detection rules
│   ├── suricata-local.rules        # Suricata detection rules (.rules format)
│   └── README.md
├── isms/
│   ├── controls.md                 # ISO 27001 Annex A control mapping
│   ├── risk-register.md            # Network risk register
│   └── README.md
├── threat-model/
│   ├── threat-model.md             # STRIDE threat model
│   └── attack-paths.md             # Attack paths + mitigations
├── scripts/
│   ├── audit_open_ports.py         # Port audit tool
│   ├── check_firewall_rules.py     # Firewall policy validator
│   └── generate_risk_report.py     # Risk register → Markdown report
├── tests/
│   └── test_scripts.py             # pytest suite
└── docs/
    └── references.md               # Standards and references
```

---

## Key Features

| Area | What's Covered |
|---|---|
| **Firewall** | Stateful iptables + nftables — all chains hardened (INPUT/FORWARD/OUTPUT default-deny) |
| **Segmentation** | VLAN design (LAN / DMZ / MGMT / GUEST / SERVER), inter-zone ACL policy |
| **IDS/IPS** | Snort rules for port scans, SQLi, reverse shells; Suricata rules for C2, RDP brute force, DNS exfil |
| **ISMS** | ISO 27001 A.8.16, A.8.20–A.8.23 mapped to concrete implementations |
| **Threat Model** | STRIDE analysis, 5 documented attack paths with mitigations |
| **Scripts** | Python tools: port auditor, firewall validator, risk report generator |
| **CI** | GitHub Actions: pytest, firewall policy validation, ruff linting |

---

## Quick Start

```bash
git clone https://github.com/giselleevita/network-security-lab
cd network-security-lab

pip install -r requirements.txt

# Audit open ports
python scripts/audit_open_ports.py --target 127.0.0.1

# Validate firewall rules
python scripts/check_firewall_rules.py firewall/iptables-baseline.sh
python scripts/check_firewall_rules.py firewall/nftables-perimeter.conf

# Generate risk report
python scripts/generate_risk_report.py

# Run tests
pytest tests/ -v
```

---

## ISMS Alignment

All controls mapped to **ISO 27001:2022 Annex A** — network security domain:

- **A.8.16** — Monitoring activities
- **A.8.20** — Networks security
- **A.8.21** — Security of network services
- **A.8.22** — Segregation of networks
- **A.8.23** — Web filtering

See [`isms/controls.md`](isms/controls.md) for the full mapping.

---

## Threat Model Summary

| Threat | Category | Mitigation |
|---|---|---|
| Port scanning / reconnaissance | Information Disclosure | IDS rules, rate limiting |
| Lateral movement via flat network | Elevation of Privilege | VLAN segmentation, ACLs |
| Unpatched internet-facing service | Tampering | DMZ isolation, WAF rules |
| Credential brute-force (SSH/RDP) | Spoofing | Rate limiting, key-only auth |
| DNS tunnelling / data exfil | Information Disclosure | Snort + Suricata DNS rules |
| C2 beaconing | Tampering | Suricata interval detection |

Full details in [`threat-model/`](threat-model/).

---

## Author

**Giselle Koch** — Cyber Security Engineer  
[github.com/giselleevita](https://github.com/giselleevita) · [linkedin.com/in/giselle-koch](https://linkedin.com/in/giselle-koch)
