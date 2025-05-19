"""
Tests for env_utils.

Covers:
  - get_env_var returns correct value
  - raises on missing required env var
"""

import pytest

from src.utils.env_utils import get_env_var


def test_get_env_var_returns_value(monkeypatch) -> None:
    monkeypatch.setenv("TEST_KEY", "sample-value")
    result = get_env_var("TEST_KEY")
    assert result == "sample-value"


def test_get_env_var_raises_if_missing(monkeypatch) -> None:
    monkeypatch.delenv("MISSING_KEY", raising=False)
    with pytest.raises(EnvironmentError):
        get_env_var("MISSING_KEY", required=True)
