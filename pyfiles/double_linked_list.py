from pydantic import BaseModel
from typing import Optional


class Node(BaseModel):
    item: int
    next: Optional['Node'] = None
    previous: Optional['Node'] = None


class DLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def insert(self, item: int) -> int:
        if not self.head or not self.tail:
            self.head = Node(item=item)
            self.tail = self.head
            return item

        self.tail.next = Node(item=item, previous=self.tail)
        self.tail = self.tail.next
        return item

    def print(self) -> str:
        current = self.head
        response = ''

        while current:
            response += str(current.item)
            current = current.next

        return response
