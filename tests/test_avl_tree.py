from unittest import TestCase
from pyfiles.domain import AVLTreeNode
from pyfiles.avl_binary_tree import AVLBinaryTree
from utils import (
    get_fake_avl_tree,
    get_left_skewd_avl_tree,
    get_right_skewd_avl_tree,
    get_avl_tree_wo_insertion
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
        avl_tree = get_left_skewd_avl_tree()

        self.assertEqual(avl_tree.get_balance(), 2)

        adj_root = avl_tree.right_rotate(z=avl_tree.root)

        self.assertEqual(adj_root.data, 5)
        self.assertEqual(adj_root.left.data, 4)
        self.assertEqual(adj_root.right.data, 7)

    def test__insertion__success(self):
        avl_tree = AVLBinaryTree()

        for i in range(1,10):
            avl_tree.insert(i)

        balance = avl_tree.get_balance()

        self.assertTrue(abs(balance) < 2)

    def test__search__success(self):
        avl_tree = get_fake_avl_tree()

        node = avl_tree.search(data=4)

        self.assertEqual(node.data, 4)

    def test__left_count__success(self):
        avl_tree = AVLBinaryTree()

        for i in range(1,4):
            avl_tree.insert(data=i)

        self.assertEqual(avl_tree.root.left_count, 1)

        for i in range(4, 7):
            avl_tree.insert(data=i)

        self.assertEqual(avl_tree.root.left_count, 3)

        for i in range(7, 16):
            avl_tree.insert(data=i)

        self.assertEqual(avl_tree.root.left_count, 7)

    def test__get_median__success(self):
        avl_tree = get_fake_avl_tree()

        self.assertEqual(avl_tree.get_median(), 8)

        avl_tree = get_fake_avl_tree(n=10)

        self.assertEqual(avl_tree.get_median(), 5.5)

        avl_tree = get_fake_avl_tree(n=12)

        self.assertEqual(avl_tree.get_median(), 6.5)

    def test__delete_data__success(self):
        avl_tree = get_fake_avl_tree(n=31)
        self.assertEqual(avl_tree.root.left_count, 15)

        avl_tree.delete(data=1)
        self.assertEqual(avl_tree.root.left_count, 14)
        avl_tree.delete(data=2)
        self.assertEqual(avl_tree.root.left_count, 13)
        avl_tree.delete(data=3)

        self.assertEqual(avl_tree.root.left_count, 12)
        self.assertEqual(avl_tree.root.left.left.data, 6)

        avl_tree = get_fake_avl_tree(n=31)
        self.assertEqual(avl_tree.root.left_count, 15)
        avl_tree.delete(data=8)

        self.assertEqual(avl_tree.root.left.data, 9)
        self.assertEqual(avl_tree.root.left_count, 14)

        avl_tree = get_fake_avl_tree(n=7)
        node = avl_tree.delete(data=9)
        self.assertEqual(avl_tree.root.left_count, 3)
        self.assertIsNone(node)

        avl_tree = get_fake_avl_tree(n=7)
        node = avl_tree.delete(data=9)
