"""
Inspiration for this script is the Jupyter Notebook of the OpenBB documentation:
https://github.com/OpenBB-finance/OpenBB/blob/develop/examples/financialStatements.ipynb
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
from openbb import obb
from dotenv import load_dotenv

if __name__ == "__main__":
    # Generate a personal access token, associate the vendors keys and save it in the .env file
    # https://my.openbb.co/app/platform/pat
    load_dotenv()
    obb.account.login(pat=os.getenv("OPENBB_API_KEY"))

    # Definition of symbol
    SYMBOL = "HIMS"
    
    # GET THE DATAFRAME VALUES AVAILABLE IN THE FINANCIAL STATEMENTS OF YFINANCE
    dfyf = (
    obb.equity.fundamental.balance(SYMBOL, provider="yfinance")
        .to_df()
    )
    print("BALANCE SHEET")
    print(dfyf.columns)

    dfyf = (
    obb.equity.fundamental.income(SYMBOL, provider="yfinance")
        .to_df()
    )
    print("INCOME STATEMENT")
    print(dfyf.columns)

    dfyf = (
    obb.equity.fundamental.cash(SYMBOL, provider="yfinance")
        .to_df()
    )
    print("CASH FLOW STATEMENT")
    print(dfyf.columns)

    # GET A DATAFRAME OF OTHER PROVIDERS TO CHECK THAT THE DATA IS THE SAME
    df = pd.DataFrame()
    df["fmp"] = (
        obb.equity.fundamental.income(SYMBOL, provider="yfinance")
        .to_df()
        .get("net_income")
    )

    df["polygon"] = (
        obb.equity.fundamental.income(SYMBOL, provider="yfinance")
        .to_df()
        .get("net_income")
    )
    print(df)
    df.plot()
    plt.show()

    # 


