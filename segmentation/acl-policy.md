# Inter-VLAN ACL Policy

> ISO 27001 A.8.22 — Segregation of networks

All rules are **deny-by-default**. Only the following explicit permits apply.

## Permit Rules

### LAN (10.20.0.0/24) → Internet
```
permit tcp 10.20.0.0/24 any eq 80
permit tcp 10.20.0.0/24 any eq 443
permit udp 10.20.0.0/24 any eq 53
deny   ip  10.20.0.0/24 any
```

### LAN (10.20.0.0/24) → SERVER (10.50.0.0/24)
```
permit tcp 10.20.0.0/24 10.50.0.0/24 eq 443   # Internal app HTTPS
permit tcp 10.20.0.0/24 10.50.0.0/24 eq 5432  # PostgreSQL (app servers only)
deny   ip  10.20.0.0/24 10.50.0.0/24
```

### DMZ (10.10.0.0/24) → Internet
```
permit tcp 10.10.0.0/24 any eq 80
permit tcp 10.10.0.0/24 any eq 443
permit udp 10.10.0.0/24 any eq 53
deny   ip  10.10.0.0/24 10.20.0.0/24   # No pivot to LAN
deny   ip  10.10.0.0/24 10.50.0.0/24   # No pivot to servers
deny   ip  10.10.0.0/24 any
```

### MGMT (10.40.0.0/24) → All Zones
```
permit tcp 10.40.0.0/24 any eq 22    # SSH
permit tcp 10.40.0.0/24 any eq 443   # HTTPS management
permit udp 10.40.0.0/24 any eq 161   # SNMP monitoring
deny   ip  10.40.0.0/24 any
```

### GUEST (10.30.0.0/24) → Internet only
```
permit tcp 10.30.0.0/24 any eq 80
permit tcp 10.30.0.0/24 any eq 443
deny   ip  10.30.0.0/24 10.0.0.0/8   # No access to any internal zone
deny   ip  10.30.0.0/24 any
```

## Implicit Deny
All traffic not explicitly permitted above is **denied and logged**.
