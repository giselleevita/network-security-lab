# VLAN Architecture & DMZ Design

> ISO 27001 A.8.22 — Segregation of networks

## Network Zones

| VLAN ID | Name | Subnet | Purpose | Trust Level |
|---|---|---|---|---|
| 10 | DMZ | 10.10.0.0/24 | Public-facing services (web, mail, VPN endpoint) | Untrusted |
| 20 | LAN | 10.20.0.0/24 | Internal workstations and file servers | Trusted |
| 30 | GUEST | 10.30.0.0/24 | Guest Wi-Fi, visitor devices | Untrusted |
| 40 | MGMT | 10.40.0.0/24 | Network infrastructure, switches, firewalls | Highly Trusted |
| 50 | SERVER | 10.50.0.0/24 | Internal application and database servers | Trusted |

## Design Principles

### 1. Zero implicit trust between zones
No VLAN can reach another without an explicit ACL permit. Default inter-VLAN policy is **DENY**.

### 2. DMZ isolation
- DMZ hosts can only reach the Internet (outbound) and accept inbound connections on defined ports (443, 25, etc.)
- DMZ **cannot** initiate connections to LAN or SERVER zones
- This prevents a compromised DMZ host from pivoting into the internal network

### 3. MGMT zone hardened access
- Only MGMT VLAN can SSH/HTTPS to network devices
- All management traffic uses dedicated MGMT interfaces
- No user workstations in MGMT zone

### 4. GUEST isolation
- GUEST zone has Internet-only access (TCP 80/443)
- No access to LAN, SERVER, DMZ, or MGMT
- Prevents rogue devices from reaching internal assets

## Traffic Flow Matrix

| Source \ Destination | Internet | DMZ | LAN | SERVER | MGMT | GUEST |
|---|---|---|---|---|---|---|
| **Internet** | — | HTTP/HTTPS/SMTP | ✗ | ✗ | ✗ | ✗ |
| **DMZ** | HTTP/HTTPS | — | ✗ | ✗ | ✗ | ✗ |
| **LAN** | HTTP/HTTPS/DNS | ✗ | — | App ports | ✗ | ✗ |
| **SERVER** | NTP/DNS | ✗ | App ports | — | ✗ | ✗ |
| **MGMT** | HTTPS (updates) | SSH/HTTPS | SSH | SSH | — | ✗ |
| **GUEST** | HTTP/HTTPS | ✗ | ✗ | ✗ | ✗ | — |
