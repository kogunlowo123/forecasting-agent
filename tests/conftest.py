"""Test configuration for Forecasting Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "forecasting-agent", "category": "Business Intelligence"}
