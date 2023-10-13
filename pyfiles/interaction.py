from pyfiles.binary_tree import RBinaryTree
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
            linked_list.insert(first_current.item)
            first_current = first_current.next
        else:
            linked_list.insert(second_current.item)
            second_current = second_current.next

    if not first_current and not second_current:
        return linked_list

    current = first_current if first_current else second_current

    while current:
        linked_list.insert(current.item)
        current = current.next

    return linked_list
