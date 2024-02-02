from unittest import TestCase
from algos.divide_and_conquer_exercises import (
    largest_subrange,
    maximum_wood_cut,
    kadane_max_subarray_sum,
    median_sorted_arrays
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

    def test__maximum_wood_cut__success(self):
        array = [5, 9, 7]
        self.assertEqual(maximum_wood_cut(
            wood=array,
            n=len(array),
            k=4
        ), 4)

        array = [10, 6, 5, 3]
        self.assertEqual(maximum_wood_cut(
            wood=array,
            n=len(array),
            k=4
        ), 5)

    def test__median_sorted_arrays__success(self):
        nums1 = [1,2]
        nums2 = [3,4]
        median = median_sorted_arrays(nums1=nums1,nums2=nums2)
        assert median == 2.5
