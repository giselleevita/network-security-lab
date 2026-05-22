# network-security-lab

> Practical network security hardening for SME infrastructure — firewall policy, network segmentation, IDS/IPS rules, and ISMS controls aligned to ISO 27001 Annex A.

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![ISO 27001](https://img.shields.io/badge/ISO%2027001-Annex%20A-blueviolet)](docs/isms-controls.md)

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
│   ├── nftables-perimeter.conf     # Perimeter firewall (stateful)
│   └── README.md
├── segmentation/
│   ├── vlan-design.md              # VLAN architecture + DMZ design
│   ├── acl-policy.md               # Inter-VLAN ACL policy
│   └── topology.md                 # Network topology diagram (text)
├── ids-ips/
│   ├── snort-local.rules           # Custom Snort detection rules
│   ├── suricata-rules.yaml         # Suricata YAML rule set
│   └── README.md
├── isms/
│   ├── controls.md                 # ISO 27001 Annex A control mapping
│   ├── risk-register.md            # Sample risk register (network scope)
│   └── README.md
├── threat-model/
│   ├── threat-model.md             # STRIDE threat model for SME network
│   └── attack-paths.md             # Documented attack paths + mitigations
├── scripts/
│   ├── audit_open_ports.py         # Port audit script
│   ├── check_firewall_rules.py     # Firewall rule validator
│   └── generate_risk_report.py     # Risk register → Markdown report
├── tests/
│   └── test_scripts.py             # pytest tests for all scripts
└── docs/
    └── references.md               # Standards and references
```

---

## Key Features

| Area | What's Covered |
|---|---|
| **Firewall** | Stateful iptables + nftables perimeter rules, default-deny, explicit allow-lists |
| **Segmentation** | VLAN design (LAN / DMZ / MGMT / GUEST), inter-zone ACL policy |
| **IDS/IPS** | Snort rules for port scans, SQLi probes, reverse shells; Suricata YAML |
| **ISMS** | ISO 27001 A.8.20–A.8.23 network controls mapped to implementations |
| **Threat Model** | STRIDE analysis, attack path documentation, mitigations |
| **Scripts** | Python tools for port auditing, firewall rule validation, risk reporting |

---

## Quick Start

```bash
git clone https://github.com/giselleevita/network-security-lab
cd network-security-lab

# Run Python scripts
pip install -r requirements.txt
python scripts/audit_open_ports.py --target 127.0.0.1
python scripts/generate_risk_report.py

# Run tests
pytest tests/ -v
```

---

## ISMS Alignment

All controls are mapped to **ISO 27001:2022 Annex A** — specifically the network security domain:

- **A.8.20** — Networks security
- **A.8.21** — Security of network services
- **A.8.22** — Segregation of networks
- **A.8.23** — Web filtering

See [`isms/controls.md`](isms/controls.md) for the full mapping.

---

## Threat Model Summary

Based on **STRIDE** methodology applied to a typical SME perimeter:

| Threat | Category | Mitigation |
|---|---|---|
| Port scanning / reconnaissance | Information Disclosure | IDS rules, rate limiting |
| Lateral movement via flat network | Elevation of Privilege | VLAN segmentation, ACLs |
| Unpatched internet-facing service | Tampering | DMZ isolation, WAF rules |
| Credential brute-force (SSH/RDP) | Spoofing | Fail2ban, key-only auth |
| Exfiltration via DNS tunnelling | Information Disclosure | DNS monitoring, Suricata rules |

Full details in [`threat-model/threat-model.md`](threat-model/threat-model.md).

---

## Author

**Giselle Koch** — Cyber Security Engineer  
[github.com/giselleevita](https://github.com/giselleevita) · [linkedin.com/in/giselle-koch](https://linkedin.com/in/giselle-koch)
