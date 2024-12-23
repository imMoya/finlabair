import os
import pandas as pd
from openbb import obb
from dotenv import load_dotenv
import yfinance as yf

if __name__ == "__main__":

    pd.set_option('display.max_rows', 5)
    pd.set_option('display.max_columns', 12)
    pd.set_option('display.width', 1000)

    ######################### API KEYS SECTION #########################
    # BEFORE RUNNING IT IS NECESSARY TO CREATE A FILE ".env" containing all the API KEYS
    # for example: OPENBB_API_KEY=a1b2c3d4e5
    # Load the ".env" file
    load_dotenv()
    # Obtain the KEY at https://my.openbb.co/app/platform/pat
    obb.account.login(pat=os.getenv("OPENBB_API_KEY"))
    # Obtain the KEY at https://site.financialmodelingprep.com/ RE NEW EACH DAY
    obb.user.credentials.fmp_api_key = os.getenv("FMP_API_KEY")
    # Obtain the KEY at https://polygon.io/dashboard/keys
    obb.user.credentials.polygon_api_key = os.getenv("POLYGON_API_KEY")
    # Obtain the KEY at https://www.tiingo.com/account/api/token
    obb.user.credentials.tiingo_token = os.getenv("TIINGO_TOKEN")
    ####################### END API KEYS SECTION #######################

    ##### yfinance ####
    # openBB API:
    # aapl_yf = (obb.equity.price.historical(symbol="AAPL", start_date="2022-01-01", end_date="2022-01-05",
    #                                       provider="yfinance").to_df())
    # yfinance API:
    # For yfinance it is better to use the original API with the version 0.2.50, since it contains the
    # 'Adj Close' price, while the last version of yfinance (used by openBB) does not contain this info
    aapl_yf = yf.download("AAPL", start="2022-01-01", end="2022-01-05")
    print(aapl_yf['Adj Close'])

    #### Polygon provides an error ####
    # aapl_po = (obb.equity.price.historical(symbol="AAPL", start_date="2022-03-15", end_date="2022-05-05",
    #                                         provider="polygon").to_df())
    # print(aapl_po)

    #### Intrinio need to pay for subscription ####
    # aapl_it = (obb.equity.price.historical(symbol="AAPL", start_date="2022-01-01", end_date="2022-01-05",
    #                                         provider="intrinio").to_df())
    # print(aapl_it)

    #### Financial Modelling Prer ####
    aapl_fmp = (obb.equity.price.historical(symbol="AAPL", start_date="2022-01-01", end_date="2022-01-05",
                                           provider="fmp").to_df())
    print(aapl_fmp['adj_close'])

    #### Tiingo ####
    aapl_tng = (obb.equity.price.historical(symbol="AAPL", start_date="2022-01-01", end_date="2022-01-05",
                                           provider="tiingo").to_df())
    print(aapl_tng['adj_close'])

