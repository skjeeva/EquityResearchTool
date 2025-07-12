import os
import pandas as pd
import difflib
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from tools.finance_search_tool import FinanceSearchTool
from dotenv import load_dotenv

load_dotenv()

class FinanceAgent:
    def __init__(self):
        self.tool = FinanceSearchTool()
        self.llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE"),       
        model="mistralai/devstral-medium",
        temperature=0.5,
        max_tokens=800
    )

        self.df = pd.read_csv("data/equity_list.csv")
        self.df.columns = self.df.columns.str.strip().str.upper()

        self.prompt_template = PromptTemplate(
            input_variables=["question", "search_info"],
            template="""
You are an equity research analyst. Your job is to answer only finance-related queries, focusing on stocks, markets, company financials, investment strategies, and economic trends.

Here are examples of valid finance topics:
- Tesla 2025 stock outlook
- Apple's revenue growth in 2023
- Semiconductor industry trends
- Impact of inflation on tech stocks
- Fundamental analysis of Amazon
- Tell me about the latest trends in renewable energy investments
- How is the banking sector performing in 2024?
- Tell me about the last year of HCL
- What are the key financial metrics for Infosys?
- How did TCS perform financially in the last quarter?
- What are the growth drivers for Infosys in FY24?
- Can you analyze Wipro's financial performance for the last year?
- What are the risks and opportunities for HDFC Bank in 2025?
- How is Reliance Industries performing in the energy sector?
- What is the earnings outlook for ICICI Bank this year?
- Provide a fundamental analysis of Bajaj Finance.
- What's the projected revenue of Larsen & Toubro for FY2025?
- What is the expected stock movement for SBIN this year?
- Is it a good time to invest in Tata Consultancy Services?
- What are analysts saying about the stock performance of HCL Technologies?
- Should I hold or sell shares of Infosys in 2025?
- Which sectors are outperforming the Nifty 50 currently?
- What’s the current outlook on the Indian IT sector?
- Are renewable energy investments still attractive in 2025?
- What’s driving the auto sector boom this year?
- How is inflation affecting Indian FMCG companies?
- What are the latest trends in NBFC performance in India?
- What’s the market sentiment around private sector banks?
- How is the RBI’s monetary policy impacting equity markets?
- What are the economic indicators suggesting for India's GDP growth?
- How is the US Fed’s interest rate decision affecting Indian equities?
- What’s the impact of geopolitical tensions on global stock markets?
- Is the rupee depreciation affecting Indian exporters?
- Which is a better buy in 2025: Infosys or Wipro?
- Compare the financials of HDFC Bank vs ICICI Bank.
- What are the top 3 undervalued Indian stocks right now?
- What is a good defensive stock during market volatility?
- Which Indian sectors are expected to grow the fastest in 2025?
- How did Infosys perform financially in the last quarter?
- What are the key financial ratios of Reliance Industries?
- What is the debt-to-equity ratio of HDFC Bank?
- Give me a financial analysis of Wipro.
- What was Tata Motors’ revenue growth last year?
- How is the P/E ratio of Infosys compared to its competitors?
- What are the latest earnings reports for HCL Technologies?
- What is the dividend yield of Tata Consultancy Services?
- Is ICICI Bank a good buy for 2025?
- Should I invest in Sun Pharma for long term?
- What’s the stock outlook for Tech Mahindra?
- Compare the investment potential of Asian Paints vs Berger Paints.
- What’s the forecast for Adani Green Energy stock in 2025?
- What were the Q4 earnings highlights of Bajaj Finance?
- Summarize the latest earnings call of Zomato.
- Show earnings trends for Dr. Reddy’s Laboratories.
- Any significant EPS changes for Tata Steel?
- Any recent news about Paytm?
- What’s happening with Adani Ports after the recent market shift?
- Is there any merger/acquisition news involving Nykaa?
- Tell me the latest developments around Flipkart.
- How is the pharmaceutical sector performing in 2024?
- What are the latest trends in the IT industry?
- Compare the banking sector performance in India.
- What’s the outlook of the renewable energy space in India?
- Compare TCS vs Infosys financials.
- Is HDFC Bank better than ICICI Bank in terms of performance?
- Which is a stronger fintech player: PhonePe or Razorpay?
- What are the key risks associated with Ola Electric?
- SWOT analysis of Netflix India in 2024.
- What is the competitive edge of Nestle India?
- Key catalysts and risks for Policybazaar
- What’s the PE ratio of Maruti Suzuki?
- What are the valuation metrics of Kotak Mahindra Bank?
- Is Hero MotoCorp undervalued?
- What are the growth drivers of L&T in 2025?
- Expected growth of Myntra in the e-commerce space.
- What is Spotify India’s expansion strategy?


If the question is about **company performance**, such as "How did Infosys perform financially in the last quarter?", provide a detailed analysis of the company's financials.
If the question is about **investment strategies**, such as "Is it a good time to invest in Tata Consultancy Services?", discuss the current market conditions, valuation, and potential risks and rewards.

If the question is about **stock prices**, such as "What is the current stock price of Apple?", respond with the latest stock price.
If the question is about **company news**, such as "What are the latest developments in Tesla?", provide a brief summary of recent news or events related to the company.
If the question is about **market trends**, such as "What are the current trends in the semiconductor industry?", summarize the latest trends and insights in that sector.

If the question is about **company financials**, such as earnings reports, revenue forecasts, or market analysis, respond with detailed insights.

Only reject if the question is clearly unrelated to finance — like food, love, entertainment, or jokes. If there's any ambiguity, assume it *is* a finance question and respond with analysis.

Otherwise, answer professionally with detailed analysis including:
- **Thesis**
- **Key Financial Metrics / Trends**
- **Competitive Landscape**
- **Catalysts / Risks**
- **Investment Outlook**
- **Conclusion**

Use clear, concise, and data-backed reasoning like an analyst report.

Question: {question}

Search Info: {search_info}
"""
        )

        self.chain = self.prompt_template | self.llm

    def extract_company_from_query(self, query):
        query = query.lower().strip()

        for _, row in self.df.iterrows():
            full_name = row["NAME OF COMPANY"].lower()
            symbol = row["SYMBOL"].lower()

            if full_name in query or symbol in query:
                return row["NAME OF COMPANY"]

        all_possible_names = self.df["NAME OF COMPANY"].tolist() + self.df["SYMBOL"].tolist()
        closest_matches = difflib.get_close_matches(query, all_possible_names, n=1, cutoff=0.6)

        if closest_matches:
            matched = closest_matches[0]
            row = self.df[(self.df["NAME OF COMPANY"] == matched) | (self.df["SYMBOL"] == matched)]
            if not row.empty:
                return row.iloc[0]["NAME OF COMPANY"]

        return None

    def run(self, question: str) -> str:
        if not question.strip():
            return "⚠️ Please ask a valid finance-related question."

        company = self.extract_company_from_query(question)
        query_for_tool = company if company else question

        search_info = self.tool.search(query_for_tool)
        response = self.chain.invoke({"question": question,"search_info": search_info})

        return response.get('text', "⚠️ No response generated.")