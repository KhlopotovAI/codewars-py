from unittest import TestCase

from .kata import unique_in_order


class TestUniqueInOrder(TestCase):
    def test_unique_in_order(self):
        self.assertEqual(['A', 'B', 'C', 'D', 'A', 'B'], unique_in_order('AAAABBBCCDAABBB'))
