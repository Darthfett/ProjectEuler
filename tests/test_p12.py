from p12 import get_triangle_numbers, factor_primes

from collections import Counter
from itertools import islice
import unittest

class TriangleNumberTest(unittest.TestCase):
    def test_get_ten_triangle_numbers(self):
        first_ten = list(islice(get_triangle_numbers(), 10))
        self.assertEqual(first_ten, [1, 3, 6, 10, 15, 21, 28, 36, 45, 55])

class GetFactorsTest(unittest.TestCase):
    def test_get_factors(self):
        self.assertEqual(factor_primes(28), Counter([2, 2, 7]))