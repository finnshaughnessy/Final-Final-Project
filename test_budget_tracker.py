import unittest
import json
from budget_tracker import calculate_balance, display_budget_summary

def load_test_data(path):
    """Load test data from a JSON file."""
    with open(path, 'r') as file:
        data = json.load(file)
    return data

class TestBudgetTracker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Load test data from JSON file before running tests."""
        cls.test_data = load_test_data('test_data.json')

    def test_calculate_balance(self):
        """Test the calculate_balance function to ensure it correctly calculates the balance."""
        for item in self.test_data['tests']:
            with self.subTest(item=item):
                income = item['income']
                expenses = item['expenses']
                expected_balance = item['expected_balance']
                calculated_balance = calculate_balance(income, expenses)
                self.assertEqual(calculated_balance, expected_balance)

    def test_display_budget_summary(self):
        """Mock test to demonstrate how to test output functions. In practice, this would capture printed outputs."""
        # This is a mock test and should be implemented based on specific requirements and environment.
        pass

if __name__ == '__main__':
    unittest.main()
