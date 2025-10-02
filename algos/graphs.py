from enum import Enum, auto
from collections import deque
from typing import List, Optional, Callable

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

g = read_graph([[6,6],[1,2],[2,3],[3,4],[4,5],[5,3],[1,4]], True)
# g = read_graph([[7,5],[1,2],[1,4],[2,3],[4,5],[4,6]], True)

# print_graph(g)

class Color(Enum):
    BLACK = auto()
    WHITE = auto()
    UNCOLORED = auto

    @classmethod
    def complement(cls, color):
        if color == cls.BLACK:
            return cls.WHITE
        elif color == cls.WHITE:
            return cls.BLACK
        return cls.UNCOLORED

class GraphTraversal:
    def __init__(
            self,
            graph: Graph,
            preprocess: Callable = None,
            edge_process: Callable = None,
            postprocess: Callable = None
        ):
        self.graph = graph
        self.parents = [-1 for _ in range(graph.nvertices)]
        self.discovered = [False for _ in range(graph.nvertices)]
        self.processed = [False for _ in range(graph.nvertices)]
        self.preprocess = preprocess
        self.edge_process = edge_process
        self.postprocess = postprocess

# bfs: shortest path for unweighted graphs from root to ith node
# parents: gives the paths from root to ith node
# discovered and processed could be a pair of sets and adding the vertices to those (pythonic)
class BFS(GraphTraversal):
    def __init__(
            self,
            graph: Graph,
            preprocess: Callable = None,
            edge_process: Callable = None,
            postprocess: Callable = None
        ):
        super().__init__(graph, preprocess, edge_process, postprocess)
        self.is_bipartite = True

    def search(self, start: int):
        queue = deque([start])
        self.discovered[start] = True

        while queue:
            vertex = queue.popleft()

            if self.preprocess:
                self.preprocess(vertex)

            self.processed[vertex] = True

            current = self.graph.edges[vertex]
            while current:
                value = current.val
                if (not self.processed[value] or self.graph.directed) and self.edge_process:
                    self.edge_process(vertex, value)
                if not self.discovered[value]:
                    queue.append(value)
                    self.discovered[value] = True
                    self.parents[value] = vertex

                current = current.next

            if self.postprocess:
                self.postprocess(vertex)

    def check_color(self, x, y):
        if self.colors[x] == self.colors[y]:
            self.is_bipartite = False

        self.colors[y] = Color.complement(self.colors[x])

    def check_bipartite(self):
        self.colors = [Color.UNCOLORED for _ in range(self.graph.nvertices)]
        self.edge_process = self.check_color

        for i in range(self.graph.nvertices):
            if not self.discovered[i]:
                self.colors[i] = Color.WHITE
                self.search(i)

        print(self.is_bipartite)

    def restart_search(self):
        self.discovered = [False for _ in range(self.graph.nvertices)]
        self.processed = [False for _ in range(self.graph.nvertices)]

    # Shortest path to the root node
    def find_path(self, start: int, end: int):
        if start == end or end == -1:
            print(start)
        else:
            self.find_path(start , self.parents[end])
            print(end)

bfs = BFS(graph=g, preprocess=lambda x: print(x), edge_process=lambda x, y: print(x, ' -> ', y))
bfs.search(1)
# bfs.find_path(1, 5)
# bfs.restart_search()
# bfs.check_bipartite()

print('-------------------------------------------------------')

class DFS(GraphTraversal):
    def __init__(self, graph, preprocess = None, edge_process = None, postprocess = None):
        super().__init__(graph, preprocess, edge_process, postprocess)
        self.entry_time = [0 for _ in range(graph.nvertices)]
        self.exit_time = [0 for _ in range(graph.nvertices)]
        self.time = 0

    def search(self, vertex):
        self.discovered[vertex] = True
        self.time += 1
        self.entry_time[vertex] = self.time

        if self.preprocess:
            self.preprocess(vertex)

        current = self.graph.edges[vertex]
        while current:
            sibling = current.val
            if not self.discovered[sibling]:
                self.parents[sibling] = vertex
                if self.edge_process:
                    self.edge_process(vertex, sibling)
                self.search(sibling)
            elif ((not self.processed[sibling] and self.parents[vertex] != sibling) or self.graph.directed) and self.edge_process:
                self.edge_process(vertex, sibling)

            current = current.next

        if self.postprocess:
            self.postprocess(vertex)
        self.time += 1
        self.exit_time = self.time
        self.processed[vertex] = True

dfs = DFS(graph=g, preprocess=lambda x: print(x), edge_process=lambda x, y: print(x, '->', y))
dfs.search(1)
pass

