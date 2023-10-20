from unittest import TestCase
from pyfiles.double_linked_list import (
    DLinkedList
)


class TestLinkedList(TestCase):

    def test__append_double_linked_list__success(self):
        linked_list = DLinkedList()

        for i in range(1, 11):
            linked_list.append(i)

        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.tail.data, 10)

    def test__print_double_linked_list__success(self):
        linked_list = DLinkedList()

        for i in range(1, 11):
            linked_list.append(i)

        result = linked_list.print()

        self.assertEqual(result, '12345678910')

    def test__extend_double_linked_list__success(self):
        first_list, second_list = DLinkedList(), DLinkedList()

        for i in range(1, 21):
            if i < 11:
                first_list.append(i)
                continue
            second_list.append(i)

        first_list.extend(dlist=second_list)

        self.assertEqual(first_list.tail.data, 20)
        self.assertEqual(first_list.n, 20)
