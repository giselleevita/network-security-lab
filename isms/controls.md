# ISO 27001:2022 Annex A — Network Security Controls

> Mapping of implemented technical controls to ISO 27001:2022 Annex A requirements.

## A.8.20 — Networks Security

**Requirement**: Networks shall be managed and controlled to protect information in systems and applications.

| Control Implementation | Location | Status |
|---|---|---|
| Stateful perimeter firewall (nftables) | `firewall/nftables-perimeter.conf` | ✅ Implemented |
| Host-based firewall (iptables) | `firewall/iptables-baseline.sh` | ✅ Implemented |
| IDS/IPS monitoring | `ids-ips/snort-local.rules` | ✅ Implemented |
| Dropped packet logging | `firewall/iptables-baseline.sh` | ✅ Implemented |

---

## A.8.21 — Security of Network Services

**Requirement**: Security mechanisms, service levels and requirements of network services shall be identified, implemented and monitored.

| Control Implementation | Location | Status |
|---|---|---|
| ACL policy per service/VLAN | `segmentation/acl-policy.md` | ✅ Implemented |
| DMZ for public-facing services | `segmentation/vlan-design.md` | ✅ Implemented |
| SSH rate-limiting and key auth | `firewall/iptables-baseline.sh` | ✅ Implemented |
| HTTPS-only management access | `segmentation/acl-policy.md` | ✅ Implemented |

---

## A.8.22 — Segregation of Networks

**Requirement**: Groups of information services, users and information systems shall be segregated in networks.

| Control Implementation | Location | Status |
|---|---|---|
| VLAN segmentation (5 zones) | `segmentation/vlan-design.md` | ✅ Implemented |
| Inter-VLAN deny-by-default ACL | `segmentation/acl-policy.md` | ✅ Implemented |
| DMZ → LAN pivot prevention | `firewall/nftables-perimeter.conf` | ✅ Implemented |
| GUEST → Internal full block | `segmentation/acl-policy.md` | ✅ Implemented |
| MGMT zone isolation | `segmentation/vlan-design.md` | ✅ Implemented |

---

## A.8.23 — Web Filtering

**Requirement**: Access to external websites shall be managed to reduce exposure to malicious content.

| Control Implementation | Location | Status |
|---|---|---|
| Outbound HTTP/HTTPS restriction per zone | `firewall/nftables-perimeter.conf` | ✅ Implemented |
| DNS monitoring for tunnelling | `ids-ips/snort-local.rules` | ✅ Implemented |
| GUEST internet-only policy | `segmentation/acl-policy.md` | ✅ Implemented |

---

## A.8.16 — Monitoring Activities

**Requirement**: Networks shall be monitored for anomalous behaviour.

| Control Implementation | Location | Status |
|---|---|---|
| IDS port scan detection | `ids-ips/snort-local.rules` | ✅ Implemented |
| Brute-force detection (SSH/RDP) | `ids-ips/snort-local.rules` | ✅ Implemented |
| C2 beaconing detection | `ids-ips/suricata-rules.yaml` | ✅ Implemented |
| Reverse shell detection | `ids-ips/snort-local.rules` | ✅ Implemented |
| Firewall drop logging | `firewall/iptables-baseline.sh` | ✅ Implemented |
