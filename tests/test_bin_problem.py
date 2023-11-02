from unittest import TestCase
from pyfiles.bin_problem_structure import Bins
from tests.utils import get_fake_bins_tree


class TestBinProblem(TestCase):
    def test__is_there_space_for__successful(self):
        bins = get_fake_bins_tree()

        self.assertEqual(bins.n, 5)

        to_insert = [0.2,0.3,0.4,0.5]

        for weight in to_insert:
            tree = bins.get_best_fit(weight=weight)

            if tree:
                data = tree.data
                bins.delete(data=data)
                bins.insert(data=round(data+weight,2))
            else:
                bins.insert(data=weight)

        self.assertEqual(bins.n, 6)

        to_insert = [0.2,0.8,0.4,0.7,0.5,0.6,0.9,0.5,0.1,0.2]

        bins = Bins(capacity=1)

        for weight in to_insert:
            tree = bins.get_best_fit(weight=weight)

            if tree:
                data = tree.data
                bins.delete(data=data)
                bins.insert(data=round(data+weight,2))
            else:
                bins.insert(data=weight)

        self.assertEqual(bins.n, 5)
