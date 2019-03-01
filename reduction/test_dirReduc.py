from unittest import TestCase

from .kata import dirReduc


class TestDirReduc(TestCase):
    def test_dirReduc(self):
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        self.assertEqual(['WEST'], dirReduc(a))
        u = ["NORTH", "WEST", "SOUTH", "EAST"]
        self.assertEqual(["NORTH", "WEST", "SOUTH", "EAST"], dirReduc(u))
