import os
from src.data_collection import fetch_stock_data
from src.preprocessing import preprocess_data
from src.eda import plot_data
from src.modeling import train_model

# Step 1: Data Collection
print("Step 1: Data Collection")
raw_data_dir = 'data/raw/'
os.makedirs(raw_data_dir, exist_ok=True)
raw_data_path = os.path.join(raw_data_dir, 'aapl.csv')

data = fetch_stock_data('AAPL', '2020-01-01', '2023-01-01')
data.to_csv(raw_data_path)
print(f"Data collected and saved to {raw_data_path}")

# Step 2: Data Preprocessing
print("Step 2: Data Preprocessing")
processed_data_dir = 'data/processed/'
os.makedirs(processed_data_dir, exist_ok=True)
processed_data_path = os.path.join(processed_data_dir, 'aapl_processed.csv')

processed_data = preprocess_data(raw_data_path)
processed_data.to_csv(processed_data_path)
print(f"Data preprocessed and saved to {processed_data_path}")

# Step 3: Exploratory Data Analysis (EDA)
print("Step 3: Exploratory Data Analysis")
plot_data(processed_data)
print("EDA completed and plots displayed")

# Step 4: Model Training and Evaluation
print("Step 4: Model Training and Evaluation")
model, mae, rmse = train_model(processed_data)
print(f"Model trained. MAE: {mae}, RMSE: {rmse}")

print("All steps completed successfully!")
