from unittest import TestCase
from algos.sorting import merge_sort, quick_sort
from tests.utils import get_unsorted_array


class TestSorting(TestCase):
    def test__merge_sort__sucess(self):
        array = get_unsorted_array(n=10)

        merge_sort(array=array, low=0, high=len(array))

        for i in range(len(array)-1):
            self.assertTrue(array[i] < array[i+1])
