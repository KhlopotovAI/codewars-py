from unittest import TestCase

from .kata import duplicate_encode


class TestDuplicateEncode(TestCase):
    def test_duplicate_encode(self):
        self.assertEqual("(((", duplicate_encode("din"))
        self.assertEqual("()()()", duplicate_encode("recede"))
        self.assertEqual(")())())", duplicate_encode("Success"))
        self.assertEqual("))((", duplicate_encode("(( @"))
