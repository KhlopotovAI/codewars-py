from unittest import TestCase

from .kata import duplicate_count


class TestDuplicateCount(TestCase):
    def test_duplicate_count(self):
        self.assertEqual(0, duplicate_count("abcde"))
        self.assertEqual(1, duplicate_count("abcdea"))
        self.assertEqual(1, duplicate_count("indivisibility"))
