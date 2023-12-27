from random import randint
from datetime import datetime, timedelta
from unittest import TestCase
from utils import get_unsorted_array
from algos.sorting_exercises import (
    find_median,
    binary_search,
    k_element_sum,
    most_people_at_party,
    max_intervals_points,
    unique_elements_array,
    merge_overlapping_intervals,
    reconstruct_queue_by_height
)


class TestExercises(TestCase):
    def test__k_element_sum__success(self):
        array = [1,2,3,4,5,6]
        self.assertTrue(k_element_sum(array=array, k=2, t=3))
        self.assertFalse(k_element_sum(array=array, k=3, t=3))
        self.assertTrue(k_element_sum(array=array, k=2, t=6))


    def test__binary_search__success(self):
        array = [1,2,3,4,5,6]
        self.assertTrue(binary_search(array=array, element=5))

        array = list(range(50))
        for i in range(50):
            self.assertTrue(binary_search(array=array, element=i))
        self.assertFalse(binary_search(array=array, element=51))
        self.assertFalse(binary_search(array=array, element=-1))

    def test__unique_elements_array__success(self):
        array1 = [5, 6, 7, 8, 10, 12, 13]
        array2 = [1, 2, 3, 5, 8, 12]

        unique = unique_elements_array(array1=array1, array2=array2)

        self.assertEqual(unique, [1,2,3,5,6,7,8,10,12,13])

    def test__most_people_at_party__success(self):
        array = []

        for _ in range(10):
            delta = randint(-10, 10)
            now = datetime.now() + timedelta(minutes=delta)
            delta = randint(0, 10)
            start = now - timedelta(minutes=delta)
            delta = randint(0, 10)
            end = now + timedelta(minutes=delta)
            array.append((start,end))

        start, end = most_people_at_party(array=array)

        self.assertTrue(start < end)

    def test__merge_overlapping_intervals__success(self):
        array = [(13, 19), (15, 26), (17, 27), (18, 18), (19, 21), (22, 28), (31, 35), (32, 36), (33, 42), (41, 54)]
        merged = merge_overlapping_intervals(array=array)
        self.assertEqual(len(merged), 2)

        array = [(9, 20), (13, 13), (22, 29), (23, 30), (27, 35), (33, 40), (44, 48), (44, 53), (45, 48), (45, 57)]
        merged = merge_overlapping_intervals(array=array)
        self.assertEqual(len(merged), 3)

    def test__max_intervals_points(self):
        array = [(13, 19), (15, 26), (17, 27), (18, 18), (19, 21), (22, 28), (31, 35), (32, 36), (33, 42), (41, 54)]
        interval = max_intervals_points(array=array)
        self.assertEqual(interval, (18, 18))

        array = [(9, 20), (13, 13), (22, 29), (23, 30), (27, 35), (33, 40), (44, 48), (44, 53), (45, 48), (45, 57)]
        interval = max_intervals_points(array=array)
        self.assertEqual(interval, (45, 48))

    def test__find_median_by_partition__success(self):
        array = [4,2,9,7,6,34,10,33,24,8]
        median = find_median(array=array)
        self.assertEqual(median, 9)

        array = get_unsorted_array(n=21)
        median = find_median(array=array)
        self.assertEqual(median, 11)

    def test__reconstruct_queue_by_height__success(self):
        array = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
        resp = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

        self.assertEqual(reconstruct_queue_by_height(array=array), resp)
