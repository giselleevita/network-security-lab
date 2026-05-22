#!/bin/bash
# iptables-baseline.sh
# Hardened iptables ruleset for Linux hosts
# ISO 27001 A.8.20 — Network security
# Author: Giselle Koch

set -euo pipefail

IPT="iptables"

echo "[*] Flushing existing rules..."
$IPT -F
$IPT -X
$IPT -t nat -F
$IPT -t nat -X
$IPT -t mangle -F
$IPT -t mangle -X

echo "[*] Setting default policies to DROP..."
$IPT -P INPUT DROP
$IPT -P FORWARD DROP
$IPT -P OUTPUT DROP

# --- LOOPBACK ---
echo "[*] Allowing loopback..."
$IPT -A INPUT  -i lo -j ACCEPT
$IPT -A OUTPUT -o lo -j ACCEPT

# --- ESTABLISHED / RELATED ---
echo "[*] Allowing established/related connections..."
$IPT -A INPUT  -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
$IPT -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# --- ICMP (rate-limited) ---
echo "[*] Allowing rate-limited ICMP..."
$IPT -A INPUT  -p icmp --icmp-type echo-request -m limit --limit 5/s --limit-burst 10 -j ACCEPT
$IPT -A OUTPUT -p icmp -j ACCEPT

# --- SSH (rate-limited, specific source if known) ---
echo "[*] Allowing SSH with rate limiting..."
$IPT -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW \
    -m recent --set --name SSH_BRUTE
$IPT -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW \
    -m recent --update --seconds 60 --hitcount 4 --name SSH_BRUTE -j DROP
$IPT -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -j ACCEPT

# --- DNS (outbound) ---
echo "[*] Allowing outbound DNS..."
$IPT -A OUTPUT -p udp --dport 53 -j ACCEPT
$IPT -A OUTPUT -p tcp --dport 53 -j ACCEPT

# --- HTTP/HTTPS (outbound) ---
echo "[*] Allowing outbound HTTP/HTTPS..."
$IPT -A OUTPUT -p tcp --dport 80  -m conntrack --ctstate NEW -j ACCEPT
$IPT -A OUTPUT -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT

# --- NTP (outbound) ---
$IPT -A OUTPUT -p udp --dport 123 -j ACCEPT

# --- LOG DROPPED PACKETS ---
echo "[*] Enabling drop logging..."
$IPT -A INPUT  -m limit --limit 5/min -j LOG --log-prefix "[IPT-DROP-IN] "  --log-level 4
$IPT -A OUTPUT -m limit --limit 5/min -j LOG --log-prefix "[IPT-DROP-OUT] " --log-level 4

echo "[+] iptables baseline applied successfully."
iptables -L -v -n
