import pandas as pd

class DataHandler:
    def __init__(self, file_path: str) -> None:
        self.data = pd.read_csv(file_path, parse_dates=["Datetime"])
        self.data.sort_values("Datetime", inplace=True)
        self.index = 0

    def df(self) -> pd.DataFrame:
        return self.data.copy()