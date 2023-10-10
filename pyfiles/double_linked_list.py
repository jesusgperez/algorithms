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
        self.n: int = 0

    def insert(self, item: int) -> None:
        if not self.head or not self.tail:
            self.head = Node(item=item)
            self.tail = self.head
            self.n += 1
            return

        self.tail.next = Node(item=item, previous=self.tail)
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
            self.insert(current.item)
            current = current.next

        return

    def print(self) -> str:
        current = self.head
        response = ''

        while current:
            response += str(current.item)
            current = current.next

        return response
