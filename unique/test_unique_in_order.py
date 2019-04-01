from unittest import TestCase

from .kata import unique_in_order


class TestUniqueInOrder(TestCase):
    def test_unique_in_order(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'])
