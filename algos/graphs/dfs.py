from typing import List, Dict
from pydantic import BaseModel

# Undirected analysis

def create_adj(n_vertices: int, edges: List[List]):
    adj = [[] for i in range(n_vertices)]

    for x, y in edges:
        adj[x] = y
    
    return adj


adj = create_adj(6, [[1,2],[1,3],[3,4],[2,5],[3,2],[5,4]])


def bfs():
    pass
