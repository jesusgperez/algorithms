from unittest import TestCase
from typing import List
from pyfiles.binary_tree import (
    TreeNode,
    ListOptions,
    TreeTraversal,
    RBinaryTree
)
from pyfiles.double_linked_list import (
    DLinkedList
)
from utils import(
    get_basic_tree,
    get_depth_tree,
    get_balanced_tree,
    get_unbalanced_tree,
    get_tree_for_deletion
)

class TestBinaryTree(TestCase):

    def test__recursive_insertion__successful(self):
        rtree = get_basic_tree()

        self.assertEqual(rtree.root.data, 5)
        self.assertEqual(rtree.root.left.left.data, 2)

    def test__recursive_traverse__successful(self):
        rtree = get_basic_tree()

        traverse = rtree.traverse(TreeTraversal.INORDER)
        self.assertEqual(traverse, '-2-3-4-5-6-7-8')
    
        traverse = rtree.traverse(TreeTraversal.PREORDER)
        self.assertEqual(traverse, '-5-3-2-4-7-6-8')

        traverse = rtree.traverse(TreeTraversal.POSTORDER)
        self.assertEqual(traverse, '-2-4-3-6-8-7-5')

    def test__recursive_get_depth__successful(self):
        rtree = get_basic_tree()

        depth = rtree.get_depth()

        self.assertEqual(depth, 3)

        rtree = get_depth_tree()

        depth = rtree.get_depth()

        self.assertEqual(depth, 5)

    def test__recursive_search__successful(self):
        rtree = get_basic_tree()
        SEARCH_DATA = 6

        tree_node = rtree.search(data=SEARCH_DATA)

        self.assertEqual(tree_node.data, SEARCH_DATA)

    def test__swapped_data__successful(self):
        rtree = get_basic_tree()
        rtree.root.left.right.data = 6
        rtree.root.right.left.data = 4

        swapped: List[TreeNode] = rtree.find_swapped()

        self.assertEqual(len(swapped), 2)
        self.assertEqual(swapped[0], '6')
        self.assertEqual(swapped[1], '4')

    def test__to_list__successful(self):
        rtree = get_basic_tree()
        dlist = rtree.to_list()

        self.assertEqual(dlist.head.data, 2)
        self.assertEqual(dlist.tail.data, 8)
        self.assertEqual(type(dlist), DLinkedList)

        dlist = rtree.to_list(list_option=ListOptions.ARRAY)

        self.assertEqual(dlist[0], 2)
        self.assertEqual(dlist[-1], 8)
        self.assertEqual(type(dlist), list)

    def test__is_balanced__successful(self):
        rtree = get_basic_tree()
        balanced = rtree.is_balanced()

        self.assertTrue(balanced)

        rtree = get_unbalanced_tree()
        balanced = rtree.is_balanced()

        self.assertFalse(balanced)

        rtree = get_depth_tree()
        balanced = rtree.is_balanced()

        self.assertFalse(balanced)

    def test__balanced_tree(self):
        rtree = get_balanced_tree()
        self.assertEqual(rtree.root.data, 8)

        rtree = get_balanced_tree(n=32)
        self.assertEqual(rtree.root.data, 17)

    def test__get_successor__successful(self):
        rtree = get_balanced_tree()
        successor10 = rtree.get_successor(data=10)

        self.assertEqual(successor10.data, 11)

        successor11 = rtree.get_successor(data=11)

        self.assertEqual(successor11.data, 12)

    def test__get_predecessor__successful(self):
        rtree = get_balanced_tree(n=32)

        predecessor20 = rtree.get_predecessor(data=20)

        self.assertEqual(predecessor20.data, 19)

    def test__insert_node__successful(self):
        rtree = get_balanced_tree(start=4, n=15)

        new_node = TreeNode(data=2)

        rtree.insert_node(new_node=new_node)

        self.assertEqual(rtree.find_minimum().data, 2)

        new_node = TreeNode(data=1)
        new_node.left = TreeNode(data=0, parent=new_node)

        rtree.insert_node(new_node=new_node)

        self.assertEqual(rtree.find_minimum().data, 0)

    def test__get_median__successful(self):
        rtree = get_balanced_tree()

        median = rtree.get_median()

        self.assertEqual(median, 7)

    def test__get_n_recursive__sucessful(self):
        rtree = get_balanced_tree()
        self.assertEqual(rtree.get_n(), 15)

        rtree = get_balanced_tree(start=1, n=7)
        self.assertEqual(rtree.get_n(), 7)

    def test__delete_data__successful(self):
        rtree = get_balanced_tree()

        rtree.delete(data=4)

        self.assertEqual(rtree.root.left.data, 5)

        rtree = get_tree_for_deletion()

        rtree.delete(data=4)

        self.assertEqual(rtree.root.left.data, 5)

    def test__create_tree_from_inpre_order__success(self):
        preorder = [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]
        inorder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        rtree = RBinaryTree()

        rtree.create_from_orders(
            preorder=preorder,
            inorder=inorder
        )

        self.assertEqual(rtree.root.data, 8)
        self.assertEqual(rtree.root.left.data, 4)
        self.assertEqual(rtree.root.left.left.data, 2)
        self.assertEqual(rtree.root.left.right.data, 6)
        self.assertEqual(rtree.root.right.data, 12)
        self.assertEqual(rtree.root.right.left.data, 10)
        self.assertEqual(rtree.root.right.right.data, 14)
