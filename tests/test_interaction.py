from unittest import TestCase
from pyfiles.interaction import (
    merge_two_binary_search_trees,
    balance_binary_search_tree
)
from utils import (
    get_basic_tree,
    get_depth_tree,
    get_unbalanced_tree,
    get_second_basic_tree
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

        self.assertEqual(linked_list.head.item, 2)
        self.assertEqual(linked_list.tail.item, 18)

    def test__balance_tree__successful(self):
        rtree = get_unbalanced_tree()
        balanced_tree = balance_binary_search_tree(tree=rtree)

        self.assertTrue(balanced_tree.is_balanced())

        rtree = get_depth_tree()
        balanced_tree = balance_binary_search_tree(tree=rtree)

        self.assertTrue(balanced_tree.is_balanced())
