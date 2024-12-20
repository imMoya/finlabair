"""
Validation utilities for the trading package.
"""
import re
from typing import Optional

def validate_ticker(ticker: str) -> str:
    """
    Validate and normalize a ticker symbol.

    Args:
        ticker: Stock ticker symbol

    Returns:
        Normalized ticker symbol

    Raises:
        ValueError: If ticker is invalid
    """
    if not isinstance(ticker, str):
        raise ValueError("Ticker must be a string")
    
    # Remove whitespace and convert to uppercase
    ticker = ticker.strip().upper()
    
    # Basic validation of ticker format
    if not re.match(r'^[A-Z0-9\.\-]{1,10}$', ticker):
        raise ValueError(
            "Invalid ticker format. Tickers should be 1-10 characters "
            "and contain only letters, numbers, dots, or hyphens."
        )
    
    return ticker