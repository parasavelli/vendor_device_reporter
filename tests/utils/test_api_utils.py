"""
Tests for API utility.

Covers:
  - Successful device fetch with mocked API response
"""

from unittest.mock import MagicMock, patch

from src.utils.api_utils import fetch_devices


@patch("src.utils.api_utils.httpx.Client")
@patch("src.utils.api_utils.get_env_var", return_value="fake-token")
def test_fetch_devices_returns_list(mock_token, mock_client) -> None:
    """
    Ensures fetch_devices returns parsed list when API returns valid JSON.
    """
    # Mock context manager behavior
    mock_instance = MagicMock()
    mock_instance.get.return_value.json.return_value = [
        {"name": "device1"},
        {"name": "device2"},
    ]
    mock_instance.get.return_value.raise_for_status.return_value = None
    mock_client.return_value.__enter__.return_value = mock_instance

    devices = fetch_devices()

    assert isinstance(devices, list)
    assert devices[0]["name"] == "device1"
