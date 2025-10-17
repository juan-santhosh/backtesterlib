import matplotlib.pyplot as plt
from .portfolio import Portfolio

def plot_portfolio_history(portfolio: Portfolio):
    value_history = portfolio.value_history["Value"]

    plt.figure(figsize=(10, 5))
    plt.plot(value_history, label="Value")
    plt.title("Portfolio Value Over Time")
    plt.xlabel("Date")
    plt.ylabel("Porfolio Value ($)")

    buys = portfolio.trade_history[portfolio.trade_history["Action"] == "BUY"]
    sells = portfolio.trade_history[portfolio.trade_history["Action"] == "SELL"]

    if not buys.empty:
        plt.scatter(
            x=buys.index, y=value_history[buys.index],
            color="green", marker="^", label="Buy", s=10
        )

    if not sells.empty:
        plt.scatter(
            x=sells.index, y=value_history[sells.index],
            color="red", marker="v", label="Sell", s=10
        )

    plt.legend()
    plt.grid(True)
    plt.show()