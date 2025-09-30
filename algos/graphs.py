from typing import List

class EdgeNode:
    def __init__(self, y: int, weight: int, next: 'EdgeNode'):
        self.y = y
        self.weight = weight
        self.next = next


class Graph:
    def __init__(
        self,
        edges: List['EdgeNode'],
        degree: List[int],
        nvertices: int,
        nedges: int,
        directed: bool
    ):
        self.edges = edges
        self.degree = degree
        self.nvertices = nvertices
        self.nedges = nedges
        self.directed = directed
