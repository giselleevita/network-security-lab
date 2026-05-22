# IDS/IPS Rules

This directory contains detection rules for two leading open-source IDS/IPS engines:

- **Snort 3** (`snort-local.rules`) — signature-based detection
- **Suricata** (`suricata-rules.yaml`) — multi-threaded, YAML-based

## Covered Threat Categories

| Rule Set | Detects |
|---|---|
| Port scan detection | Nmap SYN, FIN, NULL, XMAS scans |
| Brute force | SSH, RDP, HTTP Basic Auth attempts |
| Reverse shell | Common payloads (bash, python, nc) |
| SQL injection | HTTP parameter injection probes |
| DNS tunnelling | High-entropy TXT queries, long subdomains |
| C2 beaconing | Regular-interval outbound connections |

## Deployment

```bash
# Snort 3
snort -c /etc/snort/snort.lua \
      --plugin-path /etc/snort/plugins \
      -R ids-ips/snort-local.rules \
      -i eth0 -A alert_fast

# Suricata
suricata -c /etc/suricata/suricata.yaml \
         -S ids-ips/suricata-rules.yaml \
         -i eth0
```
