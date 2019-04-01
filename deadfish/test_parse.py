from unittest import TestCase

from .kata import parse


class TestParse(TestCase):
    def test_parse(self):
        self.assertEqual([0], parse("codewars"))
        self.assertEqual([0, 0, 0], parse("ooo"))
        self.assertEqual([1, 2, 3], parse("ioioio"))
        self.assertEqual([0, 1], parse("idoiido"))
        self.assertEqual([1, 4, 25], parse("isoisoiso"))
