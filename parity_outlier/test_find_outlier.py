from unittest import TestCase

from .kata import find_outlier


class TestFindOutlier(TestCase):
    def test_find_outlier(self):
        self.assertEqual(3, find_outlier([2, 4, 6, 8, 10, 3]))
        self.assertEqual(11, find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
        self.assertEqual(160, find_outlier([160, 3, 1719, 19, 11, 13, -21]))
