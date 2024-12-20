from finlabair.data.yahoo_fetcher import YahooDataFetcher

# Create a fetcher instance
fetcher = YahooDataFetcher()

# Get historical data for a single ticker
apple_data = fetcher.get_historical_data("AAPL", period="1mo")

# Get data for multiple tickers
tech_stocks = fetcher.get_multiple_tickers(
    ["AAPL", "MSFT", "GOOGL"],
    period="1mo"
)
print(tech_stocks)