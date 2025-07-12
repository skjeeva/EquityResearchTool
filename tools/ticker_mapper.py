import pandas as pd
import os

def load_nse_tickers():
    url = "https://www1.nseindia.com/content/equities/EQUITY_L.csv"
    file_path = os.path.join("data", "equity_list.csv")
    os.makedirs("data", exist_ok=True)
    df = pd.read_csv(url)
    df["YF_TICKER"] = df["SYMBOL"].str.strip() + ".NS"
    df.to_csv(file_path, index=False)
    return df[["NAME OF COMPANY", "SYMBOL", "YF_TICKER"]]

# Optional: Fuzzy match company name to ticker
def get_yahoo_ticker(company_name):
    df = load_nse_tickers()
    matches = df[df["NAME OF COMPANY"].str.contains(company_name, case=False, na=False)]
    if not matches.empty:
        return matches.iloc[0]["YF_TICKER"]
    return None
