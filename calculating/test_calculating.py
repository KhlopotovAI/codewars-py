from unittest import TestCase

from .kata import *


class TestCalculating(TestCase):
    def test_calculating(self):
        self.assertEqual(35, seven(times(five())))
        self.assertEqual(13, four(plus(nine())))
        self.assertEqual(5, eight(minus(three())))
        self.assertEqual(3, six(divided_by(two())))
