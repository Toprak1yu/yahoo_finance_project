import logging
from yahooquery import Ticker

logger = logging.getLogger(__name__)

class IncomeStatement:
    # Get quarterly income statement data
    def __init__(self, symbol):
        try:
            logger.info(f"Fetching income statement for {symbol}")
            self.symbol = symbol
            self.ticker = Ticker(symbol)
            self.income_statement_data = self.ticker.income_statement(frequency='q')
        except Exception as e:
            logger.error(f"Error fetching income statement for {symbol}: {e}")
            self.income_statement_data = None

    # Filter data by year range
    def get_income_statement_by_year(self,start_year,end_year=2025):
        if self.income_statement_data is None:
            logger.warning(f"No income statement data available for {self.symbol}")
            return None
        
        # Filter by date range
        logger.info(f"Filtering income statement data for {self.symbol} from {start_year} to {end_year}")
        filtered_data = self.income_statement_data[
            (self.income_statement_data.asOfDate >= f'{start_year}-01-01') & 
            (self.income_statement_data.asOfDate <= f'{end_year}-12-31')
        ]
        
        # Keep only quarterly data (3M periods)
        filtered_data=filtered_data[filtered_data['periodType'] == '3M']
        
        if filtered_data.empty:
            logger.warning(f"No income statement data available for {self.symbol} from {start_year} to {end_year}")
            return None
        
        return filtered_data
    
class BalanceSheet:
    # Get quarterly balance sheet data
    def __init__(self, symbol):
        try:
            logger.info(f"Fetching balance sheet for {symbol}")
            self.symbol = symbol
            self.ticker = Ticker(symbol)
            self.balance_sheet_data = self.ticker.balance_sheet(frequency='q')
        except Exception as e:
            logger.error(f"Error fetching balance sheet for {symbol}: {e}")
            self.balance_sheet_data = None

    # Filter balance sheet by year range
    def get_balance_sheet_by_year(self,start_year,end_year=2025):
        if self.balance_sheet_data is None:
            logger.warning(f"No balance sheet data available for {self.symbol}")
            return None
        
        # Filter by date range
        logger.info(f"Filtering balance sheet data for {self.symbol} from {start_year} to {end_year}")
        filtered_data = self.balance_sheet_data[
            (self.balance_sheet_data.asOfDate >= f'{start_year}-01-01') & 
            (self.balance_sheet_data.asOfDate <= f'{end_year}-12-31')
        ]
        
        # Keep only quarterly data
        filtered_data=filtered_data[filtered_data['periodType'] == '3M']
        
        if filtered_data.empty:
            logger.warning(f"No balance sheet data available for {self.symbol} from {start_year} to {end_year}")
            return None
        
        return filtered_data
    
class CashFlow:
    # Get quarterly cash flow data
    def __init__(self, symbol):
        try:
            logger.info(f"Fetching cash flow for {symbol}")
            self.symbol = symbol
            self.ticker = Ticker(symbol)
            self.cash_flow_data = self.ticker.cash_flow(frequency='q')
        except Exception as e:
            logger.error(f"Error fetching cash flow for {symbol}: {e}")
            self.cash_flow_data = None

    # Filter cash flow by year range
    def get_cash_flow_by_year(self,start_year,end_year=2025):
        if self.cash_flow_data is None:
            logger.warning(f"No cash flow data available for {self.symbol}")
            return None
        
        # Filter by date range
        logger.info(f"Filtering cash flow data for {self.symbol} from {start_year} to {end_year}")
        filtered_data = self.cash_flow_data[
            (self.cash_flow_data.asOfDate >= f'{start_year}-01-01') & 
            (self.cash_flow_data.asOfDate <= f'{end_year}-12-31')
        ]
        
        # Keep only quarterly data
        filtered_data=filtered_data[filtered_data['periodType'] == '3M']
        
        if filtered_data.empty:
            logger.warning(f"No cash flow data available for {self.symbol} from {start_year} to {end_year}")
            return None
        
        return filtered_data