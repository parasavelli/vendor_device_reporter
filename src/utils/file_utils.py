"""
File Utility

Handles CSV file output for the vendor device reporter.

Contents:
  - write_hostnames_to_csv(): Writes a list of hostnames to a .csv file.

Dependencies:
  - pathlib
  - csv

Notes:
  - Output is written to a single-row CSV file: hostname1,hostname2,...
  - The file is overwritten if it already exists.
"""

import csv
from pathlib import Path


def write_hostnames_to_csv(
    hostnames: list[str], file_path: str = "hostnames.csv"
) -> None:
    """
    Writes hostnames to a single-row CSV file.

    Args:
      hostnames (list[str]): List of hostnames to include in the CSV.
      file_path (str): Output file path (default: hostnames.csv).

    Returns:
      None

    Raises:
      OSError: If the file cannot be written to disk.
    """
    output = Path(file_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(hostnames)
