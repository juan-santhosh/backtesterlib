import pandas as pd

class Portfolio:
    def __init__(self, initial_cash: float = 100_000) -> None:
        self.cash = initial_cash
        self.position = 0

        self.trade_history = pd.DataFrame(columns=["Datetime", "Action", "Price"])
        self.value_history = pd.DataFrame(columns=["Datetime", "Value"])

    def record_trade(self, timestamp, action: str, price) -> None:
        self.trade_history.loc[len(self.trade_history)] = [timestamp, action, price]

    def record_value(self, timestamp, price) -> None:
        current_value = self.cash + self.position * price
        self.value_history.loc[len(self.value_history)] = [timestamp, current_value]

    def update(self, bar, action: str) -> None:
        timestamp = bar["Datetime"]
        price = bar["Close"]

        if action in ("BUY", "SELL"):
            if action == "BUY" and self.cash >= price:
                self.position += 1
                self.cash -= price
                
            elif action == "SELL" and self.position > 0:
                self.position -= 1
                self.cash += price

            self.record_trade(timestamp, action, price)

        self.record_value(timestamp, price)