"""
Tests for file utility.

Covers:
  - CSV file is created with correct hostnames
"""

from pathlib import Path

from src.utils.file_utils import write_hostnames_to_csv


def test_write_hostnames_to_csv_creates_expected_file(tmp_path: Path) -> None:
    output = tmp_path / "hostnames.csv"
    hostnames = ["router1", "router2", "switch1"]

    write_hostnames_to_csv(hostnames, file_path=str(output))

    contents = output.read_text().strip()
    assert contents == "router1,router2,switch1"
