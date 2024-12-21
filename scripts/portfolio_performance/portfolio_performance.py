from scripts.portfolio_performance.class_portfolio import Stock, Portfolio
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime, timedelta

def portfolio_performance(init_cash:float, initial_date_portfolio: datetime, final_date_portfolio:datetime, strategy: dict):
    # Create a Portfolio instance
    portfolio = Portfolio(init_cash, initial_date_portfolio) # This instance will contain the portfolio info at each instant of time

    # Compute Portfolio performance
    difference = final_date_portfolio - initial_date_portfolio
    n_days=difference.days
    portfolio_value = pd.Series([], dtype=float) # Time serie to plot the portfolio performance
    for n in range(0,n_days+1): # Loop for all days to compute the portfolio performance
        today = initial_date_portfolio + timedelta(days=n)
        #print(today)
        if today.weekday() < 5:
            # Check for transaction this day
            for i in range(0,len(strategy['symbol'])):
                if strategy['date'][i] == today:
                    ticker = strategy['symbol'][i]
                    quantity = strategy['quantity'][i]
                    transaction = Stock(ticker, today, quantity)
                    if transaction.flag ==1:
                        if strategy['transaction_type'][i] == 'buy':
                            portfolio.buy_stock(transaction)
                        elif strategy['transaction_type'][i] == 'sell':
                            portfolio.sell_stock(transaction)
                        else:
                            print('Error: Transaction type not allowed')
                    else:
                        print('Could not recover the price of the transaction')
            # Update portfolio value as of today
            portfolio.update_portfolio_value(today)
        # Save the value of portfolio value in a time series to plot afterwards
        portfolio_value[today] = portfolio.current_value

    portfolio_value.plot(linestyle='-', color='b')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Portfolio Value', fontsize=12)
    plt.grid(True)
    plt.tight_layout()  # Ajustar el layout para evitar recortes
    plt.show()

    # # Create buy order
    # date = datetime(2022, 12, 15, 00, 00, 00)
    # ticker = "AAPL"
    # transaction = Stock(ticker, date, 10)
    # portfolio.buy_stock(transaction)