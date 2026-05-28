# Contributing

Thank you for your interest in contributing to network-security-lab.

## Getting started

```bash
git clone https://github.com/giselleevita/network-security-lab
cd network-security-lab
pip install -r requirements.txt
pytest tests/ -v
```

## Branch naming

| Type | Pattern | Example |
|---|---|---|
| Feature | `feat/description` | `feat/zerotrust-segmentation` |
| Bug fix | `fix/description` | `fix/iptables-output-chain` |
| Docs | `docs/description` | `docs/threat-model-update` |
| Rules | `rules/description` | `rules/add-suricata-http-exfil` |

## PR checklist

- [ ] `pytest tests/` passes
- [ ] New firewall rules validated with `check_firewall_rules.py`
- [ ] New IDS/IPS rules include a comment with MITRE ATT&CK technique ID (e.g. `# T1046`)
- [ ] ISMS control mapping updated in `isms/controls.md` if new controls are addressed
- [ ] Threat model updated in `threat-model/` if new attack paths are added
- [ ] No real IP addresses, hostnames, or credentials committed

## Code style

```bash
ruff check scripts/
```

## Adding IDS/IPS rules

- Snort 3 rules go in `ids-ips/snort-local.rules`
- Suricata rules go in `ids-ips/suricata-local.rules`
- Each rule must include a `msg` with a descriptive name and a `classtype`
- Reference MITRE ATT&CK technique IDs in comments where applicable

## Scope

This lab is for **defensive, educational purposes only**. Do not add offensive tooling or active exploitation scripts.
