from unittest import TestCase

from .kata import make_readable


class TestMakeReadable(TestCase):
    def test_make_readable(self):
        self.assertEqual("00:00:00", make_readable(0))
        self.assertEqual("00:00:05", make_readable(5))
        self.assertEqual("00:01:00", make_readable(60))
        self.assertEqual("23:59:59", make_readable(86399))
        self.assertEqual("99:59:59", make_readable(359999))
