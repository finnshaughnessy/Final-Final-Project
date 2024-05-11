# budget_tracker.py

def input_financial_data():
    """Prompts the user to input their financial data."""
    income = float(input("Enter your monthly income: "))
    expenses = {}
    more_expenses = True
    while more_expenses:
        category = input("Enter expense category (e.g., rent, groceries): ")
        amount = float(input(f"Enter amount for {category}: "))
        expenses[category] = amount
        more = input("Add more expenses? (yes/no): ")
        if more.lower() != 'yes':
            more_expenses = False
    return income, expenses

def calculate_balance(income, expenses):
    """Calculates the balance after expenses."""
    total_expenses = sum(expenses.values())
    return income - total_expenses

def display_budget_summary(income, expenses, balance):
    """Displays a summary of the budget."""
    print("\n--- Budget Summary ---")
    print(f"Total Income: ${income:.2f}")
    print("Expenses:")
    for category, amount in expenses.items():
        print(f"  {category}: ${amount:.2f}")
    print(f"Remaining Balance: ${balance:.2f}")



