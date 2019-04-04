from unittest import TestCase

from .kata import check_generator


class TestCheckGenerator(TestCase):
    def test_check_generator(self):
        gen = (i for i in range(1))
        self.assertEqual('Created', check_generator(gen))
        next(gen, None)
        self.assertEqual('Started', check_generator(gen))
        next(gen, None)
        self.assertEqual('Finished', check_generator(gen))
