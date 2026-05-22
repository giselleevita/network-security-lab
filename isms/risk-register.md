# Network Security Risk Register

> Scope: SME perimeter and internal network infrastructure  
> Standard: ISO 27001:2022 — Information Security Risk Treatment

| Risk ID | Asset | Threat | Vulnerability | Likelihood (1-5) | Impact (1-5) | Risk Score | Treatment | Residual Risk |
|---|---|---|---|---|---|---|---|---|
| R-NET-01 | Perimeter firewall | External intrusion | Misconfigured rules | 3 | 5 | 15 (HIGH) | Hardened nftables policy + IDS | LOW |
| R-NET-02 | Internal workstations | Lateral movement | Flat network | 4 | 4 | 16 (HIGH) | VLAN segmentation + ACLs | LOW |
| R-NET-03 | SSH management | Brute-force attack | Weak credentials | 4 | 5 | 20 (CRITICAL) | Rate limiting + key-only auth | LOW |
| R-NET-04 | DNS infrastructure | DNS tunnelling/exfil | Unmonitored DNS | 2 | 4 | 8 (MEDIUM) | Snort DNS rules + log monitoring | LOW |
| R-NET-05 | Web server (DMZ) | SQL injection | Unvalidated input | 4 | 4 | 16 (HIGH) | WAF + IDS SQLi rules | MEDIUM |
| R-NET-06 | Guest Wi-Fi | Rogue device pivot | No segmentation | 3 | 4 | 12 (HIGH) | GUEST VLAN isolation | LOW |
| R-NET-07 | Internal servers | C2 beaconing | Undetected malware | 2 | 5 | 10 (MEDIUM) | Suricata C2 detection | LOW |
| R-NET-08 | Network devices | Unauthorised access | Shared credentials | 3 | 5 | 15 (HIGH) | MGMT VLAN + RBAC | LOW |

## Risk Scoring Matrix

| Score | Level | Response |
|---|---|---|
| 1–5 | LOW | Accept / monitor |
| 6–12 | MEDIUM | Treat within 90 days |
| 13–20 | HIGH / CRITICAL | Treat immediately |
