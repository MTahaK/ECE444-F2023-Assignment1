from utils import utils
import unittest

class TestUtilsFunctions(unittest.TestCase):

    def test_reversed_int(self):
        self.assertEqual(utils.reversed(12345), 54321)
    
    def test_reversed_string(self):
        self.assertEqual(utils.reversed("hello"), "ERROR: Input must be an int.")

    def test_reversed_float(self):
        self.assertEqual(utils.reversed(5.0), "ERROR: Input must be an int.")

    def test_formatter_int(self):
        self.assertEqual(utils.formatter(123), ('0b1111011', '0o173'))
    
    def test_formatter_string(self):
        self.assertEqual(utils.formatter("hello"), "ERROR: Input must be an int.")

    def test_formatter_float(self):
        self.assertEqual(utils.formatter(5.0), "ERROR: Input must be an int.")

if __name__ == "__main__":
    unittest.main()

