import unittest
from all_class import Employee

class TestClassEmployee(unittest.TestCase):
    def setUp(self):
        self.test_emp = Employee("xiaoming","wang",3000)

    def test_give_default_raise(self):
        test_salary = self.test_emp.give_raise()
        self.assertEqual(test_salary,8000)
        
    def test_give_custom_raise(self):
        test_salary = self.test_emp.give_raise(1000)
        self.assertEqual(test_salary,4000)
    
unittest.main()
