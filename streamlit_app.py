import streamlit as st
from agents.finance_agent import FinanceAgent

# Set page config
st.set_page_config(page_title="Equity Research Analyst", layout="centered")
st.title("📊 Equity Research Analyst")
st.markdown("Ask me about any public company (e.g.,Last 5 years analysis on equity)")

# User input
user_input = st.text_input("Ask a finance-related question")

if user_input:
    with st.spinner("Thinking..."):
        agent = FinanceAgent()
        response = agent.run(user_input)
        st.markdown("### 💡 Analyst Report")
        st.write(response)

    # News section appears ONLY after user query
    st.markdown("---")
    with st.expander("📰 Market Insights & Related News", expanded=True):
        # News 1 - Reuters
        col1, col2 = st.columns([1, 9])
        with col1:
            st.image("https://www.google.com/s2/favicons?domain=https://www.reuters.com&sz=32")
        with col2:
            st.markdown("**[Top Indian funds bet on domestic sectors to lead market rebound amid global jitters](https://www.reuters.com/world/india/top-indian-funds-bet-domestic-sectors-lead-market-rebound-amid-global-jitters-2025-04-23/?utm_source=chatgpt.com)**  \n_Reuters | Apr 23, 2025_")

        # News 2 - Times of India
        col1, col2 = st.columns([1, 9])
        with col1:
            st.image("https://www.google.com/s2/favicons?domain=https://timesofindia.indiatimes.com&sz=32")
        with col2:
            st.markdown("**[Realty outpaces Nifty 50: Analysts pick stocks with upside](https://timesofindia.indiatimes.com/business/india-business/realty-breaks-out-nifty-realty-outpaces-nifty-50-jumps-8-in-a-month-analysts-pick-these-stocks-with-upside/articleshow/122075070.cms?utm_source=chatgpt.com)**  \n_Times of India | 16 days ago_")

        # News 3 - Economic Times
        col1, col2 = st.columns([1, 9])
        with col1:
            st.image("https://www.google.com/s2/favicons?domain=https://economictimes.indiatimes.com&sz=32")
        with col2:
            st.markdown("**[Nifty cracks 20-DMA amid bearish momentum](https://economictimes.indiatimes.com/markets/expert-view/fo-talk-nifty-cracks-20-dma-amid-bearish-momentum-macro-cues-keep-investors-on-edge-sudeep-shah/articleshow/122403835.cms?utm_source=chatgpt.com)**  \n_Economic Times | Today_")
