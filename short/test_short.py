from unittest import TestCase

from .kata import short


class TestShort(TestCase):
    def test_short(self):
        tests = [
            # [input, expected]
            [[{1, 2, 3}, {2, 3, 4}], {1: 1, 2: 2, 3: 2, 4: 1}],
            [[{1, 2, 3, 4}], {1: 1, 2: 1, 3: 1, 4: 1}],
            [[{1}, {1, 3, 4, 5}], {1: 2, 3: 1, 4: 1, 5: 1}]
        ]

        for inp, exp in tests:
            self.assertEqual(
                short(inp),
                exp
            )
