import unittest
from func import city_functions

class OutputTestCase(unittest.TestCase):
    """测试输出"""
##    def test_city_country(self):
##        msg = city_functions('chengdu','china')
##        self.assertEqual(msg,'Chengdu,China')
    def test_city_country_population(self):
        msg = city_functions('chengdu','china',population=500000)
        self.assertEqual(msg,'Chengdu,China - population 500000')

unittest.main()
