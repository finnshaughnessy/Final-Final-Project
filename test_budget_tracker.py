# test_budget_tracker.py
import unittest
from budget_tracker import calculate_balance

class TestBudgetTracker(unittest.TestCase):
    def test_calculate_balance(self):
        income = 1000
        expenses = {'rent': 500, 'groceries': 200, 'utilities': 100}
        expected_balance = 200
        calculated_balance = calculate_balance(income, expenses)
        self.assertEqual(calculated_balance, expected_balance)

if __name__ == '__main__':
    unittest.main()
