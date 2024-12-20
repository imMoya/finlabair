"""
Module for fetching financial data from Yahoo Finance.
"""
from datetime import datetime, timedelta
from typing import Optional, Union, List

import pandas as pd
import yfinance as yf

from finlabair.utils.validation import validate_ticker

class YahooDataFetcher:
    """A class to fetch and manage financial data from Yahoo Finance."""
    
    def __init__(self):
        """Initialize the YahooDataFetcher."""
        self._cache = {}

    def get_historical_data(
        self,
        ticker: str,
        start_date: Optional[Union[str, datetime]] = None,
        end_date: Optional[Union[str, datetime]] = None,
        period: str = "1mo",
        interval: str = "1d"
    ) -> pd.DataFrame:
        """
        Fetch historical data for a given ticker.

        Args:
            ticker: Stock ticker symbol
            start_date: Start date for data retrieval (optional)
            end_date: End date for data retrieval (optional)
            period: Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            interval: Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo

        Returns:
            DataFrame with historical data
        """
        ticker = validate_ticker(ticker)
        
        # Create cache key
        cache_key = f"{ticker}_{start_date}_{end_date}_{period}_{interval}"
        
        # Check cache first
        if cache_key in self._cache:
            return self._cache[cache_key]

        # Get data from Yahoo Finance
        stock = yf.Ticker(ticker)
        df = stock.history(
            start=start_date,
            end=end_date,
            period=period,
            interval=interval
        )
        
        # Cache the result
        self._cache[cache_key] = df
        
        return df

    def get_multiple_tickers(
        self,
        tickers: List[str],
        start_date: Optional[Union[str, datetime]] = None,
        end_date: Optional[Union[str, datetime]] = None,
        period: str = "1mo",
        interval: str = "1d"
    ) -> dict[str, pd.DataFrame]:
        """
        Fetch historical data for multiple tickers.

        Args:
            tickers: List of stock ticker symbols
            start_date: Start date for data retrieval (optional)
            end_date: End date for data retrieval (optional)
            period: Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            interval: Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo

        Returns:
            Dictionary mapping tickers to their respective DataFrames
        """
        return {
            ticker: self.get_historical_data(ticker, start_date, end_date, period, interval)
            for ticker in tickers
        }

    def clear_cache(self):
        """Clear the data cache."""
        self._cache = {}