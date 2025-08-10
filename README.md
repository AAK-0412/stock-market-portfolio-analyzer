📈 Stock Market Portfolio Analyzer
A simple Python-based tool to analyze the performance of selected top companies from the stock market.
This script fetches historical stock data, calculates performance metrics, and visualizes trends using Yahoo Finance.
--------------------------------------------------
✨ Features
Preloaded list of Top 25 Companies with their stock symbols.

User can select one or more companies to analyze.

Fetches historical data using yfinance.

Supports multiple time periods (1mo, 3mo, 6mo, 1y, 5y, max).

Calculates:

Individual stock percentage change.

Average daily return.

Portfolio volatility.

Total portfolio percentage change.

Visualizes stock price trends in a line chart.
--------------------------------------------------
📦 Requirements
Make sure you have Python 3.7+ installed.
Install dependencies using:

pip install yfinance pandas matplotlib
--------------------------------------------------
🚀 How to Use
Clone or download this repository.

Open a terminal in the project folder.

Run:


python portfolio_analyzer.py


Select companies from the displayed list (comma-separated).

Choose the desired time period.

View the portfolio analysis in the terminal and chart window.
--------------------------------------------------
📊 Example Output
yaml
Copy
Edit
Fetching data for: AAPL, MSFT, TSLA

📊 Individual Stock Performance:
AAPL: 8.52%
MSFT: 5.73%
TSLA: -2.14%

💼 Portfolio Statistics:
Average Daily Return: 0.14%
Volatility (Std Dev): 1.25%
Total Portfolio Change: 4.03%
--------------------------------------------------
📌 Notes
Stock data is fetched in real-time from Yahoo Finance, so internet access is required.

If an invalid company name is entered, it will be ignored.

For multiple stocks, the portfolio analysis assumes equal weighting.
--------------------------------------------------
🖼 Preview
Example of the stock price chart generated:

(Chart showing stock prices over selected period)
--------------------------------------------------
🛠 Tech Stack
Python

yfinance → Market data

pandas → Data processing

matplotlib → Data visualization
--------------------------------------------------
📄 License
This project is open-source and available under the MIT License.
--------------------------------------------------
