class EdgeNode:
    def __init__(self, y: int, weight: int, next: 'EdgeNode'):
        self.y = y
        self.weight = weight
        self.next = next


class Graph:
    def __init__(
        self,
        edges: 'EdgeNode',
        degree: int,
        nvertices: int,
        nedges: int,
        directed: int
    ):
        self.edges = edges
        self.degree = degree
        self.nvertices = nvertices
        self.nedges = nedges
        self.directed = directed
