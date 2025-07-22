import logging
from financial_classes import IncomeStatement, BalanceSheet, CashFlow
from historical_data_class import HistoricalData

logger = logging.getLogger(__name__)

class Company:
    # Main company class to fetch all financial data
    def __init__(self, symbol, start_date,end_date):
        try:
            logger.info(f"Initializing Company class for {symbol}")
            self.symbol = symbol
            start_year = start_date.split('-')[0]
            end_year = end_date.split('-')[0]

        except Exception as e:
            logger.error(f"Error initializing Company class for {symbol}: {e}")
            self.symbol = None
        # Initialize all data classes
        try:
            logger.info(f"Fetching all data for {symbol}")
            self.income_statement = IncomeStatement(symbol)
            self.balance_sheet = BalanceSheet(symbol)
            self.cash_flow = CashFlow(symbol)
            self.historical_data = HistoricalData(symbol)
        except Exception as e:
            logger.error(f"Error fetching all data for {symbol}: {e}")
        
        # Fetch filtered data for specified years
        self.income_statement_data = self.income_statement.get_income_statement_by_year(start_year, end_year)
        self.balance_sheet_data = self.balance_sheet.get_balance_sheet_by_year(start_year, end_year)
        self.cash_flow_data = self.cash_flow.get_cash_flow_by_year(start_year, end_year)
        self.historical_data = self.historical_data.get_historical_data(start_date, end_date)
        
    # Return all data if at least one type is available
    def get_all_data(self):
        
        logger.info(f"Compiling all data for {self.symbol}")
        if (self.income_statement_data is not None or 
            self.balance_sheet_data is not None or 
            self.cash_flow_data is not None or 
            self.historical_data is not None):
            logger.info(f"Data available for {self.symbol}")
            logger.debug(f"Income Statement Data: {self.income_statement_data}")
            logger.debug(f"Balance Sheet Data: {self.balance_sheet_data}")
            logger.debug(f"Cash Flow Data: {self.cash_flow_data}")
            logger.debug(f"Historical Data: {self.historical_data}")
            logger.info(f"Returning all data for {self.symbol}")
            # Return a dictionary of all data types
            return {
                'income_statement': self.income_statement_data,
                'balance_sheet': self.balance_sheet_data,
                'cash_flow': self.cash_flow_data,
                'historical_data': self.historical_data
            }
        logger.warning(f"No data available for {self.symbol}")
        return None
    
    # Save data to SQLite database
    def to_db(self,conn):
        try:
            cursor= conn.cursor()
            # Save each data type to separate tables
            if self.income_statement_data is not None:
                logger.info(f"Saving income statement data for {self.symbol}")
                self.income_statement_data.to_sql(f'{self.symbol}_income_statement', conn, if_exists='replace', index=False)
            if self.balance_sheet_data is not None:
                logger.info(f"Saving balance sheet data for {self.symbol}")
                self.balance_sheet_data.to_sql(f'{self.symbol}_balance_sheet', conn, if_exists='replace', index=False)
            if self.cash_flow_data is not None:
                logger.info(f"Saving cash flow data for {self.symbol}")
                self.cash_flow_data.to_sql(f'{self.symbol}_cash_flow', conn, if_exists='replace', index=False)
            if self.historical_data is not None:
                logger.info(f"Saving historical data for {self.symbol}")
                self.historical_data.to_sql(f'{self.symbol}_historical_data', conn, if_exists='replace', index=True)
            conn.commit()
            # Return True if all data types were saved successfully
            return True
        except Exception as e:
            logger.error(f"Error saving data to database: {e}")
            return False