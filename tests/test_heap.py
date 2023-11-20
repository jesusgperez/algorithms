from unittest import TestCase
from data_structures.heap import Heap
from data_structures.domain import HeapChild
from tests.utils import (
    get_basic_heap
)


class TestHeap(TestCase):
    def test__get_parent_position__successful(self):
        heap = Heap(size=8)
        heap.queue = [None, 1, 2, 3, 5, 7, 6, 9]
        heap.n = 8

        parent = heap.get_parent_position(position=4)
        self.assertEqual(heap.queue[parent], 2)

    def test__get_childs_position__successful(self):
        heap = Heap(size=8)
        heap.queue = [None, 1, 2, 3, 5, None, 6, 9]
        heap.n = 8

        left_child = heap.get_child(
            child_type=HeapChild.LEFT,
            position=1
        )

        self.assertEqual(heap.queue[left_child], 2)

        right_child = heap.get_child(
            child_type=HeapChild.RIGHT,
            position=1
        )

        self.assertEqual(heap.queue[right_child], 3)

        left_child = heap.get_child(
            child_type=HeapChild.LEFT,
            position=2
        )

        self.assertEqual(heap.queue[left_child], 5)

        right_child = heap.get_child(
            child_type=HeapChild.RIGHT,
            position=2
        )

        self.assertEqual(heap.queue[right_child], None)

    def test__insert__success(self):
        heap = get_basic_heap
        self.assertEqual(heap.queue[1], 3)

    def test__extract_min__success(self):
        heap = get_basic_heap()

        min_value = heap.extract_min()
        self.assertEqual(min_value, 3)
        self.assertEqual(heap.queue[1], 4)

        min_value = heap.extract_min()
        self.assertEqual(min_value, 4)
        self.assertEqual(heap.queue[1], 5)

        min_value = heap.extract_min()
        self.assertEqual(min_value, 5)
        self.assertEqual(heap.queue[1], 7)

        min_value = heap.extract_min()
        self.assertEqual(min_value, 7)
        self.assertEqual(heap.queue[1], 8)

