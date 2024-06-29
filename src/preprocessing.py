import pandas as pd

def preprocess_data(filepath):
    data = pd.read_csv(filepath, index_col='Date', parse_dates=True)
    data.dropna(inplace=True)
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()
    return data

if __name__ == "__main__":
    data = preprocess_data('data/raw/aapl.csv')
    data.to_csv('data/processed/aapl_processed.csv')
