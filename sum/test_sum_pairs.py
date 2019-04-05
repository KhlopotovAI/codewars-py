from unittest import TestCase

from .kata import sum_pairs


class TestSumPairs(TestCase):
    def test_sum_pairs(self):
        l1 = [1, 4, 8, 7, 3, 15]
        l2 = [1, -2, 3, 0, -6, 1]
        l3 = [20, -13, 40]
        l4 = [1, 2, 3, 4, 1, 0]
        l5 = [10, 5, 2, 3, 7, 5]
        l6 = [4, -2, 3, 3, 4]
        l7 = [0, 2, 0]
        l8 = [5, 9, 13, -3]
        l9 = [1] * 10000000
        l9[(len(l9) // 2) - 1] = 6
        l9[(len(l9) // 2)] = 7
        l9[len(l9) - 2] = 8
        l9[len(l9) - 1] = -3
        l9[0] = 13
        l9[1] = 3
        self.assertEqual(sum_pairs(l1, 8), [1, 7])
        self.assertEqual(sum_pairs(l2, -6), [0, -6])
        self.assertIsNone(sum_pairs(l3, -7), None)
        self.assertEqual(sum_pairs(l4, 2), [1, 1])
        self.assertEqual(sum_pairs(l5, 10), [3, 7])
        self.assertEqual(sum_pairs(l6, 8), [4, 4])
        self.assertEqual(sum_pairs(l7, 0), [0, 0])
        self.assertEqual(sum_pairs(l8, 10), [13, -3])
        self.assertEqual(sum_pairs(l9, 13), [6, 7])
        self.assertEqual(sum_pairs(l9, 5), [8, -3])
        self.assertEqual(sum_pairs(l9, 16), [13, 3])
        self.assertIsNone(sum_pairs(l9, 31))
