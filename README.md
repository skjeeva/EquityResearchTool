### 📊 Equity Research Analyst App

This is a Streamlit-based AI-powered equity research assistant. It uses `LangChain`, `OpenAI`, and `yFinance` to provide stock-specific and sector-wide insights, including financial summaries, trends, and related news headlines.

---

### 🚀 Features

* ✅ Ask questions about Indian companies (e.g. “Tell about last year of HCL”)
* 📈 Financial metrics using `yFinance` (Revenue, Net Income, EPS, PE Ratio, etc.)
* 📊 5-Year revenue & income trend generation
* 🧠 LLM-generated analyst summaries via OpenAI / Mistral models
* 🔎 Auto-detect company names from a CSV list
* 📰 Display hand-curated related finance news at the bottom
* ✅ Streamlit frontend interface

---

### 🛠️ Tech Stack

* **Frontend:** Streamlit
* **LLM:** LangChain + OpenAI or DevStral (via `langchain-openai`)
* **Finance Data:** yFinance
* **Ticker Mapping:** NSE + `equity_list.csv`
* **Backend:** Python 3.11+

---

### 📂 Project Structure

```
EquityResearchTool/
│
├── app/
│   └── streamlit_app.py         # Main frontend file
│
├── agents/
│   └── finance_agent.py         # LangChain agent logic
│
├── tools/
│   └── finance_search_tool.py   # yFinance data fetcher + NSE scraper
│
├── data/
│   └── equity_list.csv          # NSE stocks & symbols
│
├── .env                         # Your API keys (OpenAI, etc.)
├── requirements.txt             # Dependencies
└── README.md                    # You're here!
```

---

### 📦 Installation

```bash
# 1. Clone the repo
git clone https://github.com/yourname/equity-research-tool.git
cd equity-research-tool

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API keys
touch .env
# inside .env:
# OPENAI_API_KEY=your_key_here
# OPENAI_API_BASE=https://api.openai.com
# OPENAI_API_MODEL=gpt-4 (or mistralai/devstral-medium)

# 4. Run the app
streamlit run app/streamlit_app.py
```

---

### 🧪 Example Questions You Can Ask

* "Tell about last year of HCL"
* "What are the financials of Reliance?"
* "Give revenue trend of Infosys"
* "How is the banking sector performing?"
* "Is Tata Motors doing well?"

---

### 📜 License

MIT License – free to use, modify, and share.

---