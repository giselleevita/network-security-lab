# STRIDE Threat Model — SME Network

> Methodology: STRIDE (Microsoft)  
> Scope: Perimeter + internal network  
> Author: Giselle Koch

---

## System Description

A typical SME network with:
- Internet-facing web and mail servers in a DMZ
- Internal workstations (LAN zone)
- Application and database servers (SERVER zone)
- Network management infrastructure (MGMT zone)
- Guest Wi-Fi (GUEST zone)

---

## STRIDE Analysis

### S — Spoofing

| Threat | Target | Mitigation |
|---|---|---|
| ARP spoofing on LAN | Workstations / switches | Dynamic ARP Inspection (DAI), static ARP entries for critical hosts |
| SSH credential spoofing | Management servers | Key-only SSH auth, rate limiting |
| IP spoofing inbound | Perimeter firewall | Ingress filtering (RFC 3704), uRPF |

### T — Tampering

| Threat | Target | Mitigation |
|---|---|---|
| Unpatched web service exploited | DMZ web server | DMZ isolation, regular patching, WAF |
| Firewall rule manipulation | nftables config | Config stored in VCS, change control process |
| Log tampering | SIEM / syslog | Append-only remote syslog, hash-chained audit |

### R — Repudiation

| Threat | Target | Mitigation |
|---|---|---|
| Admin action without audit trail | Network devices | Centralised syslog, RADIUS AAA |
| Firewall change without record | Perimeter FW | Git-tracked config, change tickets |

### I — Information Disclosure

| Threat | Target | Mitigation |
|---|---|---|
| Port scanning / reconnaissance | All zones | IDS SYN scan rules, rate limiting |
| DNS tunnelling exfiltration | Internal hosts | Snort/Suricata DNS monitoring |
| Unencrypted management traffic | Switch/router | SSH/HTTPS only in MGMT zone, TLS 1.3 |

### D — Denial of Service

| Threat | Target | Mitigation |
|---|---|---|
| SYN flood on web server | DMZ (10.10.0.10) | Perimeter FW SYN cookies, rate limiting |
| ICMP flood | All zones | ICMP rate limiting in nftables/iptables |
| SSH connection exhaustion | SSH daemon | Rate limiting (4 new conn/min per src) |

### E — Elevation of Privilege

| Threat | Target | Mitigation |
|---|---|---|
| Lateral movement from DMZ → LAN | Internal network | DMZ → LAN ACL deny, VLAN segmentation |
| Compromised workstation → server | SERVER zone | LAN → SERVER app-ports-only ACL |
| Guest device → internal access | Internal zones | GUEST VLAN fully isolated |

---

## Attack Surface Summary

| Entry Point | Exposure | Control |
|---|---|---|
| Internet → DMZ | HIGH | Perimeter FW, IDS, WAF |
| SSH (MGMT) | MEDIUM | Rate limit, key auth, MGMT-only |
| Guest Wi-Fi | LOW | Isolated VLAN, Internet-only |
| Internal LAN | LOW | Segmentation, ACLs |
| DNS | LOW | Monitoring, rate limiting |
