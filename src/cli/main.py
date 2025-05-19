"""
CLI Entrypoint

Parses command-line arguments and runs the device report job.

Contents:
  - parse_args(): Parses CLI arguments
  - main(): CLI dispatcher to call service logic

Dependencies:
  - argparse
  - src.services.device_reporter.run_device_report

Notes:
  - Output CSV path is optional; defaults to `hostnames.csv`
"""

import argparse

from src.services.device_reporter import run_device_report


def parse_args() -> argparse.Namespace:
    """
    Parses CLI arguments for output file.

    Returns:
      argparse.Namespace: Parsed arguments including output path.
    """
    parser = argparse.ArgumentParser(description="Vendor Device Reporter CLI")
    parser.add_argument(
        "--output",
        default="hostnames.csv",
        help="Path to output CSV file (default: hostnames.csv)",
    )
    return parser.parse_args()


def main() -> None:
    """
    CLI dispatcher that invokes the report generator.
    """
    args = parse_args()
    run_device_report(output_path=args.output)


if __name__ == "__main__":
    main()
