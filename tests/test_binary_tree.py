from unittest import TestCase
from pyfiles.binary_tree import (
    RBinaryTree,
    TreeTraversal
)


class TestBinaryTree(TestCase):

    def test__recursive_insertion__successful(self):
        rtree = RBinaryTree()
        rtree.insert(5)
        rtree.insert(3)
        rtree.insert(7)
        rtree.insert(4)
        rtree.insert(2)
        rtree.insert(6)
        rtree.insert(8)

        self.assertEqual(rtree.root.item, 5)
        self.assertEqual(rtree.root.left.left.item, 2)

    def test__recursive_traverse__successful(self):
        rtree = RBinaryTree()
        rtree.insert(5)
        rtree.insert(3)
        rtree.insert(7)
        rtree.insert(4)
        rtree.insert(2)
        rtree.insert(6)
        rtree.insert(8)

        traverse = rtree.traverse(TreeTraversal.INORDER)
        self.assertEqual(traverse, '2345678')
    
        traverse = rtree.traverse(TreeTraversal.PREORDER)
        self.assertEqual(traverse, '5324768')

        traverse = rtree.traverse(TreeTraversal.POSTORDER)
        self.assertEqual(traverse, '2436875')

    def test__recursive_get_depth__successful(self):
        rtree = RBinaryTree()
        rtree.insert(5)
        rtree.insert(3)
        rtree.insert(7)
        rtree.insert(4)
        rtree.insert(2)
        rtree.insert(6)
        rtree.insert(8)

        depth = rtree.get_depth()

        self.assertEqual(depth, 3)

