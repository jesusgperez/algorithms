from collections import deque
from typing import List, Optional

class EdgeNode:
    def __init__(self, val: int, weight: int = 0, next: 'EdgeNode' = None):
        self.val = val
        self.weight = weight
        self.next = next


class Graph:
    def __init__(
        self,
        nvertices: int = 0,
        nedges: int = 0,
        directed: bool = True
    ):
        self.edges: List[Optional[EdgeNode]] = [None for _ in range(nvertices)]
        self.degree: List[int] = [0 for _ in range(nvertices)]
        self.nvertices = nvertices
        self.nedges = nedges
        self.directed = directed

def read_graph(graph_info: List[List], directed: bool = True) -> Graph:
    nvertices, nedges = graph_info[0]
    graph = Graph(nvertices=nvertices, nedges=nedges, directed=directed)

    for i in range(1, nedges + 1):
        x, y = graph_info[i]
        insert_edge(graph, x, y, graph.directed)
    
    return graph


def insert_edge(graph: Graph, x: int, y: int , directed: bool):
    new_edge = EdgeNode(val=y, next=graph.edges[x])
    graph.edges[x] = new_edge
    graph.degree[x] += 1

    if not directed:
        insert_edge(graph, y, x, True)
    else:
        graph.nedges += 1


def print_graph(graph: Graph):
    for i in range(graph.nvertices):
        current = graph.edges[i]
        print(f'{i}:' ,end=' ')
        while current:
            print(current.val, end=' ')
            current = current.next
        print('')

g = read_graph([[6, 6],[1,2],[2,3],[3,4],[4,5],[5,3],[1, 4]], True)

print_graph(g)


def bfs(graph: Graph, start: int):
    queue = deque([start])

    discovered = [False for _ in range(graph.nvertices)]
    processed = [False for _ in range(graph.nvertices)]
    parents = [-1 for _ in range(graph.nvertices)]

    while queue:
        vertex = queue.popleft()

        ## process vertex early

        processed[vertex] = True
        current = graph.edges[vertex]
        while current:
            value = current.val
            if not processed[value] or not graph.directed:
                ## process the edge (vertex, value)
                pass
            if not discovered[value]:
                queue.append(value)
                discovered[value] = True
                parents[value] = vertex
            current = current.next

        ## process vertex late
