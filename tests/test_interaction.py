from unittest import TestCase
from pyfiles.leetcode_problems.count_smaller_nums import CountTree
from pyfiles.interaction import (
    is_array_k_unique,
    balance_binary_search_tree,
    merge_two_binary_search_trees,
    concatenate_binary_search_tree,
)
from utils import (
    get_basic_tree,
    get_depth_tree,
    get_balanced_tree,
    get_unbalanced_tree,
    get_second_basic_tree,
    get_tree_of_failing_test_case
)


class TestInteraction(TestCase):
    def test__merge_two_binary_search_trees__successful(self):
        first_tree = get_basic_tree()
        second_tree = get_second_basic_tree()

        # Test separate trees

        linked_list = merge_two_binary_search_trees(
            first_tree=first_tree,
            second_tree=second_tree
        )

        self.assertEqual(linked_list.head.data, 2)
        self.assertEqual(linked_list.tail.data, 18)

    def test__balance_tree__successful(self):
        rtree = get_unbalanced_tree()
        balanced_tree = balance_binary_search_tree(tree=rtree)

        self.assertTrue(balanced_tree.is_balanced())

        rtree = get_depth_tree()
        balanced_tree = balance_binary_search_tree(tree=rtree)

        self.assertTrue(balanced_tree.is_balanced())

    def test__concatenate_binary_search_tree__successful(self):
        first_tree = get_balanced_tree()
        second_tree = get_balanced_tree(start=16, n=15)

        concat_tree = concatenate_binary_search_tree(
            first_tree=first_tree,
            second_tree=second_tree
        )

        self.assertEqual(concat_tree.get_depth(), 8)

    def test__is_array_k_unique__success(self):
        array = [1,2,3,4,5,6,7,1]

        self.assertTrue(is_array_k_unique(array=array,k=6))
        self.assertTrue(is_array_k_unique(array=array,k=7))
        self.assertFalse(is_array_k_unique(array=array,k=8))

    def test__is_tree_valid__failed(self):
        rtree = get_tree_of_failing_test_case()

        self.assertFalse(rtree.is_valid())


    def test__count_smaller_after_self__success(self):
        rtree = CountTree()

        to_insert = [5,2,6,1]

        for num in to_insert:
            rtree.insert(num)

        resp = []

        for num in to_insert:
            node = rtree.search(data=num)
            resp.append(node.left_count)

        self.assertEqual(resp, [2,1,1,0])

        rtree = CountTree()

        to_insert = [-1]

        for num in to_insert:
            rtree.insert(num)

        resp = []

        for num in to_insert:
            node = rtree.search(data=num)
            resp.append(node.left_count)

        self.assertEqual(resp, [0])

        rtree = CountTree()

        to_insert = [-1, -1]

        for num in to_insert:
            rtree.insert(num)

        resp = []

        for num in to_insert:
            node = rtree.search(data=num)
            resp.append(node.left_count)

        self.assertEqual(resp, [0, 0])


