import logging

def setup_logging():
    """Setup logging configuration for the application"""
    
    logging.basicConfig(
        # Set logging level to INFO
        level=logging.INFO,
        # Define log message format with timestamp
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            # Save logs to file
            logging.FileHandler('finance_yahoo.log'),
            # Display logs in console
            logging.StreamHandler()
        ]
    )