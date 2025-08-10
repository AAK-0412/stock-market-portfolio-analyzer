# 📈 Stock Portfolio Analysis Tool  

This Python script allows users to *select companies from the top 25 global stocks, fetch their historical price data using **Yahoo Finance, visualize performance, and calculate portfolio statistics such as **returns, volatility, and total change*.

---

## 🚀 Features  
- ✅ Choose from *Top 25 companies* with predefined stock symbols  
- ✅ Select *time periods* (1mo, 3mo, 6mo, 1y, 5y, max)  
- ✅ Fetch *adjusted closing prices* via yfinance  
- ✅ Plot stock price trends for selected companies  
- ✅ Calculate *individual and portfolio performance metrics*:  
  - Average Daily Return  
  - Volatility (Standard Deviation)  
  - Total Portfolio Change  

---

## 📦 Requirements  
Make sure you have Python installed (>= 3.7) and install the required packages:  
bash
pip install yfinance matplotlib pandas

---

## 🛠 Code Structure  
- **top_companies** → Dictionary of top 25 companies & their stock symbols  
- **get_user_choices()** → Lets user select companies to analyze  
- **get_period_choice()** → Lets user choose analysis time period  
- **analyze_portfolio()** → Fetches data, plots graphs, calculates metrics  
- **main()** → Orchestrates the program flow  

---

## ⚠ Notes  
- Ensure your internet connection is active — the script fetches live data from Yahoo Finance  
- If a company name is misspelled, it will be skipped with a warning  
- Script uses *Adjusted Close* prices for accuracy in historical analysis  

---
