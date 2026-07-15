import json
from pathlib import Path


def load_report():
    with open("/app/report.json") as f:
        return json.load(f)


def test_total_requests():
    """Verifies success criterion #1."""
    assert load_report()["total_requests"] == 6


def test_unique_ips():
    """Verifies success criterion #2."""
    assert load_report()["unique_ips"] == 3


def test_top_path():
    """Verifies success criterion #3."""
    assert load_report()["top_path"] == "/index.html"


def test_report_exists():
    """Verifies success criterion #4."""
    assert Path("/app/report.json").exists()


def test_report_not_empty():
    """Verifies success criterion #5."""
    assert Path("/app/report.json").stat().st_size > 0