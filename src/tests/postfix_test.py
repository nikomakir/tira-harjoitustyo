import unittest
from services.postfix import Postfixconverter


class TestPostfixconverter(unittest.TestCase):
    def setUp(self):
        self.converter = Postfixconverter()

    def test_convert(self):
        infix = [3, "+", 4, "*", 2, "/", "(", 1, "-", 5, ")", "^", 2, "^", 3]
        expected = [3, 4, 2, "*", 1, 5, "-", 2, 3, "^", "^", "/", "+"]
        result = self.converter.convert(infix)
        self.assertEqual(expected, result)
