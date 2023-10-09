from unittest import TestCase
from pyfiles.double_linked_list import (
    Node,
    DLinkedList
)


class TestLinkedList(TestCase):

    def test__insert_double_linked_list__success(self):
        linked_list = DLinkedList()

        for i in range(1, 11):
            _ = linked_list.insert(i)

        self.assertEqual(linked_list.head.item, 1)
        self.assertEqual(linked_list.tail.item, 10)

    def test__print_double_linked_list__success(self):
        linked_list = DLinkedList()

        for i in range(1, 11):
            _ = linked_list.insert(i)

        result = linked_list.print()

        self.assertEqual(result, '12345678910')
