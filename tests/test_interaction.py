from unittest import TestCase
from pyfiles.binary_tree import RBinaryTree
from pyfiles.interaction import merge_two_binary_search_trees

def get_basic_tree() -> RBinaryTree:
    rtree = RBinaryTree()
    rtree.insert(5)
    rtree.insert(3)
    rtree.insert(7)
    rtree.insert(4)
    rtree.insert(2)
    rtree.insert(6)
    rtree.insert(8)

    return rtree

def get_second_basic_tree() -> RBinaryTree:
    rtree = RBinaryTree()
    rtree.insert(15)
    rtree.insert(13)
    rtree.insert(17)
    rtree.insert(14)
    rtree.insert(12)
    rtree.insert(16)
    rtree.insert(18)

    return rtree


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
