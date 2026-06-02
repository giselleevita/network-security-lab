# Case Study: Network Security Lab

## Problem

Many security projects describe controls in policy language but do not connect them to concrete infrastructure. This lab shows how network segmentation, firewall policy, IDS/IPS rules, and ISMS controls can be tied together in a practical environment.

## Solution

The project models a small organization network with segmented zones, hardened firewall rules, IDS/IPS detections, a threat model, a risk register, and Python scripts for validation and reporting.

## Architecture

- VLAN and DMZ segmentation design.
- Stateful firewall rules using iptables and nftables.
- Snort and Suricata local detection rules.
- STRIDE threat model and documented attack paths.
- ISO 27001 Annex A control mapping.
- Python validation and reporting scripts.

## Engineering Choices

- The lab connects security controls to implementation artifacts.
- Scripts make parts of the review process repeatable.
- Threat-model files explain why each control exists.
- ISO mapping makes the technical work legible to governance and audit readers.
- CI validates scripts and policy checks.

## Security And Reliability Controls

- Default-deny firewall posture.
- Inter-zone access control.
- IDS/IPS signatures for common attack paths.
- Risk register and mitigation mapping.
- Automated validation for firewall and reporting scripts.

## What This Shows

This repo is useful for consulting-style interviews because it bridges technical security implementation with documentation, standards mapping, and client-readable risk language.

It also shows that the portfolio is not only AI security; it includes classic infrastructure and security fundamentals.

## Next Improvements

- Add a network topology diagram image.
- Add a reproducible container or VM lab environment.
- Add example generated risk report output.
- Add more tests for firewall policy edge cases.
