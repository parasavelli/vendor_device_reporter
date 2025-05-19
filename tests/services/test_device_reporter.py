"""
Tests for device_reporter orchestration logic.

Covers:
  - End-to-end flow from fetch to file output
"""

from unittest.mock import patch

from src.services.device_reporter import run_device_report


@patch("src.services.device_reporter.write_hostnames_to_csv")
@patch("src.services.device_reporter.fetch_devices")
def test_run_device_report_saves_hostnames(mock_fetch, mock_write) -> None:
    mock_fetch.return_value = [
        {"name": "host1"},
        {"name": "host2"},
    ]

    run_device_report(output_path="test.csv")

    mock_write.assert_called_once_with(["host1", "host2"], "test.csv")
