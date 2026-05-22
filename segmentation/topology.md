# Network Topology

```
                          ┌─────────────────────────────────────┐
                          │           INTERNET                  │
                          └──────────────┬──────────────────────┘
                                         │
                               ┌─────────▼─────────┐
                               │  PERIMETER FW     │
                               │  (nftables)       │
                               │  stateful, L3/L4  │
                               └──┬────┬────┬───┬──┘
                                  │    │    │   │
              ┌───────────────────┘    │    │   └──────────────────┐
              │                        │    │                      │
    ┌─────────▼──────┐    ┌────────────▼┐  ┌▼───────────┐  ┌──────▼──────┐
    │  DMZ           │    │  LAN        │  │ SERVER     │  │ MGMT        │
    │  VLAN 10       │    │  VLAN 20    │  │ VLAN 50    │  │ VLAN 40     │
    │  10.10.0.0/24  │    │  10.20.0.0  │  │ 10.50.0.0  │  │ 10.40.0.0  │
    │                │    │  /24        │  │ /24        │  │ /24        │
    │ [Web Server]   │    │ [Workstns]  │  │ [App DBs]  │  │ [Net Infra] │
    │ [Mail Server]  │    │ [Printers]  │  │            │  │ [Switches]  │
    │ [VPN GW]       │    │             │  │            │  │ [Firewalls] │
    └────────────────┘    └─────────────┘  └────────────┘  └─────────────┘
                                │
                      ┌─────────▼──────┐
                      │  GUEST         │
                      │  VLAN 30       │
                      │  10.30.0.0/24  │
                      │ [Visitor WiFi] │
                      └────────────────┘
```

## Key Security Boundaries

- **Internet → DMZ**: Only defined inbound ports (443, 25, 993)
- **DMZ → LAN/SERVER**: Blocked completely (anti-pivot)
- **LAN → SERVER**: App-layer ports only (443, 5432)
- **GUEST → Internal**: Fully blocked
- **MGMT → All**: SSH/HTTPS management only
- **All zones**: Logged at perimeter firewall
