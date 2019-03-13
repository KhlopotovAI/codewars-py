from unittest import TestCase

from .kata import fibonacci


class TestFibonacci(TestCase):
    def test_fibonacci(self):
        self.assertEqual(190392490709135, fibonacci(70))
        self.assertEqual(1548008755920, fibonacci(60))
        self.assertEqual(12586269025, fibonacci(50))
        self.assertEqual(222232244629420445529739893461909967206666939096499764990979600, fibonacci(300))
