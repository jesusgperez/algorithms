from data_structures.domain import Node
from typing import Optional


class DLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.n: int = 0

    def append(self, data: int) -> None:
        if not self.head or not self.tail:
            self.head = Node(data=data)
            self.tail = self.head
            self.n += 1
            return

        self.tail.next = Node(data=data, previous=self.tail)
        self.tail = self.tail.next
        self.n += 1
        return

    def extend(
        self,
        dlist: Optional['DLinkedList']
    ) -> None:
        if not dlist:
            return

        if not getattr(dlist, 'head') or not getattr(dlist, 'tail'):
            return

        current = dlist.head

        while current:
            self.append(current.data)
            current = current.next

        return

    def merge_sort(self) -> None:
        self.head = self._merge_sort_recursive(node=self.head)

    def _merge_sort_recursive(self, node) -> Optional[Node]:
        """
            Thios algorithm  will run O(logn)
        """
        if not node or not node.next:
            return node

        middle = self._get_middle_recursive(slow=node, fast=node)
        middle__next = middle.next

        middle.next = None

        left = self._merge_sort_recursive(node=node)
        right = self._merge_sort_recursive(node=middle__next)

        return self.sorted_merge(left=left, right=right)

    def sorted_merge(
        self,
        left: Optional[Node],
        right: Optional[Node]
    ) -> Optional[Node]:
        """
            This algorithm will run O(n)
        """
        result = None

        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left=left.next, right=right)
        else:
            result = right
            result.next = self.sorted_merge(left=left, right=right.next)

        return result

    def get_middle(self) -> Optional[Node]:
        return self._get_middle_recursive(slow=self.head, fast=self.head)

    def _get_middle_recursive(
        self,
        slow: Optional[Node],
        fast: Optional[Node]
    ) -> Optional[Node]:
        """
            This algorithm will run O(n)
        """
        if not slow and not fast:
            return

        if not fast.next or not fast.next.next:
            return slow

        return self._get_middle_recursive(
            slow=slow.next,
            fast=fast.next.next
        )

    def print(self) -> str:
        current = self.head
        response = ''

        while current:
            response += str(current.data)
            current = current.next

        return response
