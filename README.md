# BIST 100 Financial Data Fetcher 📈

This project is a Python application that automatically fetches financial data from BIST 100 companies using Yahoo Finance API. This tool, developed as part of my university project, collects financial statements and historical price data of Turkish stocks and stores them in an SQLite database.

## 🎯 Project Purpose

To develop a system that easily collects and stores BIST 100 companies':
- Income statement data
- Balance sheet data  
- Cash flow statement data
- Historical stock price data

in an analyzable format for those who want to perform financial analysis.

## 🚀 Features

- **Bulk Data Fetching**: Automatically fetches data from all BIST 100 companies
- **Individual Company Analysis**: Ability to fetch data for specific companies
- **Date Range Selection**: Filter data within desired date ranges
- **SQLite Database**: Secure local database storage
- **Error Handling**: Robust structure against API errors
- **Logging**: Detailed operation logs

## 📋 Requirements

Python 3.7+ is required. Required libraries:

```
pandas>=1.5.0
yfinance>=0.2.18
yahooquery>=2.3.0
numpy>=1.21.0
requests>=2.28.0
python-dateutil>=2.8.0
```

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/username/yahoo_finance.git
cd yahoo_finance/finance_project
```

2. **Install required libraries:**
```bash
pip install -r requirements.txt
```

3. **Prepare BIST 100 company list:**
Make sure the `bist100.csv` file is in the project root directory.

## 💻 Usage

### To fetch data from all BIST 100 companies:
```bash
python main.py
```

### To fetch data from a specific company:
```bash
python main.py --symbols AKBNK.IS
```

### To fetch data with date range:
```bash
python main.py --symbols THYAO.IS --start 2023-01-01 --end 2023-12-31
```

## 📁 Project Structure

```
finance_project/
│
├── main.py                 # Main application file
├── company_class.py        # Company class
├── financial_classes.py    # Financial statement classes
├── historical_data_class.py # Historical data class
├── arg_parse.py            # Command line argument parser
├── setup_log.py            # Logging configuration
├── requirements.txt        # Required libraries
└── finance_yahoo.db        # SQLite database 
```

## 📊 Database Structure

Separate tables are created for each company:
- `{symbol}_income_statement` - Income statement
- `{symbol}_balance_sheet` - Balance sheet  
- `{symbol}_cash_flow` - Cash flow statement
- `{symbol}_historical_data` - Historical price data

## ⚠️ Important Notes

- Due to Yahoo Finance API rate limiting rules, there are waiting periods between requests
- Some companies may have missing data, which will be indicated in logs
- Internet connection is required
- Data from API may not be up-to-date

## 🐛 Known Issues

- Some BIST companies may contain incomplete data on Yahoo Finance
- API timeouts may cause longer execution times
- Historical data gaps may occur

## 📝 Development Notes

This project was developed during my university education to learn Python and financial data analysis. The code structure and practices reflect my learning process.

### Future Plans:
- Adding web interface
- Calculating more financial metrics
- Graphing and visualization features
- Excel export functionality

## 🤝 Contributing

This is a student project, and your suggestions and feedback are valuable. You can open issues or send pull requests.

## 📞 Contact

For questions about the project, you can contact me through GitHub.

---

*This project was developed for educational purposes. Please seek professional financial advice for your investment decisions.*
