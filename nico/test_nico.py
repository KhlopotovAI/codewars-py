from unittest import TestCase

from .kata import nico


class TestNico(TestCase):
    def test_nico(self):
        self.assertEqual("cseerntiofarmit on  ", nico("crazy", "secretinformation"))
        self.assertEqual("abcd  ", nico("abc", "abcd"))
        self.assertEqual("2143658709", nico("ba", "1234567890"))
        self.assertEqual("message", nico("a", "message"))
        self.assertEqual("eky", nico("key", "key"))
        self.assertEqual("abcd    ", nico("abcdefgh", "abcd"))
