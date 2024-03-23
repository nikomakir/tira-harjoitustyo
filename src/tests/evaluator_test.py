import unittest
from services.evaluator import Evaluator


class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = Evaluator()

    def test_evaluate_returns_correct_value(self):
        postix = [3, 4, 2, "*", 1, 5, "-", 2, 3, "^", "^", "/", "+"]
        expected_result = 3.00012207
        result = self.evaluator.evaluate(postix)
        self.assertAlmostEqual(expected_result, result)

    def test_evaluate_returns_zero_division_error(self):
        postfix = [4, 0, "/"]
        result = self.evaluator.evaluate(postfix)
        self.assertEqual("Virhe: Nollalla jako", result)
