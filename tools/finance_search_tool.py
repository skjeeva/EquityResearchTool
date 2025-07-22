import pandas as pd
import yfinance as yf

class FinanceSearchTool:
    def __init__(self):
        self.ticker_data = self._load_nse_tickers()

    def _load_nse_tickers(self):
        import requests
        import pandas as pd
        import os
        from time import sleep

        # NSE API and Headers
        url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
        homepage = "https://www.nseindia.com"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": homepage,
            "Connection": "keep-alive"
        }

        file_path = os.path.join("data", "equity_list.csv")
        os.makedirs("data", exist_ok=True)

        # First try to load from existing CSV
        try:
            df = pd.read_csv(file_path)
            print("✅ Loaded from existing CSV.")
            return df
        except Exception:
            print("⬇️ Downloading from NSE...")

        # Proper session setup
        session = requests.Session()
        session.headers.update(headers)

        try:
            # Visit homepage to set cookies
            session.get(homepage, timeout=5)
            sleep(1)

            # Now fetch stock list
            response = session.get(url, timeout=10)

            if response.status_code != 200:
                raise Exception(f"❌ Failed to fetch data: {response.status_code}")

            data = response.json()
            df = pd.DataFrame(data['data'])
            df["YF_TICKER"] = df["symbol"].str.strip() + ".NS"
            df.to_csv(file_path, index=False)
            print("✅ Saved to CSV.")
            return df[["symbol", "identifier", "YF_TICKER"]].rename(columns={"symbol": "NAME OF COMPANY"})

        except Exception as e:
            print(f"❌ Failed to fetch from NSE: {e}")
            return pd.DataFrame(columns=["NAME OF COMPANY", "YF_TICKER"])



    def _get_ticker(self, query):
        matches = self.ticker_data[self.ticker_data["NAME OF COMPANY"].str.contains(query, case=False, na=False)]
        if not matches.empty:
            return matches.iloc[0]["YF_TICKER"]
        return None
    
    def human_readable(self, n):
        if n == "N/A" or pd.isna(n):
            return "N/A"
        try:
            return f"{n / 1e7:.2f} Cr"  # Converts to Crores
        except:
            return n

    def search(self, query: str) -> str:
        ticker = self._get_ticker(query)
        if not ticker:
            return f"No data found for query: {query}"

        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            # Historical Financials
            financials = stock.financials.fillna(0)
            years = financials.columns.tolist()

            revenue_trend = []
            net_income_trend = []

            for year in years:
                revenue = financials.at["Total Revenue", year] if "Total Revenue" in financials.index else "N/A"
                income = financials.at["Net Income", year] if "Net Income" in financials.index else "N/A"
                revenue_trend.append(f"{year.year}: {self.human_readable(revenue)}")
                net_income_trend.append(f"{year.year}: {self.human_readable(income)}")

            data = {
                "Company": info.get("shortName", "N/A"),
                "Sector": info.get("sector", "N/A"),
                "Market Cap": self.human_readable(info.get("marketCap", "N/A")),
                "Current Price": info.get("currentPrice", "N/A"),
                "52 Week High": info.get("fiftyTwoWeekHigh", "N/A"),
                "52 Week Low": info.get("fiftyTwoWeekLow", "N/A"),
                "Revenue": self.human_readable(info.get("totalRevenue", "N/A")),
                "Revenue Trend (5Y)": ", ".join(revenue_trend),
                "Net Income": self.human_readable(info.get("netIncomeToCommon", "N/A")),
                "Net Income Trend (5Y)": ", ".join(net_income_trend),
                "PE Ratio": info.get("trailingPE", "N/A"),
                "EPS": info.get("trailingEps", "N/A"),
            }

            return "\n".join([f"{k}: {v}" for k, v in data.items()])

        except Exception as e:
            return f"Error fetching financial data: {e}"
