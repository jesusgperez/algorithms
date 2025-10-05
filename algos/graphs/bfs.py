from typing import List, Dict
from collections import deque, defaultdict
from pydantic import BaseModel

def create_adj(nvertices: int, edges: List[List]):
    adj = [[] for _ in range(nvertices)]

    for x, y in edges:
        adj[x].append(y)

    return adj

# Directed graph

adj = create_adj(6, [[1,2], [1,3], [2,3], [3,4], [4,3], [2,5], [5,4]])

class Info(BaseModel):
    discovered: bool = False
    processed: bool = False
    parent: int = -1
    color: int = -1

vertex_info = defaultdict(Info)

queue = deque((1,))
vertex_info[1].discovered = True
vertex_info[1].color = 1

def process_vertex(parent: int, child: int, vertex_info: List[Info]):
    print(parent, ' -> ', child)

    if vertex_info[parent].color == vertex_info[child].color:
        return False

    vertex_info[child].color = (vertex_info[parent].color + 1) % 2

    return True

while queue:
    vertex = queue.popleft()

    for child in adj[vertex]:
        # print(process_vertex(vertex, child, vertex_info))

        if not vertex_info[child].discovered:
            vertex_info[child].discovered = True
            queue.append(child)
            vertex_info[child].parent = vertex

    vertex_info[child].processed = True

print(list(map(lambda x: print(x[0], x[1].parent), vertex_info.items())))

# This is a stack, since recursion uses the call stack
def find_path(start: int, end: int, vertex_info: Dict):
    if start == end or vertex_info[end].parent == -1:
        print(start)
    else:
        find_path(start, vertex_info[end].parent, vertex_info)
        print(end)

find_path(1, 4, vertex_info)

# Undirected graph

def create_undirected(n_vertices, edges):
    adj = [[] for _ in range(n_vertices)]

    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    return adj

n_vertex = 9

adj = create_undirected(n_vertex, [[1,2],[2,5],[1,3],[3,4],[2,3],[4,5],[3,5],[6,7],[7,8],[8,6]])

vertex_info = defaultdict(Info)

process_edge = lambda x, y: print(x, ' -> ', y)

def bfs(start):
    queue = deque((start,))
    vertex_info[start].discovered = True

    while queue:
        vertex = queue.popleft()

        for child in adj[vertex]:
            if not vertex_info[child].processed:
                process_edge(vertex, child)
            
            if not vertex_info[child].discovered:
                vertex_info[child].discovered = True
                queue.append(child)
                vertex_info[child].parent = vertex

        vertex_info[vertex].processed = True

components = 0

for i in range(n_vertex):
    if not vertex_info[i].discovered:
        components += 1
        bfs(i)

print(components)
