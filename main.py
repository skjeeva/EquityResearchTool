from agents.finance_agent import FinanceAgent
from tasks.finance_task import FinanceTask

def main():
    question = input("Ask a finance-related question: ")
    task = FinanceTask(question)
    agent = FinanceAgent()

    print("\nThinking...\n")
    result = agent.run(task.question)

    print("\nAnswer:")
    print(result)

if __name__ == "__main__":
    main()
