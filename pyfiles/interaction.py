from typing import List, Optional
from pyfiles.binary_tree import (
    TreeNode,
    RBinaryTree,
    ListOptions
)
from pyfiles.double_linked_list import DLinkedList


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
        if first_current.item < second_current.item:
            linked_list.append(first_current.item)
            first_current = first_current.next
        else:
            linked_list.append(second_current.item)
            second_current = second_current.next

    if not first_current and not second_current:
        return linked_list

    current = first_current if first_current else second_current

    while current:
        linked_list.append(current.item)
        current = current.next

    return linked_list


def balance_binary_search_tree(tree: RBinaryTree) -> RBinaryTree:
    array = tree.to_list(list_option=ListOptions.ARRAY)
    balanced_tree = RBinaryTree()
    balanced_tree.root = _balance_bst_recursive(
        array=array,
        parent=None
    )

    return balanced_tree


def _balance_bst_recursive(
    array: List[int],
    parent: Optional[TreeNode]
) -> Optional[TreeNode]:
    if not array:
        return None

    mid = len(array) // 2

    root = TreeNode(item=array[mid])
    root.parent = parent

    root.left = _balance_bst_recursive(array=array[:mid],parent=root)
    root.right = _balance_bst_recursive(array=array[mid+1:], parent=root)

    return root
