from backtesterlib import Backtester, plot_portfolio_history

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

backtester = Backtester(sma_test_signal, "../data/MSFT_1h_2y.csv")
portfolio, metrics = backtester.run()

print(metrics)

plot_portfolio_history(portfolio)