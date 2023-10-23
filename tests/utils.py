from pyfiles.domain import TreeNode, AVLTreeNode
from pyfiles.binary_tree import RBinaryTree
from pyfiles.avl_binary_tree import AVLBinaryTree
from pyfiles.interaction import _create_balance_bst_recursive


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
