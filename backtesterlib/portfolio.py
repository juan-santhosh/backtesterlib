import pandas as pd

class Portfolio:
    """
    Tracks portfolio cash, position, and value over time.
    """

    def __init__(self, initial_cash: float = 100_000) -> None:
        self.initial_cash: float = initial_cash
        self.cash: float = initial_cash
        self.position: int = 0

        self.trade_history: pd.DataFrame = pd.DataFrame(columns=["Datetime", "Action", "Price"])
        self.value_history: pd.DataFrame = pd.DataFrame(columns=["Datetime", "Value"])

    def _record_trade(self, timestamp, action: str, price) -> None:
        self.trade_history.loc[len(self.trade_history)] = [timestamp, action, price]

    def _record_value(self, timestamp, price) -> None:
        current_value = self.cash + self.position * price
        self.value_history.loc[len(self.value_history)] = [timestamp, current_value]

    def update(self, bar, action: str) -> None:
        """
        Apply a trading action for the given bar.
        Only "BUY" and "SELL" modify positions.
        """

        timestamp = pd.Timestamp(bar["Datetime"])
        price = float(bar["Close"])

        if action in ("BUY", "SELL"):
            if action == "BUY" and self.cash >= price:
                self.position += 1
                self.cash -= price
                
            elif action == "SELL" and self.position > 0:
                self.position -= 1
                self.cash += price

            self._record_trade(timestamp, action, price)

        self._record_value(timestamp, price)