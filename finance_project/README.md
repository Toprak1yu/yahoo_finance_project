# 📈 BIST 100 Financial Data Fetcher

A Python application that automatically fetches comprehensive financial data for BIST 100 (Borsa Istanbul) companies using Yahoo Finance APIs and stores it in a SQLite database for analysis.

## 🚀 Features

- **📊 Quarterly Financial Statements**: Income statements, balance sheets, and cash flow statements
- **📈 Historical Price Data**: Complete price history with OHLCV data
- **🗄️ SQLite Database Storage**: Organized data storage with separate tables for each company and data type
- **🛡️ Error Handling**: Gracefully handles missing data and API errors
- **⏱️ Rate Limiting**: Respects API limits with automatic delays
- **🎯 Flexible Data Retrieval**: Works even when some data types are unavailable

## 📋 Prerequisites

- Python 3.7 or higher
- Internet connection for API access

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Toprak1yu/yahoo_finance.git
cd yahoo_finance/finance_project
```

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

3. **Prepare BIST 100 symbols file:**
   - Create a `bist100.csv` file with a 'Symbol' column
   - Include stock symbols in format: `AKBNK.IS`, `THYAO.IS`, etc.

## 💻 Usage

Simply run the main script:

```bash
python yahoo_datas.py
```

The script will:
1. Load stock symbols from `bist100.csv`
2. Fetch financial data for each company (2020-2025)
3. Store data in `finance_yahoo.db` SQLite database
4. Display progress and save status for each symbol

## 📁 Output Structure

The SQLite database contains separate tables for each company:
- `{SYMBOL}_income_statement` - Quarterly income statements
- `{SYMBOL}_balance_sheet` - Quarterly balance sheets  
- `{SYMBOL}_cash_flow` - Quarterly cash flow statements
- `{SYMBOL}_historical_data` - Historical price data

## 📊 Database Schema

Each financial table includes:
- `asOfDate` - Statement date
- `periodType` - Period type (3M for quarterly)
- Financial metrics (revenue, expenses, assets, etc.)

Historical data includes:
- Date index
- Open, High, Low, Close prices
- Volume data

## 🎯 Use Cases

Perfect for:
- **Financial Analysis** - Analyze company performance trends
- **Portfolio Optimization** - Build diversified investment strategies  
- **Machine Learning** - Train predictive models on financial data
- **Research Projects** - Academic research on Turkish stock market
- **Algorithmic Trading** - Develop trading strategies

## ⚙️ Configuration

Modify the date range in the script:
```python
Company(symbol, '2020-01-01', '2025-07-20')  # Change dates as needed
```

Skip problematic symbols by adding them to the filter:
```python
if symbol in ['DOAS.IS', 'TURSG.IS', 'GLCVY.IS', 'ISBIR.IS']:
    continue
```

## 🚨 Rate Limiting

The script includes automatic delays (1 second) between requests to respect Yahoo Finance API limits. For large datasets, consider increasing the delay.

## ⚠️ Known Issues

Some symbols may not have complete financial data available. The script handles these cases gracefully and continues processing other symbols.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Financial data may have delays and should not be used for actual trading decisions without proper verification.

## 🙏 Acknowledgments

- [Yahoo Finance](https://finance.yahoo.com/) for providing free financial data
- [yfinance](https://github.com/ranaroussi/yfinance) library for easy API access
- [yahooquery](https://github.com/dpguthrie/yahooquery) for comprehensive financial data
- [Borsa Istanbul](https://www.borsaistanbul.com/) for market data

## 👨‍💻 Author

**Aziz Toprak Yılmaz**
- GitHub: [@Toprak1yu](https://github.com/Toprak1yu)


