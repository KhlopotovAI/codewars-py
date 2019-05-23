from random import randint
from unittest import TestCase

from .kata import solution


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual('-6,-3-1,3-5,7-11,14,15,17-20',
                         solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
        self.assertEqual('-3--1,2,10,15,16,18-20', solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
        self.assertEqual('1-5', solution([1, 2, 3, 4, 5]))

        def solver(args):
            rnge, ans = [], []
            for n1, n2 in zip(args, args[1:] + ['']):
                if n1 + 1 == n2:
                    if not rnge:
                        rnge = [n1, n2]
                    else:
                        rnge[1] = n2

                else:
                    if rnge:
                        if rnge[0] + 1 == rnge[1]:
                            ans.extend(map(str, rnge))
                        else:
                            ans.append('-'.join(map(str, rnge)))
                        rnge = []
                    else:
                        ans.append(str(n1))

            return ",".join(ans)

        for _ in range(20):
            y = randint(-100, -50)
            x = [y]
            for __ in range(randint(10, 30)):
                y += randint(1, 3)
                x.append(y)
            self.assertEqual(solver(x), solution(list(x)), "It should work for random inputs too")
