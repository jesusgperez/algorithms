from unittest import TestCase
from data_structures.bin_problem_structure import Bins
from tests.utils import get_fake_bins_tree


class TestBinProblem(TestCase):
    def test__is_there_space_for__successful(self):
        to_pack = [0.2,0.8,0.4,0.7,0.5,0.6,0.9,0.5,0.1,0.2]

        bins = Bins(capacity=1)

        for weight in to_pack:
            bins.pack(weight=weight)

        self.assertEqual(bins.n, 6)

        to_pack = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

        bins = Bins(capacity=1)

        for weight in to_pack:
            bins.pack(weight=weight)

        self.assertEqual(bins.n, 6)
