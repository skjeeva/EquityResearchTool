from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()

from tools.finance_search_tool import FinanceSearchTool

class FinanceAgent:
    def __init__(self):
        self.tool = FinanceSearchTool()
        self.llm = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-3.5-turbo",
            temperature=0.5
        )

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

If the question is clearly **not related to finance or investing**, such as topics about food, entertainment, programming, history, or general trivia,dont answer 

Otherwise, answer professionally with detailed analysis including:
- **Thesis**
- **Key Financial Metrics / Trends**
- **Competitive Landscape**
- **Catalysts / Risks**
- **Investment Outlook**
- **Conclusion**

Use clear, concise, and data-backed reasoning as if writing an analyst report.

Question: {question}

Search Info: {search_info}
"""
        )

        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)

    def run(self, question: str) -> str:
        search_info = self.tool.search(question)

        # Debug print to check prompt formatting during dev
        # print(self.prompt_template.format(question=question, search_info=search_info))

        response = self.chain.invoke({"question": question, "search_info": search_info})
        return response['text']
