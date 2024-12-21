import yfinance as yf
from datetime import datetime, timedelta

class Stock:
    """
    The stock class contains a transaction information about a stock:
    - Symbol
    - Date (which is used to obtain the price of the stock)
    - Number of shares

    This is a general transaction class. Whether if it is a buy or a sell
    will depend on the method that it is used inside the Portfolio class
    (explained later)
    """
    def __init__(self, symbol:str, date: datetime, number_of_shares:int):
        self.symbol = symbol
        self.avg_price, self.flag = self.compute_price(date)
        self.number_of_shares = number_of_shares

    def compute_price(self,date):
        ticker_data = None
        flag = 1
        try:
            ticker_data = yf.download(self.symbol, start=date, end=date + timedelta(days=1), progress=False)
            if ticker_data.empty:
                raise ValueError("No data found for the requested date")
        except (ValueError, IndexError) as e:
            print(f"No data found for {self.symbol} on {date}, trying the previous day.")
            ticker_data = yf.download(self.symbol, start=date, end=date + timedelta(days=1), progress=False)

        if not ticker_data.empty:
            price = ticker_data['Adj Close'].values[0]  # Asumiendo que la columna 'Adj Close' tiene los datos
            price = price[0]  # this is a float
        else:
            print(f"Could not retrieve data for {self.symbol} on {date}, skipping this stock.")
            price = 0
            flag = 0

        return price, flag


class Portfolio:
    """
    The Portfolio class includes all the information abot the cash and the
    stocks currently held in the portfolio.
    - Each instance(portfolio) is created with a certain amount of cash.
    - Instances "add_cash" and "extract" cash let the user modify the cash amount solely.
    - They buy and sell operations (methods) exchanges cash by a certain amount of stock,
    based on the transaction information passed through the class "Stock" explained before.
    - Update_portfolio_value method updated the current value of the stock, in order to now
    the current value of the stock held + cash
    - Portfolio_summary method prints a summary of the portfolio

    """
    def __init__(self, cash:float, initial_date: datetime):
        # Initialize an empty list to store Stock instances
        self.stocks = []
        self.cash = cash
        self.current_value = cash
        self.initial_date = initial_date

    def add_cash(self, additional_cash: float):
        self.cash += additional_cash

    def extract_cash(self, extracted_cash: float):
        self.cash -= extracted_cash

    def buy_stock(self, stock: Stock):
        if self.cash >= stock.number_of_shares*stock.avg_price:
            is_in_portfolio = False
            for iter_stock in self.stocks:
                if stock.symbol == iter_stock.symbol:
                    is_in_portfolio = True
                    iter_stock.avg_price = ((iter_stock.number_of_shares*iter_stock.avg_price +
                                                     stock.number_of_shares*stock.avg_price) /
                                                     (iter_stock.number_of_shares + stock.number_of_shares))
                    iter_stock.number_of_shares += stock.number_of_shares
                    break
            if is_in_portfolio == False:
                self.stocks.append(stock)
            self.cash -= stock.number_of_shares * stock.avg_price
            print("Purchase done")
        else:
            print("Not enough money to make the purchase")

    def sell_stock(self, stock:Stock): # NOT FIFO APPLIED
        is_in_portfolio=False
        for iter_stock in self.stocks:
            if stock.symbol == iter_stock.symbol:
                is_in_portfolio = True
                if stock.number_of_shares > iter_stock.number_of_shares:
                    print("You're trying to sell more shares than you own")

                else:
                    iter_stock.number_of_shares -= stock.number_of_shares
                    self.cash += stock.avg_price*stock.number_of_shares
                    print("Sell done")
                break
        if is_in_portfolio == False:
            print("You're trying to sell an stock that you do not own")

    def update_portfolio_value(self, date: datetime):
        """Calculate the total value of the portfolio based on current prices.
        Does not modify self.cash because it is already modified when buying
        or selling
        """
        total = 0

        for stock in self.stocks:
            ticker_data = None
            try:
                ticker_data = yf.download(stock.symbol, start=date, end=date + timedelta(days=1), progress=False)
                if ticker_data.empty:
                    raise ValueError("No data found for the requested date")
            except (ValueError, IndexError) as e:
                print(f"No data found for {stock.symbol} on {date}, trying the previous day.")
                ticker_data = yf.download(stock.symbol, start=date - timedelta(days=1), end=date + timedelta(days=2), progress=False)

            if not ticker_data.empty:
                price = float(ticker_data['Adj Close'].values[0])  # Asumiendo que la columna 'Adj Close' tiene los datos
                total += stock.number_of_shares * price
            else:
                print(f"Could not retrieve data for {stock.symbol} on {date}, skipping this stock.")
        self.current_value = float(total) + self.cash

    def portfolio_summary(self, date: datetime):
        """Print a summary of the portfolio."""
        self.update_portfolio_value(date)
        print("Summary of stocks owned: ")
        for stock in self.stocks:
            value = stock.number_of_shares*stock.avg_price
            print(f"{stock.symbol} - {stock.number_of_shares} shares - ${stock.avg_price:.2f} per share - Total: ${value}")
        print("----------------------------------------")
        print(f"Total Portfolio Value: \n${self.current_value:.2f} (${self.cash} in cash)")