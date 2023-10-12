from pyfiles.binary_tree import RBinaryTree


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