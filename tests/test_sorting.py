from unittest import TestCase
from algos.sorting import (
    merge_sort,
    quick_sort,
    heap_sort
)
from tests.utils import get_unsorted_array
from datetime import datetime


class TestSorting(TestCase):
    def test__merge_sort__success(self):
        array = get_unsorted_array(n=10)
        merge_sort(array=array, low=0, high=len(array) - 1)
        for i in range(len(array)-1):
            self.assertTrue(array[i] < array[i+1])

        array = get_unsorted_array(n=30)
        merge_sort(array=array, low=0, high=len(array) - 1)
        for i in range(len(array)-1):
            self.assertTrue(array[i] < array[i+1])

    def test__quick_sort__success(self):
        array = get_unsorted_array(n=10)
        quick_sort(array=array, low=0, high=len(array)-1)
        for i in range(len(array)-1):
            self.assertTrue(array[i] < array[i+1])

        array = get_unsorted_array(n=30)
        quick_sort(array=array, low=0, high=len(array)-1)
        for i in range(len(array)-1):
            self.assertTrue(array[i] < array[i+1])


    def test__heap_sort__success(self):
        test_n = 10
        array = get_unsorted_array(n=test_n)
        sorted_array = heap_sort(array=array)
        self.assertEqual(sorted_array, list(range(1, test_n+1)))

        test_n = 30
        array = get_unsorted_array(n=test_n)
        sorted_array = heap_sort(array=array)
        self.assertEqual(sorted_array, list(range(1, test_n+1)))


    def test__compare_running_time__success(self):
        RUNNING_TIMES, ARRAY_SIZE = 100, 20

        heap_array = []
        merge_array = []
        quick_array = []

        for i in range(RUNNING_TIMES):
            array = get_unsorted_array(n=ARRAY_SIZE+i)
            start = datetime.now()
            _ = heap_sort(array=array.copy())
            heap_array.append((datetime.now() - start).microseconds)
            start = datetime.now()
            _ = merge_sort(array=array.copy(), low=0, high=len(array) - 1)
            merge_array.append((datetime.now() - start).microseconds)
            start = datetime.now()
            _ = quick_sort(array=array.copy(), low=0, high=len(array) - 1)
            quick_array.append((datetime.now() - start).microseconds)

        print((heap_array, merge_array, quick_array))

        self.assertTrue(True)
