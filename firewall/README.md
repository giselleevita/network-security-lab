# Firewall Configurations

This directory contains hardened firewall rule sets for two common deployment scenarios:

1. **`iptables-baseline.sh`** — Linux host-level hardening (servers, workstations)
2. **`nftables-perimeter.conf`** — Perimeter firewall for network edge

## Design Principles

- **Default-deny** on all chains (INPUT, OUTPUT, FORWARD)
- Explicit allow-lists only — no implicit permits
- Stateful connection tracking for all allowed traffic
- Rate limiting on SSH and ICMP to prevent brute-force and flood
- Logging of all dropped packets for IDS/SIEM correlation

## Deployment

```bash
# Apply iptables baseline (run as root)
bash firewall/iptables-baseline.sh

# Apply nftables perimeter config
nft -f firewall/nftables-perimeter.conf
```

## Testing

After applying, verify with:
```bash
iptables -L -v -n           # Check iptables rules
nft list ruleset            # Check nftables rules
nmap -sS -p 1-1024 <host>   # Verify closed ports from outside
```
