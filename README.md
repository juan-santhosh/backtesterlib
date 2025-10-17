# BacktesterLib

A modular, extensible Python backtesting engine that takes user-written signals and tests it over supplied historical time-series data.

## Example Usage

```python
from backtesterlib import Backtester, plot_portfolio_history

# Example SMA signal to test backtester. Signal function should return "BUY", "SELL", or "HOLD"
def sma_test_signal(bar, context):
    prices = context.setdefault("prices", [])
    prices.append(bar["Close"])

    if len(prices) < 20:
        return "HOLD"
    
    short_ma = sum(prices[-5:]) / 5
    long_ma = sum(prices[-20:]) / 20

    if short_ma > long_ma:
        return "BUY"
    elif short_ma < long_ma:
        return "SELL"
    
    return "HOLD"

# Pass in signal function, file path to data, and optionally initial cash (defaults to $100,000)
backtester = Backtester(sma_test_signal, "../data/MSFT_1h_2y.csv")

# Runs backtester and returns portfolio object and performance metrics
portfolio, metrics = backtester.run()

print(metrics)

plot_portfolio_history(portfolio) # Plot portfolio value over time with trade history
