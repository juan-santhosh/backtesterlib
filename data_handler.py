import pandas as pd

class DataHandler:
    def __init__(self, file_path: str) -> None:
        self.data = pd.read_csv(file_path, parse_dates=["Datetime"])
        self.data.sort_values("Datetime", inplace=True)
        self.index = 0

    def has_next(self) -> bool:
        return self.index < len(self.data)

    def next_bar(self) -> pd.Series:
        bar = self.data.iloc[self.index]
        self.index += 1
        
        return bar