# run_tracker.py
from budget_tracker import input_financial_data, calculate_balance, display_budget_summary

def main():
    print("Welcome to the Personal Budget Tracker")
    income, expenses = input_financial_data()
    balance = calculate_balance(income, expenses)
    display_budget_summary(income, expenses, balance)

if __name__ == "__main__":
    main()
