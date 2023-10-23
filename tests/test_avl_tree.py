from unittest import TestCase
from pyfiles.domain import AVLTreeNode
from pyfiles.avl_binary_tree import AVLBinaryTree
from utils import (
    get_avl_tree_wo_insertion,
    get_right_skewd_avl_tree
)


class TestAvlTree(TestCase):
    def test__get_balance__success(self):
        avl_tree = get_avl_tree_wo_insertion()
        self.assertEqual(avl_tree.get_balance(), 0)

        avl_tree = get_avl_tree_wo_insertion(skip_level_left=True)
        self.assertEqual(avl_tree.get_balance(), -1)

        avl_tree = get_avl_tree_wo_insertion(skip_level_right=True)
        self.assertEqual(avl_tree.get_balance(), 1)

        avl_tree = get_avl_tree_wo_insertion(
            skip_level_right=True,
            skip_level_left=True
        )
        self.assertEqual(avl_tree.get_balance(), 0)

    def test__get_depth__success(self):
        avl_tree = get_avl_tree_wo_insertion()
        self.assertEqual(avl_tree.get_depth(), 3)

        avl_tree = get_avl_tree_wo_insertion(skip_level_left=True)
        self.assertEqual(avl_tree.get_depth(), 3)

        avl_tree = get_avl_tree_wo_insertion(skip_level_right=True)
        self.assertEqual(avl_tree.get_depth(), 3)

        avl_tree = get_avl_tree_wo_insertion(
            skip_level_right=True,
            skip_level_left=True
        )
        self.assertEqual(avl_tree.get_depth(), 2)

    def test__get_height__success(self):
        avl_tree = AVLBinaryTree()

        self.assertEqual(avl_tree.get_height(tree=None), 0)

        node = AVLTreeNode(data=3, height=2)

        self.assertEqual(avl_tree.get_height(tree=node), 2)

    def test__left_rotate__success(self):
        avl_tree = get_right_skewd_avl_tree()

        self.assertEqual(avl_tree.get_balance(), -2)

        adj_root = avl_tree.left_rotate(z=avl_tree.root)

        self.assertEqual(adj_root.data, 7)
        self.assertEqual(adj_root.left.data, 5)
        self.assertEqual(adj_root.right.data, 8)

    def test__right_rotate__success(self):
        pass
