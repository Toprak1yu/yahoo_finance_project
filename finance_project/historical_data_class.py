import logging
import yfinance as yf

logger = logging.getLogger(__name__)

class HistoricalData:
    # Get historical price data using yfinance
    def __init__(self, symbol):
        try:
            logger.info(f"Fetching historical data for {symbol}")
            self.symbol = symbol
            self.ticker = yf.Ticker(symbol)
            self.historical_data = self.ticker.history(period='max')
        except Exception as e:
            logger.error(f"Error fetching historical data for {symbol}: {e}")
            self.historical_data = None

    # Filter historical data by date range
    def get_historical_data(self,start_date='2020-01-01', end_date='2025-07-20'):
        if self.historical_data is None:
            logger.warning(f"No historical data available for {self.symbol}")
            return None
        # Filter by date range
        logger.info(f"Filtering historical data for {self.symbol} from {start_date} to {end_date}")
        filtered_data = self.historical_data[
            (self.historical_data.index >= start_date) &
            (self.historical_data.index <= end_date)
        ]
        if filtered_data.empty:
            logger.warning(f"No historical data available for {self.symbol} from {start_date} to {end_date}")
            return None
        return filtered_data