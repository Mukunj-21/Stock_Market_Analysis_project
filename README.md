# Stock Market Analysis Project

## Description
This project is a comprehensive analysis of stock market data for the Apple Inc. (AAPL) stock. It involves collecting historical stock price data, preprocessing the data to add useful features, performing exploratory data analysis (EDA), and building predictive models to forecast future stock prices.

## Features
- **Data Collection**: Fetches historical stock data from Yahoo Finance using the yfinance library and saves it to `data/raw/`.
- **Data Preprocessing**: Cleans the data and adds features such as moving averages (MA50 and MA200), saving the processed data to `data/processed/`.
- **Exploratory Data Analysis (EDA)**: Visualizes stock prices and moving averages to identify trends and patterns.
- **Predictive Modeling**: Builds a linear regression model to predict future stock prices and evaluates the model using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

## Technologies Used
- **Python**: Programming language used for all scripts.
- **Pandas**: For data manipulation and analysis.
- **yfinance**: For fetching historical stock data.
- **Matplotlib**: For data visualization.
- **Scikit-learn**: For building and evaluating the predictive model.
- **Jupyter Notebook**: For detailed analysis and documentation.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/stock-market-analysis.git
    cd stock-market-analysis
    ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the data collection script:
    ```bash
    python src/data_collection.py
    ```
2. Preprocess the data:
    ```bash
    python src/preprocessing.py
    ```
3. Perform EDA:
    ```bash
    python src/eda.py
    ```
4. Train and evaluate the model:
    ```bash
    python src/modeling.py
    ```

Alternatively, you can run all the steps at once:
```bash
python main.py
