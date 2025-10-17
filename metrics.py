import numpy as np
import pandas as pd
from portfolio import Portfolio

def compute_metrics(portfolio: Portfolio) -> dict[str, float]:
    """
    Compute standard backtest performance metrics.
    """

    values = portfolio.value_history["Value"]

    if values.empty or len(values) < 2:
        return {
            "Final Value": portfolio.cash, 
            "Total Return (%)": 0.0, 
            "Sharpe Ratio": 0.0, 
            "Number of Trades": 0.0
        }
    
    returns = values.pct_change().fillna(0.0)
    
    final_value = values.iloc[-1]
    total_return = ((final_value / portfolio.initial_cash) - 1.0) * 100.0

    sharpe = 0.0

    std_returns = returns.std()
    if (std_returns != 0):
        sharpe = (returns.mean() / std_returns) * np.sqrt(252)

    return {
        "Final Value": round(final_value, 2),
        "Total Return %": round(total_return, 2),
        "Sharpe Ratio": round(sharpe, 2),
        "Number of Trades": len(portfolio.trade_history)
    }