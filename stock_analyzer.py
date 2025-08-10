import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Top 25 companies and their stock symbols
top_companies = {
    'Apple': 'AAPL', 'Microsoft': 'MSFT', 'Amazon': 'AMZN', 'Tesla': 'TSLA', 'Google': 'GOOGL',
    'Facebook': 'META', 'NVIDIA': 'NVDA', 'Berkshire Hathaway': 'BRK-B', 'Visa': 'V',
    'Johnson & Johnson': 'JNJ', 'JPMorgan Chase': 'JPM', 'UnitedHealth': 'UNH',
    'Procter & Gamble': 'PG', 'Mastercard': 'MA', 'Pfizer': 'PFE', 'Exxon Mobil': 'XOM',
    'Intel': 'INTC', 'Walmart': 'WMT', 'Bank of America': 'BAC', 'Disney': 'DIS',
    'Coca-Cola': 'KO', 'PepsiCo': 'PEP', 'Oracle': 'ORCL', 'IBM': 'IBM', 'Adobe': 'ADBE'
}

def get_user_choices():
    print("Choose companies to analyze (separate names with commas):")
    for company in top_companies:
        print(f"- {company}")
    
    selected_names = input("\nEnter company names: ").split(",")
    selected_symbols = []
    
    for name in selected_names:
        name = name.strip()
        if name in top_companies:
            selected_symbols.append(top_companies[name])
        else:
            print(f"⚠ Company '{name}' not found in the top 25 list.")
    
    return list(set(selected_symbols))  # Remove duplicates

def get_period_choice():
    valid_periods = ['1mo', '3mo', '6mo', '1y', '5y', 'max']
    period = input(f"Enter time period {valid_periods}: ").strip()
    return period if period in valid_periods else '1y'

def analyze_portfolio(stock_symbols, period):
    if not stock_symbols:
        print("❌ No valid companies selected.")
        return

    print(f"\nFetching data for: {', '.join(stock_symbols)}")
    data = yf.download(stock_symbols, period=period, auto_adjust=False)['Adj Close']
    
    if isinstance(data, pd.Series):
        data = data.to_frame()

    # Calculate returns
    returns = data.pct_change().dropna()
    portfolio_returns = returns.mean(axis=1)
    
    # Plot all stocks
    plt.figure(figsize=(12, 7))
    for symbol in stock_symbols:
        plt.plot(data[symbol], label=symbol)
    plt.title(f"Stock Prices ({period})")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Portfolio statistics
    start_price = data.iloc[0]
    end_price = data.iloc[-1]
    pct_changes = ((end_price - start_price) / start_price * 100).round(2)
    
    print("\n📊 Individual Stock Performance:")
    for symbol in stock_symbols:
        print(f"{symbol}: {pct_changes[symbol]}%")

    avg_return = portfolio_returns.mean() * 100
    volatility = portfolio_returns.std() * 100
    total_change = ((data.mean(axis=1).iloc[-1] - data.mean(axis=1).iloc[0]) / data.mean(axis=1).iloc[0]) * 100

    print("\n💼 Portfolio Statistics:")
    print(f"Average Daily Return: {avg_return:.2f}%")
    print(f"Volatility (Std Dev): {volatility:.2f}%")
    print(f"Total Portfolio Change: {total_change:.2f}%")

def main():
    symbols = get_user_choices()
    period = get_period_choice()
    analyze_portfolio(symbols, period)

if __name__ == "__main__":
    main()
