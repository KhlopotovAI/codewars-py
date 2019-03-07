from unittest import TestCase

from .kata import increment_string


class TestIncrementString(TestCase):
    def test_increment_string(self):
        self.assertEqual("foo1", increment_string("foo"))
        self.assertEqual("foobar002", increment_string("foobar001"))
        self.assertEqual("foobar2", increment_string("foobar1"))
        self.assertEqual("foobar01", increment_string("foobar00"))
        self.assertEqual("foobar100", increment_string("foobar99"))
        self.assertEqual("foobar100", increment_string("foobar099"))
        self.assertEqual("1", increment_string(""))
