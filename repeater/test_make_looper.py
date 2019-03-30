from unittest import TestCase

from .kata import make_looper


class TestMakeLooper(TestCase):
    def test_repeater(self):
        abc = make_looper("abc")
        self.assertEqual('a', abc())
        self.assertEqual('b', abc())
        self.assertEqual('c', abc())
        self.assertEqual('a', abc())
        self.assertEqual('b', abc())
        self.assertEqual('c', abc())
