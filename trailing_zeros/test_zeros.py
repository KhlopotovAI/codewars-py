from unittest import TestCase

from .kata import zeros


class TestZeros(TestCase):
    def test_zeros(self):
        self.assertEqual(zeros(0), 0, "Testing with n = 0")
        self.assertEqual(zeros(6), 1, "Testing with n = 6")
        self.assertEqual(zeros(30), 7, "Testing with n = 30")
