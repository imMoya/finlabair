"""
Tests for the Yahoo data fetcher module.
"""
import pytest
from datetime import datetime, timedelta
import pandas as pd

from finlabair.data.yahoo_fetcher import YahooDataFetcher
from finlabair.utils.validation import validate_ticker

def test_validate_ticker():
    """Test ticker validation."""
    # Valid cases
    assert validate_ticker("AAPL") == "AAPL"
    assert validate_ticker("  aapl  ") == "AAPL"
    assert validate_ticker("BRK.A") == "BRK.A"
    
    # Invalid cases
    with pytest.raises(ValueError):
        validate_ticker("")
    with pytest.raises(ValueError):
        validate_ticker("TOO-LONG-TICKER")
    with pytest.raises(ValueError):
        validate_ticker("INVALID@CHAR")

def test_yahoo_fetcher_basic():
    """Test basic functionality of YahooDataFetcher."""
    fetcher = YahooDataFetcher()
    
    # Test single ticker fetch
    df = fetcher.get_historical_data("AAPL", period="5d")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    
    # Test multiple tickers fetch
    data = fetcher.get_multiple_tickers(["AAPL", "MSFT"], period="5d")
    assert isinstance(data, dict)
    assert len(data) == 2
    assert all(isinstance(df, pd.DataFrame) for df in data.values())
    
    # Test cache functionality
    df2 = fetcher.get_historical_data("AAPL", period="5d")
    assert df2 is df  # Should return cached data
    
    fetcher.clear_cache()
    df3 = fetcher.get_historical_data("AAPL", period="5d")
    assert df3 is not df  # Should fetch new data after cache clear