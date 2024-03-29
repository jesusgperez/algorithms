from random import randint
from datetime import datetime, timedelta
from unittest import TestCase
from utils import get_unsorted_array
from data_structures.double_linked_list import (
    DLinkedList
)
from algos.sorting_exercises import (
    find_median,
    binary_search,
    k_element_sum,
    most_people_at_party,
    max_intervals_points,
    unique_elements_array,
    merge_overlapping_intervals,
    reconstruct_queue_by_height,
    merge_sorted_lists,
    k_smallest_pairs
)


class TestExercises(TestCase):
    def test__k_element_sum__success(self):
        array = [1, 2, 3, 4, 5, 6]
        self.assertTrue(k_element_sum(array=array, k=2, t=3))
        self.assertFalse(k_element_sum(array=array, k=3, t=3))
        self.assertTrue(k_element_sum(array=array, k=2, t=6))

    def test__binary_search__success(self):
        array = [1, 2, 3, 4, 5, 6]
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

        self.assertEqual(unique, [1, 2, 3, 5, 6, 7, 8, 10, 12, 13])

    def test__most_people_at_party__success(self):
        array = []

        for _ in range(10):
            delta = randint(-10, 10)
            now = datetime.now() + timedelta(minutes=delta)
            delta = randint(0, 10)
            start = now - timedelta(minutes=delta)
            delta = randint(0, 10)
            end = now + timedelta(minutes=delta)
            array.append((start, end))

        start, end = most_people_at_party(array=array)

        self.assertTrue(start < end)

    def test__merge_overlapping_intervals__success(self):
        array = [(13, 19), (15, 26), (17, 27), (18, 18), (19, 21),
                 (22, 28), (31, 35), (32, 36), (33, 42), (41, 54)]
        merged = merge_overlapping_intervals(array=array)
        self.assertEqual(len(merged), 2)

        array = [(9, 20), (13, 13), (22, 29), (23, 30), (27, 35),
                 (33, 40), (44, 48), (44, 53), (45, 48), (45, 57)]
        merged = merge_overlapping_intervals(array=array)
        self.assertEqual(len(merged), 3)

    def test__max_intervals_points(self):
        array = [(13, 19), (15, 26), (17, 27), (18, 18), (19, 21),
                 (22, 28), (31, 35), (32, 36), (33, 42), (41, 54)]
        interval = max_intervals_points(array=array)
        self.assertEqual(interval, (18, 18))

        array = [(9, 20), (13, 13), (22, 29), (23, 30), (27, 35),
                 (33, 40), (44, 48), (44, 53), (45, 48), (45, 57)]
        interval = max_intervals_points(array=array)
        self.assertEqual(interval, (45, 48))

    def test__find_median_by_partition__success(self):
        array = [4, 2, 9, 7, 6, 34, 10, 33, 24, 8]
        median = find_median(array=array)
        self.assertEqual(median, 9)

        array = get_unsorted_array(n=21)
        median = find_median(array=array)
        self.assertEqual(median, 11)

    def test__reconstruct_queue_by_height__success(self):
        array = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        resp = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

        self.assertEqual(reconstruct_queue_by_height(array=array), resp)

    def test__merge_sorted_lists__success(self):
        lists = []
        max_num = 5
        for i in range(0, max_num, 2):
            llist = DLinkedList()
            ilist = list(range(i, max_num))
            for element in ilist:
                llist.append(element)
            lists.append(llist.head)

        final = merge_sorted_lists(lists=lists, low=0, high=len(lists)-1)

        self.assertEqual(final.data, 0)

    def test__k_smallest_pairs__success(self):
        left, right = [1, 7, 11], [2, 4, 6]
        k = 3
        self.assertEqual(
            k_smallest_pairs(nums1=left, nums2=right, k=k),
            [(1, 2), (1, 4), (1, 6)]
        )

        k = 4
        self.assertEqual(
            k_smallest_pairs(nums1=left, nums2=right, k=k),
            [(1, 2), (1, 4), (1, 6), (7, 2)]
        )

        left, right = [1, 1, 2], [1, 2, 3]
        k = 2
        self.assertEqual(
            k_smallest_pairs(nums1=left, nums2=right, k=k),
            [(1, 1), (1, 1)]
        )

        left, right = [1, 2], [3]
        k = 3
        self.assertEqual(
            k_smallest_pairs(nums1=left, nums2=right, k=k),
            [(1, 3), (2, 3)]
        )

        left = [0, 0, 0, 0, 0, 2, 2, 2, 2]
        right = [-3, 22, 35, 56, 76]
        k = 22
        self.assertEqual(
            k_smallest_pairs(nums1=left, nums2=right, k=k),
            [
                (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (2, -3), (2, -3),
                (2, -3), (2, -3), (0, 22), (0, 22), (0, 22), (0, 22), (0, 22),
                (2, 22), (2, 22), (2, 22), (2, 22), (0, 35), (0, 35), (0, 35),
                (0, 35)
            ]
        )
