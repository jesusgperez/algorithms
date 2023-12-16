from typing import List
from random import choice, randint
from data_structures.binary_tree import RBinaryTree
from data_structures.bin_problem_structure import Bins
from data_structures.domain import TreeNode, AVLTreeNode
from data_structures.avl_binary_tree import AVLBinaryTree
from data_structures.interaction import _create_balance_bst_recursive
from data_structures.heap import Heap


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


def get_unbalanced_tree(n: int = 6) -> RBinaryTree:
    rtree = RBinaryTree()

    for i in range(1, n + 1):
        rtree.insert(i)

    return rtree


def get_balanced_tree(start: int = 1, n: int = 15) -> RBinaryTree:
    balanced_tree = RBinaryTree()
    delta = start + n
    balanced_tree.root = _create_balance_bst_recursive(
        array=list(range(start, delta))
    )

    balanced_tree.n = n

    return balanced_tree


def get_tree_for_deletion() -> RBinaryTree:
    tree = RBinaryTree()
    tree.insert(7)
    tree.insert(8)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree.insert(6)

    return tree


def get_avl_tree_wo_insertion(
    skip_level_right: bool = False,
    skip_level_left: bool = False
) -> AVLBinaryTree:
    root = TreeNode(data=4)
    rl = TreeNode(data=2)
    root.left = rl
    rl.parent = root
    rr = TreeNode(data=5)
    root.right = rr
    rr.parent = root
    if not skip_level_left:
        rll = TreeNode(data=1)
        rl.left = rll
        rll.parent = rl
        rlr = TreeNode(data=3)
        rl.right = rlr
        rlr.parent = rl
    if not skip_level_right:
        rrr = TreeNode(data=6)
        rr.right = rrr
        rrr.parent = rr
    AVLTree = AVLBinaryTree()
    AVLTree.root = root
    return AVLTree


def get_right_skewd_avl_tree() -> AVLBinaryTree:
    root = AVLTreeNode(data=5, height=3)
    r = AVLTreeNode(data=7, height=2, parent=root)
    root.right = r
    rr = AVLTreeNode(data=8, parent=r)
    r.right = rr
    rl = AVLTreeNode(data=6, parent=r)
    r.left = rl

    avl_tree = AVLBinaryTree()
    avl_tree.root = root

    return avl_tree


def get_left_skewd_avl_tree() -> AVLBinaryTree:
    root = AVLTreeNode(data=7, height=3)
    l = AVLTreeNode(data=5, height=2, parent=root)
    root.left = l
    ll = AVLTreeNode(data=4, parent=l)
    l.left = ll
    lr = AVLTreeNode(data=6, parent=l)
    l.right = lr

    avl_tree = AVLBinaryTree()
    avl_tree.root = root

    return avl_tree


def get_fake_avl_tree(start: int = 1, n: int = 15) -> AVLBinaryTree:
    avl_tree = AVLBinaryTree()
    for i in range(start, start + n):
        avl_tree.insert(data=i)

    return avl_tree


def get_fake_bins_tree() -> Bins:
    bins = Bins(capacity=1)
    bins.insert(0.8)
    bins.insert(0.6)
    bins.insert(0.9)
    bins.insert(0.5)
    bins.insert(0.7)

    return bins


def get_tree_of_failing_test_case():
    rtree = RBinaryTree()

    root = TreeNode(data=32)
    rl = TreeNode(data=26)
    root.left = rl
    rr = TreeNode(data=47)
    root.right = rr
    rll = TreeNode(data=19)
    root.left.left = rll
    rllr = TreeNode(data=27)
    root.left.left.right = rllr
    rrr = TreeNode(data=56)
    root.right.right = rrr

    rtree.root = root
    return rtree


def get_basic_heap():
    heap = Heap(size=16)

    heap.insert(data=5)
    heap.insert(data=4)
    heap.insert(data=3)
    heap.insert(data=7)
    heap.insert(data=8)

    return heap


def get_unsorted_array(n: int) -> List[int]:
    lista = list(range(1, n + 1))
    unsorted = []

    for _ in range(n):
        element = choice(lista)
        unsorted.append(element)
        lista.remove(element)

    return unsorted


def intervals_generator(n: int = 10):
    array = []

    for _ in range(10):
        now = randint(20, 60)
        delta = randint(10, 15)
        start = now - delta
        delta = randint(-10, 0)
        end = now + delta
        array.append((start,end))
    
    return array
