from re import search
from unittest import TestCase

from .kata import regex


class TestPassword(TestCase):
    def test_password(self):
        self.assertTrue(bool(search(regex, 'fjd3IR9')))
        self.assertFalse(bool(search(regex, 'ghdfj32')))
        self.assertFalse(bool(search(regex, 'DSJKHD23')))
        self.assertFalse(bool(search(regex, 'dsF43')))
        self.assertTrue(bool(search(regex, '4fdg5Fj3')))
        self.assertFalse(bool(search(regex, 'DHSJdhjsU')))
        self.assertFalse(bool(search(regex, 'fjd3IR9.;')))
        self.assertFalse(bool(search(regex, 'fjd3  IR9')))
        self.assertTrue(bool(search(regex, 'djI38D55')))
        self.assertFalse(bool(search(regex, 'a2.d412')))
        self.assertFalse(bool(search(regex, 'JHD5FJ53')))
        self.assertFalse(bool(search(regex, '!fdjn345')))
        self.assertFalse(bool(search(regex, 'jfkdfj3j')))
        self.assertFalse(bool(search(regex, '123')))
        self.assertFalse(bool(search(regex, 'abc')))
        self.assertTrue(bool(search(regex, '123abcABC')))
        self.assertTrue(bool(search(regex, 'ABC123abc')))
        self.assertTrue(bool(search(regex, 'Password123')))
