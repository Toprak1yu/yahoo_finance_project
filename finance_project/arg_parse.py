import argparse
from datetime import datetime

class Arguments:
    """Class to handle command line argument parsing for finance application"""
    
    def __init__(self):
        # Get current date as default
        today = datetime.now().strftime('%y-%m-%d')
        
        parser = argparse.ArgumentParser(description="Finance Project Argument Parser")
        
        parser.add_argument('--symbols', type=str, nargs='+', help='List of stock symbols to process', required=False)
        parser.add_argument('--start', type=str, default='2020-01-01', help='Start date for data retrieval (YYYY-MM-DD)', required=False)
        parser.add_argument('--end', type=str, default=today, help='End date for data retrieval (YYYY-MM-DD)', required=False)
        
        self.args = parser.parse_args()
        
        # Store arguments as attributes
        self.symbols = self.args.symbols if self.args.symbols else None
        self.start = self.args.start if self.args.start else None
        self.end = self.args.end if self.args.end else None