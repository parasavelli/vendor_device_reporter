"""
API Utility

Handles API requests to retrieve device data from the vendor system.

Contents:
  - fetch_devices(): Calls external API and returns the parsed device list.

Dependencies:
  - httpx
  - dotenv
  - src.utils.env_utils

Notes:
  - Token is pulled from environment via VENDOR_API_TOKEN
"""

import httpx

from src.utils.env_utils import get_env_var

API_URL = "https://vendor.vendorapi.net/rest/getDevices"


def fetch_devices() -> list[dict]:
    """
    Calls the vendor API and returns a list of device records.

    Returns:
      list[dict]: Raw JSON array containing device information.

    Raises:
      httpx.HTTPError: On network failure or invalid response.
      ValueError: If the API response format is invalid.
    """
    token = get_env_var("VENDOR_API_TOKEN", required=True)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    with httpx.Client(timeout=10.0) as client:
        response = client.get(API_URL, headers=headers)
        response.raise_for_status()

    data = response.json()

    if not isinstance(data, list):
        raise ValueError("Expected a list in API response")

    return data
