from agents.finance_agent import FinanceAgent

if __name__ == "__main__":
    agent = FinanceAgent()
    while True:
        question = input("Ask a finance question (or type 'exit' to quit): ")
        if question.lower() == "exit":
            break
        response = agent.run(question)
        print("\nResponse:\n", response)