import pandas as pd

class Portfolio:
    def __init__(self, initial_cash: float = 100_000) -> None:
        self.initial_cash = initial_cash

    def simulate(self, data: pd.DataFrame, signals: pd.Series):
        cash = self.initial_cash
        position = 0
        value = []