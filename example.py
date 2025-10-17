import pandas as pd
from backtester import Backtester

def sma_test_signal(data: pd.DataFrame, context: dict):
    short_window = 5
    long_window = 20

    data["SMA Short"] = data["Close"].rolling(short_window).mean()
    data["SMA Long"] = data["Close"].rolling(long_window).mean()
    
    signal = pd.Series("HOLD", index=data.index)
    signal[data["SMA Short"] > data["SMA Long"]] = "BUY"
    signal[data["SMA Short"] < data["SMA Long"]] = "SELL"

    return signal

backtester = Backtester(sma_test_signal, "../data/MSFT_1h_2y.csv")
portfolio, metrics = backtester.run()

print("\nPerformance Summary:")
for metric, value in metrics.items():
    print(f"{metric:20s}: {value}")