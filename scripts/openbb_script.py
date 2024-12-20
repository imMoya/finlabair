import os
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from openbb import obb
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    obb.account.login(pat=os.getenv("OPENBB_API_KEY"))
    print(obb.user.credentials)
    SYMBOL = "MSTR"
    
    # GET THE DATAFRAME VALUES AVAILABLE IN THE BALANCE SHEET OF YFINANCE
    dfyf = (
    obb.equity.fundamental.balance(SYMBOL, provider="yfinance")
        .to_df()
    )
    print(dfyf.columns)

    # GET A DATAFRAME OF OTHER PROVIDERS TO CHECK THAT THE DATA IS THE SAME
    df = pd.DataFrame()
    df["fmp"] = (
        obb.equity.fundamental.balance(SYMBOL, provider="fmp", limit=3)
        .to_df()
        .get("total_assets")
    )

    df["polygon"] = (
        obb.equity.fundamental.balance(SYMBOL, provider="polygon", limit=3)
        .to_df()
        .get("total_assets")
    )
    print(df)
    df.plot()
    plt.show()
