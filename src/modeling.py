import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

def train_model(data):
    X = data[['MA50', 'MA200']].dropna()
    y = data['Close'].loc[X.index]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    
    return model, mae, rmse

if __name__ == "__main__":
    data = pd.read_csv('data/processed/aapl_processed.csv', index_col='Date', parse_dates=True)
    model, mae, rmse = train_model(data)
    print(f'MAE: {mae}, RMSE: {rmse}')
