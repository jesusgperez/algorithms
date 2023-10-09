from unittest import TestCase
from typing import List
from pyfiles.binary_tree import (
    TreeNode,
    RBinaryTree,
    TreeTraversal
)


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


def get_depth_tree() -> RBinaryTree:
    rtree = RBinaryTree()
    rtree.insert(7)
    rtree.insert(8)
    rtree.insert(3)
    rtree.insert(4)
    rtree.insert(2)
    rtree.insert(5)
    rtree.insert(6)

    return rtree


class TestBinaryTree(TestCase):

    def test__recursive_insertion__successful(self):
        rtree = get_basic_tree()

        self.assertEqual(rtree.root.item, 5)
        self.assertEqual(rtree.root.left.left.item, 2)

    def test__recursive_traverse__successful(self):
        rtree = get_basic_tree()

        traverse = rtree.traverse(TreeTraversal.INORDER)
        self.assertEqual(traverse, '2345678')
    
        traverse = rtree.traverse(TreeTraversal.PREORDER)
        self.assertEqual(traverse, '5324768')

        traverse = rtree.traverse(TreeTraversal.POSTORDER)
        self.assertEqual(traverse, '2436875')

    def test__recursive_get_depth__successful(self):
        rtree = get_basic_tree()

        depth = rtree.get_depth()

        self.assertEqual(depth, 3)

        rtree = get_depth_tree()

        depth = rtree.get_depth()

        self.assertEqual(depth, 5)

    def test__recursive_search__successful(self):
        rtree = get_basic_tree()
        SEARCH_ITEM = 6

        tree_node = rtree.search(item=SEARCH_ITEM)

        self.assertEqual(tree_node.item, SEARCH_ITEM)
        self.assertEqual(tree_node.parent.item, 7)

    def test__swapped_items__successful(self):
        rtree = get_basic_tree()
        rtree.root.left.right.item = 6
        rtree.root.right.left.item = 4

        swapped: List[TreeNode] = rtree.find_swapped()

        self.assertEqual(len(swapped), 2)
        self.assertEqual(swapped[0], 6)
        self.assertEqual(swapped[1], 4)
