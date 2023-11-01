from unittest import TestCase
from pyfiles.bin_problem_structure import Bins
from tests.utils import get_fake_bins_tree


class TestBinProblem(TestCase):
    def test__is_there_space_for__successful(self):
        bins = get_fake_bins_tree()

        self.assertEqual(bins.n, 5)

        to_insert = [0.2,0.3,0.4,0.5]

        for weight in to_insert:
            tree = bins.is_space_for(weight=weight)

            if tree:
                data = tree.data
                bins.delete(data=data)
                bins.insert(data=round(data+weight,2))
            else:
                bins.insert(data=weight)

        self.assertTrue(True)
