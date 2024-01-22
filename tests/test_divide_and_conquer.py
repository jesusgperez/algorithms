from unittest import TestCase
from algos.divide_and_conquer_exercises import (
    largest_subrange,
    kadane_max_subarray_sum
)


class TestDivideConquer(TestCase):
    def test__largest_subrange__success(self):
        array = [-2, -3, 4, -1, -2, 1, 5, -3]
        lsum = largest_subrange(
           array=array,
           low=0,
           high=len(array) - 1
        )

        self.assertEqual(lsum, 7)

    def test__kadanes_algorithm__success(self):
        array = [-2, -3, 4, -1, -2, 1, 5, -3]
        lsum, max_list = kadane_max_subarray_sum(
            array=array
        )
        self.assertEqual(lsum, 7)
