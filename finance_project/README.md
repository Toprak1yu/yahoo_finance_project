# BIST 100 Stock Data Fetcher 📈

A Python script that fetches historical stock data for BIST 100 (Borsa Istanbul 100) companies from Yahoo Finance API and stores the data in both CSV format and SQLite database for analysis.

## Features ✨

- 📊 **Fetches historical data** from 2020 to current date
- 🛡️ **Error handling** for missing or delisted stocks
- 💾 **Dual storage** in CSV and SQLite database formats
- 📈 **Progress tracking** with download statistics
- 🔄 **Auto-adjustment** for stock splits and dividends
- 🚀 **Ready for analysis** and machine learning projects

## Prerequisites 📋

- Python 3.7+
- Required Python packages (see requirements below)
- `bist100_symbols.csv` file with stock symbols

## Installation 🚀

1. **Clone the repository:**
```bash
git clone https://github.com/Toprak1yu/yahoo_finance.git
cd yahoo_finance/finance_project
```

2. **Install required packages:**
```bash
pip install yfinance pandas sqlite3
```

3. **Prepare your data:**
   - Ensure you have `bist100_symbols.csv` with a 'symbol' column
   - Example format:
   ```csv
   symbol
   AKBNK.IS
   THYAO.IS
   GARAN.IS
   ```

## Usage 💻

Simply run the script:

```bash
python yahoo_datas.py
```

### What the script does:

1. **Loads stock symbols** from `bist100_symbols.csv`
2. **Downloads historical data** for each symbol from Yahoo Finance
3. **Saves closing prices** to `bist100_closing_prices.csv`
4. **Stores data** in SQLite database (`finance_data.db`)
5. **Provides progress reports** and error handling

## Output Files 📁

After running the script, you'll get:

- **`bist100_closing_prices.csv`** - Time series of closing prices for all stocks
- **`finance_data.db`** - SQLite database with normalized stock data
- **Console output** - Download progress and summary statistics

## Database Schema 🗃️

The SQLite database contains a `stock_data` table with:

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Stock symbol (e.g., 'AKBNK.IS') |
| date   | TEXT | Date in YYYY-MM-DD format |
| close  | REAL | Closing price for that date |

## Example Usage in Analysis 📊

```python
import pandas as pd
import sqlite3

# Load data from CSV
df = pd.read_csv('bist100_closing_prices.csv')

# Or from database
conn = sqlite3.connect('finance_data.db')
df = pd.read_sql_query("SELECT * FROM stock_data WHERE symbol = 'AKBNK.IS'", conn)
conn.close()
```

## Use Cases 🎯

This data is perfect for:

- **📈 Technical analysis** and trading strategies
- **🔮 Portfolio optimization** and risk assessment
- **🤖 Machine learning** models for price prediction
- **📊 Financial research** and backtesting
- **📉 Market correlation** studies

## Error Handling 🛠️

The script handles various scenarios:

- Missing or delisted stocks
- Network connectivity issues
- Yahoo Finance API limitations
- File system permissions
- Database connection errors

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Author 👨‍💻

**Aziz Toprak Yilmaz**
- GitHub: [@Toprak1yu](https://github.com/Toprak1yu)

## Disclaimer ⚠️

This tool is for educational and research purposes only. Financial data may have delays and should not be used for actual trading decisions without proper verification.

## Acknowledgments 🙏

- [Yahoo Finance](https://finance.yahoo.com/) for providing free financial data
- [yfinance](https://github.com/ranaroussi/yfinance) library for easy API access
- [Borsa Istanbul](https://www.borsaistanbul.com/) for market data

---

⭐ **Star this repository if you found it helpful!** ⭐
