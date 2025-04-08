import yfinance as yf

class FinanceSearchTool:
    def search(self, query: str) -> str:
        # Extract ticker symbol (simple logic for now)
        query = query.lower()
        if "tesla" in query:
            ticker = "TSLA"
        elif "apple" in query:
            ticker = "AAPL"
        elif "meta" in query:
            ticker = "META"
        elif "microsoft" in query:
            ticker = "MSFT"
        else:
            return "No financial data found for your query."

        stock = yf.Ticker(ticker)

        try:
            info = stock.info
            financial_data = {
                "Company": info.get("shortName", "N/A"),
                "Sector": info.get("sector", "N/A"),
                "Market Cap": info.get("marketCap", "N/A"),
                "Current Price": info.get("currentPrice", "N/A"),
                "52 Week High": info.get("fiftyTwoWeekHigh", "N/A"),
                "52 Week Low": info.get("fiftyTwoWeekLow", "N/A"),
                "Revenue": info.get("totalRevenue", "N/A"),
                "Net Income": info.get("netIncomeToCommon", "N/A"),
                "PE Ratio": info.get("trailingPE", "N/A"),
                "EPS": info.get("trailingEps", "N/A"),
            }

            summary = "\n".join([f"{k}: {v}" for k, v in financial_data.items()])
            return summary

        except Exception as e:
            return f"Error fetching financial data: {e}"
