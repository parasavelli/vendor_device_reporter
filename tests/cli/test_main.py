"""
Tests for CLI main module.

Covers:
  - CLI argument parsing
  - main() calls report logic
"""

from argparse import Namespace
from unittest.mock import patch

from src.cli.main import main, parse_args


def test_parse_args_returns_namespace(monkeypatch) -> None:
    monkeypatch.setattr("sys.argv", ["prog", "--output", "out.csv"])
    args = parse_args()
    assert isinstance(args, Namespace)
    assert args.output == "out.csv"


@patch("src.cli.main.run_device_report")
def test_main_dispatches_to_report(mock_run, monkeypatch) -> None:
    monkeypatch.setattr("sys.argv", ["prog", "--output", "hostnames.csv"])
    main()
    mock_run.assert_called_once_with(output_path="hostnames.csv")
