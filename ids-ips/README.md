# IDS/IPS Rules

This directory contains detection rules for two leading open-source IDS/IPS engines:

- **Snort 3** (`snort-local.rules`) — signature-based detection
- **Suricata** (`suricata-local.rules`) — multi-threaded, standard `.rules` format

## Covered Threat Categories

| Rule File | Detects |
|---|---|
| `snort-local.rules` | SYN/FIN/NULL/XMAS scans, SSH brute force, SQLi probes, reverse shells, DNS tunnelling |
| `suricata-local.rules` | C2 beaconing, RDP brute force, HTTP Basic Auth brute, DNS exfil, ICMP flood, SMB lateral movement |

## Deployment

```bash
# Snort 3
snort -c /etc/snort/snort.lua \
      --plugin-path /etc/snort/plugins \
      -R ids-ips/snort-local.rules \
      -i eth0 -A alert_fast

# Suricata — add to suricata.yaml:
# rule-files:
#   - /path/to/ids-ips/suricata-local.rules
suricata -c /etc/suricata/suricata.yaml -i eth0
```

## Testing Rules

```bash
# Validate Snort rules syntax
snort -c /etc/snort/snort.lua -R ids-ips/snort-local.rules --test-mode

# Validate Suricata rules syntax
suricata -T -c /etc/suricata/suricata.yaml -S ids-ips/suricata-local.rules
```
