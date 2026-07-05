"""Forecasting Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_forecast():
    """Test Generate a forecast for a time series with confidence intervals."""
    tools = AgentTools()
    result = await tools.generate_forecast(data="test", horizon=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_seasonality():
    """Test Detect and decompose seasonal patterns in time series data."""
    tools = AgentTools()
    result = await tools.detect_seasonality(data="test", max_period=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_ensemble_forecast():
    """Test Run ensemble of forecasting methods and combine predictions."""
    tools = AgentTools()
    result = await tools.ensemble_forecast(data="test", methods="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_forecast_demand():
    """Test Generate demand forecast with external regressors."""
    tools = AgentTools()
    result = await tools.forecast_demand(historical_demand="test", external_factors="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.forecasting_agent_agent import ForecastingAgentAgent
    agent = ForecastingAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
