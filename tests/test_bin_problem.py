from random import random
from unittest import TestCase
from pyfiles.bin_problem_structure import Bins


class TestBinProblem(TestCase):
    def test__is_there_space_for__successful(self):
        bins = Bins(capacity=1)

        for _ in range(10):
            bins.insert(data=round(random(), ndigits=2))

        self.assertEqual(bins.n, 10)

        tree = bins.is_space_for(weight=0.8)

        self.assertTrue(True)
