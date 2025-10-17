import pandas as pd
from typing import Callable, Any

from data_handler import DataHandler
from portfolio import Portfolio
from metrics import compute_metrics

class Backtester:
    """
    Runs a backtest using by iterating over supplied historical data.
    """

    def __init__(
        self, 
        signal_function: Callable[[pd.Series, dict[str, Any]], str], 
        file_path: str, 
        initial_cash: float = 100_000
    ) -> None:
        if initial_cash <= 0:
            raise ValueError("Initial cash must be positive.")
        
        if not callable(signal_function):
            raise TypeError("signal_function must be callable.")
        
        if not isinstance(file_path, str):
            raise TypeError("file_path must be a string.")

        self.signal_function = signal_function
        self.data = DataHandler(file_path)
        self.portfolio = Portfolio(initial_cash)
        self.context: dict[str, Any] = {}

    def run(self) -> tuple[Portfolio, dict[str, float]]:
        """
        Executes backtest and returns performance metrics.
        """

        while self.data.has_next():
            bar = self.data.next_bar()

            if not isinstance(bar, pd.Series):
                raise TypeError("DataHandler.next_bar() must return a dict.")
            
            if "Close" not in bar or "Datetime" not in bar:
                raise KeyError("Each bar must contain 'Close' and 'Datetime' keys.")

            action = self.signal_function(bar, self.context)

            if action not in ("BUY", "SELL", "HOLD"):
                raise ValueError(f'Invalid signal: {action}. Must be "BUY", "SELL", or "HOLD"')

            self.portfolio.update(bar, action)

        metrics = compute_metrics(self.portfolio)
        return self.portfolio, metrics
