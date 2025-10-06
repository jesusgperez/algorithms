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

vertext_info, time = defaultdict(VertexInfo), 0

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

dfs(1, undirected)

pass
