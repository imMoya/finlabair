from datetime import datetime
from scripts.portfolio_performance.strategy_random.strategy import random_strategy
from scripts.portfolio_performance.portfolio_performance import portfolio_performance

if __name__ == "__main__":

    cash = 10000
    initial_date = datetime(2024, 4, 1, 00, 00, 00)
    final_date = datetime(2024, 6, 10, 00, 00, 00)

    # Creates a strategy
    # The output is a dictionary with sell/buy orders like:
    # ['symbol': 'AAPL' , 'transaction_type':'buy', 'date': '10-02-2024', 'quantity': 10]
    strategy = random_strategy(initial_date, final_date, 10)

    # Portfolio performance uses that strategy dictionary as an input and computes the performance
    portfolio_performance(cash, initial_date, final_date, strategy)

