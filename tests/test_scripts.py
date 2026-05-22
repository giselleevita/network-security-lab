"""pytest tests for network-security-lab scripts."""

import pytest
import json
import tempfile
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from audit_open_ports import parse_port_range, scan_port
from check_firewall_rules import check_rules, POLICY_CHECKS
from generate_risk_report import parse_risk_register, score_to_level, generate_report


# ─── audit_open_ports tests ───────────────────────────────────────────────────

class TestParsePortRange:
    def test_range(self):
        result = parse_port_range("22-25")
        assert result == [22, 23, 24, 25]

    def test_single(self):
        assert parse_port_range("443") == [443]

    def test_csv(self):
        assert parse_port_range("22,80,443") == [22, 80, 443]


class TestScanPort:
    def test_closed_port(self):
        result = scan_port("127.0.0.1", 19999, timeout=0.3)
        assert result["state"] == "closed"
        assert result["port"] == 19999


# ─── check_firewall_rules tests ───────────────────────────────────────────────

class TestFirewallValidator:
    def _write_rule_file(self, content: str) -> Path:
        tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".conf", delete=False)
        tmp.write(content)
        tmp.flush()
        return Path(tmp.name)

    def test_valid_iptables_passes(self):
        content = """
            -P INPUT DROP
            -P FORWARD DROP
            log prefix "DROP"
            limit rate 4/minute
            ct state established,related accept
        """
        path = self._write_rule_file(content)
        findings = check_rules(path)
        failed = [f for f in findings if f["status"] == "FAIL"]
        assert len(failed) == 0

    def test_missing_default_deny_fails(self):
        content = "# empty config"
        path = self._write_rule_file(content)
        findings = check_rules(path)
        failed_ids = [f["id"] for f in findings if f["status"] == "FAIL"]
        assert "FW-001" in failed_ids
        assert "FW-002" in failed_ids


# ─── generate_risk_report tests ───────────────────────────────────────────────

class TestRiskReport:
    def test_score_to_level(self):
        assert score_to_level(20) == "CRITICAL"
        assert score_to_level(15) == "CRITICAL"
        assert score_to_level(10) == "HIGH"
        assert score_to_level(7) == "MEDIUM"
        assert score_to_level(3) == "LOW"

    def test_generate_report_structure(self):
        mock_risks = [
            {"id": "R-NET-01", "asset": "Firewall", "threat": "Intrusion",
             "vulnerability": "Misconfig", "likelihood": 3, "impact": 5,
             "score": 15, "treatment": "Harden rules", "residual": "LOW"}
        ]
        report = generate_report(mock_risks)
        assert "R-NET-01" in report
        assert "CRITICAL" in report
        assert "Executive Summary" in report

    def test_parse_real_risk_register(self):
        path = Path("isms/risk-register.md")
        if path.exists():
            risks = parse_risk_register(path)
            assert len(risks) > 0
            for r in risks:
                assert "id" in r
                assert "score" in r
