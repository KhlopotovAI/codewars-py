from unittest import TestCase

from .kata import list_squared


class TestListSquared(TestCase):
    def test_list_squared(self):
        self.assertEquals([[1, 1], [42, 2500], [246, 84100]], list_squared(1, 250))
        self.assertEquals([[42, 2500], [246, 84100]], list_squared(42, 250))
        self.assertEquals([[287, 84100]], list_squared(250, 500))
        self.assertEquals([], list_squared(300, 600))
        self.assertEquals([[728, 722500], [1434, 2856100]], list_squared(600, 1500))
        self.assertEquals([[1673, 2856100]], list_squared(1500, 1800))
        self.assertEquals([[1880, 4884100]], list_squared(1800, 2000))
        self.assertEquals([], list_squared(2000, 2200))
        self.assertEquals([[4264, 24304900]], list_squared(2200, 5000))
        self.assertEquals([[6237, 45024100], [9799, 96079204], [9855, 113635600]], list_squared(5000, 10000))
