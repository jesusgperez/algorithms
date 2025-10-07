from enum import Enum, auto
from typing import List, Dict
from pydantic import BaseModel
from collections import defaultdict

# Undirected analysis

def create_directed(n_vertices: int, edges: List[List]):
    adj = [[] for i in range(n_vertices)]

    for x, y in edges:
        adj[x].append(y)
    
    return adj

class VertexInfo(BaseModel):
    discovered: bool = False
    processed: bool = False
    parent: int = -1
    entry: int = 0
    exit: int = 0

vertex_info, time = defaultdict(VertexInfo), 0

process_edge = lambda x, y: print(x, ' -> ', y)

directed = create_directed(6, [[1,2],[1,3],[3,4],[2,5],[3,2],[5,4]])

def dfs(vertex: int, adj: List[List]):
    global time
    time += 1
    vertex_info[vertex].discovered = True
    vertex_info[vertex].entry = time

    for child in adj[vertex]:
        if not vertex_info[child].discovered:
            vertex_info[child].parent = vertex
            process_edge(vertex, child)
            dfs(child, adj)
        else: # Not much else validated, 
            process_edge(vertex, child)

    vertex_info[vertex].processed = True
    time += 1
    vertex_info[vertex].exit = time

# dfs(1, directed)

def create_undirected(n_vertices, edges):
    adj = [[] for i in range(n_vertices)]

    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    return adj

undirected = create_undirected(6, [[1,3],[1,2],[2,5],[3,4],[4,5],[2,3],[3,5]])

vertex_info, time = defaultdict(VertexInfo), 0

finished = False

def find_path(start, end):
    if start == end or vertex_info[end].parent == -1:
        print(start)
    else:
        find_path(start, vertex_info[end].parent)
        print(end)

def process_edge(x, y):
    global finished

    if vertex_info[y].parent != x:
        finished = True
        find_path(y, x)

def dfs(vertex: int, adj: List[List]): # undirected search
    global time, finished
    time += 1
    vertex_info[vertex].discovered = True
    vertex_info[vertex].entry = time

    if finished: return

    for child in adj[vertex]:
        if not vertex_info[child].discovered:
            vertex_info[child].parent = vertex
            process_edge(vertex, child)
            dfs(child, adj)
        # undirected edge process validation first time
        elif not vertex_info[child].processed and vertex_info[vertex].parent != child: 
            process_edge(vertex, child)

        if finished: return
        # second time 
        # if vertex_info[child].processed:
        #     process_edge(vertex, child)

    time += 1
    vertex_info[vertex].processed = True
    vertex_info[vertex].exit = time

# dfs(1, undirected)

class ArticulationVertexInfo(VertexInfo):
    tree_out_degree: int = 0
    reachable_ancestor: int = -1

vertex_info = defaultdict(ArticulationVertexInfo)

undirected = create_undirected(11, [[0,1],[1,2],[2,3],[3,4],[3,5],[4,5],[2,0],[0,6],[6,7],[7,8],[8,9],[9,10],[10,8],[9,7],[7,0]])

class EdgeClass(Enum):
    TREE = auto()
    BACK = auto()
    FORWARD = auto()
    CROSS = auto()

    @classmethod
    def clasify(cls, x: int, y: int):
        if vertex_info[y].parent == x:
            return cls.TREE
        elif vertex_info[y].discovered and not vertex_info[y].processed:
            return cls.BACK
        elif vertex_info[y].processed: #X just for directed graphs
            if vertex_info[y].entry > vertex_info[x].entry:
                return cls.FORWARD
            elif vertex_info[y].entry < vertex_info[x].entry:
                return cls.CROSS

        print(f'Warning, self loop {x}, {y}')
        return -1

def preprocess(v: int):
    vertex_info[v].reachable_ancestor = v

def process_edge(x: int, y: int):
    e_class = EdgeClass.clasify(x, y)

    if e_class == EdgeClass.TREE:
        vertex_info[x].tree_out_degree += 1

    if ((e_class == EdgeClass.BACK and vertex_info[y].parent != x) and
        vertex_info[y].entry < vertex_info[vertex_info[x].reachable_ancestor].entry):
            vertex_info[x].reachable_ancestor = y

def postprocess(v: int):
    parent, ancestor = vertex_info[v].parent, vertex_info[v].reachable_ancestor

    if parent == -1 and vertex_info[v].tree_out_degree > 1:
        print(f'Root articulation vertex: {v}')
        return

    if vertex_info[parent].parent == -1:
        return

    if ancestor == parent:
        print(f'Parent articulation vertex: {parent}')
    
    if ancestor == v:
        print(f'Bridge articulation vertex: {parent}')

        if vertex_info[v].tree_out_degree > 0:
            print(f'Bridge articulation vertex: {v}')

    if vertex_info[ancestor].entry < vertex_info[vertex_info[parent].reachable_ancestor].entry:
        vertex_info[parent].reachable_ancestor = ancestor

time = 0

def dfs(v: int, adj: List[List[int]]):
    global time
    time += 1
    vertex_info[v].discovered = True
    vertex_info[v].entry = time

    preprocess(v)

    for child in adj[v]:
        if not vertex_info[child].discovered:
            vertex_info[child].parent = v
            process_edge(v, child)
            dfs(child, adj)
        elif not vertex_info[child].processed and vertex_info[v].parent != child:
            process_edge(v, child)

    postprocess(v)

    time += 1
    vertex_info[v].processed = True
    vertex_info[v].exit = time

dfs(0, undirected)

pass
