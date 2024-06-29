import pandas as pd
import matplotlib.pyplot as plt

def plot_data(data):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['MA50'], label='50-Day Moving Average')
    plt.plot(data['MA200'], label='200-Day Moving Average')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv('data/processed/aapl_processed.csv', index_col='Date', parse_dates=True)
    plot_data(data)
