import yfinance as yf
import pandas as pd
from datetime import datetime
import sqlite3
import os

data = pd.read_csv("bist100_symbols.csv")
symbols = data['symbol'].tolist()

print(f"Loaded {len(symbols)} symbols from CSV")

def get_yahoo_data(symbols, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance for the given symbols and date range.
    
    Parameters:
    symbols (list): List of stock symbols to fetch data for.
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.
    
    Returns:
    dict: A dictionary with stock symbols as keys and their historical data as values.
    """
    all_data = {}
    successful_downloads = 0
    failed_downloads = 0
    
    for i, symbol in enumerate(symbols, 1):
        try:
            print(f"Downloading {i}/{len(symbols)}: {symbol}")
            stock_data = yf.download(symbol, start=start_date, end=end_date, auto_adjust=True, progress=False)
            
            if not stock_data.empty:
                all_data[symbol] = stock_data
                successful_downloads += 1
            else:
                print(f"No data found for {symbol}")
                failed_downloads += 1
                
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            failed_downloads += 1
    
    print(f"\nDownload Summary:")
    print(f"Successful: {successful_downloads}")
    print(f"Failed: {failed_downloads}")
    
    return all_data

start_date = '2020-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')  # String formatına çevir

print(f"Fetching data from {start_date} to {end_date}")

bist100_data_dict = get_yahoo_data(symbols, start_date, end_date)

if bist100_data_dict:
    
    closing_prices = pd.DataFrame()
    
    for symbol, data in bist100_data_dict.items():
        if 'Close' in data.columns:
            closing_prices[symbol] = data['Close']
    
    if not closing_prices.empty:
        if not os.path.exists("bist100_closing_prices.csv"):
            closing_prices.to_csv("bist100_closing_prices.csv")
            print(f"Closing prices saved to bist100_closing_prices.csv")
            print(f"Data shape: {closing_prices.shape}")
            print("\nFirst 5 rows of closing prices:")
            print(closing_prices.head())
        else:
            print("bist100_closing_prices.csv already exists. Skipping save.")
    else:
        print("No closing price data available")
else:
    print("No data was successfully downloaded")

df=pd.read_csv("bist100_closing_prices.csv")

try:

    conn= sqlite3.connect('finance_data.db')
    cursor=conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS stock_data (symbol TEXT, date TEXT, close REAL)")
    df.to_sql("stock_data", conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()
    print("Data successfully saved to SQLite database.")
    
except sqlite3.Error as e:
    
    print(f"SQLite error: {e}")