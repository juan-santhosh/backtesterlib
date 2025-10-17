import numpy as np
from portfolio import Portfolio

def compute_metrics(portfolio: Portfolio) -> dict[str, float]:  
    values = portfolio.value_history["Value"]

    if len(values) < 2:
        return {
            "Final Value": portfolio.cash, 
            "Total Return (%)": 0, 
            "Sharpe Ratio": 0, 
            "Number of Trades": 0
        }
    
    returns = values.pct_change().fillna(0)
    
    final_value = values.iloc[-1]
    total_return = ((final_value / values.iloc[0]) - 1) * 100

    sharpe = 0
    if (returns.std() != 0):
        sharpe = (returns.mean() / returns.std()) * np.sqrt(252)

    return {
        "Final Value": round(final_value, 2),
        "Total Return %": round(total_return, 2),
        "Sharpe Ratio": round(sharpe, 2),
        "Number of Trades": len(portfolio.trade_history)
    }