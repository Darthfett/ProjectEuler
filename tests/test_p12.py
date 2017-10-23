from p12 import get_triangle_numbers, get_divisors

from itertools import islice
import unittest

class TriangleNumberTest(unittest.TestCase):
    def test_get_ten_triangle_numbers(self):
        first_ten = list(islice(get_triangle_numbers(), 10))
        self.assertEqual(first_ten, [1, 3, 6, 10, 15, 21, 28, 36, 45, 55])

class GetDivisorTest(unittest.TestCase):
    def test_get_divisors(self):
        self.assertEqual(sorted(list(get_divisors(28))), [1, 2, 4, 7, 14, 28])