import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

if __name__ == "__main__":
    data = fetch_stock_data('AAPL', '2020-01-01', '2023-01-01')
    data.to_csv('data/raw/aapl.csv')
