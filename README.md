# Forecasting Agent

[![CI](https://github.com/kogunlowo123/forecasting-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/forecasting-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Business Intelligence | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Business forecasting agent that builds time-series forecasts, combines statistical and ML methods, quantifies prediction uncertainty, detects seasonality, and provides demand planning and capacity forecasts.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_forecast` | Generate a forecast for a time series with confidence intervals |
| `detect_seasonality` | Detect and decompose seasonal patterns in time series data |
| `ensemble_forecast` | Run ensemble of forecasting methods and combine predictions |
| `forecast_demand` | Generate demand forecast with external regressors |
| `evaluate_forecast_accuracy` | Evaluate forecast accuracy against actuals |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/forecast/generate` | Generate forecast |
| `POST` | `/api/v1/forecast/seasonality` | Detect seasonality |
| `POST` | `/api/v1/forecast/ensemble` | Ensemble forecast |
| `POST` | `/api/v1/forecast/demand` | Forecast demand |
| `POST` | `/api/v1/forecast/evaluate` | Evaluate accuracy |

## Features

- Time Series Forecasting
- Ensemble Methods
- Uncertainty Quantification
- Seasonality Detection
- Demand Planning

## Integrations

- Prophet
- Statsmodels
- Sklearn
- Lightgbm
- Nixtla

## Architecture

```
forecasting-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── forecasting_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Prophet + AutoML + Statistical Models + LLM**

---

Built as part of the Enterprise AI Agent Platform.
