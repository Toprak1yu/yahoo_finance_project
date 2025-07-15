"""
BIST 100 Stock Data Fetcher and Database Manager

This script fetches historical stock data for BIST 100 (Borsa Istanbul 100) companies
from Yahoo Finance API and stores the data in both CSV format and SQLite database.

Features:
- Fetches historical data from 2020 to current date
- Handles missing or delisted stocks gracefully
- Saves closing prices in CSV format
- Stores data in SQLite database for efficient querying
- Provides download progress and error reporting

Author: Aziz Toprak Yilmaz
Created: July 2025

"""

import yfinance as yf
import pandas as pd
from datetime import datetime
import sqlite3
import os

# Load stock symbols from CSV file
# The CSV should contain a 'symbol' column with stock symbols like 'AKBNK.IS'
data = pd.read_csv("bist100_symbols.csv")
symbols = data['symbol'].tolist()

print(f"Loaded {len(symbols)} symbols from CSV")

def get_yahoo_data(symbols, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance for the given symbols and date range.
    
    This function downloads OHLCV (Open, High, Low, Close, Volume) data for each symbol
    and handles errors gracefully by continuing with the next symbol if one fails.
    
    Parameters:
    -----------
    symbols : list
        List of stock symbols to fetch data for (e.g., ['AKBNK.IS', 'THYAO.IS'])
    start_date : str
        Start date in 'YYYY-MM-DD' format
    end_date : str
        End date in 'YYYY-MM-DD' format
    
    Returns:
    --------
    dict
        A dictionary with stock symbols as keys and their historical data (pandas DataFrame) as values
        
    """
    all_data = {}
    successful_downloads = 0
    failed_downloads = 0
    
    # Iterate through each symbol and download data
    for i, symbol in enumerate(symbols, 1):
        try:
            print(f"Downloading {i}/{len(symbols)}: {symbol}")
            
            # Download stock data from Yahoo Finance
            # auto_adjust=True applies stock splits and dividends adjustments
            # progress=False suppresses the download progress bar for cleaner output
            stock_data = yf.download(symbol, start=start_date, end=end_date, auto_adjust=True, progress=False)
            
            # Check if data was successfully downloaded
            if not stock_data.empty:
                all_data[symbol] = stock_data
                successful_downloads += 1
            else:
                print(f"No data found for {symbol}")
                failed_downloads += 1
                
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            failed_downloads += 1
    
    # Print download summary
    print(f"\nDownload Summary:")
    print(f"Successful: {successful_downloads}")
    print(f"Failed: {failed_downloads}")
    
    return all_data

# Define date range for data fetching
# Start from 2020 to get sufficient historical data for analysis
start_date = '2020-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')  # Current date in string format

print(f"Fetching data from {start_date} to {end_date}")

# Fetch all stock data
bist100_data_dict = get_yahoo_data(symbols, start_date, end_date)

# Process and save the data if any was successfully downloaded
if bist100_data_dict:
    
    # Create a DataFrame to store closing prices for all stocks
    # This creates a time series with dates as index and stock symbols as columns
    closing_prices = pd.DataFrame()
    
    # Extract closing prices from each stock's data
    for symbol, data in bist100_data_dict.items():
        if 'Close' in data.columns:
            closing_prices[symbol] = data['Close']
    
    # Save closing prices to CSV if data exists
    if not closing_prices.empty:
        # Check if file already exists to avoid overwriting
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

# Load the saved CSV data for database operations
df = pd.read_csv("bist100_closing_prices.csv")

# Save data to SQLite database for efficient querying and analysis
try:
    # Connect to SQLite database (creates file if it doesn't exist)
    conn = sqlite3.connect('finance_data.db')
    cursor = conn.cursor()

    # Create table structure if it doesn't exist
    # This table will store stock data in a normalized format
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_data (
            symbol TEXT,     -- Stock symbol (e.g., 'AKBNK.IS')
            date TEXT,       -- Date in YYYY-MM-DD format
            close REAL       -- Closing price for that date
        )
    """)
    
    # Save DataFrame to SQLite table
    # if_exists='replace' will drop and recreate the table if it exists
    # index=False prevents saving the DataFrame index as a separate column
    df.to_sql("stock_data", conn, if_exists='replace', index=False)

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Data successfully saved to SQLite database.")
    print("Database file: finance_data.db")
    print("Table name: stock_data")
    
except sqlite3.Error as e:
    print(f"SQLite error: {e}")
    print("Failed to save data to database.")

