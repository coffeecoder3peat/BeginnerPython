import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests the Employee class."""
    def setUp(self):
        """Sets up a default test employee to use."""
        self.test_employee = Employee('Chase', 'Wilson', 117000)

    def test_give_default_raise(self):
        """Test to verify salary increments 5000 by default."""
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.annual_salary, 122000)
    
    def test_custom_raise(self):
        """Test to verify salary increments with custom raise amount."""
        self.test_employee.give_raise(10000)
        self.assertEqual(self.test_employee.annual_salary, 127000)

if __name__ == '__main__':
    unittest.main()