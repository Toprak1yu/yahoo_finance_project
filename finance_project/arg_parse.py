import argparse
from datetime import datetime

def parse_args():
    """Parse command line arguments for the finance application"""
    # Get current date as default end date
    today = datetime.now().strftime('%y-%m-%d')
    
    # Create argument parser
    parser = argparse.ArgumentParser(description="Finance Project Argument Parser")
    
    # Add stock symbols argument
    parser.add_argument('--symbols', type=str, nargs='+', help='Stock symbol to process', required=False)
    # Add start date argument
    parser.add_argument('--start', type=str, default='2020-01-01', help='Start date for data retrieval (YYYY-MM-DD)', required=False)
    # Add end date argument
    parser.add_argument('--end', type=str, default=today, help='End date for data retrieval (YYYY-MM-DD)', required=False)
    
    # Parse and return arguments
    return parser.parse_args()