from typing import List, Optional
from math import floor as math__floor
from pyfiles.domain import HeapChild

DEFAULT_HEAP_SIZE = 256


class Heap:
    def __init__(self, size: int = DEFAULT_HEAP_SIZE) -> None:
        self.queue: List[Optional[int]] = [None] * size
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

