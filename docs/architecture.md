# Forecasting Agent Architecture

Business forecasting agent that builds time-series forecasts, combines statistical and ML methods, quantifies prediction uncertainty, detects seasonality, and provides demand planning and capacity forecasts.

## Domain Tools

- **generate_forecast**: Generate a forecast for a time series with confidence intervals
- **detect_seasonality**: Detect and decompose seasonal patterns in time series data
- **ensemble_forecast**: Run ensemble of forecasting methods and combine predictions
- **forecast_demand**: Generate demand forecast with external regressors
- **evaluate_forecast_accuracy**: Evaluate forecast accuracy against actuals