# OpenBB

OpenBB is an open-source platform for fetching financial data.

## Personal Access Token
In order to connect with Python, the definition of the OpenBB Personal Access Token needs to be defined in this [webpage](https://my.openbb.co/app/platform/pat)

In addition to the generation of your OpenBB PAT, it's highly recommended to set another API Keys that OpenBB uses to connect to other providers. These credentials need to be saved in the [credentials webpage](https://my.openbb.co/app/platform/credentials).

## Connection with Python
As with other API keys, in Python it is highly desirable to keep them in a `.env` file in the root of your project. This file is ignored by the `.gitignore` file, so the user does not need to worry about their personal tokens (as long as the `.env` file is included in the `.gitignore`).
The API (or PAT) key should be defined in the `.env` file:

```
OPENBB_API_KEY = <YOUR_API_KEY>
```

In order to load the API key, it is desirable to look in the [official installation docs](https://docs.openbb.co/platform/installation) from OpenBB. In case the `.env` file contains the API key, the login through Python could be as easy as loading the environment variables with a package (such as `python-dotenv`). An example is below:
```python
from openbb import obb
from dotenv import load_dotenv
load_dotenv()
obb.account.login(pat=os.getenv("OPENBB_API_KEY"))
```
 
Once you have logged in, you can fetch data from the OpenBB platform
```python
df = obb.equity.fundamental.balance("AAPL", provider="yfinance").to_df()
```