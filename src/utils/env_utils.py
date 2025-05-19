"""
Environment Utility

Loads and validates environment variables using os.environ and dotenv support.

Contents:
  - get_env_var(): Safely retrieves environment values with optional fallback.

Dependencies:
  - os
  - dotenv (python-dotenv)

Notes:
  - Automatically loads .env at module import.
  - Used to access VENDOR_API_TOKEN securely.
"""

import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


def get_env_var(
    name: str, default: Optional[str] = None, required: bool = False
) -> str:
    """
    Loads an environment variable, with optional default and validation.

    Args:
      name (str): Environment variable key.
      default (Optional[str]): Fallback value if not found.
      required (bool): If True, raises if variable is not found or empty.

    Returns:
      str: Final resolved environment value.

    Raises:
      EnvironmentError: If required variable is missing or empty.
    """
    value = os.getenv(name, default)

    if required and not value:
        raise EnvironmentError(f"Missing required environment variable: {name}")

    assert value is not None
    return value
