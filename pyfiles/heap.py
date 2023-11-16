from typing import List
from math import floor as math__floor
from pyfiles.domain import HeapChild

class Heap:
    def __init__(self) -> None:
        self.queue: List[int] = []
        self.n: int = 0

    def insert(self, data: int) -> None:
        pass

    def bubble_up(self, position: int) -> None:
        pass

    def get_parent_position(self, position: int) -> int:
        parent_position = math__floor(position / 2)
        if parent_position < 1:
            return -1

        return parent_position

    def get_child(self, child_type: HeapChild, position: int) -> int:
        child = (2 * position 
                 if child_type == HeapChild.LEFT 
                 else 2 * position + 1)

        if child > self.n:
            return -1

        return child

