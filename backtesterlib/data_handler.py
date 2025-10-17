import pandas as pd
from pathlib import Path

class DataHandler:
    """
    Loads and iterates through market data from a CSV file.\n
    Expecting "Datetime" column as the index.
    """
    
    def __init__(self, file_path: str) -> None:
        if not Path(file_path).exists():
            raise FileNotFoundError(f"Data file not found: {file_path}")
        
        self.data: pd.DataFrame = pd.read_csv(file_path, parse_dates=["Datetime"])
        self._validate_columns()
        self.data = self.data.sort_values("Datetime").reset_index(drop=True)

        self.index: int = 0
        self.length: int = len(self.data)

    def _validate_columns(self) -> None:
        required = {"Datetime", "Close"}
        missing = required.difference(self.data.columns)

        if missing:
            raise ValueError(f"Missing required columns: {', '.join(missing)}")

    def has_next(self) -> bool:
        """Check if there are more bars to process."""
        return self.index < len(self.data)

    def next_bar(self) -> pd.Series:
        """Return the next bar of market data."""
        if not self.has_next():
            raise StopIteration("No more bars available in DataHandler.")
        
        bar = self.data.iloc[self.index]
        self.index += 1
        
        return bar