import logging
import pandas as pd
import sqlite3
import time
from datetime import datetime
from arg_parse import parse_args
from setup_log import setup_logging
from company_class import Company

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

def main():

    # Database connection
    try:
        conn = sqlite3.connect('finance_yahoo.db')
        logger.info("Connected to SQLite database")
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        conn = None
    # Parse command line arguments
    args = parse_args()
    
    # Load stock symbols
    try:
        if args.symbols:
            symbols = args.symbols
            logger.info(f"Processing {len(symbols)} stock symbol: {symbols}")
        else:
            # Load all symbols from CSV
            logger.info("Loading stock symbols from CSV")
            symbols = pd.read_csv('bist100.csv')['Symbol'].tolist()
            logger.info(f"Loaded {len(symbols)} stock symbols")
    except Exception as e:
        logger.error(f"Error loading stock symbols: {e}")
        symbols = []

    company_classes = {} # Dictionary to hold Company instances
    # Main loop - process each stock symbol
    for symbol in symbols:
        # Skip problematic symbols
        if symbol in ['DOAS.IS', 'TURSG.IS', 'GLCVY.IS', 'ISBIR.IS']:
            logger.info(f'Skipping problematic symbol: {symbol}')
            continue
        # Process company data
        try:
            logger.info(f"Processing data for {symbol}")
            today= datetime.now().strftime('%y-%m-%d')
            company = Company(symbol, args.start if args.start else '2020-01-01',
                              args.end if args.end else today)
            company_classes[symbol] = company
            data = company.get_all_data()
        except Exception as e:
            logger.error(f"Error processing {symbol}: {e}")
            continue
        # Save to database if data exists
        try:
            if data is not None:
                logger.info(f"Saving data for {symbol} to database")
                if company.to_db(conn):
                    logger.info(f'Data for {symbol} saved successfully.')
                else:
                    logger.error(f'Failed to save data for {symbol}.')
            else:
                logger.warning(f'No data available for {symbol}.')
        except Exception as e:
            logger.error(f"Error saving data for {symbol}: {e}")
            continue
        # Wait between requests
        time.sleep(1)

    # Close database connection
    if conn:
        logger.info("Closing database connection")
        conn.close()

if __name__ == "__main__":
    main()
    logger.info("Script completed successfully")