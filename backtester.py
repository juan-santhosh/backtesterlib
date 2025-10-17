from typing import Callable
from data_handler import DataHandler
from portfolio import Portfolio
from metrics import compute_metrics

class Backtester:
    def __init__(
        self, 
        signal_function: Callable, 
        file_path: str, 
        initial_cash: float = 100_000
    ) -> None:
        self.signal_function = signal_function
        self.data = DataHandler(file_path)
        self.portfolio = Portfolio(initial_cash)
        self.context = {}

    def results(self) -> tuple[Portfolio, dict[str, float]]:
        metrics = compute_metrics(self.portfolio)
        return self.portfolio, metrics

    def run(self) -> tuple[Portfolio, dict[str, float]]:
        while self.data.has_next():
            bar = self.data.next_bar()
            action = self.signal_function(bar, self.context)
            self.portfolio.update(bar, action)

        return self.results()
