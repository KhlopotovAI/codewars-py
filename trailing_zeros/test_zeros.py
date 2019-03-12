from unittest import TestCase

from .kata import zeros


class TestZeros(TestCase):
    def test_zeros(self):
        self.assertEqual(0, zeros(0), "Testing with n = 0")
        self.assertEqual(1, zeros(6), "Testing with n = 6")
        self.assertEqual(7, zeros(30), "Testing with n = 30")
