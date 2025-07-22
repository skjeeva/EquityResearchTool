from agents.finance_agent import FinanceAgent

def main():
    print(">>")
    agent = FinanceAgent()

    while True:
        question = input("Ask a finance-related question (or type 'exit' to quit): ").strip()
        if question.lower() in ['exit', 'quit']:
            print("👋 Exiting. Have a great day!")
            break

        response = agent.run(question)
        print("\n📊 Financial Insight:\n")
        print(response)
        print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    main()
