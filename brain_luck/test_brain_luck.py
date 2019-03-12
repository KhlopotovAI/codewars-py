from unittest import TestCase

from .kata import brain_luck


class TestBrainLuck(TestCase):
    def test_brain_luck(self):
        # Echo until byte(255) encountered
        self.assertEqual(
            'Codewars',
            brain_luck(',+[-.,+]', 'Codewars' + chr(255))
        )

        # Echo until byte(0) encountered
        self.assertEqual(
            'Codewars',
            brain_luck(',[.[-],]', 'Codewars' + chr(0))
        )

        # Two numbers multiplier
        self.assertEqual(
            chr(72),
            brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9))
        )
