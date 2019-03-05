from unittest import TestCase

from .kata import choose_best_sum


class TestChooseBestSum(TestCase):
    def test_choose_best_sum(self):
        xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
        self.assertEqual(230, choose_best_sum(230, 4, xs))
        self.assertEqual(430, choose_best_sum(430, 5, xs))
        self.assertEqual(None, choose_best_sum(430, 8, xs))
