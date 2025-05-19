"""
Device Reporter Service

Coordinates the retrieval of devices from the vendor API and exports
their hostnames to a CSV file.

Contents:
  - run_device_report(): Orchestrates the end-to-end report generation.

Dependencies:
  - api_utils
  - file_utils
  - logging

Notes:
  - Output file is saved as `hostnames.csv` in the working directory.
"""

import logging

from src.utils.api_utils import fetch_devices
from src.utils.file_utils import write_hostnames_to_csv

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run_device_report(output_path: str = "hostnames.csv") -> None:
    """
    Fetches device records from the vendor API and writes their hostnames to a CSV file.

    Args:
      output_path (str): Destination CSV file path (default: hostnames.csv)

    Returns:
      None

    Raises:
      Exception: Bubbles up if fetch or write fails.
    """
    logger.info("Fetching devices from API...")
    devices = fetch_devices()

    hostnames: list[str] = [device["name"] for device in devices if "name" in device]
    logger.info(f"Found {len(hostnames)} hostnames")

    write_hostnames_to_csv(hostnames, output_path)
    logger.info(f"Wrote hostnames to: {output_path}")
