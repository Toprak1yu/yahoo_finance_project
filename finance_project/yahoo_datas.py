import pandas as pd
import yfinance as yf
from yahooquery import Ticker
import sqlite3
import time

# Database connection
conn= sqlite3.connect('finance_yahoo.db')
# Load stock symbols
data=pd.read_csv('bist100.csv')
symbols=data['Symbol'].tolist()

class income_statement:
    # Get quarterly income statement data
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = Ticker(symbol)
        self.income_statement_data = self.ticker.income_statement(frequency='q')
        
    # Filter data by year range
    def get_income_statement_by_year(self,start_year,end_year=2025):
        if self.income_statement_data is None:
            return None
        
        # Filter by date range
        filtered_data = self.income_statement_data[
            (self.income_statement_data.asOfDate >= f'{start_year}-01-01') & 
            (self.income_statement_data.asOfDate <= f'{end_year}-12-31')
        ]
        
        # Keep only quarterly data (3M periods)
        filtered_data=filtered_data[filtered_data['periodType'] == '3M']
        
        if filtered_data.empty:
            return None
        
        return filtered_data
    
class balance_sheet:
    # Get quarterly balance sheet data
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = Ticker(symbol)
        self.balance_sheet_data = self.ticker.balance_sheet(frequency='q')
        
    # Filter balance sheet by year range
    def get_balance_sheet_by_year(self,start_year,end_year=2025):
        if self.balance_sheet_data is None:
            return None
        
        # Filter by date range
        filtered_data = self.balance_sheet_data[
            (self.balance_sheet_data.asOfDate >= f'{start_year}-01-01') & 
            (self.balance_sheet_data.asOfDate <= f'{end_year}-12-31')
        ]
        
        # Keep only quarterly data
        filtered_data=filtered_data[filtered_data['periodType'] == '3M']
        
        if filtered_data.empty:
            return None
        
        return filtered_data
    
class cash_flow:
    # Get quarterly cash flow data
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = Ticker(symbol)
        self.cash_flow_data = self.ticker.cash_flow(frequency='q')
        
    # Filter cash flow by year range
    def get_cash_flow_by_year(self,start_year,end_year=2025):
        if self.cash_flow_data is None:
            return None
        
        # Filter by date range
        filtered_data = self.cash_flow_data[
            (self.cash_flow_data.asOfDate >= f'{start_year}-01-01') & 
            (self.cash_flow_data.asOfDate <= f'{end_year}-12-31')
        ]
        
        # Keep only quarterly data
        filtered_data=filtered_data[filtered_data['periodType'] == '3M']
        
        if filtered_data.empty:
            return None
        
        return filtered_data

class historical_data:
    # Get historical price data using yfinance
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)
        self.historical_data = self.ticker.history(period='max')
        
    # Filter historical data by date range
    def get_historical_data(self,start_date='2020-01-01', end_date='2025-07-20'):
        if self.historical_data is None:
            return None
        # Filter by date range
        filtered_data = self.historical_data[
            (self.historical_data.index >= start_date) &
            (self.historical_data.index <= end_date)
        ]
        if filtered_data.empty:
            return None
        return filtered_data
            

class Company:
    # Main company class to fetch all financial data
    def __init__(self, symbol, start_date,end_date):
        self.symbol = symbol
        start_year = start_date.split('-')[0]
        end_year = end_date.split('-')[0]
        
        # Initialize all data classes
        self.income_statement = income_statement(symbol)
        self.balance_sheet = balance_sheet(symbol)
        self.cash_flow = cash_flow(symbol)
        self.historical_data = historical_data(symbol)
        
        # Fetch filtered data for specified years
        self.income_statement_data = self.income_statement.get_income_statement_by_year(start_year, end_year)
        self.balance_sheet_data = self.balance_sheet.get_balance_sheet_by_year(start_year, end_year)
        self.cash_flow_data = self.cash_flow.get_cash_flow_by_year(start_year, end_year)
        self.historical_data = self.historical_data.get_historical_data(start_date, end_date)
        
    # Return all data if at least one type is available
    def get_all_data(self):
        if (self.income_statement_data is not None or 
            self.balance_sheet_data is not None or 
            self.cash_flow_data is not None or 
            self.historical_data is not None):
            
            return {
                'income_statement': self.income_statement_data,
                'balance_sheet': self.balance_sheet_data,
                'cash_flow': self.cash_flow_data,
                'historical_data': self.historical_data
            }
        return None
    
    # Save data to SQLite database
    def to_db(self,conn):
        try:
            cursor= conn.cursor()
            # Save each data type to separate tables
            if self.income_statement_data is not None:
                self.income_statement_data.to_sql(f'{self.symbol}_income_statement', conn, if_exists='replace', index=False)
            if self.balance_sheet_data is not None:
                self.balance_sheet_data.to_sql(f'{self.symbol}_balance_sheet', conn, if_exists='replace', index=False)
            if self.cash_flow_data is not None:
                self.cash_flow_data.to_sql(f'{self.symbol}_cash_flow', conn, if_exists='replace', index=False)
            if self.historical_data is not None:
                self.historical_data.to_sql(f'{self.symbol}_historical_data', conn, if_exists='replace', index=True)
            conn.commit()
            return True
        except Exception as e:
            print(f'Error saving data to database: {e}')
            return False
    
# Main loop - process each stock symbol
for symbol in symbols:
    # Skip problematic symbols
    if symbol == 'DOAS.IS' or symbol == 'TURSG.IS' or symbol == 'GLCVY.IS' or symbol == 'ISBIR.IS':
        continue
    # Process company data
    company_name = symbol.split('.')[0]
    company_name = Company(symbol, '2020-01-01', '2025-07-20')
    data = company_name.get_all_data()
    # Save to database if data exists
    if data is not None:
        if company_name.to_db(conn):
            print(f'Data for {symbol} saved successfully.')
        else:
            print(f'Failed to save data for {symbol}.')
    else:
        print(f'No data available for {symbol}.')
    # Wait between requests
    time.sleep(1)

# Close database connection
conn.close()
        
    
