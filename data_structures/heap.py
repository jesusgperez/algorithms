from typing import List, Optional
from math import floor as math__floor
from data_structures.domain import HeapChild

DEFAULT_HEAP_SIZE = 256


class Heap:
    def __init__(self, size: int = DEFAULT_HEAP_SIZE) -> None:
        self.queue: List[Optional[int]] = [None] * size
        self.size = size
        self.n: int = 0

    def insert(self, data: int) -> None:
        if self.n >= self.size:
            raise Exception('Queue overflow')

        self.n += 1

        self.queue[self.n] = data

        self.bubble_up(position=self.n)

    def bubble_up(self, position: int) -> None:
        parent = self.get_parent_position(position=position)
        if parent == -1:
            return

        if self.queue[parent] > self.queue[position]:
            # Performs a swap in the positions
            buffer = self.queue[parent]
            self.queue[parent] = self.queue[position]
            self.queue[position] = buffer

            self.bubble_up(position=parent)

    def get_parent_position(self, position: int) -> int:
        parent_position = math__floor(position / 2)
        if parent_position < 1:
            return -1

        return parent_position

    def get_child(self, child_type: HeapChild, position: int) -> int:
        child = (2 * position
                 if child_type == HeapChild.LEFT
                 else 2 * position + 1)

        return child

    def extract_min(self) -> int:
        min_value = -1

        if self.n <= 0:
            return min_value

        min_value = self.queue[1]

        self.queue[1] = self.queue[self.n]
        self.queue[self.n] = None

        self.n -= 1

        self.bubble_down(parent=1)

        return min_value

    def bubble_down(self, parent: int) -> None:
        min_index = parent
        left_child = self.get_child(
            position=parent,
            child_type=HeapChild.LEFT
        )

        for i in range(2):
            if left_child + i > self.n:
                break

            if not self.queue[left_child + i] or not self.queue[parent]:
                break

            if self.queue[min_index] > self.queue[left_child + i]:
                min_index = left_child + i
        
        if min_index != parent:
            buffer = self.queue[parent]
            self.queue[parent] = self.queue[min_index]
            self.queue[min_index] = buffer

            self.bubble_down(parent=min_index)
