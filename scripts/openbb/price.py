import os
import pandas as pd
import matplotlib.pyplot as plt
from openbb import obb
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    obb.account.login(pat=os.getenv("OPENBB_API_KEY"))

    # Get historical price data for Amazon
    data = obb.equity.price.historical("AMZN", start_date = "2020-01-01").to_df()
    print(data)