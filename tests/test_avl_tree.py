from unittest import TestCase
from pyfiles.avl_binary_tree import AVLBinaryTree
from utils import get_avl_tree_wo_insertion

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
