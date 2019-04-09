import random
from unittest import TestCase

from .kata import find_uniq


class TestFindUniq(TestCase):
    def test_find_uniq(self):
        self.assertEquals(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']), 'BbBb')
        self.assertEquals(find_uniq(['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']), 'foo')
        self.assertEquals(find_uniq(['silvia', 'vasili', 'victor']), 'victor')
        self.assertEquals(find_uniq(['Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter']), 'Harry Potter')

        a = random.choice('aeiou')
        b = random.choice('pqrst')
        self.assertEquals(find_uniq([a, b, b, b]), a, 'Very first elem')
        self.assertEquals(find_uniq([b, a, b, b]), a, 'Second elem')
        self.assertEquals(find_uniq([b, b, a, b]), a, 'Third elem')
        self.assertEquals(find_uniq([b, b, b, a]), a, 'Last elem')

        self.assertEquals(find_uniq(['', '', '', 'a', '', '']), 'a')
        self.assertEquals(find_uniq(['    ', '  ', ' ', 'a', ' ', '']), 'a')
        self.assertEquals(find_uniq(['foobar', 'barfo', 'fobara', '   ', 'fobra', 'oooofrab']), '   ')

        def generate_test_arr(answer, mass, length):
            arr = [mass] * length
            arr[random.randrange(length - 1)] = answer
            return arr

        self.assertEquals(find_uniq(generate_test_arr('Loga', 'Gollum', 1500000)), 'Loga')

        answer = hex(random.randrange(9999))
        mass = hex(random.randrange(9999))
        self.assertEquals(find_uniq(generate_test_arr(answer, mass, 1000)), answer)
