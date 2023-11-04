from typing import List, Optional
from pyfiles.binary_tree import (
    TreeNode,
    RBinaryTree,
    ListOptions
)
from pyfiles.avl_binary_tree import (
    AVLBinaryTree
)
from pyfiles.double_linked_list import DLinkedList
from pyfiles.bin_problem_structure import Bins

def merge_two_binary_search_trees(
    first_tree: RBinaryTree,
    second_tree: RBinaryTree
) -> DLinkedList:
    linked_list = DLinkedList()

    first_list = first_tree.to_list()
    second_list = second_tree.to_list()

    first_current = first_list.head
    second_current = second_list.head

    while first_current and second_current:
        if first_current.data < second_current.data:
            linked_list.append(first_current.data)
            first_current = first_current.next
        else:
            linked_list.append(second_current.data)
            second_current = second_current.next

    if not first_current and not second_current:
        return linked_list

    current = first_current if first_current else second_current

    while current:
        linked_list.append(current.data)
        current = current.next

    return linked_list


def balance_binary_search_tree(tree: RBinaryTree) -> RBinaryTree:
    array = tree.to_list(list_option=ListOptions.ARRAY)
    balanced_tree = RBinaryTree()
    balanced_tree.root = _create_balance_bst_recursive(array=array)

    return balanced_tree


def _create_balance_bst_recursive(
    array: List[int],
    parent: Optional[TreeNode] = None
) -> Optional[TreeNode]:
    if not array:
        return None

    mid = len(array) // 2

    root = TreeNode(data=array[mid])
    root.parent = parent

    root.left = _create_balance_bst_recursive(
        array=array[:mid],
        parent=root
    )
    root.right = _create_balance_bst_recursive(
        array=array[mid+1:],
        parent=root
    )

    return root


def concatenate_binary_search_tree(
    first_tree: RBinaryTree,
    second_tree: RBinaryTree
) -> RBinaryTree:
    """
    first_tree: all elements should be less than all second tree elements
    second_tree: all elements should be greater than all first tree elements
    """
    if not first_tree or not second_tree:
        return None

    second_tree.insert_node(first_tree.root)

    return second_tree


def is_array_k_unique(array: List[int], k: int) -> bool:
    """
        This function run O(nlog(k))
        Better algorithm could be implemented with a hash table
    """
    avl_tree = AVLBinaryTree()

    count = 0

    for e in array:
        previous = avl_tree.search(data=e)

        if previous:
            break

        avl_tree.insert(data=e)
        count += 1

    return count >= k
