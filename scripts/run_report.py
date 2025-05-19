"""
Script Entry Point

Wraps CLI logic to run the device report generation.

Example:
  python scripts/run_report.py --output=hostnames.csv
"""

from src.cli.main import main

if __name__ == "__main__":
    main()
