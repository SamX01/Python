import unittest
from f_test import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试f_test"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('zac','baf')
        self.assertEqual(formatted_name,'Zac Baf')
    def test_first_last_mid_name(self):
        formatted_name = get_formatted_name('zac','bac','De')
        self.assertEqual(formatted_name,'Zac De Bac')
        

unittest.main()
